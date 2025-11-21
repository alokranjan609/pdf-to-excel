from dotenv import load_dotenv
import google.generativeai as genai
import pdfplumber
import pandas as pd
import json
import os
load_dotenv()  # Load environment variables from .env file

# ---------------- Gemini Setup ----------------

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "gemini-2.0-flash-lite "     # or use "gemini-1.5-pro" for maximum accuracy

# ---------------- Step 1: Extract PDF Text ----------------

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text


# ---------------- Step 2: Ask Gemini to Structure the Data ----------------

def ask_gemini_to_extract(text):
    prompt = f"""
You are an expert in document understanding.

Extract ALL important information from the PDF text below and convert it into JSON.
Rules:
- Do NOT summarize
- Do NOT omit anything important
- Identify key:value pairs based on meaningful entities
- Maintain original wording for values
- Add a "comments" field when useful context exists
- Return output ONLY in valid JSON array of objects:
  [
    {{"key": "...", "value": "...", "comments": "..."}}
  ]

Here is the PDF content:

{text}
"""

    response = genai.GenerativeModel(MODEL).generate_content(prompt)
    return response.text


# ---------------- Step 3: Convert JSON → Excel ----------------

def json_to_excel(json_str, out_path="Output.xlsx"):
    try:
        data = json.loads(json_str)
    except Exception as e:
        print("Error parsing JSON from Gemini:", e)
        print("\nRaw response:\n", json_str)
        return

    df = pd.DataFrame(data)
    df.insert(0, "#", range(1, len(df) + 1))
    df.to_excel(out_path, index=False)
    print(f"\nExcel file generated: {out_path}")


# ---------------- Main Function ----------------

def process_pdf(pdf_path, output_path="Output.xlsx"):
    print("\nExtracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("\nSending content to Gemini...")
    json_output = ask_gemini_to_extract(text)

    print("\nGenerating Excel...")
    json_to_excel(json_output, output_path)


# ---------------- Run ----------------

if __name__ == "__main__":
    process_pdf("Data Input.pdf")     # Change for new PDFs

