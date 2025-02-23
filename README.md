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
- [📁 Repository Structure](#-repository-structure)
- [⚙️ Installation & Setup](#-installation--setup)
- [▶️ Running the Application](#-running-the-application)
- [🛠️ Usage](#-usage)

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

## 📁 Repository Structure  

```bash
.
├── app.py                  # 🖥️ Main Flask backend handling requests
├── requirements.txt        # 📜 List of required Python dependencies
├── uploads/                # 📂 Directory storing uploaded files
├── extracted_text/         # 📄 Directory for storing extracted text in JSON format
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

## 📥 Step 1: Clone the Repository
First, open **Command Prompt (cmd)** or **PowerShell** and run:

```bash
git clone https://github.com/yourusername/student-performance-analyzer.git
cd student-performance-analyzer
``` 
