# EASTER Draft 2 — LaTeX / arXiv Package

Mechanical LaTeX representation of the frozen Draft 2 manuscript.

## Provenance

- **Source manuscript (frozen):** commit `a92ce76e6221aaa8eb17dba87544325d6eb29d6b`
- **Freeze attestation:** `paper/draft2/PUBLICATION-FREEZE-ATTESTATION.md`
- **Conversion:** mechanical only — no claim or prose changes. Abstract
  environment fix, §2.4 enumeration normalization, Unicode symbol
  replacement, single `\appendix`, `tabularx` for wide tables, subsection
  numbering prefixes stripped (LaTeX numbers automatically).
- **Verification:** visual final gate passed by independent reviewer (Ori),
  October 2, 2026. 73-page PDF, clean `pdflatex` compile.

## Files

- `easter-draft2.tex` — LaTeX source
- `easter-draft2.pdf` — compiled output (pdflatex, two passes)
- `md2latex.py` — the mechanical converter used to generate the `.tex`
  from the frozen Markdown sources (for reproducibility, not normative)

## Status

This package is the faithful arXiv representation of frozen Draft 2.
The manuscript phase is closed; this directory contains only mechanical
publication transformations.
