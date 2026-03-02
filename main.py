import streamlit as st
import os
from rag import create_vector_store, run_rag

st.title("📄 DocMind - RAG with LangChain")
st.header("Upload a PDF document")

# Ensure docs folder exists
os.makedirs("docs", exist_ok=True)

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Sanitize filename
    safe_filename = uploaded_file.name.replace(" ", "_").replace("(", "").replace(")", "")
    file_path = os.path.join("docs", safe_filename)

    # Save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    if "vector_store" not in st.session_state:
        with st.spinner("Indexing the document..."):
            st.session_state.vector_store = create_vector_store(file_path)

    user_question = st.text_input("Enter your question here")

    if user_question:
        with st.spinner("Generating answer..."):
            result = run_rag(st.session_state.vector_store, user_question)
            st.write("### Answer:")
            st.write(result)
