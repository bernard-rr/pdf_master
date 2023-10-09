import streamlit as st
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import zipfile
import os

def image_to_pdf(uploaded_image, output_pdf_path):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
        temp_image.write(uploaded_image.read())

    img = Image.open(temp_image.name)
    c = canvas.Canvas(output_pdf_path, pagesize=img.size)
    c.drawImage(temp_image.name, 0, 0, img.width, img.height)
    c.save()

def convert_images_to_pdf(images):
    uploaded_images = st.file_uploader("Choose images to convert to PDF", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    pdf_files = []
    
    for uploaded_image in images:
        image_name = uploaded_image.name
        output_pdf_path = f"{os.path.splitext(image_name)[0]}.pdf"
        image_to_pdf(uploaded_image, output_pdf_path)
        pdf_files.append(output_pdf_path)

    temp_dir = tempfile.mkdtemp()
    zip_folder = os.path.join(temp_dir, "converted_pdfs.zip")

    with zipfile.ZipFile(zip_folder, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for pdf_file in pdf_files:
            zip_file.write(pdf_file, os.path.basename(pdf_file))

    st.success("Images successfully converted to PDFs. Click the link below to download the ZIP:")
    st.markdown(get_binary_file_downloader_html(zip_folder, 'Download ZIP'), unsafe_allow_html=True)
    return zip_folder

# if __name__ == "__main__":
#     uploaded_images = st.file_uploader("Choose images to convert to PDF", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
#     if uploaded_images:
#         zip_folder = convert_images_to_pdf(uploaded_images)
#         st.success("Images successfully converted to PDFs. Click the link below to download the ZIP:")
#         st.markdown(get_binary_file_downloader_html(zip_folder, 'Download ZIP'), unsafe_allow_html=True)
