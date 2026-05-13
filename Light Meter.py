from adafruit_circuitplayground import cp
import time
while True:
    light = cp.light
    if light >= 30:
        pixels_on = 1
    else:
        pixels_on = 1 + (30 - light) // 3
    pixels_on = min(pixels_on, 10)
    cp.pixels.fill((0, 0, 0))
    for i in range(pixels_on):
        cp.pixels[i] = (0, 2, 1)
    time.sleep(0.1)