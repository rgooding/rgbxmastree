import random
from time import sleep, time

from colorzero import Color, Hue


# Like random_sparkles but uses a preset list of colours

def random_colours(tree, end_time):
    colours = [
        Color('red'),
        Color('yellow'),
        Color('green'),
        Color('cyan'),
        Color('blue'),
        Color('magenta'),
    ]

    tree.updates_enabled = False
    for p in tree:
        p.color = random.choice(colours)
    tree.apply()
    tree.updates_enabled = True

    while end_time == 0 or time() < end_time:
        sleep(0.1)
        pixel = random.choice(tree)
        pixel.color = random.choice(colours)
