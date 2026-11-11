---
title: DeepSeek Harness (dsh) — 모든 부품이 플러그인인 DeepSeek의 오픈소스 에이전트 하네스
category: 에이전트·하네스
tags: [DeepSeek Harness, 딥시크 하네스, dsh, DeepSeek, 딥시크, 에이전트 하네스, 코딩 에이전트, Cordis, 플러그인, Everything is a Plugin, 데스크톱 앱, Web UI, 서브에이전트, MCP, ACP, Python SDK, 오픈소스]
date: 2026-11-11
released: 2026-08-13
checked: 2026-11-11
summary: DeepSeek가 MIT로 공개한 에이전트 하네스. 모델 연결, 도구, 세션 기록, 에이전트 루프까지 전부 플러그인이라 설정만으로 갈아 끼울 수 있다. 데스크톱 앱(macOS·Windows)과 `npx @deepseek-ai/dsh web`으로 쓰며, 아직 개발자 미리보기 단계다.
cover: https://www.deepseek.com/harness/images/deepseek-harness-social.jpg
links:
  - GitHub | https://github.com/deepseek-ai/deepseek-harness
  - 공식 사이트 | https://www.deepseek.com/en/harness/
  - 개발자 문서 | https://deepseek-harness.github.io/deepseek-harness/
  - Cordis (바탕 프레임워크) | https://github.com/cordiverse/cordis
  - Cordis 논문 | https://arxiv.org/abs/2608.25512
  - 커뮤니티 플러그인 (GitHub 토픽) | https://github.com/topics/dsh-plugin
---

## 한눈에 보기

- **DeepSeek Harness**(명령 이름 `dsh`)는 DeepSeek AI가 만든 오픈소스 **에이전트 하네스**(모델에 도구·기억·실행 환경을 붙여 실제로 일을 하게 만드는 프로그램)입니다. 코드 작성뿐 아니라 문서 정리, 표 분석, 자료 조사, 예약 작업까지 맡기는 용도로 소개합니다.
- 가장 큰 특징은 **"Everything is a Plugin"**입니다. 모델 연결부, 도구 목록, 세션 기록, 에이전트 루프 자체까지 모두 플러그인이어서, 고정된 핵심부를 고치지 않고 설정으로 바꿔 끼웁니다.
- 공개 시기는 GitHub 저장소 생성일 2026-08-13을 기준으로 적었습니다. npm 패키지 `@deepseek-ai/dsh`의 첫 버전(0.0.1-rc.1)은 2026-08-10, GitHub의 첫 릴리스(`dsh-v0.1.0-rc.7`)는 2026-08-17입니다. 공식 발표 글의 날짜는 확인 못 함.
- 별 278,738개, 포크 34,283개, 주 언어 TypeScript, MIT 라이선스(2026-11-11 조회).

