import RPi.GPIO as GPIO
import spidev
import time
import numpy as np


########################################
#   Open, use and close SPI ADC
########################################

spi = spidev.SpiDev()
cs = 8

def initSpiAdc():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(cs, GPIO.OUT)
    GPIO.output(cs, 1)

    spi.open(0, 0)
    spi.max_speed_hz = 1600000
    print ("SPI for ADC have been initialized")

def deinitSpiAdc():
    GPIO.output(cs, 0)
    GPIO.cleanup()

    spi.close()
    print ("SPI cleanup finished")

def getAdc():
    GPIO.output(cs, 0)
    adcResponse = spi.xfer2([0, 0])
    GPIO.output(cs, 1)
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1


########################################
#   Save and read data
########################################

def save(samples, start, finish):
    filename = 'blood-data {}.txt'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))

    with open(filename, "w") as outfile:
        outfile.write('- Blood Lab\n')
        outfile.write('- Date: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        outfile.write('- Duration: {:.2f} s\n\n'.format(finish - start))
        
        np.savetxt(outfile, np.array(samples).T, fmt='%d')

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples, duration, len(samples)
