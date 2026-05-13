from adafruit_circuitplayground import cp
lit_pixels = 0
pixel_color = (0, 2, 1)
max_pixels = 10
cp.pixels.fill((0, 0, 0))
cp.pixels.show()
while True:
    if cp.button_a:
        if lit_pixels < max_pixels:
            cp.pixels[lit_pixels] = pixel_color
            cp.pixels.show()
            lit_pixels += 1
        while cp.button_a:
            pass
    if cp.button_b:
        if lit_pixels > 0:
            lit_pixels -= 1
            cp.pixels[lit_pixels] = (0, 0, 0)
            cp.pixels.show()
        while cp.button_b:
            pass