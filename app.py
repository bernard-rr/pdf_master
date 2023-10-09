import streamlit as st
from combine_pdf import combine_pdfs
from split_pdf import split_pdfs
from image_to_pdf import convert_image_to_pdf
import urllib.parse
from utils import get_binary_file_downloader_html


def main():
    st.title("PDF Master")

    st.markdown("[Read the instructions here](https://github.com/bernard-rr/pdf_master#usage)")

    email = "bernardchidi5@gmail.com"
    subject = urllib.parse.quote("Feedback on the PDF Master App")
    feedback_link = f"[Send me feedback](mailto:{email}?subject={subject})"
    st.markdown(feedback_link)

    action = st.radio("Select an action:", ["Split PDF", "Combine PDF", "Convert Image to PDF"])

    if action == "Split PDF":
        st.write("Split PDF files")
        split_pdfs()

    elif action == "Combine PDF":
        st.write("Combine PDF files")
        combine_pdfs()

    elif action == "Convert Image to PDF":
        st.write("Convert Image to PDF")
        convert_image_to_pdf()


if __name__ == "__main__":
    main()
