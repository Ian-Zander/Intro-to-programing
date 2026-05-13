from adafruit_circuitplayground import cp
colors = [(4, 0, 0),(4, 1, 0),(4, 4, 0),(0, 4, 0),(0, 0, 4),(1, 0, 1),(4, 2, 3)]
current_index = 0
cp.pixels.fill(colors[current_index])
while True:
    if cp.button_a:
        current_index = (current_index + 1) % len(colors)
        cp.pixels.fill(colors[current_index])
        while cp.button_a:
            pass