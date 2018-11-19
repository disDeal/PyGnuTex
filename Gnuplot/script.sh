gnuplot GnuScript.gp
latex build.tex; dvipdf build.dvi
pdfcrop build.pdf crap2.pdf
pdf2ps crap2.pdf crap2.ps
ps2eps -f crap2.ps
eps2svg crap2.eps crap2EPS.svg
pdf2svg crap2.pdf crap2PDF.svg
rm build.dvi build.aux crap2.ps build.pdf