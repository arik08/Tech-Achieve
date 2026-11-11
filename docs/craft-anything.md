---
title: Craft Anything — 웹사이트·앱·게임이 어떻게 만들어졌는지 살펴보고 AI로 내 버전을 다시 만드는 도구
category: 에이전트·하네스
tags: [Craft Anything, 복제, 클론, 리버스 엔지니어링, 클린룸, Rust, MCP, Claude Code, 웹사이트 복제, 게임 복제, ArtCraft, REA, 깃허브 트렌드]
date: 2026-11-11
released: 2026-10-31
checked: 2026-11-10
summary: 대상(웹사이트, 앱, 게임)을 지정하고 원하는 것을 말하면, 원본을 조사하고 코딩 에이전트가 새 프로젝트를 만든 뒤 원본과 비교해 다듬는 오픈소스 도구. 순수 Rust 엔진에 도구 320개가 있고, 데스크톱 앱·CLI·MCP 서버로 쓴다. 기본은 원본 내부를 읽지 않는 클린룸 방식. 초기 알파.
cover: https://raw.githubusercontent.com/storytold/craft-anything/main/docs/images/project-website.png
links:
  - GitHub | https://github.com/storytold/craft-anything
  - 공식 사이트 | https://getartcraft.com/apps/craft-anything
  - 내려받기 (릴리스) | https://github.com/storytold/craft-anything/releases
  - 한국어 README | https://github.com/storytold/craft-anything/blob/main/README.ko.md
  - 현재 상태 문서 | https://github.com/storytold/craft-anything/blob/main/docs/STATUS.md
---

## 한눈에 보기

- 어떤 웹사이트·앱·게임이든 어떻게 동작하는지 조사한 다음, AI 코딩 에이전트에게 내 버전을 새로 만들게 하는 도구입니다. ArtCraft 팀(GitHub `storytold`)이 만들었고, 같은 팀의 PhotoCraft·FilmCraft 같은 "Craft" 앱 묶음에 속합니다.
- 조사 엔진은 전부 Rust로 짰고, 데스크톱 앱·CLI·MCP 서버가 같은 엔진을 씁니다.
- 공개 시기는 저장소 생성일이자 첫 릴리스 v0.1.0이 나온 2026-10-31을 기준으로 적었습니다. 별 약 27,600개, 포크 약 5,600개, 최신 릴리스 v0.6.0(2026-11-09)입니다 (2026-11-11 조회).

