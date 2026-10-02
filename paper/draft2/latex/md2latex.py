#!/usr/bin/env python3
"""Mechanical Markdown-to-LaTeX converter for EASTER Draft 2 frozen manuscript.
Converts the frozen commit a92ce76 manuscript files to a single arXiv-ready .tex.
This is a mechanical representation transform only — no substantive changes.
"""
import re
import os

# Resolve source dir relative to this script's location in the repo
# (script lives at paper/draft2/latex/md2latex.py)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
# Allow override via env for flexibility
SRC = os.environ.get("EASTER_DRAFT2_SRC", SRC)

# Paper content files in order (excludes repo-only artifacts)
PAPER_FILES = [
    "00-abstract.md",
    "01-introduction.md",
    "02-problem-contributions.md",
    "03-easter-model.md",
    "04-reference-implementation.md",
    "05-evaluation-methodology.md",
    "06-comparative-architectural-results.md",
    "07-userland-continuity-boundary.md",
    "08-easter-in-use-contribution-provenance.md",
    "09-related-work-novelty-boundary.md",
    "10-limitations-threats-to-validity.md",
    "11-discussion-research-implications.md",
    "12-conclusion.md",
    "13-references.md",
    "APPENDIX-A-COMPARATIVE-EVIDENCE-REGISTER.md",
    "APPENDIX-B-REFERENCE-MAP.md",
]

def escape_latex(text):
    """Escape LaTeX special chars, preserving already-converted commands."""
    # Do this before inline formatting conversion
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciircum{}'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def convert_text(raw):
    """Full pipeline: stash URLs, code; escape; then inline-convert.
    Note: display math \[...\] is handled at the convert_file level (multi-line)."""
    urls = []
    def stash_url(m):
        urls.append(m.group(0))
        return f"\x00URL{len(urls)-1}\x00"
    text = re.sub(r'(?<![\(\]])(https?://[^\s\)\]]+)', stash_url, raw)
    # Stash Unicode symbols before escaping mangles them
    symbols = []
    def stash_sym(m):
        symbols.append(m.group(0))
        return f"\x00SYM{len(symbols)-1}\x00"
    text = re.sub(r'[⇏⇒→—–]', stash_sym, text)
    # Stash inline code BEFORE escaping (prevents double-escape)
    codes = []
    def stash_code(m):
        codes.append(m.group(1))
        return f"\x00CODE{len(codes)-1}\x00"
    text = re.sub(r'`([^`]+)`', stash_code, text)

    text = escape_latex(text)

    # Restore code with single escaping
    for i, code in enumerate(codes):
        safe = escape_latex(code)
        text = text.replace(f"\x00CODE{i}\x00", r'\texttt{' + safe + '}')
    # Restore symbols as LaTeX after escaping
    sym_map = {'⇏': r'$\not\Rightarrow$', '⇒': r'$\Rightarrow$',
               '→': r'$\rightarrow$', '—': '---', '–': '--'}
    for i, sym in enumerate(symbols):
        text = text.replace(f"\x00SYM{i}\x00", sym_map[sym])
    text = convert_inline(text)
    # Restore URLs (strip trailing punctuation)
    for i, url in enumerate(urls):
        clean = re.sub(r'[.,;:]+$', '', url)
        trail = url[len(clean):]
        # Escape the trail punctuation if needed
        trail = trail.replace('%', r'\%').replace('&', r'\&').replace('#', r'\#')
        text = text.replace(f"\x00URL{i}\x00", r'\url{' + clean + '}' + trail)
    return text

def convert_inline(text):
    """Convert inline markdown to LaTeX. Assumes text already escaped, code/URLs stashed."""
    # Links: [text](url) -> hyperlinked text
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\\href{\2}{\1}', text)

    # Bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', text)
    # Italic (avoid catching already-converted)
    text = re.sub(r'(?<!\\)\*(?!\*)([^*]+)(?<!\*)\*(?!\*)', r'\\textit{\1}', text)

    return text

