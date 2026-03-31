# AI 부트캠프 20기 LLM 프로젝트 - Day 3

3일차에서는 AI 에이전트의 개념부터 시작하여 실전 에이전트를 구축하고, 최종 개별 프로젝트를 진행합니다.

### 커리큘럼

1. **AI 에이전트 이해하기**
2. **[실습] Langchain의 create_agent 이해하기(도구 정의)** - `01_langchain_create_agent.ipynb`
3. **[실습] 웹 검색 에이전트 구현하기 (tavily search)** - `02_web_search_agent.ipynb`
4. **[실습] 미들웨어 활용하기** - `03_builtin_middleware.ipynb` / `04_custom_middleware.ipynb`
5. **[실습] 최종 개별 프로젝트(자율 실습)** - `05_final_project.ipynb`

| 시간 | 내용 | 유형 | 실습 코드 파일 | 세부 구성 |
|------|------|------|----------------|-----------|
| 09:00–10:00 | AI 에이전트 이해하기 | 이론 | - | - AI 에이전트의 개념<br>- 도구(Tools)의 역할<br>- ReAct 패턴 |
| 10:00–11:00 | [실습] Langchain의 create_agent 이해하기 | 실습 | `01_langchain_create_agent.ipynb` | - create_agent 함수 이해<br>- 커스텀 도구 정의하기<br>- 도구 파라미터 설정 |
| 11:00–11:10 | ☕ Break |  | - |  |
| 11:10–12:00 | [실습] 웹 검색 에이전트 구현하기 | 실습 | `02_web_search_agent.ipynb` | - Tavily Search API 설정<br>- 웹 검색 도구 통합<br>- 검색 결과 처리<br>- 에이전트 기반 웹 검색|
| 12:00–13:00 | 🍱 Lunch |  | - |  |
| 13:00–14:30 | [실습] 빌트인 미들웨어 활용하기 | 실습 | `03_builtin_middleware.ipynb` | - 미들웨어 개념 이해<br>- SummarizationMiddleware <br>- ToolCallLimitMiddleware<br>- ToolRetryMiddleware <br>- 다중 미들웨어 조합 |
| 14:30–14:40 | ☕ Break |  | - |  |
| 14:40–16:20 | [실습] 커스텀 미들웨어 만들기 | 실습 | `04_custom_middleware.ipynb` | - 미들웨어 훅(Hook) 이해<br>- 데코레이터 기반 미들웨어<br>- 클래스 기반 미들웨어<br>- 상태 추적 및 관리<br>- 실전 예제 (로깅, 캐싱) |
| 16:20–17:30 | [실습] 최종 개별 프로젝트 | 실습 | `05_final_project.ipynb` | - 필수 미들웨어 적용 (TodoList, Summarization)<br>- 커스텀 미들웨어 2개 정의<br>- 프롬프트 엔지니어링|
| 17:30–18:00 | Q&A 및 최종 마무리 | 마무리 | - | |


## 실습 환경 설정

### 사전 요구사항

- Python 3.11 이상
- OpenAI API Key (https://platform.openai.com/api-keys)
- Tavily API Key (https://app.tavily.com/home)

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

Day3 폴더로 이동한 후 아래 방법 중 하나를 선택하세요.

#### 방법 1: uv sync 사용 (권장)

```bash
# Day3 폴더로 이동
cd Day3

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
.venv\Scripts\python.exe -m ipykernel install --user --name=llm-Day3 --display-name="llm Day3"
```

#### macOS/Linux

```bash
.venv/bin/python -m ipykernel install --user --name=llm-Day3 --display-name="llm Day3"
```

커널 등록 후 **VS Code를 리로드**하면 노트북에서 "llm Day3" 커널을 선택할 수 있습니다.

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
TAVILY_API_KEY=your_tavily_api_key_here
```

