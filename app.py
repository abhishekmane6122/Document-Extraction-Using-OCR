import os
import cv2
import numpy as np
import json
import pytesseract
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path
from docx import Document
import magic  # python-magic-bin on Windows
from pdf2image import convert_from_path


# Set tesseract path (for Windows users)
pytesseract.pytesseract.tesseract_cmd = r"" # Update the Path 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB
app.config['EXTRACTED_FOLDER'] = 'extracted_text'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'docx'}
ALLOWED_MIME_TYPES = {
    'image/jpeg': ['jpg', 'jpeg'],
    'image/png': ['png'],
    'application/pdf': ['pdf'],
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['docx']
}

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['EXTRACTED_FOLDER'], exist_ok=True)


# Check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Validate file type with MIME check
def validate_file(file_path):
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(file_path)
    file_ext = file_path.rsplit('.', 1)[1].lower()

    if mime_type not in ALLOWED_MIME_TYPES:
        return False
    if file_ext not in ALLOWED_MIME_TYPES[mime_type]:
        return False
    return True


# Image Preprocessing (Grayscale, Noise reduction, Thresholding)
def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Noise reduction
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Thresholding
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh


# OCR for Image files (JPG, PNG)
def process_image(file_path):
    image = cv2.imread(file_path)
    processed = preprocess_image(image)
    text = pytesseract.image_to_string(processed)
    return text


# OCR for PDF files (Convert to Images first)
# Specify the path to the Poppler bin directory
poppler_path = r""  # Update this path as needed

def process_pdf(file_path):
    try:
        # Use the poppler_path parameter
        images = convert_from_path(file_path, poppler_path=poppler_path)
        full_text = []
        for img in images:
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            processed = preprocess_image(img_cv)
            text = pytesseract.image_to_string(processed)
            full_text.append(text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"Error processing PDF: {str(e)}"

# Extract text from DOCX
def process_docx(file_path):
    try:
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error processing DOCX: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            if not validate_file(file_path):
                os.remove(file_path)
                return "Invalid file type", 400

            mime = magic.Magic(mime=True)
            mime_type = mime.from_file(file_path)

            try:
                if mime_type.startswith('image/'):
                    extracted_text = process_image(file_path)
                elif mime_type == 'application/pdf':
                    extracted_text = process_pdf(file_path)
                elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                    extracted_text = process_docx(file_path)
                else:
                    extracted_text = "Unsupported file type"

                # Save extracted text as JSON
                output_filename = f"{os.path.splitext(filename)[0]}_extracted.json"
                output_path = os.path.join(app.config['EXTRACTED_FOLDER'], output_filename)
                with open(output_path, 'w') as f:
                    json.dump({'filename': filename, 'text': extracted_text}, f)

                return render_template('result.html', text=extracted_text)

            except Exception as e:
                return f"Error processing file: {str(e)}", 500

    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
