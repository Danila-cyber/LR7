'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 20: Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в банке на К разных вкладах.
Ограничение: На вклад нельзя положить сумму меньше, чем 25% от всей суммы.
'''
import itertools
import math
from tkinter import *
from tkinter import ttk

itstrs = []
funcstrs = []

root = Tk()
root.geometry('1200x840')
root.resizable(False, False)
root.title("Размещение суммы денег на разных вкладах")

labelSum = ttk.Label(text="Сумма для вкладов: ")
labelSum.place(anchor=NW, x = 30, y = 20, height = 25)
entrycSum = ttk.Entry()
entrycSum.place(anchor=NW, x = 170, y = 20, height = 25, width = 150)

labelcDepos = ttk.Label(text="Кол-во вкладов: ")
labelcDepos.place(anchor=NW, x = 370, y = 20, height = 25)
entrycDepos = ttk.Entry()
entrycDepos.place(anchor=NW, x = 480, y = 20, height = 25, width = 100)

labelit = ttk.Label(text="Результат Itertools : ")
labelit.place(anchor=NW, x = 30, y = 60, height = 25, width = 240)

labelal = ttk.Label(text="Результат алгоритма : ")
labelal.place(anchor=NW, x = 30, y = 420, height = 25, width = 240)

def drawScroll():
    itlist = StringVar(value=itstrs)
    listboxd = Listbox(listvariable=itlist)
    listboxd.place(anchor=NW, x=30, y=90, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=90, x=1150, width=20, height=320)
    listboxd["yscrollcommand"] = scrollbar.set

    funclist = StringVar(value=funcstrs)
    listboxt = Listbox(listvariable=funclist)
    listboxt.place(anchor=NW, x=30, y=450, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxt.yview)
    scrollbar.place(anchor=NW, y=450, x=1150, width=20, height=320)
    listboxt["yscrollcommand"] = scrollbar.set

drawScroll()

def locate(summ, countDepos, varr, result, limit):
    if countDepos == 0:
        if summ == 0:
            funcstrs.append(varr[:])
        return
    for i in range(limit, summ + 1):
        varr.append(i)  
        locate(summ - i, countDepos - 1, varr, funcstrs, limit)
        varr.pop()

def locateIterTools(summ, countDepos, limit):
    for i in itertools.combinations_with_replacement(range(limit, summ+1), countDepos):
        if sum(i) == summ:
            itstrs.append(i)
    for i in itertools.combinations_with_replacement(range(summ, limit-1, -1), countDepos):
        if sum(i) == summ and not(itstrs.count(i)):
            itstrs.append(i)

def arrFormat(arr, countDepos):
    newArr = []
    newArr.append("    ".join(map(lambda num: str(num)+" вклад", range(1, countDepos+1))))
    for nums in arr:
        newArr.append("                  ".join(map(lambda num: str(num), nums)))
    return newArr

def main():
    global funcstrs
    global itstrs
    try:
        summa = int(entrycSum.get())
        depos = int(entrycDepos.get())
    except:
        return

    limit = int(summa*0.25)
    res = []
    locate(summa, depos, [], res, limit)
    locateIterTools(summa, depos, limit)
    funcstrs = arrFormat(funcstrs, depos)
    itstrs = arrFormat(itstrs, depos)

    drawScroll()

btn = ttk.Button(text="Разместить", command=main)
btn.place(anchor=NW, x = 650, y = 20, height = 25, width = 100)

root.mainloop()   
