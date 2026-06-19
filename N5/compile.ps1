# Compile the LaTeX notes on Windows.
# Usage: .\compile.ps1 [file.tex]   (defaults to N5.tex)

param(
    [string]$TexFile = "N5.tex"
)

$PdfFile = [System.IO.Path]::ChangeExtension($TexFile, ".pdf")

# Start latexmk in continuous preview mode (background job).
Start-Process -NoNewWindow latexmk -ArgumentList "-pvc", "-pdf", "--interaction=nonstopmode", $TexFile

# Open the resulting PDF with the default viewer (e.g. SumatraPDF).
Invoke-Item $PdfFile
