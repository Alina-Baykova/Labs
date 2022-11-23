from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
#https://pyprog.pro/mpl/mpl_main_components.html

#считываем показания 2-ух измерений расстояния (начального и конечного)
data = numpy.array([0, 3.861])
#считываем показания 2-ух измерений шагов (начального и конечного)
data_steps = numpy.array([0, 700])
#параметры фигуры
fig, ax = pyplot.subplots(figsize=(9, 7), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([-20, data_steps.max() + 55, -0.2, 4])

#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя))
ax.minorticks_on()

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(25))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)

#название графика с условием для переноса строки и центрированием
ax.set_title("\n".join(wrap('Калибровочный график зависимости перемещения трубки Пито от шага двигателя', 40)), fontsize = 17, loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')

#подпись осей
ax.set_ylabel("Перемещение трубки Пито [см]", fontsize = 18)
ax.set_xlabel("Количество шагов", fontsize = 16)

#Добавление самого графика и (в конце присваивает наличие леге label =...)
ax.plot(data_steps, data, c='red', linewidth=2, label ='Y = 5.56e-05 * steps [м]')
#маркеры
ax.scatter(data_steps[0:data.size:1], data[0:data.size:1], marker ='.', c ='green', s=400, label='Измерения')
#Добавил маркеры в легенду с надписью измерения

#Добавление легенды: https://pyprog.pro/mpl/mpl_adding_a_legend.html
ax.legend(shadow = False, loc = 'upper left', fontsize = 17)

#Добавление текста  https://pyprog.pro/mpl/mpl_text.html
ax.text(320, 1.1, 'Коэффициент калибровки ' + '\n' + 'расстояния = 5.56e-05 [м]', rotation = 0, fontsize = 20)

#сохранение
fig.savefig('distance-calibration.png')