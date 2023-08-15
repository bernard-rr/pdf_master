import os
from PyPDF2 import PdfReader, PdfWriter
import streamlit as st
import tempfile
import os
from zipfile import ZipFile
import sys
import subprocess


def extract_title(page, line):
    """
    Extracts the text of a specific line from a page.

    Args:
        page: Page object from PyPDF2 representing the page to extract the title from.
        line: Line number to extract the text from.

    Returns:
        The extracted text of the specified line, or None if the line is out of range.
    """
    extracted_text = page.extract_text()
    lines = extracted_text.split('\n')
    if line and line <= len(lines):
        return lines[line - 1].strip()
    else:
        return None

def split_pdf(input_file, num_intervals=1, start_page=None, start_line=None):
    """
    Splits a PDF file into multiple smaller files based on the specified number of intervals.

    Args:
        input_file: Path to the input PDF file.
        num_intervals: Number of pages per file (default is 1).
        start_page: Start page for title extraction (optional).
        start_line: Start line on the selected page for title extraction (optional).
    """
    with open(input_file, 'rb') as file:
        pdf_reader = PdfReader(file)
        total_pages = len(pdf_reader.pages)

        pages_per_interval = num_intervals

        interval_num = 1
        start_index = 0

        while start_index < total_pages:
            end_index = min(start_index + pages_per_interval, total_pages) - 1

            pdf_writer = PdfWriter()

            # Add pages to the PdfWriter object for the current interval
            for page_index in range(start_index, end_index + 1):
                page = pdf_reader.pages[page_index]
                pdf_writer.add_page(page)

            title = extract_title(pdf_writer.pages[0], start_line)

            # Check if title is None or empty, set default title if necessary
            if not title:
                title = f"split_{os.path.splitext(os.path.basename(input_file))[0]}"

            output_file = f"{title}_{interval_num}.pdf"
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)

            print(f"Split PDF {interval_num} saved as {output_file}")

            interval_num += 1
            start_index = end_index + 1

def split_pdfs():
    # File upload
    uploaded_file = st.file_uploader("Choose PDF files to split", type=["pdf"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_file_path = tmp.name

        # Save the uploaded file with the original name
        original_file_name = uploaded_file.name
        uploaded_file_path = os.path.join(tempfile.gettempdir(), original_file_name)
        with open(uploaded_file_path, "wb") as file:
            file.write(uploaded_file.getvalue())

        intervals_input = st.text_input("Enter the number of pages per file (optional):")
        start_page_input = st.text_input("Enter the start page for title extraction (optional):")
        start_line_input = st.text_input("Enter the start line on the selected page for title extraction (optional):")

        if st.button("Split"):
            intervals = int(intervals_input) if intervals_input else 1
            start_page = int(start_page_input) if start_page_input else None
            start_line = int(start_line_input) if start_line_input else None

            split_pdf(uploaded_file_path, intervals, start_page, start_line)

            st.write("PDF splitting complete.")

            # Display the split PDF files
            file_names = []

            if start_page is None:
                file_names = [file for file in os.listdir() if file.startswith("split_") and file.endswith(".pdf")]
            else:
                for file in os.listdir():
                    if file.endswith(".pdf"):
                        page_number = int(file.split("_")[1].split(".")[0])
                        if page_number >= start_page:
                            file_names.append(file)

            if file_names:
                st.write("Split files:")
                for file_name in file_names:
                    st.write(file_name)

                # Create a zip file containing the split files
                with tempfile.TemporaryDirectory() as temp_dir:
                    zip_file_path = os.path.join(temp_dir, "split_files.zip")
                    with ZipFile(zip_file_path, "w") as zip:
                        for file_name in file_names:
                            new_name = f"{file_name}"
                            zip.write(file_name, arcname=new_name)

                    # Provide a download button for the zip file
                    with open(zip_file_path, "rb") as zip_file:
                        st.download_button("Download all files", data=zip_file, file_name="split_files.zip")
            else:
                st.write("No files were split.")

        # Clean up the temporary file
        os.remove(uploaded_file_path)
