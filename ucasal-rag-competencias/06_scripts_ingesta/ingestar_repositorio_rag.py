#!/usr/bin/env python3
"""Script base para preparar documentos Markdown del repositorio para una base RAG local.

Este script no genera embeddings por sí mismo. Produce un JSONL con texto y metadatos
que luego puede ser consumido por Chroma, FAISS, Qdrant, LanceDB u otra base vectorial.
"""
from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "index" / "documentos_rag.jsonl"

FRONTMATTER_RE = re.compile(r"^---
(.*?)
---
", re.S)

def parse_frontmatter(text):
    meta = {}
    m = FRONTMATTER_RE.match(text)
    body = text
    if m:
        body = text[m.end():]
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"')
    return meta, body.strip()

def chunk_text(text, max_chars=1800, overlap=250):
    text = re.sub(r"
{3,}", "

", text).strip()
    if len(text) <= max_chars:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        cut = text.rfind("

", start, end)
        if cut <= start + 500:
            cut = end
        chunks.append(text[start:cut].strip())
        start = max(cut - overlap, cut)
        if start >= len(text):
            break
    return [c for c in chunks if c]

with OUT.open('w', encoding='utf-8') as f:
    for path in sorted((ROOT / '02_matrices_tributacion').rglob('documento.md')):
        text = path.read_text(encoding='utf-8')
        meta, body = parse_frontmatter(text)
        for i, chunk in enumerate(chunk_text(body), 1):
            row = {
                'id': f"{meta.get('id', path.stem)}_chunk_{i:03d}",
                'text': chunk,
                'metadata': {**meta, 'path': str(path.relative_to(ROOT)), 'chunk': i}
            }
            f.write(json.dumps(row, ensure_ascii=False) + '
')
print(f"Generado: {OUT}")
