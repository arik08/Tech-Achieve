---
title: Stageshow — 에이전트가 진짜 제품처럼 보이는 가짜 UI 그림과 데모를 만들게 하는 스킬
category: 스킬·플러그인·MCP
tags: [Stageshow, 스테이지쇼, 에이전트 스킬, 제품 UI 일러스트, 벤토 그리드, 커서 데모, 모션 디자인, React, 랜딩 페이지, Benji Taylor]
date: 2026-11-11
released: 2026-10-31
checked: 2026-11-03
summary: 랜딩 페이지나 문서에 넣을 "제품 화면처럼 보이는 그림"(정지 화면, 기능 카드, 커서 데모, 벤토 그리드)을 에이전트가 React로 만들게 돕는 Agent Skill. 결과물을 녹화해 스스로 점검하는 도구까지 들어 있다. MIT 라이선스.
cover: https://raw.githubusercontent.com/benjitaylor/skills/main/.github/assets/stageshow.png
links:
  - GitHub | https://github.com/benjitaylor/skills
  - 소개 글 | https://benji.org/stageshow
  - 스킬 본문 | https://github.com/benjitaylor/skills/blob/main/stageshow/SKILL.md
---

## 한눈에 보기

- 코딩 에이전트에 설치하는 **Agent Skill**입니다. 실제 제품을 조작하는 것이 아니라, 랜딩 페이지·문서에 넣을 "제품 화면처럼 보이는 가짜 UI"(정지 그림, 기능 카드, 커서가 움직이는 데모, 벤토 그리드)를 React로 만들게 합니다.
- 만든 사람은 Benji Taylor입니다(저장소 소유자, 라이선스 저작권자). 캡처한 글은 그를 "X의 디자인 책임자"라고 소개하지만, 이번에 열어 본 저장소와 소개 글에는 직함이 적혀 있지 않아 확인하지 못했습니다.
- 공개 시기는 소개 글 날짜인 2026-10-31을 기준으로 적었습니다. 저장소는 2026-10-26에 만들어졌고, `stageshow` 폴더의 가장 이른 커밋은 2026-10-30(UTC)입니다. 별 3,053개, 포크 205개(2026-11-11 조회).

