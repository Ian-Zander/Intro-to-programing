import time
from adafruit_circuitplayground import cp
while True:
    if cp.button_a:
        for i in range(10):
            cp.pixels[i] = (0, 2, 2)
            time.sleep(0.1)
            cp.pixels[i] = (0, 0, 0)