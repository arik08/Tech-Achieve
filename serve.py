"""보관함을 로컬 서버로 연다. 이 방식으로 열어야 뷰어에서 문서를 지울 수 있다.

사용법:  python serve.py [포트]      (기본 8765, 이 PC에서만 접속 가능)
지운 문서는 없애지 않고 _trash/ 폴더로 옮긴다.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import webbrowser
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import build

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
TRASH = ROOT / "_trash"
SLUG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def delete_doc(slug: str) -> None:
    src = DOCS / f"{slug}.md"
    if not SLUG.match(slug) or not src.is_file():
        raise FileNotFoundError(slug)
    dest = TRASH / f"{datetime.now():%Y%m%d-%H%M%S}-{slug}"
    dest.mkdir(parents=True)
    shutil.move(str(src), str(dest / src.name))
    img = DOCS / "img" / slug
    if img.is_dir():
        shutil.move(str(img), str(dest / "img"))
    docs, _ = build.load_docs()
    build.write_data_js(docs)
    build.write_index_md(docs)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_json(self, code: int, obj: dict) -> None:
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/ping":
            return self.send_json(200, {"ok": True})
        if self.path.startswith("/_trash"):
            return self.send_error(404)
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/delete":
            return self.send_error(404)
        # 다른 웹사이트가 이 주소로 몰래 요청하지 못하게, 뷰어만 붙이는 머리말을 요구한다
        host = self.headers.get("Host", "")
        if self.headers.get("X-Archive") != "1" or not re.match(r"^(localhost|127\.0\.0\.1)(:\d+)?$", host):
            return self.send_json(403, {"ok": False, "error": "허용되지 않은 요청"})
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))) or b"{}")
            delete_doc(str(body.get("id", "")))
        except FileNotFoundError:
            return self.send_json(404, {"ok": False, "error": "문서를 찾을 수 없습니다"})
        except Exception as e:  # noqa: BLE001
            return self.send_json(500, {"ok": False, "error": str(e)})
        self.send_json(200, {"ok": True})

    def log_message(self, fmt, *args):
        if self.command == "POST":
            super().log_message(fmt, *args)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if a != "--no-open"]
    port = int(args[0]) if args else 8765
    docs, _ = build.load_docs()
    build.write_data_js(docs)
    build.write_index_md(docs)
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://localhost:{port}/"
    print(f"보관함: {url}  (끝내려면 Ctrl+C)")
    if "--no-open" not in sys.argv:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
