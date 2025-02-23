# 🎓 Student Performance Analyzer & Career Recommendation System 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.5-red)
![Tesseract](https://img.shields.io/badge/Tesseract-5.0.0-orange)


Welcome to the **Student Performance Analyzer & Career Recommendation System** repository! This project is designed to simplify text extraction from various document formats like **JPEG, PNG, PDF, and DOCX** using **Optical Character Recognition (OCR)** and **image processing techniques**. 📄➡️💻  

The extracted text becomes a **valuable resource for analyzing student performance** and **providing career recommendations**, helping students make informed decisions about their future! 🌟  

---

## 📜 Table of Contents
- [🔍 Overview](#-overview)
- [✨ Features](#-features)
- [📸 Screenshot and Demo](#-screenshot)
- [📁 Repository Structure](#-repository-structure)
- [⚙️ Installation & Setup](#-installation--setup)
- [🛠️ Usage & Workflow](#-usage--workflow)
- [⚠️ Troubleshooting](#-troubleshooting)

---

## 🔍 Overview
This application is powered by **cutting-edge libraries** to ensure seamless **file handling, text extraction, and analysis**:  

- **Flask** 🖥️ – A lightweight web framework to provide an interactive web interface.
- **OpenCV** 🖼️ – Enhances image quality for better OCR results (grayscale, noise removal, thresholding).
- **Tesseract OCR** 🔠 – Extracts text from images.
- **pdf2image** 📑 – Converts PDFs into images to enable OCR processing.
- **python-docx** 📄 – Reads and extracts text from Word documents.
- **python-magic** 🔍 – Verifies file types to prevent unsupported formats from being processed.

The **goal** of this project is to **streamline student data processing** and enable **personalized career guidance** based on extracted insights. 🏆  

---

## ✨ Features

✔️ **Easy File Upload**  
   - Upload **images, PDFs, or DOCX files** via an intuitive web interface.  

✔️ **File Validation**  
   - Ensures **only supported files** (JPEG, PNG, PDF, DOCX) are processed.  
   - **Max file size:** **5MB** to prevent heavy processing.  

✔️ **OCR-based Text Extraction**  
   - Uses **Tesseract OCR** for **image and PDF files**.  
   - Parses **DOCX files** to extract structured text.  

✔️ **Advanced Image Preprocessing**  
   - Converts images to **grayscale** for better OCR accuracy.  
   - Uses **thresholding** and **noise removal** to enhance clarity.  

✔️ **Structured Results Display**  
   - Extracted text is **displayed** neatly on the results page.  
   - Text is also **saved in JSON format** for further use.  

✔️ **Secure Storage**  
   - Uploaded files are stored in the **uploads/** directory.  
   - Extracted text is stored in the **extracted_text/** folder.  

✔️ **Career Guidance Integration (Future Scope)**  
   - Based on extracted academic performance, the system can provide **AI-driven career suggestions**.  

---
## 📸 Screenshot and Demo

Here’s a quick preview of how the application works:  

### 🎥 Live Demo  
Watch the full process in action!  
[![Watch Demo](https://img.shields.io/badge/🎥%20Watch%20Demo-Click%20Here-red)](https://github.com/abhishekmane6122/Document-Extraction-Using-OCR/blob/main/Screenshots/Document%20Extraction.mp4)  

### 📌 Dashboard & Extracted Results  

<div align="center">
  <table>
    <tr>
      <td align="center"><b>Dashboard View</b></td>
      <td align="center"><b>Extracted Results</b></td>
    </tr>
    <tr>
      <td><img src="https://github.com/abhishekmane6122/Document-Extraction-Using-OCR/blob/main/Screenshots/Dashboard.png" width="400"></td>
      <td><img src="https://github.com/abhishekmane6122/Document-Extraction-Using-OCR/blob/main/Screenshots/Result%20.png" width="400"></td>
    </tr>
  </table>
</div>

---
## 📁 Repository Structure  

```bash
.
├── app.py                  # 🖥️ Main Flask backend handling requests
├── requirements.txt        # 📜 List of required Python dependencies
├── uploads/                # 📂 Directory storing uploaded files
├── extracted_text/         # 📄 Directory for storing extracted text in JSON format
├── diagrams/               # 📝 Diagrams and Architecture
├── documents/              # 📄 End to End Report
├── screenshot/             # 🎥 Screenshot and recordings 
├── templates/              # 🎨 HTML templates for the web interface
│   ├── index.html          # 🖼️ Upload interface
│   └── result.html         # 📋 Results display page
├── static/                 # 🎨 CSS/JS assets for styling
``` 
# ⚙️ Installation & Setup 

## 🐍 Prerequisites  
Ensure you have the following installed before proceeding:  
- **Python 3.8+** ([Download Here](https://www.python.org/downloads/))  
- **Git** ([Download Here](https://git-scm.com/downloads))  

Verify the installations:  

```bash
python --version
git --version
```

## 📑 Table of Contents  

- [📥 Step 1: Clone the Repository](#-step-1-clone-the-repository)  
- [📦 Step 2: Create a Virtual Environment](#-step-2-create-a-virtual-environment)  
- [📜 Step 3: Install Dependencies](#-step-3-install-dependencies)  
- [📌 Step 4: Install Tesseract OCR](#-step-4-install-tesseract-ocr)  
- [📂 Step 5: Install Poppler for PDF Processing](#-step-5-install-poppler-for-pdf-processing)  
- [🚀 Step 6: Running the Application](#-step-6-running-the-application)  

---

## 📥 Step 1: Clone the Repository  

First, open **Command Prompt (cmd)** or **PowerShell** and run:  

```bash
git clone https://github.com/yourusername/student-performance-analyzer.git
cd student-performance-analyzer
```
## 📦 Step 2: Create a Virtual Environment

Create and activate a virtual environment to keep dependencies isolated.

```bash
python -m venv venv
venv\Scripts\activate
```
You should see `(venv)` appear in your terminal, indicating the virtual environment is active.

---

## 📜 Step 3: Install Dependencies
With the virtual environment activated, install all required dependencies:

```bash
pip install -r requirements.txt
```

If `pip` is outdated, upgrade it first:

```bash
python -m pip install --upgrade pip
```
### 📜 `requirements.txt`

Here’s the full list of dependencies to include in your `requirements.txt` file:

```
Flask
opencv-python
pytesseract
pdf2image
python-docx
python-magic
pillow
poppler-utils
```

---

## 📌 Step 4: Install Tesseract OCR 🖹
Tesseract OCR is required for text extraction from images and PDFs.

### 🔹 Download & Install Tesseract
1. Download the Windows installer from:
   👉 [Tesseract OCR Windows](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer (`tesseract-ocr-setup.exe`).
3. During installation, enable "Additional language packs" if needed.
4. Once installed, locate the installation path (default is usually):

```bash
C:\Program Files\Tesseract-OCR
```

### 🔹 Add Tesseract to System Path:
1. Open **Environment Variables**:
   - Press `Win + R`, type `sysdm.cpl`, and hit Enter.
   - Go to the **Advanced** tab → Click **Environment Variables**.
2. Under **System Variables**, find **Path** and edit it.
3. Click **New** and add:

```bash
C:\Program Files\Tesseract-OCR
```

### 🔹 Verify installation:

```bash
tesseract --version
```
You should see the installed version of Tesseract.

---

## 📂 Step 5: Install Poppler for PDF Processing
Poppler is required for converting PDF pages into images.

### 🔹 Download & Install Poppler
1. Download Poppler for Windows from:
   👉 [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)
2. Extract the downloaded ZIP file to a directory, e.g., `C:\poppler-xx\`

### 🔹 Add Poppler to System Path:
1. Open **Environment Variables**:
   - Press `Win + R`, type `sysdm.cpl`, and hit Enter.
   - Go to the **Advanced** tab → Click **Environment Variables**.
2. Under **System Variables**, find **Path** and edit it.
3. Click **New** and add:

```bash
C:\poppler-xx\bin
```

### 🔹 Verify installation:

```bash
pdfinfo -v
```

---

## 🚀 Step 6: Running the Application
After installing all dependencies, start the Flask application:

```bash
python app.py
```

The application should now be running at:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

--- 
## 🚀 Usage & Workflow

### 1️⃣ Step 1: Upload a File  
- Navigate to the web application:  
  👉 Open `http://127.0.0.1:5000/` in your browser.  
- Click on the **Upload File** button.  
- Select an image (JPEG/PNG), PDF, or DOCX file.  
- Click **Submit** to process the file.

### 2️⃣ Step 2: File Validation  
- The system checks:
  - ✅ File format (JPEG, PNG, PDF, DOCX).
  - ✅ File size (Max: 5MB).
  - ✅ MIME type security validation.
- If invalid, an error message will be displayed.

### 3️⃣ Step 3: Preprocessing (For Images & PDFs)  
- If an **image** is uploaded:
  - 📌 Converts to **grayscale** for better OCR accuracy.
  - 📌 Applies **thresholding** to remove noise.
- If a **PDF** is uploaded:
  - 📌 Converts each page into an image.
  - 📌 Applies preprocessing before OCR.

### 4️⃣ Step 4: Text Extraction  
- Uses **Tesseract OCR** to extract text from images/PDFs.  
- Uses **python-docx** to extract text from DOCX files.  
- Extracted text is displayed on the UI.

### 5️⃣ Step 5: Display & Download Results  
- The extracted text appears in the browser.  
- Option to **copy, download, or analyze** extracted text.  

💡 **Tip:** Ensure Tesseract and Poppler are installed correctly before running the app!  

---
## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| ❌ **File upload fails** | Check file type and size (≤5MB). |
| ❌ **JSON file not saved** | Ensure `extracted_text` folder exists. |
| ❌ **Tesseract not found** | Verify Tesseract installation and update `TESSERACT_CMD` path in `app.py`. |
| ❌ **PDF conversion failed** | Install Poppler and set `POPPLER_PATH` in environment variables. |
| ❌ **Flask server not starting** | Ensure no other application is using port `5000`. Use `flask run --port 5001` to change the port. |
| ❌ **Virtual environment not activating** | Ensure Python is installed correctly. Use `python -m venv venv` to recreate the virtual environment. |
| ❌ **Dependencies not installing** | Upgrade pip using `python -m pip install --upgrade pip` and retry. |
| ❌ **File type validation error** | Ensure the file matches the allowed MIME types (JPEG, PNG, PDF, DOCX). |

💡 **Tip:** If you're still facing issues, check the error logs in the terminal and ensure all dependencies are correctly installed. 🚀


