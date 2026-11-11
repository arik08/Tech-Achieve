---
title: Diagram Design — 에이전트가 편집 디자인 수준의 다이어그램을 그리게 하는 스킬
category: 스킬·플러그인·MCP
tags: [다이어그램, 에이전트 스킬, SVG, Claude Code, Codex, Mermaid 대안, 시각화, 아키텍처 도식]
date: 2026-11-11
released: 2026-04-16
checked: 2026-11-11
summary: 말로 설명하면 에이전트가 HTML+SVG 파일 하나로 다이어그램을 그려 주는 Agent Skill. 45가지 유형을 지원하고, 내 사이트의 색과 글꼴을 뽑아 브랜드에 맞춘다. MIT 라이선스.
cover: https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/docs/screenshots/architecture.png
origin: https://github.com/cathrynlavery/diagram-design
links:
  - GitHub | https://github.com/cathrynlavery/diagram-design
  - 공식 사이트 | https://diagramdesign.dev
  - 갤러리 데모 | https://cathrynlavery.github.io/diagram-design/
  - 변경 내역 문서 | https://github.com/cathrynlavery/diagram-design/blob/main/CHANGELOG.md
---

## 한눈에 보기

- 코딩 에이전트에 설치하는 **Agent Skill**입니다. "프런트엔드, 백엔드, DB, Redis 캐시로 된 아키텍처 그려 줘"처럼 말하면 에이전트가 유형을 고르고, 더블클릭으로 열리는 `.html` 파일 하나를 만듭니다.
- 만든 사람은 Cathryn Lavery(회사 LittleMight)입니다. 블로그 글에 넣을 도식을 모델에게 시키면 흔한 둥근 상자 그림만 나와서, 원하는 "취향"을 규칙으로 적어 둔 것이 출발점이라고 README에 밝혔습니다.
- 조사 시점(2026-11-11) 기준 GitHub 별 약 66,400개, 포크 약 4,400개, 플러그인 버전 2.6.153입니다. 공개 시기는 저장소 생성일인 2026-04-16을 기준으로 적었습니다(첫 릴리스 날짜는 따로 확인하지 않았습니다). 조사 전날(11-10)까지 커밋이 올라왔습니다.

![스킬로 그린 아키텍처 다이어그램 예시](https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/docs/screenshots/architecture.png)

## 핵심 내용

### 디자인 규칙

README가 밝힌 원칙은 다음과 같습니다.

- 강조색은 독자가 먼저 봐야 할 한두 곳에만 씁니다.
- 선은 1px, 그림자는 쓰지 않습니다.
- 모든 좌표를 4px 격자에 맞춥니다.
- 목표 밀도는 10점 만점에 4. "가장 품질을 높이는 방법은 대개 지우는 것"이라고 합니다.

### 결과물

- 인라인 SVG가 들어간 HTML 파일 하나입니다. 빌드 과정도 JavaScript도 외부 이미지도 없습니다.
- 유형마다 밝은 최소형, 어두운 최소형, 전체 편집형 세 가지 변형이 있습니다.
- SVG와 PNG로 내보낼 수 있습니다(`/export-diagram`).
- 기본 설정에서는 Google Fonts에서 글꼴(Instrument Serif, Geist, Geist Mono)을 불러오는 것이 유일한 네트워크 요청입니다. 시스템 글꼴로 바꾸면 요청이 전혀 없습니다. 사내망처럼 외부 접속이 막힌 곳에서는 이 설정이 필요합니다.
- SVG에 `role="img"`와 제목·설명을 넣어 접근성을 챙깁니다.

### 지원 유형 (45가지)

| 묶음 | 유형 |
|---|---|
| 구조 | 아키텍처, IT 현황, 배포, 레이어 스택, 중첩, 트리, 조직도, 의존성 그래프, 아키텍처 변경 전후 비교 |
| 흐름 | 플로차트, 시퀀스, 상태 기계, 스윔레인, 프로세스, 데이터 흐름, 루프·플라이휠, 사용자 여정, 서비스 블루프린트 |
| 데이터 모델 | ER, 데이터베이스 스키마, UML 클래스, 메달리온, 데이터 플랫폼 통합·보안 매트릭스 |
| 차트 | 막대, 선, 산점도, 트리맵, 생키, 히트맵, 레이더, 극좌표, 폭포 |
| 계획·전략 | 타임라인, 간트, 칸반, 스토리 맵, 사분면, 워들리 맵, 벤, 피라미드·깔때기, 피시본 |
| 입체 | 분해 축측도(부품을 한 축으로 띄운 그림), 축측 평면도(사무실·캠퍼스) |

