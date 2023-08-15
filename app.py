import streamlit as st
from combine_pdf import combine_pdfs
from split_pdf import split_pdfs

def main():
    st.title("PDF Master")

    action = st.radio("Select an action:", ["Split PDF", "Combine PDF"])

    if action == "Split PDF":
        st.write("Split PDF files")
        split_pdfs()

    elif action == "Combine PDF":
        st.write("Combine PDF files")
        combine_pdfs()


if __name__ == "__main__":
    main()
