import streamlit as st
from combine_pdf import combine_pdfs
from split_pdf import split_pdfs

def main():
    st.title("PDF Processing App")

    action = st.selectbox("Select an action:", ["Split", "Combine"])

    if action == "Split":
        st.write("Split PDF files")
        split_pdfs()

    elif action == "Combine":
        st.write("Combine PDF files")
        combine_pdfs()

if __name__ == "__main__":
    main()