![Stageshow로 만든 제품 UI 그림 모음](https://raw.githubusercontent.com/benjitaylor/skills/main/.github/assets/stageshow.png)

## 핵심 내용

### 무엇을 해결하나

소개 글에 따르면 요즘 모델은 이런 가짜 UI를 이미 만들 수 있지만 결과가 엉성해 보이는 경우가 많고, Stageshow는 그 차이를 줄이려는 것입니다. 중심 생각은 "데모는 진짜 제품처럼 읽혀야 하고, 보는 사람에게 필요한 만큼만 단순화하고, 모든 움직임에는 원인이 있어야 한다"입니다.

### 들어 있는 것

| 폴더 | 내용 |
|---|---|
| `SKILL.md`, `references/` | 구도·모션에 대한 판단 기준, API, 검증 방법 |
| `kit/` | 그대로 복사해 쓰는 React 컴포넌트와 스타일 (`Stage`, `Window` 등) |
| `examples/` | 모범 예시. Figma, Linear, Slack, Raycast 등 실제 제품을 본뜬 습작 포함 |
| `teaching/` | 일부러 틀리게 만든 것과 고친 것을 짝지은 교재 |
| `scripts/` | 결과물을 녹화하고 점검하는 도구 |
| `playground/` | 예시를 재생·일시정지·한 프레임씩 넘겨 보는 로컬 뷰어 |

### 작업 흐름

1. **코드 전에 계획**: 매체, 시각 스타일, 이야기와 장면(beat), 가장 가까운 모범 예시 고르기, 화면에 넣을 최소한의 실제 문구, 안무(겹치는 장면, 시작으로 돌아오는 반복), 리허설의 일곱 단계.
2. **만들기**: 데모는 상태(state)로 움직이는 React 무대입니다. 스크립트가 한 장면씩 상태를 바꾸고, 커서는 요소의 이름을 보고 움직입니다. `a.click()`은 클릭 효과만 그리고 `a.set()`이 장면을 바꿉니다. 실제 앱을 자동 조작하는 것이 아닙니다.
3. **녹화해서 점검**: `film.mjs`가 데모를 찍어 장면 모음과 측정 보고서를 만들고, `jumps.mjs`는 한 프레임 만에 튀는 움직임을, `layout.mjs`는 글자와 컨트롤이 넘치는지를 잡습니다. 그 뒤 에이전트가 재생 화면을 직접 보고 휴대폰 폭(358px)과 반복 이음매도 확인합니다.
4. **되풀이**: 만든 사람도 대부분의 데모가 몇 차례 피드백을 거친다고 적었습니다. 고친 내용은 스킬의 새 규칙으로 들어갑니다.

### 스킬 있을 때와 없을 때

소개 글은 같은 짧은 요청을 스킬을 준 에이전트와 안 준 에이전트에 각각 시켜 나란히 보여 줍니다(API 문서 도식, 어두운 벤토 그리드, AI 글쓰기 앱, 대시보드, iPhone 메시지, 두 화면 회의 데모의 여섯 쌍). 만든 사람의 눈으로 본 비교이고 수치는 없습니다.

캡처한 글은 "Figma, Gmail 등의 화면을 재현한 테스트에서도 결과가 더 좋았다"고 했습니다. 1차 자료에서 확인한 것은 Figma·Linear·Slack·Raycast 등이 **예시 습작**으로 들어 있다는 점까지이고, Gmail 테스트는 확인하지 못했습니다.

## 써 보려면

```sh
npx skills add benjitaylor/skills --skill stageshow
```

예시를 직접 보려면 `stageshow` 폴더에서 다음을 실행합니다(Node 20.19 이상).

```sh
npm install
npm run dev
```

- Windows에서는 Vite가 바로 뜨고, 출력되는 로컬 주소(보통 `http://127.0.0.1:5173`)를 엽니다.
- kit은 React 18 이상에서 동작하고 별도 애니메이션 라이브러리가 필요 없습니다. 녹화 도구는 `playwright-core`와 PC에 설치된 Chrome을 씁니다.
- 일부 예시는 `lucide-react` 아이콘을 씁니다.
- 라이선스: `stageshow` 폴더에 MIT 라이선스 파일이 있습니다. 저장소 전체에는 라이선스가 지정되어 있지 않고 "스킬마다 자체 라이선스를 포함한다"고 적혀 있습니다. 제3자 이름·자산은 `NOTICE.md`를 보라고 합니다.

## 눈여겨볼 점

- 결과물은 "그려 낸 삽화"입니다. 실제 서비스 화면 캡처나 동작하는 프로토타입이 아닙니다.
- README는 "자동 점검이 깨끗해도 움직임을 직접 보는 것을 대신할 수 없다"고 밝힙니다.
- 실제 제품을 본뜬 예시를 그대로 공개물에 쓰면 상표 문제가 생길 수 있으니 `NOTICE.md`를 먼저 봐야 합니다. 이번 조사에서 그 파일은 열어 보지 않았습니다.
- 직접 설치해 결과 품질을 확인하지는 않았습니다.
- 이미 다른 사람이 만든 변형이 있습니다(검색으로 이름만 확인): Svelte 5용 `maven-ammar/svelte-stageshow`, React 없이 쓰는 `rizaardiyanto1412/stageshow-js`.

## 받은 캡처

![Stageshow를 소개하는 Threads 글](img/stageshow/Screenshot_20261103_110901_Threads.jpg)

캡처 2026-11-03

## 출처

- [benjitaylor/skills 저장소 README](https://github.com/benjitaylor/skills) — 스킬 설명, 설치 명령
- [stageshow/README.md](https://github.com/benjitaylor/skills/blob/main/stageshow/README.md) — 미리 보기 방법, kit 사용법, 검증 명령, 폴더 구성
- [Stageshow 소개 글 (benji.org)](https://benji.org/stageshow) — 글 날짜(2026-10-31), 작업 흐름, 스킬 유무 비교
- [GitHub 저장소 API 정보](https://api.github.com/repos/benjitaylor/skills) — 별·포크 수, 생성일 (2026-11-11 조회)
- Threads 글(choi.openai) 캡처 — 출발점. 원문 주소는 캡처에 보이지 않음
