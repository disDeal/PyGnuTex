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
        print("wrong number of variables")
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

# commText = 'set autoscale; set grid\n\
# set mxtics 4\n\
# set mytics 4\n\
# set tics nomirror\n\
# set border 3 front lw 3\n\
# set style line 1 lc rgb "#8b1a0e" pt 1 ps 1 lt 1 lw 3\n\
# set style line 2 lc rgb "#5e9c36" pt 6 ps 1 lt 1 lw 3\n\
# set title "{0}"\n\
# set xlabel "{1}\\n{3}"; set ylabel "{2}"\n\
# set terminal epslatex newstyle color solid size {4}cm, {5}cm # размеры рисунка можно варьировать как угодно\n\
# set output "testplot.tex"\n'.format(title, xlabel, ylabel, label, size[0], size[1])

    tex_header = '\documentclass[12pt]{article}\n\
% Подключаем всяко-разное, задаем кодировку, язык и прочие параметры по вкусу\n\
\\usepackage[OT1,T2A]{fontenc}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage[english,russian]{babel}\n\
\\usepackage{amsmath,amssymb,amsfonts,textcomp,latexsym,pb-diagram,amsopn}\n\
\\usepackage{cite,enumerate,float,indentfirst}\n\
\\usepackage{graphicx,xcolor}\n\
% Порядку для задаем размер полей страницы, дальше это нам пригодится\n\
\\usepackage[left=2mm, right=2mm, top=2mm, bottom=2mm]{geometry}\n\
% Включаем Gnuplottex\n\
\\usepackage{gnuplottex}\n\
\\begin{document}\n\
\\begin{figure}\n\
  \\centering\n\
  \\begin{gnuplot}\n\  '

    commText =  "set terminal epslatex newstyle color size 17cm,8cm\n\
   set xzeroaxis lt -1\n\
   set yzeroaxis lt -1\n\
   set mxtics 4\n\
   set mytic 4\n\
   set autoscale\n\
   set tics nomirror out scale 0.75\n\
   set border 3 front lw 3\n\
   set style line 1 lt 1 lw 4 lc rgb '#4682b4' pt -1 \n\
   set style line 2 lt 1 lw 4 lc rgb '#ee0000' pt -1 \n\
   set style line 3 lt 1 lw 4 lc rgb '#008800' pt -1\n\
   set style line 4 lt 1 lw 4 lc rgb '#888800' pt -1\n\
   set style line 5 lt 1 lw 4 lc rgb '#00aaaa' pt -1\n\
   set style line 6 lt 1 lw 4 lc rgb '#cc0000' pt -1\n\
   set key bottom right   \n\
   set grid xtics lc rgb '#555555' lw 1 lt 0\n\
   set grid ytics lc rgb '#555555' lw 1 lt 0;"
    
    commGraph = "set title '{0}'\n\
set xlabel '{1}'\n\
set ylabel '{2}'\n  ".format(title, xlabel, ylabel, label, size[0], size[1])


    firstPlot = "plot 'dataOrig0.out' u 1:2 w p ps 3 ti '{0}',\\\n".format(
        OrKeysVect[0])

    orPlots = ["\t 'dataOrig{0}.out' u 1:2 w p ps 3 ti '{1}',\\\n".format(
        i + 1, OrKeysVect[i+1]) for i in range(int(half) - 1)]
    SorPlots = ''
    for i in range(len(orPlots)):
        SorPlots += orPlots[i]

    apPlots = ["\t 'dataAprx{0}.out' u 1:2 w l lw 5 ti '{1}',\\\n".format(
        i, ApKeysVect[i]) for i in range(len(arrs))]
    SapPlots = ''
    for i in range(len(apPlots)):
        SapPlots += apPlots[i]

    tex_end = '\\end{gnuplot}\n\
\\end{figure}\n\
\\end{document}'

    with open("build.tex", 'w') as outfile:
        outfile.write(tex_header + commText + commGraph + firstPlot + SorPlots + SapPlots + tex_end)

    scriptText = 'latex --shell-escape build.tex;\n\
dvips build.dvi;\n\
ps2pdf build.ps;\n\
pdfcrop build.pdf;\n\
pdf2svg build.pdf {0}.svg\n\
pdftoppm build-crop.pdf {0} -png;\n'.format(name)

    with open("script.sh", 'w') as outfile:
        outfile.write(scriptText)

    os.system("chmod +x script.sh; ./script.sh")
    return 1
