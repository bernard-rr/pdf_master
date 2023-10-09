import streamlit as st
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import zipfile
from utils import get_binary_file_downloader_html
import os

def image_to_pdf(uploaded_image, output_pdf_path):
    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
        temp_image.write(uploaded_image.read())

    # Open the temporary image using PIL
    img = Image.open(temp_image.name)

    # Create a PDF canvas with the same dimensions as the image
    c = canvas.Canvas(output_pdf_path, pagesize=img.size)

    # Draw the image on the PDF canvas
    c.drawImage(temp_image.name, 0, 0, img.width, img.height)

    # Save the PDF file
    c.save()

def convert_images_to_pdf(images):
    pdf_files = []

    # Create a temporary directory for storing PDFs
    temp_dir = tempfile.mkdtemp()

    for image in images:
        image_name = image.name
        pdf_name = os.path.splitext(image_name)[0] + ".pdf"
        output_pdf_path = os.path.join(temp_dir, pdf_name)

        # Convert each image to PDF
        image_to_pdf(image, output_pdf_path)
        pdf_files.append(output_pdf_path)

    # Create a zip folder and add the PDFs to it
    zip_folder = os.path.join(temp_dir, "converted_pdfs.zip")
    with zipfile.ZipFile(zip_folder, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for pdf_file in pdf_files:
            zip_file.write(pdf_file, os.path.basename(pdf_file))

    return zip_folder
