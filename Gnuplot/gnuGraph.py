import numpy as np
import PyGnuplot as pg

import aprox
import os

from IPython.display import SVG


def dispSVG(name):
    return SVG(name)


def SciPlot(*vect, aprx=[3, 2], xlabel="x-axis", ylabel="y-axis", title="", name="SVGplot", label="", size=[15, 9], origKeys="", aprxKeys=""):
    num = len(vect)
    half = num/2
    if num % 2 != 0:
        print("input the right number of variables")
        pass

    for i in range(int(half)):
        # save data into a file t.out
        pg.s([vect[2*i], vect[2*i + 1]], filename='dataOrig{0}.out'.format(i))

    vect = list(vect)
    for i in range(len(vect)):
        vect[i] = list(map(lambda x: float(x), vect[i]))

    OrKeysVect = 0
    if str(type(origKeys)) == "<class 'str'>":
        OrKeysVect = [origKeys] + ["" for i in range(int(half))]
    else:
        OrKeysVect = [origKeys[i] for i in range(
            len(origKeys))] + ["" for j in range(int(half - len(origKeys)))]

    ApKeysVect = 0
    if str(type(aprxKeys)) == "<class 'str'>":
        ApKeysVect = [aprxKeys] + ["" for i in range(int(half))]
    else:
        ApKeysVect = [aprxKeys[i] for i in range(
            aprxKeys)] + ["" for j in range(int(half - len(aprxKeys)))]

    aprxVect = 0
    if aprx[1] == 0 or aprx[1] == 1 or aprx[1] == 2:
        aprxVect = [aprx for i in range(int(half))]
    else:
        aprxVect = [aprx[i] for i in range(
            len(aprx))] + [aprx[0] for j in range(int(half - len(aprx)))]

    koeffs = [aprox.AprxCoeffs(
        vect[2*i], vect[2*i + 1], aprx=aprxVect[i]) for i in range(int(half))]
    arrs = [(np.linspace(min(vect[2*i]), max(vect[2*i]), 50), aprox.Polin_func2(
        np.linspace(min(vect[2*i]), max(vect[2*i]), 50), koeffs[i])) for i in range(int(half))]

    imprtArr = []
    for i in range(len(arrs)):
        imprtArr += arrs[i]

    for i in range(int(half)):
        pg.s([imprtArr[2*i], imprtArr[2*i + 1]],
             filename='dataAprx{0}.out'.format(i))

    commText = 'set autoscale; set grid\n\
set mxtics 4\n\
set mytics 4\n\
set tics nomirror\n\
set border 3 front lw 3\n\
set style line 1 lc rgb "#8b1a0e" pt 1 ps 1 lt 1 lw 3\n\
set style line 2 lc rgb "#5e9c36" pt 6 ps 1 lt 1 lw 3\n\
set title "{0}"\n\
set xlabel "{1}\\n{3}"; set ylabel "{2}"\n\
set terminal epslatex newstyle color solid size {4}cm, {5}cm # размеры рисунка можно варьировать как угодно\n\
set output "testplot.tex"\n'.format(title, xlabel, ylabel, label, size[0], size[1])

    firstPlot = 'plot "dataOrig0.out" u 1:2 w p ps 3 t "{0}",\\\n'.format(
        OrKeysVect[0])

    orPlots = ['\t "dataOrig{0}.out" u 1:2 w p ps 3 t "{1}",\\\n'.format(
        i + 1, OrKeysVect[i+1]) for i in range(int(half) - 1)]
    SorPlots = ''
    for i in range(len(orPlots)):
        SorPlots += orPlots[i]

    apPlots = ['\t "dataAprx{0}.out" u 1:2 w l lw 5 t "{1}",\\\n'.format(
        i, ApKeysVect[i]) for i in range(len(arrs))]
    SapPlots = ''
    for i in range(len(apPlots)):
        SapPlots += apPlots[i]

    with open("GnuScript.gp", 'w') as outfile:
        outfile.write(commText + firstPlot + SorPlots + SapPlots)

    latexBuild = r'''\documentclass[a4paper]{extreport}
\DeclareRobustCommand{\ttfamily}{\fontencoding{T1}\fontfamily{lmtt}\selectfont}
\DeclareRobustCommand\sectt[1]{{\fontsize{13}{12}\bfseries\ttfamily#1}}
\usepackage[outdir=./]{epstopdf}
\usepackage[TS1,T2A,T1]{fontenc}
\usepackage[babel=true]{microtype}
\usepackage[utf8]{inputenc}
\usepackage[english,russian]{babel}
\usepackage{graphics}
\usepackage{nopageno}
\usepackage{tempora}  % Times for numbers in math mode
\usepackage{newtxmath}  % Times in math mode
\usepackage{txfonts} % данный пакет позволяет вносить текст в изображении
\usepackage[usenames]{color}
\begin{document}
\begin{center}
\input{testplot}
\end{center}
\end{document}'''

    with open("build.tex", 'w') as outfile:
        outfile.write(latexBuild)

    scriptText = 'gnuplot GnuScript.gp\n\
latex build.tex; dvipdf build.dvi\n\
pdfcrop build.pdf {0}.pdf\n\
pdf2ps {0}.pdf {0}.ps\n\
ps2eps -f {0}.ps\n\
eps2svg {0}.eps {0}EPS.svg\n\
pdf2svg {0}.pdf {0}PDF.svg\n\
rm build.dvi build.aux {0}.ps build.pdf'.format(name)

    with open("script.sh", 'w') as outfile:
        outfile.write(scriptText)

    os.system("gnome-terminal -- chmod u+x script.sh; ./script.sh")
    return 1
