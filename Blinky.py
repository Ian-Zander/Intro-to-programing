import time
from adafruit_circuitplayground import cp
while True:
    cp.pixels.fill((0, 2, 0))
    time.sleep(0.367)
    cp.pixels.fill((0, 0, 0))
    time.sleep(0.367)
    