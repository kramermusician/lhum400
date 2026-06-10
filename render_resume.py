"""
render_resume.py — headless renderer that reproduces resume-builder.html's
exportPDF() output exactly, then prints it to PDF via Chrome.

Single source of truth: the print template/CSS here must mirror the
`exportPDF` function in resume-builder.html. When the app's print styles
change, mirror them here so batch-generated PDFs match what the app makes.

Usage:
    python3 render_resume.py path/to/data.json /output/Name_Resume.pdf

The JSON shape mirrors the app's saved-draft format:
    {
      "name": "...", "contact": ["email", "phone", "loc"],
      "summary": "...",
      "experience": [{"title","company","location","start","end","bullets":[...]}],
      "education":  [{"degree","school","location","start","end"}],
      "skills": ["...", "..."]
    }
"""

import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

STYLE = """
    body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333; line-height: 1.4; margin: 0; padding: 40px; }
    h1 { margin: 0 0 5px 0; font-size: 24px; text-align: center; color: #000; }
    .contact-info { text-align: center; font-size: 13px; color: #555; margin-bottom: 20px; }
    h2 { font-size: 16px; border-bottom: 1px solid #ccc; padding-bottom: 3px; margin-top: 20px; margin-bottom: 10px; color: #000; text-transform: uppercase; page-break-after: avoid; }
    .job { margin-bottom: 15px; page-break-inside: avoid; }
    .job-header { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; }
    .job-subheader { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; }
    .job-title { flex: 1 1 auto; min-width: 0; font-weight: bold; font-size: 14px; color: #000; }
    .job-company { flex: 1 1 auto; min-width: 0; font-style: italic; font-size: 14px; }
    .job-date { flex: 0 0 auto; white-space: nowrap; text-align: right; font-size: 13px; color: #555; }
    .job-location { flex: 0 0 auto; white-space: nowrap; text-align: right; font-size: 13px; color: #555; }
    ul { margin: 5px 0 0 0; padding-left: 20px; font-size: 13px; }
    li { margin-bottom: 3px; }
    .skills { font-size: 13px; line-height: 1.6; }
    .summary { font-size: 13px; margin-bottom: 15px; }
    @page { size: letter; margin: 0.75in; }
    @media print { body { padding: 0; } }
"""


def esc(s):
    return html.escape(str(s or ""))


def date_str(start, end):
    start, end = (start or "").strip(), (end or "").strip()
    if not (start or end):
        return ""
    sep = " - " if start and end else ""
    return f"{esc(start)}{sep}{esc(end)}"


def job_block(title, org, loc, start, end, bullets=None):
    d = date_str(start, end)
    out = ['<div class="job"><div class="job-header">']
    out.append(f'<div class="job-title">{esc(title)}</div>')
    if d:
        out.append(f'<div class="job-date">{d}</div>')
    out.append("</div>")
    if org or loc:
        out.append('<div class="job-subheader">')
        out.append(f'<div class="job-company">{esc(org)}</div>')
        if loc:
            out.append(f'<div class="job-location">{esc(loc)}</div>')
        out.append("</div>")
    if bullets:
        out.append("<ul>")
        for b in bullets:
            b = b.strip().lstrip("•").lstrip("-").strip()
            if b:
                out.append(f"<li>{esc(b)}</li>")
        out.append("</ul>")
    out.append("</div>")
    return "".join(out)


def build_html(d):
    parts = [
        "<!DOCTYPE html><html><head><meta charset='utf-8'>",
        f"<title>{esc(d['name'])} Resume</title><style>{STYLE}</style></head><body>",
        f'<div class="header-container"><h1>{esc(d["name"])}</h1></div>',
        f'<div class="contact-info">{" &nbsp;|&nbsp; ".join(esc(c) for c in d.get("contact", []))}</div>',
    ]
    if d.get("summary"):
        parts.append(f'<h2>Professional Summary</h2><div class="summary">{esc(d["summary"])}</div>')
    if d.get("experience"):
        parts.append("<h2>Experience</h2>")
        for e in d["experience"]:
            parts.append(job_block(e.get("title"), e.get("company"), e.get("location"),
                                    e.get("start"), e.get("end"), e.get("bullets")))
    if d.get("education"):
        parts.append("<h2>Education</h2>")
        for e in d["education"]:
            parts.append(job_block(e.get("degree"), e.get("school"), e.get("location"),
                                   e.get("start"), e.get("end")))
    if d.get("skills"):
        parts.append(f'<h2>Skills</h2><div class="skills">{" &nbsp;•&nbsp; ".join(esc(s) for s in d["skills"])}</div>')
    parts.append("</body></html>")
    return "".join(parts)


def render(data_path, out_path):
    data = json.loads(Path(data_path).read_text())
    html_str = build_html(data)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html_str)
        tmp = f.name
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={out_path}", f"file://{tmp}",
    ], check=True, capture_output=True)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
