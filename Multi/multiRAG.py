## Start local LLM
## PDF,DOC,TXT,MD Reader
## Chunking
## Embeddings
## VectorDB
## LLM for processing the extracted text
## Conversation loop

import os
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader,TextLoader,UnstructuredWordDocumentLoader,UnstructuredFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage ,AIMessage

## Start local LLM
llm = ChatOllama(
    model ="llama3.2:1b",
    base_url= "http://localhost:11434/"
)
print("Local LLM Strated")

llm2 = ChatOllama(
    model ="llama3.2",
    base_url= "http://localhost:11434/"
)
print("Local LLM Strated")

#loads ALL the files from the folder
DATA_PATH ="./knowledge"
documents =[]
for file in os.listdir(DATA_PATH):
    print(f"Processing file :{file}")

# for processing pdf
    if file.endswith(".pdf"):
        loader =PyPDFLoader(os.path.join(DATA_PATH,file))
        documents.extend(loader.load())

# for processing txt
    elif file.endswith(".txt"):
        loader =TextLoader(os.path.join(DATA_PATH,file))
        documents.extend(loader.load())
# for processing docx
    elif file.endswith(".docx"):
        loader =UnstructuredWordDocumentLoader(os.path.join(DATA_PATH,file))
        documents.extend(loader.load())

# for processing txt
    elif file.endswith(".md"):
        loader =UnstructuredFileLoader(os.path.join(DATA_PATH,file))
        documents.extend(loader.load())             

    else:
        print(f"Unsupported file format: {file}")

print(f"Loaded {len(documents)} documents from the folder ")        

## Chunking
text_splitter =RecursiveCharacterTextSplitter(chunk_size =100 ,chunk_overlap =50)
chunks =text_splitter.split_documents(documents)
print(f"Total chunks Created:{len(chunks)} from {len(documents)} documents")
noOfDocs= len(documents)
## Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

## VectorDB
vectorstore =Chroma.from_documents(documents=chunks,embedding=embeddings,persist_directory="./multirag_db")
retriever = vectorstore.as_retriever(search_kwargs={"k":2})
print("Vecort DB Created")

## LLM for processing the extracted text
prompt =ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that provides information about RAG. You must give information based on the document uploaded by user"),
    ("system","history:{history}"),
    ("system","context:{context}"),
    ("human","{input}")
])

chat_history =[]
print("\n multi file conversation RAG,(Type 'exit' to end the conversation)\n")

## Conversation loop

while True:
    user_input =input("User: ")
    if user_input.lower() =="exit":
        print("conversation Ended")
        break

    retrieved_docs =retriever.invoke(user_input)
    context ="\n".join([doc.page_content for doc in retrieved_docs])
    print(f"Retrieved context:\n{context}")

    chat_history.append(HumanMessage(content=user_input))
    if noOfDocs< 5:
        response = llm.invoke(prompt.format(history=chat_history,context=context,input=user_input))
        chat_history.append(AIMessage(content=response.content))
        print("LLM 1 is used")
        print(f"Assistant: {response.content}\n")

    else:
        response = llm2.invoke(prompt.format(history=chat_history,context=context,input=user_input))
        chat_history.append(AIMessage(content=response.content))
        print("LLM 2 is used")
        print(f"Assistant: {response.content}\n")