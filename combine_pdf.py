from PyPDF2 import PdfMerger
import os
import zipfile
import base64
import streamlit as st
from utils import get_binary_file_downloader_html

def merge_pdfs(pdf_list):
    merger = PdfMerger()
    for pdf_file in pdf_list:
        merger.append(pdf_file)
    return merger


def combine_pdfs():
    st.write("Upload multiple PDF files and combine them into a single PDF.")

    uploaded_files = st.file_uploader("Choose PDF files to combine", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        total_file_size = sum(file.size for file in uploaded_files)
        max_file_size = 50 * 1024 * 1024  # 50 MB (adjust this as needed)

        if total_file_size > max_file_size:
            st.error(f"Total file size exceeds the maximum limit of {max_file_size / (1024 * 1024)} MB.")
            return

        pdf_list = [pdf_file for pdf_file in uploaded_files]
        merger = merge_pdfs(pdf_list)

        # Merge the PDFs and create a combined PDF
        output_pdf = "combined_pdf.pdf"
        with open(output_pdf, "wb") as output:
            merger.write(output)

        # Create a zip folder and add the combined PDF to it
        zip_folder = "combined_pdfs.zip"
        with zipfile.ZipFile(zip_folder, 'w') as zip_file:
            zip_file.write(output_pdf)

        st.success("PDFs successfully combined. Click the link below to download the combined PDFs as a zip folder:")
        st.markdown(get_binary_file_downloader_html(zip_folder, 'Download Combined PDFs'), unsafe_allow_html=True)

        # Remove the temporary files
        os.remove(output_pdf)
        os.remove(zip_folder)
