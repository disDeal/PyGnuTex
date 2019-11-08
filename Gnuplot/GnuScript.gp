set autoscale; set grid
set mxtics 4
set mytics 4
set tics nomirror
set border 3 front lw 3
set style line 1 lc rgb "#8b1a0e" pt 1 ps 1 lt 1 lw 3
set style line 2 lc rgb "#5e9c36" pt 6 ps 1 lt 1 lw 3
set title "There $f_{[x_{i-1},x_i]}$  is monotonic, too"
set xlabel "Russian shall not pass  $=$ да\nSome not russian text"; set ylabel "сгномсосрьчпрьпчрп, N"
set terminal epslatex newstyle color solid size 15cm, 9cm # размеры рисунка можно варьировать как угодно
set output "testplot.tex"
plot "dataOrig0.out" u 1:2 w p ps 3 t "что-то для начальных данный",\
	 "dataOrig1.out" u 1:2 w p ps 3 t "",\
	 "dataOrig2.out" u 1:2 w p ps 3 t "до этого был пропуск",\
	 "dataAprx0.out" u 1:2 w l lw 5 t "а это для апроксимации",\
	 "dataAprx1.out" u 1:2 w l lw 5 t "",\
	 "dataAprx2.out" u 1:2 w l lw 5 t "",\
