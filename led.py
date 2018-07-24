from blinkt import set_pixel, set_brightness, show, clear
import time
import random

set_brightness(0.1)

colours = [
    (0,0,255),
    (0,255,0),
    (255,0,0),
    (0,255,255),
    (255,0,255),
    (255,255,0),
    (255,255,255),
]

while True:
    with open("animations/current.selection", "r") as selection_file:
        filename = selection_file.readline().strip("\n")
    with open("animations/{}".format(filename), "r") as animation_file:
        for line in animation_file:
            if line == "\n":
                break
            pixel_list = line.split(":")

            i = 0
            for pixel in pixel_list:
                rgb = pixel.split(",")
                set_pixel(i, rgb[0], rgb[1], rgb[2])
                i = i + 1
            show()
            time.sleep(1/30)
