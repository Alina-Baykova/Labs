#График (точки из файла)
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
x3=[]
y3=[]
with open('data', 'r') as file:
    arr=file.readlines()
    for line in arr:
        arrx, arry = line.split()
        x3.append(float(arrx))
        y3.append(float(arry))


#Рисование крестов и другое
fig, ax = plt.subplots()
ax.set_title('График зависимости расхода' + '\n' + 'от расстояния до сопла')
ax.set_xlabel("Расстояние от сопла до трубки Пито [мм]")
ax.set_ylabel("Массовый расход в сечении струи [г/с]")
ax.grid(True, linestyle='-.')
ax.tick_params(labelsize='medium', width=3)

yerr3=[]
for i in y3:
    yerr3.append(0.007*i+0.001)
ax.errorbar(x3, y3, yerr3, fmt='.', linewidth=2, capsize=6, color='k')

#Апроксимация

def mapping(x, a, b):
    return a * x + b

args, covar = curve_fit(mapping, x3, y3)
a3 = args[0]
b3 = args[1]
xx3=[]
yy3=[]
for i in range(110):
    xx3.append(i)
    yy3.append(a3 * i + b3)
plt.plot(xx3, yy3, x3, y3)
plt.show()
'''
from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
from math import sqrt
#https://pyprog.pro/mpl/mpl_main_components.html

# P = (p*V^2)/2; p(плотность воздуха) = 1.2 кг/м^3;
def Bernule(N):
    p = 1.2
    P = 0.163*(N-1000)
    V = sqrt(2*abs(P)/p)
    if P < 0 or V < 2:
        return 0
    return(V)


with open("00mm.txt", "r") as file:
    speed_00_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("10mm.txt", "r") as file:
    speed_10_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("20mm.txt", "r") as file:
    speed_20_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("30mm.txt", "r") as file:
    speed_30_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("40mm.txt", "r") as file:
    speed_40_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("50mm.txt", "r") as file:
    speed_50_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("60mm.txt", "r") as file:
    speed_60_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("70mm.txt", "r") as file:
    speed_70_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("80mm.txt", "r") as file:
    speed_80_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("90mm.txt", "r") as file:
    speed_90_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("100mm.txt", "r") as file:
    speed_100_array = [Bernule(int(i)) for i in file.read().split("\n")]
with open("distance-calibration.txt", "r") as file:
    steps_distance= [(int(i)-350)*(5.56e-02)for i in file.read().split("\n")]

#Калибровка погрешностей измерений
for j in range(0, len(steps_distance)):
        if steps_distance[j] < -4.6 or steps_distance[j] > 6:
            speed_00_array[j] = 0
        if steps_distance[j] < -5.2 or steps_distance[j] > 7:
            speed_10_array[j] = 0
        if steps_distance[j] < -6 or steps_distance[j] > 7.7:
            speed_20_array[j] = 0
        if steps_distance[j] < -6 or steps_distance[j] > 11.2:
            speed_30_array[j] = 0
        if steps_distance[j] < -10 or steps_distance[j] > 12:
            speed_40_array[j] = 0
        if steps_distance[j] < -10 or steps_distance[j] > 13:
            speed_50_array[j] = 0
        if steps_distance[j] < -13 or steps_distance[j] > 15:
            speed_60_array[j] = 0
        if steps_distance[j] < -17 or steps_distance[j] > 17:
            speed_70_array[j] = 0
        if steps_distance[j] < -15.4 or steps_distance[j] > 16:
            speed_80_array[j] = 0
        if steps_distance[j] < -16 or steps_distance[j] > 18 :
            speed_90_array[j] = 0
        if steps_distance[j] < -17 or steps_distance[j] > 20:
            speed_100_array[j] = 0

#Автоматическое центрирование графиков по равенству левой и правой площади каждого графика относительно нуля:
# m = []
# massive = [speed_00_array, speed_10_array, speed_20_array, speed_30_array, speed_40_array,
#            speed_50_array, speed_60_array, speed_70_array, speed_80_array, speed_90_array, speed_100_array]
# for m in massive:
#     k = 0
#     while k != 3:
#         summa_right = 0
#         summa_left = 0
#         delta_S = 0
#         for j in range(0, len(m)-1):
#             r_i = abs(steps_distance[j]) * (1e-03)
#             r_i_1 = abs(steps_distance[j+1]) * (1e-03)
#             V_i = m[j]
#             V_i_1 = m[j+1]
#             if steps_distance[j] < 0:
#                 summa_left = summa_left + 0.5*(V_i + V_i_1)*(abs(r_i_1 - r_i))
#             if steps_distance[j] >= 0:
#                 summa_right = summa_right + 0.5 * (V_i + V_i_1) * (abs(r_i_1 - r_i))
#         delta_S = summa_left - summa_right
#         if delta_S > 0:
#             for j in range(0, len(m) - 1):
#                 m[(len(m) - 1) - j] = m[(len(m) - 1) - j - 1]
#             k = k + 2
#         if delta_S < 0:
#             for j in range(0, len(m) - 1):
#                 m[j] = m[j+1]
#             k = 1
#         if delta_S == 0: k = 3;

#Расчёт расходов для всех сечений
m = []
Q_array = []
massive = [speed_00_array, speed_10_array, speed_20_array, speed_30_array, speed_40_array,
           speed_50_array, speed_60_array, speed_70_array, speed_80_array, speed_90_array, speed_100_array]
for m in massive:
    summa = 0
    for j in range(0, len(m)-1):
        r_i = abs(steps_distance[j]) * (1e-03)
        r_i_1 = abs(steps_distance[j+1]) * (1e-03)
        V_i = m[j]
        V_i_1 = m[j+1]
        summa = summa + (r_i * V_i + r_i_1 * V_i_1)*(abs(r_i_1 - r_i)) * (1e+03)
    Q_array.append(round(summa * 3.14 * 1.2 / 2, 2))

#Обьявляем массив значений расхода
data_Q = numpy.array(Q_array)

#массив расстояний от сопла в [мм]
data_s=numpy.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

#параметры фигуры (чем меньше фигура тем выраженее пиксели и развёртка вспомогательной и главной сетки
fig, ax=pyplot.subplots(figsize=(12, 7), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([-5, data_s.max() + 5, 1.5, data_Q.max() + 0.8])

#Включаем видимость сетки и делений и вводим их параметры ниже (Если включить сетку ниже парамтеров, то параметры не присвоятся)
ax.minorticks_on()

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'y', which = 'major', labelsize = 14, pad = 2, length = 8)
ax.tick_params(axis = 'x', which = 'major', labelsize = 10, pad = 2, length = 8)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 7, pad = 2, length = 2.5)

#название графика с условием для переноса строки и центрированием
ax.set_title('График зависимости расхода' + '\n' + 'от расстояния до сопла', fontsize = 19, pad = 14, loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')

#Подпись осей
ax.set_ylabel("Массовый расход в сечении струи [г/с]", fontsize = 14)
ax.set_xlabel("Расстояние от сопла до трубки Пито [мм]", fontsize = 12)

#Апроксимация графика в линейную зависимость y = kx + c
Apr = numpy.polyfit(data_s, data_Q, 1)
polinom = numpy.poly1d(Apr)
y = polinom(data_s)
k = 0.04262
c = 2.261
mas_y_apr = numpy.array([(k*x + c) for x in data_s])
print(polinom)

#Добавление самого графика и (в конце присваивает наличие леге label =...), настройка цветов https://pyprog.pro/mpl/mpl_plot.html
ax.plot(data_s, data_Q, c='#F97306', linewidth=3, label ='Q(s) [г/c]')
#Добавление графика аппроксимации:
ax.plot(data_s, mas_y_apr, c='g', linewidth=3, label ='Apr(Q(s)) [г/c]')

#Маркеры
ax.scatter(data_s[0:data_Q.size:1], data_Q[0:data_Q.size:1], marker ='s', c ='blue', s=80, label='Измерения')
#Добавил маркеры в легенду с надписью измерения
ax.scatter(data_s[0:mas_y_apr.size:10], mas_y_apr[0:mas_y_apr.size:10], marker ='o', c ='g', s=80)

#Добавление легенды: https://pyprog.pro/mpl/mpl_adding_a_legend.html
ax.legend(shadow = False, loc = 'upper left', fontsize = 15)

#Добавление текста  https://pyprog.pro/mpl/mpl_text.html
ax.text(90, 0.3, '', rotation = 0, fontsize = 21)
'''
#сохранение
fig.savefig('Flow_dependence_graph.png')