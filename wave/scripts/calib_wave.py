import numpy as np
import matplotlib.pyplot as plt

def read(file):
  data = []
  with open(file, 'r') as file:
    for line in file.readlines():
      data.append(float(line))
  return np.array(data)

def aver(data):
  return np.sum(data) / np.size(data)

mm_20 = read('wave-data-20mm-kalibr.txt')
mm_40 = read('wave-data-40mm.-kalibr.txt')
mm_60 = read('wave-data-60mm-kalibr.txt')
mm_80 = read('wave-data-80mm-kalibr.txt')
mm_100 = read('wave-data-100mm-kalibr.txt')
mm_120 = read('wave-data-120mm-kalibr.txt')

x = np.array([aver(mm_20), aver(mm_40), aver(mm_60), aver(mm_80), aver(mm_100), aver(mm_120)])
y = np.array([20, 40, 60, 80, 100, 120])

coeff = np.polyfit(x,y,2)
xn = np.linspace(110,220,1000)
yn = np.poly1d(coeff)

plt.figure(figsize=(8,6), dpi=100)
plt.xlim(110, 220)
plt.title('Калибровочный график зависимости показаний АЦП от уровня воды')
plt.ylabel("Уровень воды [мм]")
plt.xlabel("Отсчёты АЦП")
plt.grid(which = 'major', color = '#A0A0A0')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#E0E0E0')
plt.scatter(x, y, label = 'Измерения')
plt.plot(xn, yn(xn), label = 'Калибровочный полином', color = 'orange')
plt.legend()
plt.savefig('calib_wave.png')