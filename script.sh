gnuplot GnuScript.gp
latex build.tex; dvipdf build.dvi
pdfcrop build.pdf crap.pdf
pdf2ps crap.pdf crap.ps
ps2eps -f crap.ps
eps2svg crap.eps crapEPS.svg
pdf2svg crap.pdf crapPDF.svg
rm build.dvi build.aux crap.ps build.pdf