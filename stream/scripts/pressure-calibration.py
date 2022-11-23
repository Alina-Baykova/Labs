from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
#https://pyprog.pro/mpl/mpl_main_components.html

with open("pascal_0.txt", "r") as file:
    pressure_0 = sum([int(i) for i in file.read().split("\n")])/500

with open("pascal_55.txt", "r") as file:
    pressure_150 = sum([int(i) for i in file.read().split("\n")]) / 500
# ΔP = kN + c:
k_n = 54.5/(pressure_150 - pressure_0)
k = str(round(54.5 / (pressure_150 - pressure_0), 3))
c = str(round( k_n * pressure_0, 1))

#считываем показания АЦП в 2-ух состояниях
data = numpy.array([pressure_0, pressure_150])
#считываем показания 2-ух велечи: разницу давлений с атмосферным до включения двигателя и после
data_steps = numpy.array([0, 54.5])
#параметры фигуры
fig, ax = pyplot.subplots(figsize=(9, 7), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([-2, data_steps.max() + 5.5, 940, 1350])

#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя)
ax.minorticks_on()

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2.5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(25))

#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)

#название графика с условием для переноса строки и центрированием
ax.set_title("\n".join(wrap('Калибровочный график зависимости показаний АЦП от давления', 40)), fontsize = 20, loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')


#подпись осей
ax.set_ylabel("Отсчёты АЦП (N)", fontsize = 16)
ax.set_xlabel("Давление ΔP [Па]", fontsize = 16)


#Добавление самого графика и (в конце присваивает наличие леге label =...)
ax.plot(data_steps, data, c='red', linewidth=2, label ='ΔP = ' + k + '*N - ' + c + '[Па]')
#маркеры
ax.scatter(data_steps[0:data.size:1], data[0:data.size:1], marker ='.', c ='blue', s=350, label='Измерения')
#Добавил маркеры в легенду с надписью измерения

#Добавление легенды: https://pyprog.pro/mpl/mpl_adding_a_legend.html
ax.legend(shadow = False, loc = 'upper left', fontsize = 17)

#Добавление текста  https://pyprog.pro/mpl/mpl_text.html
ax.text(18, 1008, 'Коэффициент калибровки '+ '\n' +'          давления = '+k + '[Па]', rotation = 0, fontsize = 21)

#сохранение
fig.savefig('pressure_calibration.png')