![웹사이트 프로젝트 화면: 원본과 얼마나 닮았는지, 승인 카드, 남은 단계가 보입니다](https://raw.githubusercontent.com/storytold/craft-anything/main/docs/images/project-website.png)

## 핵심 내용

### 네 단계로 일합니다

1. **Study (조사)** — 원본을 살핍니다. 화면 폭별 페이지 모습, 코드, 파일, 실행되는 방식.
2. **Build (제작)** — 코딩 에이전트가 요청에 적힌 언어·프레임워크·엔진으로 새 프로젝트를 만듭니다.
3. **Check (대조)** — 만든 것을 원본과 비교해 아직 안 맞는 곳을 적습니다. 웹사이트는 세 가지 화면 폭에서 비교합니다.
4. **Ready (완성)** — 결과를 열어 보거나, 고칠 점을 말하면 다시 다듬습니다.

결정이 필요한 곳에서는 쉬운 말로 사용자에게 묻고, 규칙 밖의 명령은 실행 전에 승인을 받습니다.

### 클린룸과 Deep

| | Clean room (기본) | Deep |
|---|---|---|
| 원본 내부 | 읽지 않습니다. 코드, 파일, 페이지 소스 모두 보지 않습니다. | 모든 도구를 씁니다. 개인 용도라고 README가 적습니다. |
| 근거로 삼는 것 | 방문자에게 보이는 것: 화면 캡처, 보이는 글, 잰 배치·색·글꼴·간격, 사용자가 넣은 그림 | 프로그램 코드와 파일(내장 엔진, 설치돼 있으면 Ghidra), 웹사이트의 JavaScript |
| 켜는 법 | 기본값 | 제목 표시줄·설정, 또는 CLI의 `--deep` |

README는 클린룸이 "도구가 무엇을 내주고 거절하느냐"의 규칙일 뿐 운영체제 샌드박스가 아니라고 분명히 합니다. 코딩 에이전트는 여전히 사용자 권한으로 움직입니다.

### 두 가지 화면

- **Simple (기본)** — "무엇을 만들까요?"에서 웹사이트·앱·게임을 고르고 설명한 뒤 Start. 네 단계 진행, 질문·승인 카드, 원본과 닮은 정도가 보입니다.
- **Advanced** — 전체 작업대. 함수, 문자열, 의사 C 코드, 역어셈블, 헥스, 호출 그래프, 근거 기록, 에이전트 콘솔.

### 엔진과 에이전트 연결

- 도구 320개(엔진 300개, 나머지는 AI·설정 계층). 네이티브 프로그램, .NET, Java, Android, Apple, Electron/JavaScript, 웹사이트, 펌웨어, 패킷 캡처, 데이터베이스, 게임 파일을 다룹니다. 자체 디코더·역어셈블러·디컴파일러가 있어 바깥 프로그램 없이 동작합니다.
- 모든 도구가 CLI 명령이자 MCP 도구입니다. 조사만 할 때는 AI가 필요 없습니다.
- 제작에는 내 컴퓨터에 로그인된 코딩 에이전트가 필요합니다. Claude Code를 가장 먼저 지원하며, 사용자의 `claude` 프로그램을 수정 없이 그대로 실행합니다. Codex 어댑터는 있지만 실제 설치에서 검증되지 않았다고 합니다. GitHub Copilot CLI와 Grok Build는 ACP로 연결합니다.

## 써 보려면

설치 파일은 [Releases](https://github.com/storytold/craft-anything/releases)에 있습니다. Windows(x64·arm64·x86의 `.msi`와 포터블 zip), macOS(유니버설 `.dmg`), Linux(AppImage, Flatpak, deb, rpm, tarball), FreeBSD, 웹(WebAssembly 뷰어)용이 있습니다.

소스에서 빌드하려면 Rust 1.97 이상이 필요합니다.

```sh
git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything                # 데스크톱 앱
cargo install --path apps/craft-anything-cli         # CLI
craft-anything-cli doctor                            # 설치, 코딩 에이전트, 엔진 점검
```

명령줄에서 바로 다시 만들기, 그리고 다른 에이전트에 MCP로 붙이기:

```sh
craft-anything-cli rebuild https://example.com "Recreate this website"
craft-anything-cli rebuild - "A snake game in Rust" --rounds 1
craft-anything-cli mcp
```

- 새 프로젝트는 `Documents/Craft Anything`에 생깁니다.
- 라이선스: README는 MIT 또는 Apache-2.0 가운데 고르는 이중 라이선스라고 밝힙니다. GitHub API에는 Apache-2.0으로 잡힙니다. ArtCraft 이름과 로고는 상표여서 이 라이선스에 들어가지 않고, 포크는 지워야 합니다.

## 눈여겨볼 점

- **초기 알파입니다.** README의 상태표에 따르면 오늘 되는 것은 데스크톱 앱·CLI·MCP 서버, Claude Code를 쓰는 네 단계 작업, 세 화면 폭의 웹사이트 대조, Unity·Unreal·Godot 게임 재제작, Ghidra를 쓰는 Deep 모드입니다. API 키나 다른 코딩 에이전트로 만드는 것은 "만들었지만 실제로 돌려 보지 않음", 앱·게임의 동작 대조는 "부분적"입니다.
- **사용 범위.** 내가 소유했거나 살펴봐도 되는 소프트웨어에만 쓰라고 합니다. DRM·로그인·안티치트를 우회하지 않으며, 에이전트에게 로고·사진·글을 베끼지 말라고 지시한다고 합니다. 남의 서비스를 복제해 공개하는 일의 법적 문제는 이 도구가 해결해 주지 않습니다.
- **의존성 설치는 코드를 실행합니다.** 만들어진 프로젝트의 `npm install` 등은 내 컴퓨터에서 설치 스크립트를 돌립니다. `npm`을 "항상 허용"하면 이후 npm 명령이 묻지 않고 실행되니, 믿을 수 있는 프로젝트에서만 하라고 README가 경고합니다.
- **"REA 2.0"이라는 말은 영상의 표현입니다.** 캡처 속 YouTube 썸네일은 이 도구를 "REA2.0"으로 소개하지만, Craft Anything README에는 REA라는 말이 없습니다. REA(Reverse Engineer Anything)는 `morluto/rea`라는 별개의 저장소로 따로 있습니다(2026-04-14 생성, 2026-11-11 조회). 두 프로젝트가 이어진 것인지는 확인 못 함.
- **"깃허브 트렌드 1위"**라는 영상 제목의 주장은 확인하지 못했습니다. 영상 자체도 열어 보지 않았고, 영상 주소는 캡처에 없습니다.
- 직접 설치해 돌려 보지 않았습니다. 위 내용은 저장소 README와 메타데이터를 읽은 것입니다. 자세한 검증 내역이 있다는 `docs/STATUS.md`는 열어 보지 않았습니다.

## 받은 캡처

![YouTube 홈 화면의 Craft Anything 소개 영상 썸네일](img/craft-anything/Screenshot_20261110_070635_YouTube.jpg)

캡처 2026-11-10

## 출처

- [storytold/craft-anything 저장소 README](https://github.com/storytold/craft-anything) — 네 단계, 클린룸과 Deep, 지원 에이전트, 도구 수, 설치, 상태표, 사용 범위, 라이선스
- [GitHub 저장소 API 정보](https://api.github.com/repos/storytold/craft-anything) — 별·포크 수, 생성일, 릴리스 여섯 개의 날짜, 라이선스 항목 (2026-11-11 조회)
- [morluto/rea 저장소 정보](https://github.com/morluto/rea) — REA가 별개의 저장소라는 것, 생성일 (2026-11-11 조회)
- [getartcraft.com의 Craft Anything 페이지](https://getartcraft.com/apps/craft-anything) — 주소가 열리는 것만 확인
- YouTube 영상(문외인 Layperson, 캡처의 썸네일과 제목) — 처음 받은 자료. 영상은 열어 보지 않음
