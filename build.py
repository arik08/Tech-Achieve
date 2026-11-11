"""docs/*.md 를 읽어 뷰어용 data.js 와 AI용 INDEX.md 를 만든다.

사용법:  python build.py
외부 라이브러리 없이 표준 라이브러리만 쓴다.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
REQUIRED = ("title", "category", "date", "summary")
LIST_KEYS = ("tags", "links")


def parse_front_matter(text: str) -> tuple[dict, str]:
    """맨 위 --- 블록을 읽는다. 지원 형식: `key: 값`, `key: [a, b]`, `key:` 뒤의 `- 항목` 목록."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return {}, text
    meta: dict = {}
    key = None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        item = re.match(r"\s+-\s+(.*)$", raw) or (re.match(r"-\s+(.*)$", raw) if key else None)
        if item and key:
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(unquote(item.group(1)))
            continue
        kv = re.match(r"([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            meta[key] = [unquote(v) for v in val[1:-1].split(",") if v.strip()]
        elif val == "":
            meta[key] = []
        else:
            meta[key] = unquote(val)
    return meta, text[m.end():]


def unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def parse_links(items) -> list[dict]:
    """`이름 | URL` 형식. 이름이 없으면 URL만으로도 받는다."""
    out = []
    for it in items if isinstance(items, list) else []:
        if "|" in it:
            label, url = (p.strip() for p in it.split("|", 1))
        else:
            label, url = "", it.strip()
        if url:
            out.append({"label": label or url, "url": url})
    return out


def load_docs() -> tuple[list[dict], list[str]]:
    docs, problems = [], []
    for path in sorted(DOCS.glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8-sig"))
        slug = path.stem
        for k in REQUIRED:
            if not meta.get(k):
                problems.append(f"{path.name}: `{k}` 가 비어 있습니다")
        for k in LIST_KEYS:
            if isinstance(meta.get(k), str):
                meta[k] = [meta[k]] if meta[k] else []
        cover = meta.get("cover", "") or ""
        if cover and not re.match(r"https?://", cover) and not (DOCS / cover).exists():
            problems.append(f"{path.name}: cover 파일이 없습니다 ({cover})")
        for src in re.findall(r"!\[[^\]]*\]\(([^)\s]+)", body):
            if not re.match(r"(https?:)?//|data:", src) and not (DOCS / src).exists():
                problems.append(f"{path.name}: 이미지 파일이 없습니다 ({src})")
        docs.append({
            "id": slug,
            "path": f"docs/{path.name}",
            "title": meta.get("title") or slug,
            "category": meta.get("category") or "미분류",
            "tags": meta.get("tags") or [],
            "date": str(meta.get("date") or ""),
            "released": str(meta.get("released") or ""),
            "checked": str(meta.get("checked") or meta.get("date") or ""),
            "summary": meta.get("summary") or "",
            "cover": cover,
            "origin": meta.get("origin") or "",
            "links": parse_links(meta.get("links")),
            "body": body.strip(),
        })
    docs.sort(key=lambda d: (d["checked"], d["date"], d["id"]), reverse=True)  # 최근에 확인한 문서가 먼저
    return docs, problems


def write_data_js(docs: list[dict]) -> None:
    payload = {"generated": datetime.now().strftime("%Y-%m-%d %H:%M"), "docs": docs}
    text = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    (ROOT / "data.js").write_text(
        "// build.py 가 만든 파일입니다. 직접 고치지 마세요.\nwindow.ARCHIVE = " + text + ";\n",
        encoding="utf-8",
    )


def write_index_md(docs: list[dict]) -> None:
    by_cat: dict[str, list[dict]] = {}
    for d in docs:
        by_cat.setdefault(d["category"], []).append(d)
    lines = [
        "# 색인",
        "",
        "build.py 가 만든 파일입니다. 직접 고치지 마세요.",
        f"문서 {len(docs)}건, 분류 {len(by_cat)}개. 한 줄에 문서 하나이며, 자세한 내용은 연결된 md 파일에 있습니다.",
        "",
    ]
    for cat in sorted(by_cat):
        lines += [f"## {cat} ({len(by_cat[cat])})", ""]
        for d in by_cat[cat]:
            lines.append(f"- [{d['title']}]({d['path']}) · 공개 {d['released'] or '시기 미확인'} · 확인 {d['checked']} · 보관 {d['date']}")
            if d["summary"]:
                lines.append(f"  - 요약: {d['summary']}")
            if d["tags"]:
                lines.append(f"  - 태그: {', '.join(d['tags'])}")
            if d["links"]:
                lines.append("  - 링크: " + " · ".join(f"[{l['label']}]({l['url']})" for l in d["links"]))
        lines.append("")
    (ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    DOCS.mkdir(exist_ok=True)
    docs, problems = load_docs()
    write_data_js(docs)
    write_index_md(docs)
    cats = sorted({d["category"] for d in docs})
    print(f"문서 {len(docs)}건, 분류 {len(cats)}개: {', '.join(cats) or '-'}")
    for p in problems:
        print("확인 필요:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
