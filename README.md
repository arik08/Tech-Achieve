# AI 기술 보관함 (Tech-Achieve)

인터넷에서 본 AI 관련 글, 저장소, 캡처를 AI에게 던져 주면 조사해서 문서로 쌓아 두는 개인 보관함입니다. 사람은 뷰어로 훑어보고, AI는 색인을 읽고 찾아서 답합니다.

- 문서 목록: [INDEX.md](INDEX.md)
- 문서 원본: [docs/](docs/)

## 보는 법

저장소를 내려받은 뒤 둘 중 하나로 엽니다.

- `index.html`을 더블클릭: 읽기 전용으로 열립니다.
- `start.bat`을 더블클릭하거나 `python serve.py` 실행: 로컬 서버(`http://localhost:8765`)로 열리고, 문서 삭제 버튼이 나옵니다. Python 3만 있으면 되고 따로 설치할 것은 없습니다.

## 문서를 넣는 법

Claude Code 같은 코딩 에이전트를 이 폴더에서 열고 주소, 복사한 글, 캡처, 한 문장 중 아무거나 주면 됩니다. 에이전트가 따르는 절차와 문서 형식은 [CLAUDE.md](CLAUDE.md)에 있습니다.

문서마다 다음을 적습니다.

- 그 기술이 처음 나온 때(`released`)와 내용을 확인한 날(`checked`)
- GitHub, 공식 사이트, 문서, 논문 링크
- 확인하지 못한 점과 출처

## 알아 둘 점

- 문서는 AI가 조사해 쓴 것입니다. 각 문서의 "눈여겨볼 점"에 확인하지 못한 내용이 적혀 있으니, 중요한 결정에는 출처를 직접 확인하세요.
- 별 수, 버전 같은 수치는 문서에 적힌 조회 날짜 기준입니다.
- `docs/img/`의 캡처와 문서에 링크된 이미지의 권리는 각 원작자에게 있습니다. 문제가 되는 자료가 있으면 이슈로 알려 주세요.
- `vendor/`에는 [marked](https://github.com/markedjs/marked)(MIT), [DOMPurify](https://github.com/cure53/DOMPurify)(Apache-2.0 또는 MPL-2.0), [Lucide](https://github.com/lucide-icons/lucide)(ISC)가 들어 있습니다.