묶음은 이 문서에서 보기 좋게 나눈 것이고, 저장소는 01~45번 번호로 관리합니다. 일부 유형은 변형을 포함합니다(선 차트에 슬로프그래프·범프 차트, 산점도에 버블·박스 플롯 등).

### 브랜드 맞추기 (온보딩)

"onboard diagram-design to https://내사이트" 라고 하면 에이전트가 홈페이지를 읽어 주요 색과 글꼴을 뽑고, 이를 `paper`, `ink`, `muted`, `accent` 같은 역할에 대응시킨 뒤 바뀔 내용을 보여 주고 `references/style-guide.md`에 씁니다.

- 쓰기 전에 본문색과 배경색의 WCAG AA 대비를 검사하고, 기준에 못 미치면 조정값을 제안합니다.
- 새 프로젝트에서 스타일 가이드가 기본값 그대로면 첫 다이어그램 전에 온보딩할지 묻습니다.
- 여러 고객사를 다룰 때는 브랜드를 이름 붙은 프로필로 저장하고(`~/.diagram-design/profiles/`), 프로젝트마다 `.diagram-design` 표식 파일로 프로필을 지정합니다.

### 기존 도구와 비교 (README의 비교표 요약)

| | Mermaid / PlantUML | draw.io / Excalidraw | Diagram Design |
|---|---|---|---|
| 만드는 법 | 텍스트 작성 | 손으로 도형 배치 | 에이전트에게 설명 |
| 배치 | 자동 | 수동 | 에이전트가 4px 격자에 배치 |
| 결과물 | GitHub에서 렌더되는 텍스트 | 편집 가능한 원본 파일 | 인라인 SVG가 든 HTML 한 개 |
| 기존 도식 | | | Mermaid, draw.io, Excalidraw, PlantUML 파일을 다시 그려 줌 |

## 써 보려면

Agent Skills를 읽는 호스트(Cursor, Claude Code, Codex, GitHub Copilot, Gemini CLI, Cline, Windsurf 등) 공통:

```bash
npx skills add cathrynlavery/diagram-design
```

Claude Code에서는 플러그인 마켓플레이스로 설치하면 업데이트와 슬래시 명령까지 함께 받습니다.

```text
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
```

Codex:

```bash
codex plugin marketplace add cathrynlavery/diagram-design
codex plugin add diagram-design@diagram-design
```

- 슬래시 명령: `/export-diagram`, `/import-mermaid`, `/import-drawio`, `/import-excalidraw`, `/import-plantuml`, `/profile`, `/doctor`. `npx skills add`로 설치하면 스킬만 들어오고 이 명령들은 빠집니다.
- 스타일 가이드를 직접 고쳐 쓰려면 저장소를 clone해서 `skills/diagram-design` 폴더를 `~/.claude/skills/diagram-design`으로 연결하는 방법을 안내합니다. 패키지로 설치한 경우 업데이트 때 스타일 가이드 수정이 덮어써질 수 있습니다.
- 라이선스는 MIT입니다.

## 눈여겨볼 점

- README가 스스로 밝힌 한계: 결과 품질은 쓰는 모델에 좌우되고, 같은 요청도 배치가 달라질 수 있습니다. 결과물은 편집용 원본 형식이 아니어서 PR에서 텍스트로 비교하거나 캔버스에서 상자를 끌 수 없습니다. Git에 두고 자주 바뀌는 문서용 도식에는 Mermaid가 여전히 더 맞고, 이 스킬은 "발행할 그림"용이라고 합니다.
- 공식 빌드는 이 저장소에서만 나온다고 명시합니다. 다른 이름으로 올라온 플러그인 목록은 비공식 복사본입니다.
- 스킬이 네트워크로 보내는 내용은 저장소의 `PRIVACY.md`에 있다고 하나, 이번 조사에서 그 파일은 열어 보지 않았습니다.
- 실제 설치와 결과 품질은 직접 확인하지 않았습니다. 위 내용은 저장소 README와 메타데이터를 읽은 것입니다.

## 출처

- [cathrynlavery/diagram-design 저장소 README](https://github.com/cathrynlavery/diagram-design) — 기능, 설치 방법, 유형 목록, 비교표, 한계
- [GitHub 저장소 API 정보](https://api.github.com/repos/cathrynlavery/diagram-design) — 별·포크 수, 생성일, 최근 커밋일, 라이선스 (2026-11-11 조회)
- [.claude-plugin/plugin.json](https://github.com/cathrynlavery/diagram-design/blob/main/.claude-plugin/plugin.json) — 플러그인 버전, 만든 사람
- [diagramdesign.dev](https://diagramdesign.dev), [갤러리](https://cathrynlavery.github.io/diagram-design/) — 주소가 열리는 것만 확인
