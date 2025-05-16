# 📝 HTML Form to DOCX → PDF Generator

This Python-based tool captures data from a local HTML form, fills a `.docx` template with the submitted information, and generates a formatted PDF document. It's perfect for use cases like ticket delivery confirmations, reports, receipts, or any custom form-based document automation.

---

## 🚀 Features

- 🧾 Accepts submissions from a local HTML form  
- 📄 Replaces placeholders in a `.docx` template  
- 📑 Converts the filled-in DOCX to PDF  
- 🌐 Runs locally using Flask  
- 🗂️ Supports dynamic filenames and multilingual templates  
- ☁️ Compatible with deployment on Render (backend) + Netlify (frontend)

---

## 🛠️ Requirements

- Python 3.7+
- `flask`
- `python-docx`
- `docx2pdf` (Windows only) or `pypandoc`/LibreOffice for Linux/Mac
- `python-dotenv` (optional, for environment variable loading)

Install dependencies:

```bash
pip install flask python-docx docx2pdf python-dotenv
```

---

## 📁 Project Structure

```
project/
│
├── Templates/
│   └── your_template.docx
│
├── Static/
│   └── DocumentDeliveryForm.html
│
├── template-pdf-generator.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

- 🖥️ The user opens a local HTML form served via Flask  
- 📤 On submission, the form data is sent to the backend  
- 🧩 The backend uses `python-docx` to replace placeholders like `{{name}}`, `{{OS_number}}` in a `.docx` template  
- 📄 The filled-in DOCX is converted to a PDF  
- 💾 The resulting PDF is saved locally or sent as needed  

---

## ▶️ Running Locally

```bash
python template-pdf-generator.py
```

This starts the Flask server. Open your browser and go to:

```
http://localhost:5000
```

Submit the form to generate a PDF from the filled `.docx`.

---

## 🧪 Example Placeholders in `.docx` Template

Use double curly braces in your `.docx` file to define placeholders:

```
Hello {{name}},
Your OS number is {{OS_number}}.
```

These placeholders will be replaced by values from the form submission.

---

## 🌍 Deployment

You can deploy the app using:

- **Frontend (HTML form):** [Netlify](https://www.netlify.com/)
- **Backend (Flask app):** [Render](https://render.com/)

> ✅ Ensure that both Netlify and Render allow **CORS** (cross-origin requests).

---

## 📃 License

MIT License
