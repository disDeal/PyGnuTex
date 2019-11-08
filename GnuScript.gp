set autoscale; set grid
set mxtics 4
set mytics 4
set tics nomirror
set border 3 front lw 3
set style line 1 lc rgb "#8b1a0e" pt 1 ps 1 lt 1 lw 3
set style line 2 lc rgb "#5e9c36" pt 6 ps 1 lt 1 lw 3
set title "There $f_{[x_{i-1},x_i]}$  is monotonic, too"
set xlabel "Russian shall $ \\lim_{x\\to 0}{\\frac{e^x-1}{2x}} \\overset{\\left[\\frac{0}{0}\\right]}{\\underset{\\mathrm{H}}{=}} \\lim_{x\\to 0}{\\frac{e^x}{2}}$=${\\frac{1}{2}} $ not pass да\nSome no russian text"; set ylabel "сгномсоср $ \\sum\\int_{-\\pi}^{\\pi} x^3 \\pm y^3 $= $ (x \\pm y)(x^2 \\mp xy $+$ y^2) $ ьчпрьпчрп, N"
set terminal epslatex newstyle color solid size 15cm, 9cm # размеры рисунка можно варьировать как угодно
set output "testplot.tex"
plot "dataOrig0.out" u 1:2 w p ps 3 t "",\
	 "dataAprx0.out" u 1:2 w l lw 5 t "",\
