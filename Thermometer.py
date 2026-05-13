from adafruit_circuitplayground import cp


def temperature_fahrenheit():
    return cp.temperature * 9 / 5 + 32

while True:
    temp_f = temperature_fahrenheit()
    pixels = [(0, 0, 0)] * 10

    if temp_f < 78:
        pixels[0] = (0, 0, 1)
    else:
        pixels[0] = (0, 0, 1)
        if temp_f > 78:
            pixels[1] = (0, 0, 1)
        if temp_f > 79:
            pixels[2] = (0, 0, 1)
        if temp_f > 80:
            pixels[3] = (1, 1, 0)
        if temp_f > 81:
            pixels[4] = (1, 1, 0)
        if temp_f > 82:
            pixels[5] = (1, 1, 0)
        if temp_f > 83:
            pixels[6] = (1, 1, 0)
        if temp_f > 84:
            pixels[7] = (1, 0, 0)
        if temp_f > 85:
            pixels[8] = (1, 0, 0)
        if temp_f > 86:
            pixels[9] = (1, 0, 0)

    cp.pixels[:] = pixels