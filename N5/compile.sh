#!/usr/bin/env bash
# Compile the LaTeX notes and open them in okular.
# Usage: ./compile.sh [file.tex]   (defaults to N5.tex)
set -euo pipefail

TEX_FILE="${1:-N5.tex}"
PDF_FILE="${TEX_FILE%.tex}.pdf"

latexmk -pvc -pdf --interaction=nonstopmode "$TEX_FILE" &
okular "$PDF_FILE"
