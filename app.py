import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI PDF Search", layout="wide")

st.title("📄 AI PDF Search Platform")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    if text.strip() == "":
        st.error("No readable text found in document.")
    else:
        st.success("PDF loaded successfully ✅")

        query = st.text_input("Ask something from this PDF")

        if query:
            results = []
            lines = text.split("\n")

            for line in lines:
                if query.lower() in line.lower():
                    results.append(line)

            if results:
                st.subheader("🔍 Results")
                for r in results[:10]:
                    st.write("•", r)
            else:
                st.warning("No relevant answer found.")
