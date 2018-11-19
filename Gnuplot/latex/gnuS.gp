set terminal epslatex newstyle color solid size 9cm, 8cm # размеры рисунка можно варьировать как угодно
set output "testplot.tex"
unset key
set format xy "$%g$"
set xtics 2.5
set ytics 2.5
set xlabel '$xтакже русский текст$'
set ylabel offset +3.0 '$y\frac{1}{2}$'
set title 'что угодно'
set xrange [0:5.5]
set yrange [-5.5:5.5]
plot sqrt(x) lt -1, -sqrt(x) lt -1

