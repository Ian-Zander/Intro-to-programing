import random
import time
from adafruit_circuitplayground import cp

while True:
    if cp.shake():
        for i in range(len(cp.pixels)):
            cp.pixels[i] = (
                random.randrange(32),
                random.randrange(32),
                random.randrange(32),
            )
        cp.pixels.show()
        time.sleep(0.5)