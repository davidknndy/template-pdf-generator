# 📝 HTML Form to DOCX → PDF Generator

This Python-based tool captures data from a local HTML form, fills a `.docx` template with the submitted information, and generates a formatted PDF document. It's perfect for use cases like ticket delivery confirmations, reports, receipts, or any custom form-based document automation.

## 🚀 Features

- 🧾 Accepts submissions from a local HTML form
- 📄 Replaces placeholders in a `.docx` template
- 📑 Converts the filled-in DOCX to PDF
- 🌐 Runs locally using Flask
- 🗂️ Supports dynamic filenames and multilingual templates
- ☁️ Compatible with deployment on Render (backend) + Netlify (frontend)

## 🛠️ Requirements

- Python 3.7+
- `flask`
- `python-docx`
- `docx2pdf` (Windows only) or `pypandoc`/LibreOffice for Linux/Mac
- `python-dotenv` (optional for environment config)

Install dependencies:

```bash
pip install flask python-docx docx2pdf python-dotenv

project/
│
├── Templates/
│   ├── your_templates.docx
│
├── Static/
│   └── DocumentDeliveryForm.html
│
├── template-pdf-generator.py
├── requirements.txt
└── README.md


⚙️ How It Works
The user opens a local HTML form served via Flask.
On submission, the data is sent to the backend.
The backend uses python-docx to replace placeholders (e.g., {{name}}, {{OS_number}}) in a .docx file.
The filled DOCX is converted to a PDF.
The resulting PDF is saved or sent as needed.


▶️ Running Locally
python template-pdf-generator.py


🧪 Example Placeholders in Template
Inside your .docx template, use placeholders like:

Hello {{name}},  
Your OS number is {{OS_number}}.


🌍 Deployment
You can host:

The frontend (HTML form) on Netlify
The backend (Flask app) on Render

Make sure both are configured to allow cross-origin requests.



📃 License
MIT License