def convert_table(lines, idx):
    """Convert a markdown table block to LaTeX tabular. Returns (latex, new_idx)."""
    rows = []
    while idx < len(lines) and re.match(r'^\s*\|', lines[idx]):
        rows.append(lines[idx].strip())
        idx += 1
    # Parse rows
    parsed = []
    for r in rows:
        cells = [c.strip() for c in r.strip('|').split('|')]
        parsed.append(cells)
    # Remove separator row (all dashes)
    data = [r for r in parsed if not all(re.match(r'^:?-{2,}:?$', c) for c in r)]
    if not data:
        return "", idx
    ncols = max(len(r) for r in data)
    # Check if table needs wrapping (any cell > 60 chars)
    needs_wrap = any(len(c) > 60 for r in data for c in r)
    out = ["\\begin{table}[htbp]", "\\centering", "\\small"]
    if needs_wrap:
        # Use tabularx with X columns for text wrapping
        colspec = ' '.join(['X'] * ncols)
        out.append(f"\\begin{{tabularx}}{{\\textwidth}}{{{colspec}}}")
        out.append("\\toprule")
        for i, row in enumerate(data):
            cells = [convert_text(c) for c in row]
            cells += [''] * (ncols - len(cells))
            out.append(" & ".join(cells) + r" \\")
            if i == 0:
                out.append("\\midrule")
        out += ["\\bottomrule", "\\end{tabularx}", "\\end{table}"]
    else:
        colspec = 'l' * ncols
        out.append(f"\\begin{{tabular}}{{{colspec}}}")
        out.append("\\toprule")
        for i, row in enumerate(data):
            cells = [convert_text(c) for c in row]
            cells += [''] * (ncols - len(cells))
            out.append(" & ".join(cells) + r" \\")
            if i == 0:
                out.append("\\midrule")
        out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out) + "\n", idx

def convert_file(path, is_appendix=False):
    text = open(path).read()
    lines = text.split('\n')
    out = []
    i = 0
    in_list = None  # 'itemize' or 'enumerate'

    def close_list():
        nonlocal in_list
        if in_list:
            out.append(f"\\end{{{in_list}}}")
            in_list = None

    while i < len(lines):
        line = lines[i]

        # Table block
        if re.match(r'^\s*\|', line):
            close_list()
            latex, i = convert_table(lines, i)
            out.append(latex)
            continue

        # Headers
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            close_list()
            level = len(m.group(1))
            title = convert_text(m.group(2).strip())
            # Abstract special-case at any level
            if 'abstract' in m.group(2).strip().lower() and level <= 2:
                j = i + 1
                # Skip blank lines after header
                while j < len(lines) and not lines[j].strip():
                    j += 1
                paras = []
                # Collect all paragraphs until next header or EOF
                while j < len(lines) and not re.match(r'^#{1,4}\s', lines[j]):
                    if lines[j].strip():
                        paras.append(convert_text(lines[j].strip()))
                    j += 1
                out.append("\\begin{abstract}")
                out.append("\n\n".join(paras))
                out.append("\\end{abstract}")
                i = j
                continue
            # Strip leading "N. " numbering from h1 (LaTeX numbers automatically)
            if level == 1:
                title = re.sub(r'^\d+\.\s+', '', title)
                if 'references' in title.lower():
                    out.append("\\begin{thebibliography}{99}")
                    j = i + 1
                    bib_items = []
                    current = ""
                    # Stop at next heading (don't consume to EOF)
                    while j < len(lines) and not re.match(r'^#{1,4}\s', lines[j]):
                        lj = lines[j]
                        if re.match(r'^\d+\.\s', lj):
                            if current:
                                bib_items.append(current)
                            current = re.sub(r'^\d+\.\s*', '', lj)
                        elif lj.strip() == "" and current:
                            bib_items.append(current)
                            current = ""
                        elif current:
                            current += " " + lj.strip()
                        j += 1
                    if current:
                        bib_items.append(current)
                    for b in bib_items:
                        # strip leading intro paragraph (non-numbered)
                        out.append("\\bibitem{ref" + str(len([l for l in out if "bibitem" in l])+1) + "} " + convert_text(b.strip()))
                    out.append("\\end{thebibliography}")
                    i = j
                    continue
                elif 'appendix' in title.lower():
                    # Only emit \appendix once (track via function attribute)
                    if not hasattr(convert_file, '_appendix_started'):
                        out.append("\\appendix")
                        convert_file._appendix_started = True
                    # Strip "Appendix X — " or "Appendix X. " prefix, keep the rest
                    clean = re.sub(r'^Appendix\s+[A-Z]\s*[—.:\-]\s*', '', m.group(2).strip())
                    out.append("\\section{" + convert_text(clean) + "}")
                else:
                    out.append("\\section{" + title + "}")
            elif level == 2:
                # Strip leading numbering: "N.M ", "A.1 ", "B.2 " etc.
                # (LaTeX numbers automatically via \section/\appendix)
                raw_title = m.group(2).strip()
                clean_title = re.sub(r'^(\d+\.\d+|[A-Z]\.\d+)\s+', '', raw_title)
                out.append("\\subsection{" + convert_text(clean_title) + "}")
            elif level == 3:
                # Strip leading "N.M.K " or "A.1.2 " numbering
                raw_title = m.group(2).strip()
                clean_title = re.sub(r'^(\d+\.\d+\.\d+|[A-Z]\.\d+\.\d+)\s+', '', raw_title)
                out.append("\\subsubsection{" + convert_text(clean_title) + "}")
            else:
                out.append("\\paragraph{" + title + "}")
            i += 1
            continue

        # Blockquote
        if re.match(r'^>\s?', line):
            close_list()
            out.append("\\begin{quote}")
            while i < len(lines) and re.match(r'^>\s?', lines[i]):
                out.append(convert_text(re.sub(r'^>\s?', '', lines[i])))
                i += 1
            out.append("\\end{quote}")
            continue

        # Unordered list
        if re.match(r'^-\s+', line):
            if in_list != 'itemize':
                close_list()
                out.append("\\begin{itemize}")
                in_list = 'itemize'
            content = re.sub(r'^-\s+', '', line)
            # Handle continuation lines (indented)
            j = i + 1
            while j < len(lines) and re.match(r'^ {2,}\S', lines[j]) and not re.match(r'^ {2,} [-*\d]', lines[j]):
                content += " " + lines[j].strip()
                j += 1
            out.append("\\item " + convert_text(content))
            i = j
            continue

        # Ordered list
        if re.match(r'^\d+\.\s+', line):
            if in_list != 'enumerate':
                close_list()
                out.append("\\begin{enumerate}")
                in_list = 'enumerate'
            content = re.sub(r'^\d+\.\s+', '', line)
            j = i + 1
            while j < len(lines) and re.match(r'^ {2,}\S', lines[j]) and not re.match(r'^ {2,} [-*\d]', lines[j]):
                content += " " + lines[j].strip()
                j += 1
            out.append("\\item " + convert_text(content))
            i = j
            continue

        # Horizontal rule -> skip
        if re.match(r'^---\s*$', line):
            close_list()
            i += 1
            continue

        # Blank line - keep list open if next non-blank is same list type
        if line.strip() == "":
            # Peek ahead to see if list continues
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            continues = False
            if j < len(lines):
                if in_list == 'itemize' and re.match(r'^-\s+', lines[j]):
                    continues = True
                elif in_list == 'enumerate' and re.match(r'^\d+\.\s+', lines[j]):
                    continues = True
            if not continues:
                close_list()
            out.append("")
            i += 1
            continue

        # Display math block: \[ ... \] (may span lines) - preserve verbatim
        if re.match(r'^\\\[\s*$', line):
            close_list()
            math_lines = [line]
            i += 1
            while i < len(lines) and not re.match(r'^\\\]\s*$', lines[i]):
                math_lines.append(lines[i])
                i += 1
            if i < len(lines):
                math_lines.append(lines[i])  # closing \]
                i += 1
            out.append("\n".join(math_lines))
            continue

        # Regular paragraph
        close_list()
        out.append(convert_text(line.strip()))
        i += 1

    close_list()
    return "\n".join(out)

