# 색인

build.py 가 만든 파일입니다. 직접 고치지 마세요.
문서 33건, 분류 8개. 한 줄에 문서 하나이며, 자세한 내용은 연결된 md 파일에 있습니다.

## 개발 도구 (6)

- [Skullet — 실제 컴포넌트를 재서 로딩 뼈대 화면을 자동으로 그려 주는 라이브러리](docs/skullet.md) · 2026-11-11
  - 요약: 데이터가 오기 전에 보여 주는 회색 뼈대 화면(스켈레톤)을 따로 디자인하지 않아도, 실제 컴포넌트를 보이지 않게 배치해 크기를 잰 뒤 같은 자리에 그려 주는 오픈소스 라이브러리. React·Vue·Svelte·순수 JS 지원, MIT.
  - 태그: Skullet, 스켈레톤, skeleton, 로딩 화면, 로딩 UI, React, Vue, Svelte, 레이아웃 흔들림, 바이브 코딩, 프런트엔드
  - 링크: [GitHub](https://github.com/lochie/skullet) · [공식 사이트](https://skullet.lochie.me) · [패키지 문서](https://github.com/lochie/skullet/blob/main/packages/skullet/README.md)
- [Open Notebook — 직접 설치해 쓰는 오픈소스 NotebookLM 대안](docs/open-notebook.md) · 2026-11-11
  - 요약: 구글 NotebookLM처럼 문서·링크·영상을 넣으면 요약하고 노트를 쓰고 그 내용으로 대화하는 오픈소스 도구. 내 PC나 서버에 Docker로 설치하고, OpenAI·Anthropic·Ollama 등 20여 개 제공자 중 골라 내 API 키로 쓴다. MIT 라이선스.
  - 태그: Open Notebook, NotebookLM, 노트북LM, 오픈소스, 셀프호스팅, 문서 요약, 팟캐스트 생성, 자료 정리, Ollama, Docker, RAG
  - 링크: [GitHub](https://github.com/lfnovo/open-notebook) · [공식 사이트](https://www.open-notebook.ai) · [문서](https://github.com/lfnovo/open-notebook/tree/main/docs)
- [MarkItDown — 문서를 LLM이 읽기 좋은 Markdown으로 바꾸는 마이크로소프트 오픈소스](docs/markitdown.md) · 2026-11-11
  - 요약: PDF, 워드, 엑셀, 파워포인트, 이미지, 오디오, HTML, 유튜브 주소 등을 Markdown으로 바꿔 주는 가벼운 Python 도구. 사람이 보기 좋은 변환이 아니라 LLM과 텍스트 분석에 넣기 위한 변환이 목적이다. MIT 라이선스.
  - 태그: MarkItDown, 마크잇다운, Markdown 변환, 문서 변환, PDF, 워드, 엑셀, 파워포인트, RAG 전처리, Microsoft, Python, MCP, opendataloader-pdf
  - 링크: [GitHub](https://github.com/microsoft/markitdown) · [PyPI](https://pypi.org/project/markitdown/) · [MCP 서버 패키지](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)
- [DeepInfer — DeepSeek이 공개한 자사 서비스용 대규모 추론 프레임워크](docs/deepinfer.md) · 2026-11-11
  - 요약: DeepSeek이 실제 서비스에 쓰는 추론 프레임워크를 오픈소스로 낸 것. 지금은 DeepSeek-V4.1-Flash의 오프라인 추론을 지원하고, NVIDIA SM100 GPU와 Huawei Ascend 950 NPU에서 돈다. Apache 2.0 라이선스.
  - 태그: DeepInfer, 딥인퍼, DeepSeek, 딥시크, 추론 프레임워크, 추론 엔진, 모델 서빙, DeepSeek-V4.1-Flash, vLLM, deepseek-recipe, 구조화 출력, 결정적 샘플링, Ascend
  - 링크: [GitHub](https://github.com/deepseek-ai/DeepInfer) · [deepseek-recipe (요청·프롬프트·토큰 변환)](https://github.com/deepseek-ai/deepseek-recipe) · [모델(Hugging Face)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [Astryx — Meta가 8년간 내부에서 쓰던 디자인 시스템을 공개한 것 (사람과 에이전트가 같은 도구로 UI 제작)](docs/astryx.md) · 2026-11-11
  - 요약: Meta가 사내에서 8년간 키운 디자인 시스템을 오픈소스로 낸 것. 접근성을 갖춘 React 컴포넌트 150개 이상, 테마, 다크 모드, 템플릿, CLI를 한 묶음으로 준다. CLI와 문서를 사람과 AI 에이전트가 똑같이 쓰도록 설계했다. MIT 라이선스, 현재 베타.
  - 태그: 디자인 시스템, Meta, 메타, React, StyleX, UI 컴포넌트, 테마, 다크 모드, CLI, 에이전트용 UI, 프런트엔드, astryx
  - 링크: [GitHub](https://github.com/meta/astryx) · [공식 사이트·문서](https://astryx.atmeta.com) · [Storybook 데모](https://astryx.atmeta.com/storybook/) · [Sandbox](https://astryx.atmeta.com/sandbox/) · [npm (@astryxdesign/core)](https://www.npmjs.com/package/@astryxdesign/core)
- [agent-desktop — 에이전트가 데스크톱 앱을 직접 조작하게 해 주는 Vercel Labs의 CLI](docs/agent-desktop.md) · 2026-11-11
  - 요약: 화면 캡처 대신 운영체제의 접근성 트리를 읽어 에이전트가 맥·윈도우·리눅스 앱을 누르고 입력하게 해 주는 CLI. 마우스를 움직이거나 포커스를 뺏지 않고 동작하며 MCP 서버로도 쓸 수 있다. Apache-2.0.
  - 태그: agent-desktop, 컴퓨터 사용, computer use, 데스크톱 자동화, 접근성 트리, Vercel Labs, CLI, MCP, Claude Code, Codex, 윈도우 앱 조작
  - 링크: [GitHub](https://github.com/vercel-labs/agent-desktop) · [공식 문서](https://agent-browser.dev/desktop) · [스킬 페이지 (skills.sh)](https://skills.sh/vercel-labs/agent-desktop/agent-desktop)

## 모델 (1)

- [Gemini 4 (Argon·Carbon)와 Gemini 3.8 Flash — 캡처 속 "Gemini 4 Pro" 소문과 실제 출시 내용](docs/gemini-4-argon-carbon.md) · 2026-11-11
  - 요약: Threads에서 "gemini carbon"을 검색한 화면. 아레나에서 가명으로 시험되던 "Gemini 4 Pro" 소문 글과 Gemini 3.8 Flash 발표 정리 글이 보인다. 구글이 실제로 낸 것은 Gemini 4 Argon(2026-10-13)과 Carbon(10-28 발표, 11-10 일반 공개), Gemini 3.8 Flash(09-02)다.
  - 태그: Gemini 4, Gemini 4 Pro, Gemini 4 Argon, Gemini 4 Carbon, gemini carbon, Gemini 3.8 Flash, 구글, Google, 아레나, LMArena, three.js, 모델 가격
  - 링크: [Gemini 4 Argon 발표 글](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/) · [Gemini 4 Carbon 발표 글](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) · [Gemini 4 Carbon 일반 공개 글](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) · [Gemini 3.8 Flash 발표 글](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

## 스킬·플러그인·MCP (10)

- [teardown — 기계를 분해해 볼 수 있는 3D 시뮬레이터로 만들어 주는 Claude Code 스킬](docs/teardown.md) · 2026-11-11
  - 요약: "이건 어떻게 움직여?"라고 물으면 가운데서 기계가 돌아가고 버튼으로 부품을 열어 볼 수 있는 3D 시뮬레이터를 인터넷 없이 열리는 HTML 한 파일로 만들어 주는 Claude Code 스킬. 영상과 효과음도 뽑는다. MIT.
  - 태그: teardown, 3D 시뮬레이터, 분해도, Claude Code 스킬, three.js, HTML 한 파일, 기계 설명, 영상 제작, 로봇 문어
  - 링크: [GitHub](https://github.com/elvarofficial/teardown) · [바탕이 된 저장소 claude-motion](https://github.com/whaleyxbt/claude-motion)
- [Stageshow — 에이전트가 진짜 제품처럼 보이는 가짜 UI 그림과 데모를 만들게 하는 스킬](docs/stageshow.md) · 2026-11-11
  - 요약: 랜딩 페이지나 문서에 넣을 "제품 화면처럼 보이는 그림"(정지 화면, 기능 카드, 커서 데모, 벤토 그리드)을 에이전트가 React로 만들게 돕는 Agent Skill. 결과물을 녹화해 스스로 점검하는 도구까지 들어 있다. MIT 라이선스.
  - 태그: Stageshow, 스테이지쇼, 에이전트 스킬, 제품 UI 일러스트, 벤토 그리드, 커서 데모, 모션 디자인, React, 랜딩 페이지, Benji Taylor
  - 링크: [GitHub](https://github.com/benjitaylor/skills) · [소개 글](https://benji.org/stageshow) · [스킬 본문](https://github.com/benjitaylor/skills/blob/main/stageshow/SKILL.md)
- [pstack — 에이전트가 덜 쓰되 검증된 코드를 내게 하는 Cursor의 스킬 묶음](docs/pstack.md) · 2026-11-11
  - 요약: Cursor의 엔지니어 poteto(Lauren Tan)가 자기가 매일 쓰는 스킬을 공개한 플러그인. `/poteto-mode` 하나가 작업을 23개 플레이북 중 하나에 맞추고 24개 원칙에 따라 재현·수정·검증까지 끌고 간다. Claude Code에도 설치된다. MIT.
  - 태그: pstack, poteto-mode, Cursor 플러그인, 에이전트 스킬, 코딩 워크플로, 플레이북, 원칙, Claude Code, Codex, gstack, 김플립
  - 링크: [GitHub (원본, cursor/plugins의 pstack 폴더)](https://github.com/cursor/plugins/tree/main/pstack) · [다른 에이전트용 포트 pstack-claude](https://github.com/michael-denyer/pstack-claude) · [미러 backnotprop/pstack](https://github.com/backnotprop/pstack)
- [insane-search — 막힌 공개 웹 페이지를 Claude Code가 읽게 해 주는 플러그인](docs/insane-search.md) · 2026-11-11
  - 요약: Claude Code의 기본 웹 가져오기가 403·봇 차단으로 실패할 때, 공개 API·피드 → TLS 흉내 → 실제 헤드리스 브라우저 순으로 단계를 올려 가며 공개 내용을 읽어 오는 플러그인. API 키와 로그인 없이 쓰고, 로그인·유료 벽에서는 멈춘다. MIT 라이선스.
  - 태그: insane-search, 웹 검색, WebFetch, 크롤링, 403 우회, Claude Code 플러그인, GPTaku, 레딧, 트위터 X, 네이버, 쿠팡, 유튜브 자막
  - 링크: [GitHub](https://github.com/fivetaku/insane-search) · [공식 사이트](https://fivetaku.github.io/gptaku_plugins/insane-search/) · [플러그인 마켓플레이스(gptaku_plugins)](https://github.com/fivetaku/gptaku_plugins)
- [insane-design — 사이트 주소 하나로 디자인 시스템을 뽑아 design.md로 만드는 Claude Code 플러그인](docs/insane-design.md) · 2026-11-11
  - 요약: 웹사이트 주소를 주면 실제 CSS를 내려받아 색·글꼴·간격·둥글기·그림자 값을 뽑고, AI 에이전트가 읽을 design.md와 눌러서 복사하는 HTML 리포트를 만들어 주는 Claude Code 플러그인. 미리 분석한 사이트 100곳이 들어 있다. MIT 라이선스.
  - 태그: insane-design, design.md, 디자인 시스템 추출, 디자인 토큰, CSS, Tailwind, Claude Code 플러그인, GPTaku, 바이브 디자인
  - 링크: [GitHub](https://github.com/fivetaku/insane-design) · [갤러리 데모](https://fivetaku.github.io/insane-design/) · [플러그인 마켓플레이스(gptaku_plugins)](https://github.com/fivetaku/gptaku_plugins)
- [Diagram Design — 에이전트가 편집 디자인 수준의 다이어그램을 그리게 하는 스킬](docs/diagram-design.md) · 2026-11-11
  - 요약: 말로 설명하면 에이전트가 HTML+SVG 파일 하나로 다이어그램을 그려 주는 Agent Skill. 45가지 유형을 지원하고, 내 사이트의 색과 글꼴을 뽑아 브랜드에 맞춘다. MIT 라이선스.
  - 태그: 다이어그램, 에이전트 스킬, SVG, Claude Code, Codex, Mermaid 대안, 시각화, 아키텍처 도식
  - 링크: [GitHub](https://github.com/cathrynlavery/diagram-design) · [공식 사이트](https://diagramdesign.dev) · [갤러리 데모](https://cathrynlavery.github.io/diagram-design/) · [변경 내역 문서](https://github.com/cathrynlavery/diagram-design/blob/main/CHANGELOG.md)
- [Dashi PPT Skill — 문서를 주면 브라우저에서 고칠 수 있는 PPT를 만들어 주는 스킬](docs/dashi-ppt-skill.md) · 2026-11-11
  - 요약: 문서를 에이전트에게 주면 웹 화면에서 바로 고칠 수 있는 발표 자료를 만들고, 편집 가능한 PPTX·PDF·HTML로 내보내는 Agent Skill. 테마 12종, 레이아웃 1,020개, 차트와 분석 모델(SWOT 등) 내장. AGPL-3.0.
  - 태그: PPT, 발표 자료, 슬라이드, 에이전트 스킬, PPTX 내보내기, HTML 덱, Claude Code, Codex, 大师PPT, dashi
  - 링크: [GitHub](https://github.com/chuspeeism/dashi-ppt-skill) · [영문 README](https://github.com/chuspeeism/dashi-ppt-skill/blob/main/README.en.md)
- [claude-mem — 코딩 에이전트의 작업을 압축해 다음 세션에 기억으로 넣어 주는 플러그인](docs/claude-mem.md) · 2026-11-11
  - 요약: 에이전트가 세션 중에 읽고 고치고 실행한 것을 옆에서 두 번째 에이전트가 짧은 관찰 기록으로 압축해 두었다가, 다음 세션 시작 때 관련 색인을 넣어 주는 오픈소스 메모리 시스템. Claude Code, Codex, Cursor, OpenCode 등 여러 에이전트 지원. Apache-2.0.
  - 태그: claude-mem, 클로드 멤, 에이전트 메모리, 세션 간 기억, 컨텍스트 주입, Claude Code 플러그인, Codex, Gemini, MCP, SQLite, Chroma, 장기 기억
  - 링크: [GitHub](https://github.com/thedotmack/claude-mem) · [공식 사이트](https://claude-mem.ai) · [문서](https://docs.claude-mem.ai/)
- [Architecture Diagram Generator — 설명만 주면 어두운 테마의 아키텍처 다이어그램을 HTML로 그려 주는 Claude 스킬](docs/architecture-diagram-generator.md) · 2026-11-11
  - 요약: 시스템 구성을 글로 설명하면 Claude가 어두운 테마의 아키텍처 다이어그램을 HTML 파일 하나(인라인 SVG)로 만들어 주는 스킬. 파일 안에 복사·PNG·PDF 내보내기 버튼이 들어 있다. MIT 라이선스.
  - 태그: 아키텍처 다이어그램, architecture-diagram-generator, Cocoon AI, Claude 스킬, SVG, HTML, 시스템 구성도, 시각화, 다크 테마
  - 링크: [GitHub](https://github.com/Cocoon-AI/architecture-diagram-generator) · [만든 곳(Cocoon AI)](https://cocoon-ai.com) · [자매 스킬(프로세스 흐름도)](https://github.com/Cocoon-AI/process-flow-diagram-generator)
- [AI Website Cloner Template — 주소 하나로 웹사이트를 Next.js 앱으로 다시 만드는 템플릿](docs/ai-website-cloner-template.md) · 2026-11-11
  - 요약: 코딩 에이전트에서 `/clone-website 주소`를 실행하면 그 사이트를 살펴보고 Next.js 앱으로 다시 짓는 템플릿 저장소. 원본과 나란히 비교해 차이를 고치는 단계까지 스킬에 들어 있다. MIT.
  - 태그: 웹사이트 복제, clone-website, 사이트 클론, Next.js, 에이전트 스킬, Claude Code, Codex, Cursor, 마이그레이션, 프런트엔드
  - 링크: [GitHub](https://github.com/JCodesMore/ai-website-cloner-template) · [데모 영상](https://youtu.be/O669pVZ_qr0)

## 업계 동향 (2)

- [샘 알트만 YC 강연 (2026) — "석 달 걸리던 일을 코딩 에이전트가 7분에"](docs/sam-altman-startup-school-2026.md) · 2026-11-11
  - 요약: OpenAI CEO 샘 알트만이 YC Startup School 2026에서 한 대담. 예전 YC 회사가 석 달 걸려 만들던 것을 코딩 에이전트가 7분쯤에 만든다, 경력 연차보다 도구를 다루는 유창함·안목·주체성이 중요해진다, 최상위 사용자의 토큰 사용량이 6년 반 사이 월 10만에서 수천억으로 늘었다는 내용.
  - 태그: 샘 알트만, Sam Altman, OpenAI, Y Combinator, YC, Startup School 2026, 코딩 에이전트, 토큰 사용량, 안목, 주체성, 창업
  - 링크: [대담 녹취 (podscripts)](https://podscripts.co/podcasts/y-combinator-startup-podcast/sam-altman-never-a-better-time-to-do-a-startup) · [영상 (YouTube)](https://www.youtube.com/watch?v=ZIaOBAjvc38)
- [GitHub 트렌딩 Top 10 (2026-10-28) — 에이전트 하네스와 디자인 스킬이 대부분](docs/github-trending-2026-10-28.md) · 2026-11-11
  - 요약: 2026-10-28 GitHub 트렌딩 상위 10개를 정리한 Threads 글과, 각 저장소를 GitHub에서 찾아 확인한 정보. 10개 중 3개가 디자인 스킬이고 나머지도 대부분 에이전트 도구다.
  - 태그: GitHub 트렌딩, 오픈소스, 에이전트, 디자인 스킬, thinkrail, DeepTutor, ECC, postiz, cindy, impeccable, superpowers, openbot, hallmark, ai-design-skills
  - 링크: [GitHub 트렌딩 (오늘 기준 목록)](https://github.com/trending)

## 에이전트·하네스 (7)

- [Learn Harness Engineering — 하네스 엔지니어링을 0부터 배우는 프로젝트형 강의](docs/learn-harness-engineering.md) · 2026-11-11
  - 요약: AI 코딩 에이전트가 안정적으로 일하도록 환경·상태 관리·검증·제어 장치를 만드는 법을 가르치는 무료 공개 강의. 강의 14개와 실습 8개, Pi·Claude Code·Codex·DeepSeek 하네스 분석이 있고 한국어를 포함해 15개 언어로 제공된다. MIT.
  - 태그: Learn Harness Engineering, 하네스 엔지니어링, harness engineering, 강의, 튜토리얼, 코딩 에이전트, AGENTS.md, 루프 엔지니어링, 그래프 엔지니어링, Claude Code 하네스 분석, walkinglabs
  - 링크: [GitHub](https://github.com/walkinglabs/learn-harness-engineering) · [강의 사이트](https://walkinglabs.github.io/learn-harness-engineering/) · [관련 목록 (Awesome Harness Engineering)](https://github.com/walkinglabs/awesome-harness-engineering)
- [Energy — 로그인된 브라우저로 업무를 대신 처리하는 데스크톱 AI 에이전트](docs/energy.md) · 2026-11-11
  - 요약: 오픈AI 출신 Gabriel Petersson이 만든 업무용 AI 에이전트 앱. 내 계정으로 로그인된 브라우저와 파일, 메일을 오가며 일을 끝까지 처리한다. 무료 요금제는 이미 쓰는 ChatGPT 요금제로 돌아가고, 내려받기는 macOS만 확인됐다.
  - 태그: Energy, 에너지, getenergy, Gabriel Petersson, 가브리엘 피터슨, 업무 자동화, 브라우저 에이전트, 데스크톱 에이전트, 일반 사용자용 에이전트, ChatGPT 구독 연결, Gmail, Slack, Outlook
  - 링크: [공식 사이트](https://getenergy.com) · [요금 안내](https://getenergy.com/pricing) · [보안 안내(Trust Center)](https://trust.getenergy.com) · [출시 글(X)](https://x.com/gabriel1/status/2085418582192841147)
- [ego lite — 코딩 에이전트와 함께 쓰는 브라우저 (Aside와 비교)](docs/ego-lite.md) · 2026-11-11
  - 요약: Claude Code나 Codex 같은 에이전트가 내 로그인 상태를 그대로 쓰면서, 내 화면을 빼앗지 않고 별도 작업 공간(Space)에서 웹 작업을 하게 해 주는 무료 브라우저. macOS와 Windows를 지원한다. 같은 때 화제가 된 AI 브라우저 Aside와의 차이도 정리했다.
  - 태그: ego lite, 에고 라이트, ego-browser, citrolabs, AI 브라우저, 에이전트 브라우저, 브라우저 자동화, Aside, 어사이드, Claude Code, Codex, 로그인 상태 공유, Windows, Space
  - 링크: [GitHub](https://github.com/citrolabs/ego-lite) · [공식 사이트](https://lite.ego.app) · [문서](https://lite.ego.app/document/) · [Aside 공식 사이트](https://aside.com) · [Aside 문서](https://docs.aside.com)
- [DOT Studio (현재 APM Studio) — 에이전트를 화면에서 조립하고 여러 코딩 도구로 내보내는 로컬 작업실](docs/dot-studio.md) · 2026-11-11
  - 요약: 에이전트마다 시스템 프롬프트·스킬·MCP·모델을 화면에서 조립해 재사용하고 여러 에이전트를 팀으로 묶어 돌리는 오픈소스 로컬 도구. 캡처 속 이름은 dot-studio이지만 저장소가 지금은 apm-studio/apm-studio(APM Studio)로 옮겨졌고 설명도 바뀌었다. MIT.
  - 태그: dot-studio, DOT Studio, Dance of Tal, APM Studio, apm-studio, 멀티에이전트, 에이전트 구성, 퍼포머, OpenCode, Codex 연동, 시스템 프롬프트, 스킬, MCP
  - 링크: [GitHub (현재 이름 APM Studio)](https://github.com/apm-studio/apm-studio) · [DOT Studio 문서](https://dance-of-tal-web.vercel.app/docs/studio) · [Dance of Tal 사이트](https://dance-of-tal-web.vercel.app/)
- [deepseek-bot — DeepSeek Harness에 기억과 메신저 연결을 얹는 플러그인](docs/deepseek-bot.md) · 2026-11-11
  - 요약: DeepSeek가 공개한 에이전트 하네스(DeepSeek Harness, dsh) 위에 대화 간 기억과 Slack·Discord·Telegram 연결만 가볍게 얹은 개인 제작 오픈소스 플러그인. 터미널에서 `dsh`만 치면 기억하는 상시 에이전트가 된다. macOS 전용, MIT.
  - 태그: deepseek-bot, 딥시크봇, DeepSeek Harness, dsh, 에이전트 메모리, 메신저 게이트웨이, Slack, Discord, Telegram, 상시 에이전트, rlaope
  - 링크: [GitHub](https://github.com/rlaope/deepseek-bot) · [설치 문서](https://github.com/rlaope/deepseek-bot/blob/master/docs/setup.md) · [DeepSeek Harness 저장소](https://github.com/deepseek-ai/deepseek-harness) · [DeepSeek Harness 공식 페이지](https://deepseek.com/harness)
- [dzhng/deep-research — 500줄 안쪽으로 만든 가장 단순한 딥 리서치 에이전트](docs/deep-research.md) · 2026-11-11
  - 요약: 질문 하나를 받아 검색, 읽기, 다음 질문 만들기를 되풀이한 뒤 마크다운 보고서를 써 주는 오픈소스 딥 리서치 에이전트. 탐색의 넓이와 깊이를 숫자로 정한다. 구조를 배우거나 내 것으로 고쳐 쓰기 좋게 500줄 안쪽을 목표로 한다. MIT 라이선스.
  - 태그: deep-research, 딥 리서치, Open Deep Research, dzhng, 심층 조사, 보고서 자동 작성, 웹 검색, Firecrawl, 오픈소스 에이전트, TypeScript, 재귀 탐색
  - 링크: [GitHub](https://github.com/dzhng/deep-research) · [Python 구현(커뮤니티)](https://github.com/Finance-LLMs/deep-research-python)
- [Craft Anything — 웹사이트·앱·게임이 어떻게 만들어졌는지 살펴보고 AI로 내 버전을 다시 만드는 도구](docs/craft-anything.md) · 2026-11-11
  - 요약: 대상(웹사이트, 앱, 게임)을 지정하고 원하는 것을 말하면, 원본을 조사하고 코딩 에이전트가 새 프로젝트를 만든 뒤 원본과 비교해 다듬는 오픈소스 도구. 순수 Rust 엔진에 도구 320개가 있고, 데스크톱 앱·CLI·MCP 서버로 쓴다. 기본은 원본 내부를 읽지 않는 클린룸 방식. 초기 알파.
  - 태그: Craft Anything, 복제, 클론, 리버스 엔지니어링, 클린룸, Rust, MCP, Claude Code, 웹사이트 복제, 게임 복제, ArtCraft, REA, 깃허브 트렌드
  - 링크: [GitHub](https://github.com/storytold/craft-anything) · [공식 사이트](https://getartcraft.com/apps/craft-anything) · [내려받기 (릴리스)](https://github.com/storytold/craft-anything/releases) · [한국어 README](https://github.com/storytold/craft-anything/blob/main/README.ko.md) · [현재 상태 문서](https://github.com/storytold/craft-anything/blob/main/docs/STATUS.md)

## 연구·논문 (1)

- [Retrieval as Reasoning (LLM-Wiki) — 문서를 위키로 엮어 에이전트가 돌아다니며 찾게 하는 검색 논문](docs/retrieval-as-reasoning-llm-wiki.md) · 2026-11-11
  - 요약: 문서를 조각내 임베딩으로 한 번 찾아오는 RAG 대신, 문서를 양방향 링크가 달린 위키 페이지로 미리 엮어 두고 에이전트가 검색·읽기·링크 따라가기 도구로 스스로 돌아다니며 근거를 모으게 하는 방법. 위키의 오류를 스스로 찾아 고치는 Error Book도 함께 제안한다. 텐센트 위챗 연구진의 arXiv 논문.
  - 태그: LLM-Wiki, Retrieval as Reasoning, 추론으로서의 검색, RAG, 에이전트 검색, 위키, 양방향 링크, Error Book, 오답 노트, 멀티홉 질의응답, GraphRAG, LightRAG, HippoRAG, 텐센트
  - 링크: [논문 (arXiv)](https://arxiv.org/abs/2605.25480) · [논문 HTML 판](https://arxiv.org/html/2605.25480) · [논문 PDF](https://arxiv.org/pdf/2605.25480)

## 프롬프트·컨텍스트 (5)

- [Swagger → SDK → 프런트엔드 한 번에 — Swagger를 AI의 컨텍스트이자 하네스로 쓰는 방법 (Nestia)](docs/swagger-sdk-ai-frontend.md) · 2026-11-11
  - 요약: 백엔드에 잘 쓴 Swagger 문서가 있으면 그것을 타입이 있는 SDK로 바꿔 AI에게 주라는 글. SDK가 맥락(타입·주석), 제약(컴파일 오류), 검증(서버 없는 목업)을 한꺼번에 제공해, 쇼핑몰 프런트엔드 전체를 프롬프트 하나로 만들었다고 주장한다.
  - 태그: Swagger, OpenAPI, SDK, Nestia, typia, 프런트엔드 자동화, 컨텍스트 엔지니어링, 하네스, TypeScript, 목업 시뮬레이터, samchon, AutoBe
  - 링크: [원문(dev.to)](https://dev.to/samchon/nestia-well-designed-backend-fully-automated-frontend-development-45d9) · [데모 저장소(samchon/shopping)](https://github.com/samchon/shopping) · [프런트엔드용 프롬프트(CLAUDE.md)](https://github.com/samchon/shopping/blob/master/packages/frontend/CLAUDE.md) · [Nestia GitHub](https://github.com/samchon/nestia) · [Nestia Editor 문서](https://nestia.io/docs/swagger/editor)
- [Say who owns the code — Claude Fable 5.2에게 "이 코드는 네 것"이라고 알려 주면 중복 코드를 더 정리한다](docs/fable-5-2-code-ownership-prompt.md) · 2026-11-11
  - 요약: Anthropic 공식 프롬프트 안내의 한 대목. Claude Fable 5.2는 프롬프트가 코드의 주인을 누구라고 하느냐에 따라 행동이 달라져서, 코드베이스가 모델 자신의 것이라고 한 문장 적어 주면 중복 코드를 합치는 비율이 10% 미만에서 절반쯤으로 오른다. 대신 토큰을 더 쓰고 시키지 않은 변경도 늘어난다.
  - 태그: 프롬프트, Claude Fable 5.2, Anthropic, 코드 소유권, 코드베이스 소유, 중복 코드 정리, 리팩터링, 시스템 프롬프트, 코딩 에이전트, Say who owns the code
  - 링크: [문서 (해당 대목)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#say-who-owns-the-code) · [문서 (Prompting Claude Fable 5.2 전체)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) · [문서 (Claude Fable 5.2 모델 소개)](https://platform.claude.com/docs/en/models/fable-5-2/overview)
- [Awesome DESIGN.md — 유명 사이트의 디자인 시스템을 DESIGN.md로 모아 둔 저장소](docs/awesome-design-md.md) · 2026-11-11
  - 요약: Apple, Stripe, Spotify, IBM, NVIDIA 같은 사이트의 색·글꼴·간격·컴포넌트 규칙을 DESIGN.md 파일 하나씩으로 정리해 둔 모음. 파일을 프로젝트에 넣고 코딩 에이전트에게 "이대로 만들어"라고 하면 그 스타일에 맞춘 화면을 만든다. MIT 라이선스.
  - 태그: DESIGN.md, awesome-design-md, VoltAgent, 디자인 시스템, 디자인 토큰, Google Stitch, 바이브 디자인, getdesign.md, UI 생성
  - 링크: [GitHub](https://github.com/VoltAgent/awesome-design-md) · [공식 사이트](https://getdesign.md/) · [DESIGN.md 형식 문서(Google Stitch)](https://stitch.withgoogle.com/docs/design-md/overview/)
- [추론 유지와 압축 — OpenAI가 설정 두 개로 ARC-AGI-3 점수를 3배 올린 방법](docs/arc-agi-3-retained-reasoning-compaction.md) · 2026-11-11
  - 요약: OpenAI가 GPT-5.6 Sol을 ARC-AGI-3 공개 세트에 돌릴 때, 모델은 그대로 두고 "이전 추론을 버리지 않기"와 "오래된 대화를 자르지 않고 요약하기" 두 설정만 켜서 13.3%를 38.3%로 올렸다는 발표. 긴 에이전트 작업에서 컨텍스트를 어떻게 넘기느냐가 성능을 크게 좌우한다는 사례다.
  - 태그: 추론 유지, retained reasoning, 압축, compaction, 컨텍스트 관리, Responses API, previous_response_id, GPT-5.6 Sol, ARC-AGI-3, 벤치마크, 하네스, OpenAI
  - 링크: [OpenAI 발표 글](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/) · [압축(compaction) 문서](https://developers.openai.com/api/docs/guides/compaction) · [ARC-AGI-3 공개 게임](https://arcprize.org/tasks)
- [andrej-karpathy-skills — Karpathy의 관찰을 네 가지 원칙으로 옮긴 CLAUDE.md 한 장](docs/andrej-karpathy-skills.md) · 2026-11-11
  - 요약: Andrej Karpathy가 지적한 LLM 코딩의 흔한 실수(멋대로 가정, 과한 설계, 상관없는 코드 건드리기)를 막으려고 네 가지 원칙을 CLAUDE.md 파일 하나에 적어 둔 저장소. 프로젝트에 파일을 넣거나 Claude Code 플러그인으로 설치한다. Cursor 규칙 파일도 들어 있다.
  - 태그: CLAUDE.md, Karpathy, 카파시, Claude Code, Cursor, 코딩 지침, 에이전트 규칙, 최소 수정, 과잉 설계 방지, 플러그인, karpathy-guidelines
  - 링크: [GitHub](https://github.com/multica-ai/andrej-karpathy-skills) · [CLAUDE.md 원문](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md) · [Cursor 안내 문서](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CURSOR.md) · [바탕이 된 Karpathy의 X 글](https://x.com/karpathy/status/2015883857489522876)

## 활용 사례 (1)

- [바이브코딩으로 만든 앱 배포하기 — 웹앱과 백엔드별 배포 서비스 정리](docs/vibe-coding-deploy-options.md) · 2026-11-11
  - 요약: 바이브코딩으로 앱은 만들었는데 어떻게 배포하느냐는 질문에 답하는 Threads 정리 글. 웹앱은 Vercel·Netlify·Cloudflare Pages, 백엔드가 있으면 Railway·Render·Supabase를 쓰고, GitHub에 연결하면 푸시할 때마다 자동 배포된다는 내용이다.
  - 태그: 배포, 바이브코딩, Vercel, Netlify, Cloudflare Pages, Railway, Render, Supabase, 호스팅, 무료 요금제
  - 링크: [Vercel 요금](https://vercel.com/pricing) · [Railway 요금](https://railway.com/pricing) · [Render 요금](https://render.com/pricing)
