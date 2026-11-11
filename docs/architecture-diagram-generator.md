---
title: Architecture Diagram Generator — 설명만 주면 어두운 테마의 아키텍처 다이어그램을 HTML로 그려 주는 Claude 스킬
category: 스킬·플러그인·MCP
tags: [아키텍처 다이어그램, architecture-diagram-generator, Cocoon AI, Claude 스킬, SVG, HTML, 시스템 구성도, 시각화, 다크 테마]
date: 2026-11-11
released: 2025-12-22
checked: 2026-04-16
summary: 시스템 구성을 글로 설명하면 Claude가 어두운 테마의 아키텍처 다이어그램을 HTML 파일 하나(인라인 SVG)로 만들어 주는 스킬. 파일 안에 복사·PNG·PDF 내보내기 버튼이 들어 있다. MIT 라이선스.
cover: https://raw.githubusercontent.com/Cocoon-AI/architecture-diagram-generator/main/examples/images/microservices.png
links:
  - GitHub | https://github.com/Cocoon-AI/architecture-diagram-generator
  - 만든 곳(Cocoon AI) | https://cocoon-ai.com
  - 자매 스킬(프로세스 흐름도) | https://github.com/Cocoon-AI/process-flow-diagram-generator
---

## 한눈에 보기

- Claude에 올려 쓰는 **스킬**입니다. "React 프런트엔드, Node.js API, PostgreSQL, Redis" 같은 설명을 주면 브라우저에서 바로 열리는 HTML 다이어그램을 만듭니다.
- 만든 곳은 Cocoon AI입니다.
- 공개 시기는 저장소 생성일이자 첫 릴리스(1.0)일인 2025-12-22를 기준으로 적었습니다. 최신 릴리스는 1.1(2026-05-09)입니다. 캡처(2026-04-16)의 링크 카드에는 별 2k, 포크 166개로 보였고, 지금은 별 7,570개, 포크 578개입니다 (2026-11-11 조회).

![마이크로서비스 예시 다이어그램](https://raw.githubusercontent.com/Cocoon-AI/architecture-diagram-generator/main/examples/images/microservices.png)

## 핵심 내용

### 쓰는 흐름 (README의 3단계)

1. 스킬을 설치합니다.
2. 시스템을 설명하는 글을 마련합니다. 코딩 에이전트에게 코드베이스를 분석해 구성 요소와 연결을 목록으로 적게 하거나, 직접 몇 줄로 쓰거나, Claude에게 "SaaS의 전형적인 아키텍처"를 물어 출발점으로 삼습니다.
3. 그 글을 붙이고 "architecture diagram 스킬로 그려 줘"라고 합니다. 이어서 대화로 "○○을 추가해 줘"처럼 고쳐 나갑니다.

### 결과물

- CSS와 인라인 SVG가 들어간 HTML 파일 하나입니다. 글꼴(JetBrains Mono)만 Google Fonts에서 불러옵니다.
- 구성: 제목 머리말, 다이어그램 본체, 요약 카드 3개, 꼬리말.
- 머리말의 버튼으로 내보냅니다: 복사(고해상도 PNG를 클립보드로), PNG 저장, PDF 저장(어두운 테마 유지).
- 배경은 `#020617`에 40px 격자 무늬이고, 화살표를 먼저 그려 상자 뒤로 깔끔하게 지나가게 합니다.

### 색 규칙

| 종류 | 색 | 쓰는 곳 |
|---|---|---|
| 프런트엔드 | 청록(Cyan) | 클라이언트 앱, UI, 엣지 기기 |
| 백엔드 | 초록(Emerald) | 서버, API, 서비스 |
| 데이터베이스 | 보라(Violet) | DB, 저장소, AI/ML |
| 클라우드/AWS | 호박색(Amber) | 클라우드 서비스, 인프라 |
| 보안 | 장미색(Rose) | 인증, 보안 그룹, 암호화 |
| 외부 | 회청색(Slate) | 일반, 외부 시스템 |

## 써 보려면

**Claude.ai**: 저장소의 `architecture-diagram.zip`을 받아 Customize → Skills → + → Create skill → Upload a skill로 올리고 켭니다. README는 Free, Pro, Max, Team, Enterprise 요금제에서 쓸 수 있고, 먼저 설정에서 Code Execution을 켜야 한다고 안내합니다.

**Claude Code**: 스킬 폴더에 풉니다.

```bash
# 전역
unzip architecture-diagram.zip -d ~/.claude/skills/
# 프로젝트 전용
unzip architecture-diagram.zip -d ./.claude/skills/
```

스킬의 실체는 `SKILL.md`와 `resources/template.html` 두 파일입니다. 라이선스는 MIT입니다.

## 눈여겨볼 점

- 캡처의 글은 "Hermes에서는 스킬을 받아 `/architecture-digram` 프롬프트로도 가능하다고 한다"고 적었습니다. README에는 Hermes에 관한 내용이 없어 확인하지 못했습니다.
- 캡처에 붙은 예시 그림(채널 관리자, 쿼리 엔진, 도구 등록소 등이 있는 에이전트 구조도)이 어떤 시스템을 그린 것인지는 캡처에 설명이 없어 확인하지 못했습니다.
- 어두운 테마 한 가지와 아키텍처 구성도에 맞춰진 스킬입니다. 유형이 다양하고 밝은 테마, 브랜드 맞춤이 필요하면 보관함의 [Diagram Design](diagram-design.md)과 비교해 볼 만합니다. 순서가 있는 업무 흐름은 같은 곳의 자매 스킬 process-flow-diagram-generator를 쓰라고 README가 안내합니다.
- Google Fonts를 불러오므로 외부 접속이 막힌 곳에서는 글꼴이 기본 글꼴로 바뀔 수 있습니다(직접 시험하지 않음).
- 실제 설치와 결과 품질은 직접 확인하지 않았습니다.

## 받은 캡처

![ai.corder의 소개 글과 저장소 링크 카드](img/architecture-diagram-generator/Screenshot_20260416_073755_Threads.jpg)

캡처 2026-04-16

## 출처

- [Cocoon-AI/architecture-diagram-generator 저장소 README](https://github.com/Cocoon-AI/architecture-diagram-generator) — 사용 흐름, 결과물 구성, 색 규칙, 설치 방법
- [GitHub 저장소 API 정보](https://api.github.com/repos/Cocoon-AI/architecture-diagram-generator) — 생성일, 별·포크 수, 릴리스 목록, 라이선스 (2026-11-11 조회)
- [cocoon-ai.com](https://cocoon-ai.com), [process-flow-diagram-generator](https://github.com/Cocoon-AI/process-flow-diagram-generator) — 주소가 열리는 것만 확인
- Threads ai.corder 글(캡처) — 소개 문구, 당시 별·포크 수. 원문 주소는 `github.com/Cocoo...`까지만 보임
