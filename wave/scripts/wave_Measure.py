import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
import numpy as np
import math


def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples


avg_h = []
avg_h.append(np.average(read("20mm.txt")))
avg_h.append(np.average(read("40mm.txt")))
avg_h.append(np.average(read("60mm.txt")))
avg_h.append(np.average(read("80mm.txt")))
avg_h.append(np.average(read("100mm.txt")))
avg_h.append(np.average(read("120mm.txt")))
v = [20, 40, 60, 80, 100, 120]
#h = [math.log10(x/1000) for x in h1]
fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500)

#ax.axis([math.log10(0.13), 0, 0, v.max()])s

ax.set_title('Зависимость сигнала АЦП от глубины жидкости')
ax.set_ylabel("Величина сигнала")
ax.set_xlabel("Глубина, мм")


#ax.scatter(h[0:5:100], v[0:5:100], marker = 's', c = 'green', s=10)


z = np.polyfit(v, avg_h, 4)
p = np.poly1d(z)

xp = np.linspace(20, 120, 100)
pyplot.plot(xp, p(xp), '-', c='red', label='S(t)')
ax.scatter(v, avg_h, c='black', linewidth=1)
ax.legend(shadow = False, loc = 'right', fontsize = 30)
pyplot.grid()
fig.savefig('graphic.png')
#fig.savefig('graphic.svg')


pyplot.show()


import RPi.GPIO as gpio
from time import sleep
import time
from matplotlib import pyplot
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
knop_out=2
knop_in=22
gpio.setup(knop_out, gpio.OUT, initial=gpio.HIGH)
gpio.setup(knop_in, gpio.IN)
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, perev(k))
        sleep(0.005)
        if gpio.input(comp)==0:
            k-=2**i
    return k

def waitForOpen():

    print('GPIO initialized. Wait for door opening...')

    while gpio.input(knop_in) > 0:
        pass

    print('The door is open. GPIO has been cleaned up. Start sampling...')

volt=[]
time_start=0
time_len=0

try:
    waitForOpen()
    time_start=time.time()
    while time.time()- 15 < time_start:
        volt.append(adc()/256*3.3)
    
    
finally:
    time_len=time.time()-time_start

    with open('wave-data- 40mm-measure.txt', 'w') as file:
        file.write(str(time_len) +'\n')
        for i in volt:
            file.write(str(i) +'\n')

    
    time_step=[i*time_len/len(volt) for i in range(len(volt))]
    pyplot.plot(time_step, volt)
    pyplot.show()
    gpio.output(dac, 0)
    gpio.cleanup() 