![DeepSeek Harness 공식 소개 이미지](https://www.deepseek.com/harness/images/deepseek-harness-social.jpg)

## 핵심 내용

### 전부 플러그인이라는 구조

- 바탕은 **Cordis**라는 프레임워크입니다. 플러그인이 공용 컨텍스트에 서비스, 이벤트, "되돌릴 수 있는 효과"를 등록하고, 플러그인을 내리면 등록한 것이 함께 풀립니다. 설계는 논문 *A Programming Paradigm for Spatiotemporal Composability*에 설명돼 있다고 README가 밝힙니다.
- 구조 문서의 표현으로는 "고칠 특권적 핵심부가 없다"입니다. 기능을 더하려면 다른 플러그인 옆에 새 플러그인을 올립니다.
- 실행 중인 `dsh`는 부팅할 때 여러 겹을 순서대로 쌓아 만든 플러그인 나무입니다.

| 용어 | 뜻 |
|---|---|
| 프로필(profile) | 이름이 붙은 구성. 어떤 번들을 쌓을지, 따로 설치한 플러그인, 사용자의 덮어쓰기 설정(`cordis.patch.yml`)을 담습니다 |
| 번들(bundle) | 설정 줄과 그 코드를 묶어 배포하는 단위. 위에 쌓인 겹이 다시 고칠 수 있습니다 |
| 패치(patch) | 설정 줄 하나를 통째로 바꾸거나 새 줄을 넣는 덮어쓰기 |
| 솔기(seam) | 갈아 끼울 수 있는 능력. 인터페이스 정의, 구현 제공자, 사용처 세 역할로 이뤄집니다 |

- 기본 제공 프로필은 `web`(브라우저 화면), `headless`(한 번 실행하고 끝), `sdk`·`sdk-minimal`(JSON-RPC 서버), `acp`(자동화용 ACP 서버)입니다. `dsh --profile web --dump-config`로 내 PC에서 뜨는 플러그인 나무를 볼 수 있습니다.
- 솔기 덕분에 제공자 하나만 바꿔도 제품 전체가 따라 바뀐다고 설명합니다. 예를 들어 파일시스템·프로세스 제공자를 원격 샌드박스로 돌리면 Bash, 터미널, LSP가 함께 옮겨 갑니다.

### 세션 기록이 곧 모델이 보는 것

- 세션은 덧붙이기만 하는 이벤트 기록(JSONL)입니다. 모델에 보내는 대화 이력은 이 기록에서 계산해 냅니다.
- 원칙은 **"모델이 본 것은 모두 기록된다"**입니다. 모든 모델 요청을 기록만으로 다시 만들 수 있어야 하며, 분기(fork), 이어 하기, 대화록, 원격 측정이 모두 이 기록에서 나옵니다.
- 한 **스텝**은 모델 요청 한 번과 그때 부른 도구들이고, 한 **턴**은 스텝 0개 이상입니다. 요청 전·도구 실행 전후 등에 끼어드는 이벤트 지점이 마련돼 있습니다.

### 들어 있는 도구 (도구 목록 문서 기준)

| 묶음 | 모델이 쓰는 도구 |
|---|---|
| 파일 | `read`, `write`, `edit`, `apply_patch`, `read_image`, `glob`, `grep` |
| 실행 | `bash`, `pwsh`, 지속 터미널(`terminal_open` 등), `run_code`, 백그라운드 작업(`job_list` 등) |
| 문서 | `office_convert`, `office_recalculate`, `office_render`, `present` |
| 웹 | `web_search`, `web_fetch`, 브라우저 조작(`stagehand_*`, 실험적) |
| 협업 | `subagent`, `send_message`, `wait_agent`, 에이전트 팀 작업판(`team_task_*`), `workflow` |
| 관리 | `todo_write`, 목표(`create_goal` 등), 예약(`schedule_create` 등), 계획 모드, `skill`, `lsp`, MCP 리소스 |
| 자기 확장 | `plugin_manager`, `plugin_market`, `cordis_inspect_*` |

- 실험적 도구 `subagent_oar`는 외부 에이전트를 서브에이전트로 부릅니다. 문서에 나온 예는 Codex와 Claude Code입니다.
- 공식 사이트는 **"창조 모드"**를 내세웁니다. 대화로 플러그인을 만들어 달라고 하면 하네스가 직접 코드를 쓰고 설치합니다(사이트의 예시는 뽀모도로 타이머 플러그인).

### 모델 연결

- 기본은 DeepSeek API 키입니다. 공식 사이트 화면에는 DeepSeek-V41-Flash가 보입니다.
- 내장 제공자 목록에서 `anthropic`, `openai`, `moonshotai`(Kimi), `zai`(GLM) 등을 고를 수 있습니다.
- 사내 게이트웨이나 자체 서버는 **Custom model API**로 붙입니다. 지원 프로토콜은 OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, Gemini API 네 가지입니다.
- 키는 쓰기 전용입니다. 저장한 뒤에는 화면에 가려진 형태만 보이고 `$DSH_HOME/.credentials.yaml`에 저장됩니다.

![모델 설정 화면](https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/master/docs/user/guide/providers-models-page.png)

### 쓰는 형태

| 형태 | 내용 |
|---|---|
| 데스크톱 앱 | Electron 기반. 공식 사이트에서 macOS(Apple 실리콘)와 Windows(64비트)용을 받습니다. 창을 닫아도 작업은 계속 돕니다 |
| Web UI | `npx @deepseek-ai/dsh web`으로 `http://127.0.0.1:3080`에 뜹니다 |
| 헤드리스 | `dsh --profile headless "할 일"`로 한 번 실행하고 답을 출력한 뒤 끝냅니다 |
| SDK | TypeScript SDK와 Python SDK가 `dsh --profile sdk`를 띄워 JSON-RPC로 대화합니다 |
| ACP | `dsh --profile acp`로 자동화 클라이언트를 받습니다 |

## 써 보려면

```sh
npx @deepseek-ai/dsh web
```

- 필요한 것: Node.js. npm 패키지의 요구 버전은 **24.9.0 이상**입니다(2026-11-11 조회).
- 실행한 뒤 **Settings → Models**에서 DeepSeek API 키를 넣고, **Choose workspace**로 작업 폴더를 고르면 대화를 시작할 수 있습니다.
- 소스로 실행하려면 저장소를 받은 뒤 `pnpm install`, `pnpm run build`, `pnpm dsh web` 순으로 실행합니다.
- 플러그인 관리는 `dsh plugin --profile <이름> <pnpm 인자>`입니다. 내 플러그인 저장소에 `dsh-plugin` 토픽을 달면 찾기 쉬워진다고 안내합니다.
- 라이선스는 MIT입니다.

## 눈여겨볼 점

- **개발자 미리보기**입니다. README가 대문자로 "호환성을 깨는 변경이 있을 것"이라고 적었습니다. 릴리스 38개가 모두 사전 릴리스이고, 가장 최근 것은 `dsh-v0.2.2-rc.2`(2026-11-11)입니다. npm의 `latest`는 0.2.2-rc.1입니다(2026-11-11 조회).
- **보안 감사를 받지 않았습니다.** 안전 안내문은 샌드박스와 승인 창이 위험을 줄일 뿐 격리를 보장하지 않으니, 일회용 가상 머신이나 컨테이너에서 최소 권한으로 돌리고 백업을 두라고 권합니다.
- 플러그인 색인(Discover 탭)은 실험 기능이고, 기본으로 들어 있는 색인 주소는 없습니다. `http:` 색인은 중간에서 바뀔 수 있으니 `https:`를 쓰라고 합니다.
- 2차 자료(기사)에는 "공개 일주일 만에 별 16만 5천 개", "8일 만에 19만 7천 개" 같은 수치가 나오지만 서로 다르고 1차 자료로 확인하지 못했습니다. 지금 별 수만 직접 확인했습니다.
- 한 사용기는 `npx` 실행이 실패해 소스로 돌렸다고 적었습니다. 직접 설치해 보지는 않았습니다.
- 같은 조직에 `deepseek-ai/dsh-superagent-prototype`(2026-10-31 생성, "Towards a More Autonomous Agent System")이 따로 있습니다. 내용은 열어 보지 않았습니다.
- 이 하네스에 기억과 메신저 연결을 얹는 개인 제작 플러그인은 [deepseek-bot](deepseek-bot.md) 문서에 있습니다.

## 출처

- [deepseek-ai/deepseek-harness README](https://github.com/deepseek-ai/deepseek-harness) — 소개, 실행 방법, 개발자 미리보기 경고, 라이선스
- [구조 문서 docs/architecture.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md) — Cordis, 프로필·번들, 턴 흐름, 세션 기록, 솔기
- [도구 목록 docs/tool-catalog.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/tool-catalog.md) — 도구 이름과 패키지
- [안전 안내 SAFETY.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/SAFETY.md) — 실험 단계, 샌드박스 한계, 권장 사용법
- [모델 설정 안내](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/providers.md) — 제공자, 프로토콜, 키 저장 방식
- [CLI 안내 apps/cli/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/README.md) — 실행 모드와 프로필
- [플러그인 색인 안내](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/plugin-market.md) — Discover 탭, 색인 주소
- [공식 사이트](https://www.deepseek.com/en/harness/) — 용도 소개, 데스크톱 앱 지원 운영체제, 창조 모드 예시
- [GitHub 저장소 API 정보](https://api.github.com/repos/deepseek-ai/deepseek-harness) — 생성일, 별·포크 수, 릴리스 목록 (2026-11-11 조회)
- [npm 레지스트리 정보](https://registry.npmjs.org/@deepseek-ai%2Fdsh) — 첫 버전 날짜, 최신 버전, Node.js 요구 버전 (2026-11-11 조회)
- 검색으로 본 기사들 — 별 수 증가 속도, 사용기. 1차 자료로 확인되지 않은 내용은 위에 따로 표시
