
# PDF → Excel Converter (Powered by Google Gemini LLM)

Automatically extract structured information from **any PDF** and convert it into a clean, organized **Excel (XLSX)** file using **gemini-2.0-flash-lite**.

## 🚀 Features
- AI-powered extraction using Gemini LLM  
- Works for ANY type of PDF 
- Produces structured key:value pairs  

## 📂 Project Structure
```
pdf-to-excel-gemini/
│── gemini_output_extractor.py
│── requirements.txt
│── README.md
│── .env
│── Data Input.pdf
│── Output.xlsx
```

## 🔧 Installation
```bash
pip install -r requirements.txt
```

## ▶️ Run the  App
```bash
python gemini_output_extractor.py
```

## 🧠 How It Works
1. Extract PDF text using pdfplumber  
2. Send text to Gemini for structured extraction  
3. Gemini returns JSON  
4. Convert JSON → Excel  



## 🔐 Environment Variables
```
GOOGLE_API_KEY=your_key_here
```

## 📜 License
MIT License