def main():
    # Read front matter for title/author
    fm = open(os.path.join(SRC, "front-matter.md")).read()
    title_m = re.search(r'^#\s+(.*)', fm, re.M)
    title = title_m.group(1).strip() if title_m else "EASTER"

    preamble = r"""\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{amsmath}
\geometry{margin=1in}
\setlength{\parskip}{0.5em}
\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue, citecolor=blue}

\title{""" + escape_latex(title) + r"""}
\author{Nathan Woolen \\ \small\textit{with substantive intellectual and technical contributions from ChatGPT/Sol, Pax/Muse, Clawde/Sonnet, and Hermes} \\ \small WitsBI}
\date{October 2026 \\ Draft 2}

\begin{document}
\maketitle
"""

    body_parts = []
    for f in PAPER_FILES:
        path = os.path.join(SRC, f)
        print(f"Converting {f}...")
        body_parts.append(f"% === {f} ===\n" + convert_file(path))

    ending = r"""
\end{document}
"""
    full = preamble + "\n".join(body_parts) + ending

    # Output alongside the script (paper/draft2/latex/)
    outdir = SCRIPT_DIR
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "easter-draft2.tex")
    open(outpath, "w").write(full)
    print(f"Wrote {outpath} ({len(full)} chars, {full.count(chr(10))} lines)")

if __name__ == "__main__":
    main()
