import bloodFunctions as b
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)

b.initSpiAdc()

PRESSURE_LOWER_BOUND = 450
calibr = False
if calibr is False:
    try:
        data = []
        start = time.time()
        while True:
            current_data = b.getAdc()
            data.append(current_data)

            if current_data < PRESSURE_LOWER_BOUND:
                break
        
        finish = time.time()

        b.save(data, start, finish)

        plt.plot(data)
        plt.show()
    except KeyboardInterrupt:
        finish = time.time()
        b.save(data, start, finish)
        plt.plot(data)
        plt.show()
    finally:
        b.deinitSpiAdc()
else:
    try:
        data = []

        start = time.time()
        

        while True:
            now = time.time()
            current_data = b.getAdc()
            data.append(current_data)

            if now - start >= 60:
                break
                 
        finish = time.time()

        b.save(data, start, finish)
    except KeyboardInterrupt:
        finish = time.time()
        b.save(data, start, finish)
        plt.plot(data)
        plt.show()
    finally:
        b.deinitSpiAdc()