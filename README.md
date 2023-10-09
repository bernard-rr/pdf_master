# PDF Master

Welcome to PDF Master! This is a Python application built with Streamlit that allows you to perform three main operations on PDF files: splitting, combining, and converting images to PDFs. With PDF Master, you can easily manage your PDF files by breaking them into smaller parts, merging multiple PDFs into a single file, and converting images to PDF format.

**Live Deployment**: [PDF Master](https://pdfmaster.streamlit.app/)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Split PDF](#split-pdf)
  - [Combine PDF](#combine-pdf)
  - [Convert Images to PDF](#convert-images-to-pdf)
- [Live Demo](#live-demo)
- [Requirements](#requirements)
- [Contact](#contact)

---

## Features

PDF Master provides the following features:

- **Split PDF**: Divide a PDF file into multiple smaller PDF files based on the number of pages per file or specify a starting page and line for title extraction.
- **Combine PDF**: Merge multiple PDF files into a single PDF and download them as a zip folder.
- **Convert Images to PDF**: Convert multiple images (JPEG, PNG) into a PDF and download them as a zip folder.

---

## Installation

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/bernard-rr/pdf_master.git
   ```

1. Install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Split PDF

The "Split PDF" feature allows you to break a PDF file into smaller parts.

To use this feature:

1. Run the `app.py` file:

   ```bash
   streamlit run app.py
   ```

2. Select "Split PDF" from the options.

3. Upload a PDF file that you want to split.

4. Optionally, you can specify the following parameters:
   - **Number of pages per file**: Enter the desired number of pages per split PDF file (optional).
   - **Start page for title extraction**: Enter the page number where title extraction should start (optional).
   - **Start line on the selected page for title extraction**: Enter the line number on the selected page for title extraction (optional).

5. Click the "Split" button to split the PDF.

6. Once the splitting is complete, you will see the split PDF files listed.

7. You can download all the split files as a zip folder using the "Download all files" button.

### Combine PDF

The "Combine PDF" feature allows you to merge multiple PDF files into a single PDF.

To use this feature:

1. Run the `app.py` file:

   ```bash
   streamlit run app.py
   ```

2. Select "Combine PDF" from the options.

3. Upload multiple PDF files that you want to combine. You can upload multiple PDFs at once.

4. PDFs will be merged into a single PDF file, and a zip folder containing the merged PDF will be created.

5. Once the merging is complete, you can download the combined PDFs as a zip folder using the "Download Combined PDFs" link.

### Convert Images to PDF

The "Convert Images to PDF" feature allows you to convert multiple images (JPEG, PNG) into a PDF.

To use this feature:

1. Run the `app.py` file:

   ```bash
   streamlit run app.py
   ```

2. Select "Convert Images to PDF" from the options.

3. Upload one or more images (JPEG, PNG) that you want to convert to PDF.

4. The images will be converted to PDF format, and a zip folder containing the PDFs will be created.

5. Once the conversion is complete, you can download the converted PDFs as a zip folder using the provided link.

---

## Live Demo

You can access a live demo of PDF Master hosted on Streamlit Cloud at [https://pdfmaster.streamlit.app/](https://pdfmaster.streamlit.app/). Try it out without the need to install anything!

---

## Requirements

The following Python packages are required to run PDF Master:

- `streamlit`
- `PyPDF2`
- `Pillow`

You can install these packages by running the following command:

```bash
pip install -r requirements.txt
```

---

## Contact

For feedback and inquiries, please feel free to reach out to the project owner:

- Email: [bernardchidi5@gmail.com](mailto:bernardchidi5@gmail.com?subject=Feedback%20on%20PDF%20Master%20App)

Enjoy using PDF Master for managing your PDF files!

```