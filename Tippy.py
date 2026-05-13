import time
from adafruit_circuitplayground import cp

green_pixels = [1, 2, 3]
red_pixels = [6, 7, 8]

def set_pixels(indices, color):
    for i in indices:
        cp.pixels[i] = color

while True:
    x = cp.acceleration[0]
    if x < 0:
        set_pixels(green_pixels, (0, 2, 0))
        set_pixels(red_pixels, (0, 0, 0))
    elif x > 0:
        set_pixels(green_pixels, (0, 0, 0))
        set_pixels(red_pixels, (2, 0, 0))
    else:
        set_pixels(green_pixels + red_pixels, (0, 0, 0))
    time.sleep(0.1)
