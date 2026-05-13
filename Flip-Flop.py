from adafruit_circuitplayground import cp

while True:
    if cp.switch:
        # Switch in right position
        for i in range(5):
            cp.pixels[i] = (0, 2, 0)  # off
        for i in range(5, 10):
            cp.pixels[i] = (0, 0, 0)  # green
    else:
        # Switch in left position
        for i in range(5):
            cp.pixels[i] = (0, 0, 0)  # green
        for i in range(5, 10):
            cp.pixels[i] = (0, 2, 0)  # off
