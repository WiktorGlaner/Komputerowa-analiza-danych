import matplotlib.pyplot as plt
import numpy as np

def sum(tab, index):
    suma = 0
    for elem in tab:
        suma += float(elem[index])
    return suma


def max(tab, index):
    res = float(tab[0][index])
    for elem in tab:
        if(float(elem[index]) > res):
            res = float(elem[index])
        
    return res

def min(tab, index):
    res = float(tab[0][index])
    for elem in tab:
        if(float(elem[index]) < res):
            res = float(elem[index])
        
    return res

def sortTab(tab, index):
    sortedTab = []
    for elem in tab:
        sortedTab.append(float(elem[index]))
    sortedTab.sort()
    return sortedTab


def avg(suma, liczba):
    return suma/liczba


def quartile(tab, q):
    if(len(tab)%2 == 1):
        #nieparzysta
        qIndex = int(len(tab) * (q/4))
        return tab[qIndex]
    else:
        #parzysta
        qIndex1 = int(len(tab) * (q/4))-1
        qIndex2 = int(len(tab) * (q/4))
        return (tab[qIndex1]+tab[qIndex2])/2


def stdProba(tab,index):
    avgX = avg(sum(tab,index),len(tab))
    res = 0
    for elem in tab:
        res += (float(elem[index]) - avgX)**2
    res /= len(tab)-1
    res **= 0.5
    return res
    

def filterDataBySpecies(tab, targetSpecies):
    res = []
    for elem in tab:
        if(elem[4] == targetSpecies):
            res.append(elem)
    return res


def makeHistogramSimple(tab, index, title, maxN, minX, maxX, step):
    plt.hist(sortTab(tab,index),np.arange(minX,maxX,step),edgecolor='black')
    plt.xticks(np.arange(minX,maxX,step))
    plt.yticks(np.arange(0,maxN+1,5))
    plt.ylim([0, maxN])
    plt.title(title)
    plt.xlabel(title.split(" ")[0]+" (cm)")
    plt.ylabel("Liczebność")

    plt.show()

def makeBoxplot(tab, index, title, minY, maxY):
    #2.2
    plt.boxplot([
        sortTab(filterDataBySpecies(tab,"0"),index),
        sortTab(filterDataBySpecies(tab,"1"),index),
        sortTab(filterDataBySpecies(tab,"2"),index)
    ])
    plt.ylim([minY, maxY])
    plt.xlabel("Gatunek")
    plt.ylabel(title.split(" ")[0]+" (cm)")
    plt.title(title)
    plt.xticks([1,2,3], ["setosa","versicolor", "virginica"])
    plt.yticks(np.arange(minY,maxY+0.1,1))

    plt.show()


def makeHistogramComplex(tab, index, title, maxN, minX, maxX, step):
    
    plt.title(title)
    
    plt.hist([sortTab(filterDataBySpecies(tab,"0"),index),
              sortTab(filterDataBySpecies(tab,"1"),index),
              sortTab(filterDataBySpecies(tab,"2"),index)
    ],np.arange(minX, maxX, step),label=["Setosa","Versicolor","Virginica"],edgecolor='black')
            
    
    
    plt.xlabel(title.split(" ")[0]+" (cm)")
    plt.ylabel("Liczebność")
    plt.ylim([0, maxN])
    plt.xticks(np.arange(minX,maxX,step))
    plt.yticks(np.arange(0,maxN+1,5))
    plt.legend()
    plt.show()