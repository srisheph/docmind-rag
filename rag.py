from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_vector_store(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs= text_splitter.split_documents(docs)


    embedder = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=OPENAI_API_KEY,
    )
    vector_store=QdrantVectorStore.from_documents(
        documents=split_docs,
        url="http://localhost:6333",
        collection_name="building_rag",
        embedding=embedder
    )
    
    return vector_store

def transform_query(question):
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

    prompt = f"""
    Rewrite the following user question to be more clear, specific and suitable for semantic search 
    over a technical PDF document. Do not answer the question.

    Question: {question}

    Rewritten Query:

    Example:

    Example 1:
        Question: What is Node.js?
        Rewritten Query: What is Node.js and what are its main features?
    Example 2:
        Question: How to use Python?
        Rewritten Query: What are the steps to get started with Python programming and what are its common use cases?
    """

    response = llm.invoke(prompt)
    return response.content.strip()


def run_rag(vector_store,question):
    question = transform_query(question)
    search_result=vector_store.similarity_search(
        query=question,
        k=3
    )

    relevant_chunks = ""

    for i, doc in enumerate(search_result):
        relevant_chunks += f"Chunk {i+1}:\n{doc.page_content}\n\n"

    SYSTEM_PROMPT=f"""
    You are a helpful assistant built to answer question about the pdf document provided. 
    You will be given a question and a list of relevant passages from the document.
    Use the information in the passages to answer the question as accurately as possible. 
    If you don't know the answer, understand the question and recommend the user with multiple rephrasing of the question.

    CONSTRAINTS:
        - Use only the information provided in the passages to answer the question.
        - If the passages do not contain enough information to answer the question, rephrase the question in multiple ways to help the user clarify their query.
        - Be concise while being as informative as possible. 

    Output Format:
        -Cite the page number.
        -Answer in bullet points.
        -Limit to 3 sentences.
        -If you don't know the answer, provide 3 different rephrasing of the question to help the user clarify their query.

    Context:
        {relevant_chunks}
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY
    )

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=question)
    ]

    response = llm.invoke(messages)
    return response.content