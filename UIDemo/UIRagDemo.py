#Import Streamlit for UI
import streamlit as st
import tempfile
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader,TextLoader,UnstructuredWordDocumentLoader,UnstructuredFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.title("Multi RAG Chatbot")
st.write("Welcome evryone to building UI session")

#Taking input From the user 
question =st.text_input("Ask your question")

#Button to submit the question
if st.button("Ask"):
    st.write(question)

#Uploade doc option
uploaded_file =st.file_uploader(
    "Upload Document",
    type=["pdf","docx","txt","md"]
)    
#Handling file uploads
if uploaded_file:
    temp_dir =tempfile.mkdtemp()
    temp_path =os.path.join(temp_dir,uploaded_file.name)
    with open(temp_path,"wb")as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded")    

    suffix =Path(temp_path).suffix

    if suffix==".pdf":
        loader =PyPDFLoader(temp_path)

    elif suffix==".docx":
        loader =UnstructuredWordDocumentLoader(temp_path)

    elif suffix==".txt":
        loader=TextLoader(temp_path)

    elif suffix==".md":
        loader=UnstructuredFileLoader(temp_path)

    documents =loader.load()    
    st.success("Documents Loaded")  

with st.spinner("Creating Chunks"):
    text_splitter =RecursiveCharacterTextSplitter(chunk_size =100 ,chunk_overlap =50)
    chunks =text_splitter.split_documents(documents)
    st.success(f"{len(chunks)} chunks created")
        

