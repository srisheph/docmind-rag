import streamlit as st
import os
from rag import create_vector_store,run_rag

st.title("📄 DocMind - RAG with LangChain")
st.header("Upload a PDF document")

#Upload a PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    file_path = os.path.join("docs", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    if "vector_store" not in st.session_state:
        with st.spinner("Indexing the document..."):
            st.session_state.vector_store = create_vector_store(file_path)

    user_question = st.text_input("Enter your question here")
    if user_question:
        with st.spinner("Processing the document and building the RAG system..."):
            result=run_rag(st.session_state.vector_store,user_question)
            st.write("Answer:")
            st.write(result)
