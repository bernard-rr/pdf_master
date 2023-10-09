import streamlit as st
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def image_to_pdf(input_image_path, output_pdf_path):
    # Open the image using PIL
    img = Image.open(input_image_path)

    # Create a PDF canvas with the same dimensions as the image
    c = canvas.Canvas(output_pdf_path, pagesize=img.size)

    # Draw the image on the PDF canvas
    c.drawImage(input_image_path, 0, 0, img.width, img.height)

    # Save the PDF file
    c.save()

def convert_image_to_pdf():
    st.write("Convert an image to PDF")

    uploaded_image = st.file_uploader("Choose an image to convert to PDF", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        output_pdf_path = "image_to_pdf.pdf"
        image_to_pdf(uploaded_image, output_pdf_path)

        st.success("Image successfully converted to PDF. Click the link below to download the PDF:")
        st.markdown(get_binary_file_downloader_html(output_pdf_path, 'Download PDF'), unsafe_allow_html=True)
