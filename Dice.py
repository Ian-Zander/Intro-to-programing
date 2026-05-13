import random
from adafruit_circuitplayground import cp
import time
cp.pixels.auto_write = False

while True:
    if cp.button_a:
        num = random.randint(1, 10)
        cp.pixels.fill((0, 0, 0))
        for i in range(num):
            cp.pixels[i] = (0, 2, 1)
            time.sleep(0.1)
        cp.pixels.show()
    elif cp.button_b:
        cp.pixels.fill((0, 0, 0))