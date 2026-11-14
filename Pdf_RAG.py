## Start local LLM
## PDF Reader
## Chunking
## Embeddings
## VectorDB
## LLM for processing the extracted text
## Conversation loop

from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
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

## PDF Reader
loader =PyPDFLoader("rag_intro.pdf")
pages =loader.load()
print(f"Total pages:{len(pages)}")

## Chunking
text_splitter =RecursiveCharacterTextSplitter(chunk_size =100 ,chunk_overlap =50)
chunks =text_splitter.split_documents(pages)
print(f"Total chunks:{len(chunks)}")

## Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

## VectorDB
vectorstore =Chroma.from_documents(documents=chunks,embedding=embeddings,persist_directory="./rag_demo")
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
print("\n PDF conversation RAG,(Type 'exit' to end the conversation)\n")

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

    response = llm.invoke(prompt.format(history=chat_history,context=context,input=user_input))
    chat_history.append(AIMessage(content=response.content))
    print(f"Assistant: {response.content}\n")

