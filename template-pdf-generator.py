from flask import Flask, request
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches
from docx2pdf import convert
import pythoncom
import os
import uuid

app = Flask(__name__)

# <-- adjust these paths to your environment -->
TEMPLATE_DIR = r"C:\PATH\TO\YOUR\TEMPLATES"
OUTPUT_DIR = r"C:PATH\TO\YOUR\OUTPUTS"

PRODUCT_LABELS = {
    "Product A": "Windows",
    "Product B": "Linux",
    "Product C": "MacOS",
}
ALLOWED_LANGUAGES = {"EN", "PT"}

@app.route('/submit', methods=['POST'])
def submit():
    # 1) grab form fields + uploaded file
    form_data     = request.form.to_dict()
    product_key   = form_data.get("Product")
    language      = form_data.get("Language")
    OS_number = form_data.get("OS_number")
    evidence_file = request.files.get("evidence")

    # 2) validate inputs
    product_code = PRODUCT_LABELS.get(product_key)
    if not product_code or language not in ALLOWED_LANGUAGES:
        return "Invalid product or language", 400
    if not evidence_file:
        return "Evidence file is required", 400

    # 3) pick the right template file
    if language == "EN":
        tpl_name = f"Document Delivery {product_code}_{language}.docx"
    else:
        tpl_name = f"Documento de Entrega {product_code}_{language}.docx"
    tpl_path = os.path.join(TEMPLATE_DIR, tpl_name)
    if not os.path.isfile(tpl_path):
        return f"Template not found: {tpl_path}", 404

    # 4) save the uploaded image to disk
    uid = str(uuid.uuid4())
    _, ext = os.path.splitext(evidence_file.filename)
    img_path = os.path.join(OUTPUT_DIR, f"{uid}{ext}")
    evidence_file.save(img_path)

    # 5) load & render with docxtpl
    tpl = DocxTemplate(tpl_path)
    context = form_data.copy()
    # InlineImage will replace your {{evidence}} placeholder
    context["evidence"] = InlineImage(tpl, img_path, width=Inches(4.5))
    tpl.render(context)

    # 6) save the filled‐in .docx (not used for now)
    out_docx = os.path.join(OUTPUT_DIR, f"{uid}.docx")
    tpl.save(out_docx)

    # 7) convert to PDF with dynamic file name
    if language == "EN":
        out_pdf = os.path.join(OUTPUT_DIR, f"Document Delivery - {OS_number}.pdf")
    else:
        out_pdf = os.path.join(OUTPUT_DIR, f"Documento de Entrega - {OS_number}.pdf")

    try:
        pythoncom.CoInitialize()
        convert(out_docx, out_pdf)
    finally:
        pythoncom.CoUninitialize()

    # 8) cleanup
    os.remove(img_path)
    os.remove(out_docx)

    return f"✅ PDF generated at: {out_pdf}"

if __name__ == "__main__":
    app.run(debug=True)