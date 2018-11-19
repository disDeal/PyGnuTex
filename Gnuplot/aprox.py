# coding: utf-8

import numpy as np
from numpy import zeros, dot, savetxt
import matplotlib
from matplotlib import pylab as plt
from math import ceil


##############################################################

def AprxCoeffs(x, y, aprx=[8, 0]):

    izn2 = list(x)
    fzn2 = list(y)

    if aprx[1] == 2:
        npCoeff = np.polyfit(x, y, aprx[0])
        return [npCoeff[len(npCoeff) - i - 1] for i in range(len(npCoeff))]

    if aprx[1] == 0:
        aprx[0] = len(x) - aprx[0] - 1

    if aprx[1] == 1:
    
        l = int(len(x)/aprx[0])
        izn3 = [izn2[n*l] for n in range(aprx[0])] + [izn2[-1]]
        fzn3 = [fzn2[n*l] for n in range(aprx[0])] + [fzn2[-1]]
    
    else:
        
        def halfchange(arr, size): #разбиваем участок на интервалы, находим среднее по интервалу и строим линии 
            return list(map(lambda x: arr[x * size:x * size + size],
                            list(range(0, ceil(len(arr) / size)))))
        izn3 = [];fzn3 = []
        izn3 += [sum(i)/len(i) for i in halfchange(izn2, aprx[0])]
        fzn3 += [sum(i)/len(i) for i in halfchange(fzn2, aprx[0])]

    def coeff_search(izn3 = izn3, fzn3 = fzn3):
        work_m = list(map(lambda x: float(x), izn3))
        znach_func = list(map(lambda x: float(x), fzn3))
        for i in range(len(work_m)):            #из списка в матрицу
            work_m[i] = [work_m[i]]
        for i in range(len(work_m)):            #умножения количества элементов 
            work_m[i] = work_m[i] * (len(work_m))
        N = 0
        for i in range(len(work_m)):            #создание матрицы квадратов
            for j in range(len(work_m)):
                work_m[i][j] = work_m[i][j] ** N
                N += 1
            N = 0
        koeff = np.linalg.solve(work_m, znach_func) #Находим решение системы
        return koeff
    
    return coeff_search()
######################################################################

def Polin_func2(vector, koeff):
    znach_v = []
    shab = []
    for znach in vector:
        for i in range(len(koeff)):
            shab += [koeff[i] * (znach ** i)]
        znach_v += [float(sum(shab))]
        shab = []
    return znach_v
    


def DrawApx(mn, mx, koeff, x, y):
    # Построение графика

    dis = np.linspace(mn, mx, mx - mn)
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.grid(1)
    plt.plot(x, y, '*', dis, Polin_func2(dis, koeff),'-b')
    plt.show()

def FromData(name):
    with open(name) as f:
        lines = f.read()

    spltText = lines.split("\n")
    wArr = []
    for i in range(len(spltText) - 1):
        if spltText[i][0] != "#":
            wArr.append(spltText[i])

    numVar = len(wArr[0].split(" "))
    arr = [wArr[i].split(" ")[:numVar - 1] for i in range(len(wArr))][:len(wArr) - 1]

    vect = [[] for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(vect)):
            vect[j].append(arr[i][j])

    return vect
