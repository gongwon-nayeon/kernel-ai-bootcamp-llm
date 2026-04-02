import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.tools import create_retriever_tool


def setup_retriever():
    """
    PDF 문서를 로딩하고 Retriever와 Retriever Tool을 생성합니다.
    ChromaDB가 이미 존재하면 로드하고, 없으면 생성합니다.
    """
    persist_directory = "./chroma_db"
    embeddings = OpenAIEmbeddings()

    # ChromaDB가 이미 존재하는지 확인
    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        print(f"기존 ChromaDB를 로드합니다: {persist_directory}")
        vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )
    else:
        print("새로운 ChromaDB를 생성합니다...")
        # PDF 문서 로딩
        file_path = "AI브리프_3월_260303.pdf"
        loader = PyPDFLoader(file_path)

        # 동기 방식으로 문서 로딩
        pages = loader.load()

        # Semantic Chunking
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        docs = text_splitter.split_documents(pages)

        print(f"총 {len(docs)}개의 문서로 분할되었습니다.")

        # ChromaDB 벡터스토어 생성 및 저장
        vectorstore = Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=persist_directory
        )
        print(f"ChromaDB가 저장되었습니다: {persist_directory}")

    # Retriever 생성
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    # Retriever Tool 생성
    retriever_tool = create_retriever_tool(
        retriever,
        "retrieve_AI_brief",
        "Search and return information about AI Technology and Industry from SPRi AI Brief."
    )

    return retriever, retriever_tool
