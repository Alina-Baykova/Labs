import bloodFunctions as func
import time

try:
    func.initSpiAdc()

    duration = 60
    samples = []

    start = time.time()

    while(time.time() - start < duration):
        samples.append(func.getAdc())

    finish = time.time()

    func.save(samples, start, finish)

finally:
    func.deinitSpiAdc()
