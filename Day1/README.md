# AI 부트캠프 20기 LLM 프로젝트 - Day 1

1일차에서는 LangChain과 LangGraph의 기초를 학습하고, 간단한 LLM 챗봇을 구현합니다.

### 커리큘럼

1. **LangChain 소개**
2. **[실습] LangChain 기반 LLM 사용하기** - `01_langchain_llm_basics.ipynb`
3. **LangGraph 소개**
4. **[실습] LangGraph 기초 사용법** - `02_langgraph_essentials.ipynb`
5. **[실습] LangGraph 메시지 관리 그래프** - `03_langgraph_messages_state.ipynb`
6. **[실습] LangGraph 노드·엣지 연결 / 조건부 엣지** - `04_langgraph_nodes_edges.ipynb`
7. **[실습] 도구 기반 에이전트 그래프** - `05_langgraph_tools_chatbot.ipynb`
9. **[실습] 구조화된 출력 구현하기 (Structured Output)** - `06_structured_output.ipynb`


| 시간 | 내용 | 유형 | 실습 코드 파일 | 세부 구성 |
|------|------|------|----------------|-----------|
| 09:00–09:20 | LangChain 소개 | 이론 | - | - 생성형 AI / LLM 애플리케이션의 이해 |
| 09:20–10:10 | [실습] LangChain 기반 LLM 사용하기 | 실습 | `01_langchain_llm_basics.ipynb` | - OpenAI 연결<br>- 메시지 프롬프트 사용<br>- 스트리밍 응답<br>- 멀티턴 구현 |
| 10:10–10:20 | ☕ Break |  | - |  |
| 10:20–11:00 | LangGraph 소개 | 이론 | - | - 왜 LangGraph인가?(AI Agent, Agentic Workflow) <br>- State 기반 흐름 제어<br>- Node / Edge 개념 |
| 11:00–12:00 | [실습] LangGraph 기초 사용법 | 실습 | `02_langgraph_essentials.ipynb` | - TypedDict, Pydantic Base Model 이해<br>- State, Reducer 정의<br>- 그래프 연결 |
| 12:00–13:00 | 🍱 Lunch |  | - |  |
| 13:00–14:00 | [실습] LangGraph 메시지 관리 그래프 | 실습 | `03_langgraph_messages_state.ipynb` | - add_messages 메시지 관리<br>- LLM기반 챗봇 그래프 구현<br>- 스트리밍 응답 |
| 14:00–15:00 | [실습] LangGraph 노드·엣지 연결 / 조건부 엣지 | 실습 | `04_langgraph_nodes_edges.ipynb` | - 다중 노드 연결<br>- 조건 분기 (Conditional Edge) |
| 15:00–15:10 | ☕ Break |  | - |  |
| 15:10–16:20 | [실습] 도구 기반 에이전트 그래프 | 실습 | `05_langgraph_tools_chatbot.ipynb` | - 랭체인 도구 만들기<br>- 도구 바인딩<br>- 도구 호출 에이전트 |
| 16:20–16:30 | ☕ Break |  | - |  |
| 16:30–17:30 | [실습] 구조화된 출력 구현하기 (Structured Output) | 실습 | `06_structured_output.ipynb` | - Pydantic 모델 정의<br>- 답변 출력 형태 정의 |
| 17:30–18:00 | Q&A 및 코드 정리 | 마무리 | - |  |




## 실습 환경 설정

### 사전 요구사항

- Python 3.11 이상
- OpenAI API Key (https://platform.openai.com/api-keys)

### 1. uv 설치

#### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치 후 터미널을 재시작하거나 다음 명령으로 PATH를 업데이트하세요.

---

### 2. 가상환경 생성 및 패키지 설치

Day1 폴더로 이동한 후 아래 방법 중 하나를 선택하세요.

#### 방법 1: uv sync 사용 (권장)

```bash
# Day1 폴더로 이동
cd Day1

# pyproject.toml을 기반으로 가상환경 생성 및 패키지 설치
uv sync

# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate
```

#### 방법 2: requirements.txt 사용

```bash
# 가상환경 생성
uv venv

# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate

# 패키지 설치
uv pip install -r requirements.txt
```

---

### 3. Jupyter Notebook 커널 등록

VS Code에서 Jupyter Notebook을 사용하려면 커널을 등록해야 합니다.

#### Windows

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name=llm-day1 --display-name="llm Day1"
```

#### macOS/Linux

```bash
.venv/bin/python -m ipykernel install --user --name=llm-day1 --display-name="llm Day1"
```

커널 등록 후 **VS Code를 리로드**하면 노트북에서 "llm Day1" 커널을 선택할 수 있습니다.

---

### 4. 환경변수 설정

`.env.example` 파일을 `.env`로 복사하고 본인의 API 키를 입력하세요.

#### Windows (PowerShell)

```powershell
Copy-Item .env.example .env
```

#### macOS/Linux

```bash
cp .env.example .env
```

`.env` 파일을 열고 다음과 같이 수정:

```
OPENAI_API_KEY=your_openai_api_key_here
```