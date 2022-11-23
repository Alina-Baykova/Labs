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
m = []
massive = [speed_00_array, speed_10_array, speed_20_array, speed_30_array, speed_40_array,
           speed_50_array, speed_60_array, speed_70_array, speed_80_array, speed_90_array, speed_100_array]
for m in massive:
    k = 0
    while k != 3:
        summa_right = 0
        summa_left = 0
        delta_S = 0
        for j in range(0, len(m)-1):
            r_i = abs(steps_distance[j]) * (1e-03)
            r_i_1 = abs(steps_distance[j+1]) * (1e-03)
            V_i = m[j]
            V_i_1 = m[j+1]
            if steps_distance[j] < 0:
                summa_left = summa_left + 0.5*(V_i + V_i_1)*(abs(r_i_1 - r_i))
            if steps_distance[j] >= 0:
                summa_right = summa_right + 0.5 * (V_i + V_i_1) * (abs(r_i_1 - r_i))
        delta_S = summa_left - summa_right
        if delta_S > 0:
            for j in range(0, len(m) - 1):
                m[(len(m) - 1) - j] = m[(len(m) - 1) - j - 1]
            k = k + 2
        if delta_S < 0:
            for j in range(0, len(m) - 1):
                m[j] = m[j+1]
            k = 1
        if delta_S == 0: k = 3;

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
    Q_array.append(str(round(summa * 3.14 * 1.2 / 2, 2)))

#Обьявляем массивов скоростей для Y оси
data_V_00 = numpy.array(speed_00_array)
data_V_10 = numpy.array(speed_10_array)
data_V_20 = numpy.array(speed_20_array)
data_V_30 = numpy.array(speed_30_array)
data_V_40 = numpy.array(speed_40_array)
data_V_50 = numpy.array(speed_50_array)
data_V_60 = numpy.array(speed_60_array)
data_V_70 = numpy.array(speed_70_array)
data_V_80 = numpy.array(speed_80_array)
data_V_90 = numpy.array(speed_90_array)
data_V_100 = numpy.array(speed_100_array)
#массив шагов в [м]
data_steps=numpy.array(steps_distance)

#параметры фигуры (чем меньше фигура тем выраженее пиксели и развёртка вспомогательной и главной сетки
fig, ax=pyplot.subplots(figsize=(12, 7), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([-22, data_steps.max() + 2, -1.4, data_V_00.max() + 1.3])

#Включаем видимость сетки и делений и вводим их параметры ниже (Если включить сетку ниже парамтеров, то параметры не присвоятся)
ax.minorticks_on()

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'y', which = 'major', labelsize = 14, pad = 2, length = 8)
ax.tick_params(axis = 'x', which = 'major', labelsize = 10, pad = 2, length = 8)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 7, pad = 2, length = 2.5)

#название графика с условием для переноса строки и центрированием
ax.set_title('Скорость потока воздуха' + '\n' + 'в сечении затопленной струи', fontsize = 19, pad = 14, loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')

#Подпись осей
ax.set_ylabel("Скорость воздуха [м/c]", fontsize = 16)
ax.set_xlabel("Положение трубки Пито относительно центра струи [мм]", fontsize = 12)

#Добавление самого графика и (в конце присваивает наличие леге label =...), настройка цветов https://pyprog.pro/mpl/mpl_plot.html
ax.plot(data_steps, data_V_00, c='indigo', linewidth=1.5, label = 'Q (00 мм) = '+ Q_array[0] + '[г/c]')
ax.plot(data_steps, data_V_10, c='b', linewidth=1.5, label ='Q (10 мм) = '+ Q_array[1] + '[г/c]')
ax.plot(data_steps, data_V_20, c='g', linewidth=1.5, label ='Q (20 мм) = '+ Q_array[2] + '[г/c]')
ax.plot(data_steps, data_V_30, c='r', linewidth=1.5, label ='Q (30 мм) = '+ Q_array[3] + '[г/c]')
ax.plot(data_steps, data_V_40, c='#F97306', linewidth=1.5, label ='Q (40 мм) = '+ Q_array[4] + '[г/c]')
ax.plot(data_steps, data_V_50, c='m', linewidth=1.5, label ='Q (50 мм) = '+ Q_array[5] + '[г/c]')
ax.plot(data_steps, data_V_60, c='c', linewidth=1.5, label ='Q (60 мм) = '+ Q_array[6] + '[г/c]')
ax.plot(data_steps, data_V_70, c='y', linewidth=1.5, label ='Q (70 мм) = '+ Q_array[7] + '[г/c]')
ax.plot(data_steps, data_V_80, c='#AAFF32', linewidth=1.5, label ='Q (80 мм) = '+ Q_array[8] + '[г/c]')
ax.plot(data_steps, data_V_90, c='#FF81C0', linewidth=1.5, label ='Q (90 мм) = '+ Q_array[9] + '[г/c]')
ax.plot(data_steps, data_V_100, c='#653700', linewidth=1.5, label ='Q (100 мм) = '+ Q_array[10] + '[г/c]')

#Маркеры---
#Добавил маркеры в легенду с надписью измерения

#Добавление легенды: https://pyprog.pro/mpl/mpl_adding_a_legend.html
ax.legend(shadow = False, loc = 'upper right', fontsize = 13)

#Добавление текста  https://pyprog.pro/mpl/mpl_text.html
ax.text(90, 0.3, '', rotation = 0, fontsize = 21)

#сохранение
fig.savefig('velocity-outgo.png')