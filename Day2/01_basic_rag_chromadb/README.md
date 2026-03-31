# 01 ChromaDB로 만드는 기본 RAG

PDF 문서를 로딩하고 ChromaDB 벡터스토어를 구축하여 기본적인 RAG 시스템을 구현합니다.

## 파일 구조

```
01_basic_rag_chromadb/
├── state.py           # Graph State 정의
├── retriever.py       # Ensemble Retriever 설정
├── nodes.py           # 노드 함수들 (retriever, answer, chatbot)
├── graph.py           # 그래프 구성 (기본 버전 & 에이전트 버전)
├── __init__.py        # 패키지 초기화
├── langgraph.json     # LangGraph Studio 설정
└── .env.example       # 환경변수 예시
```

## 실행 방법

### LangGraph Studio 실행

```bash
# 01_basic_rag_chromadb 폴더로 이동
cd 01_basic_rag_chromadb

# LangGraph Studio 실행
uv run langgraph dev
```
