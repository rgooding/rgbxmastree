import random
from time import sleep, time

from colorzero import Color

from lib.fade import fade_to_multi


# Like random_sparkles but uses a preset list of colours
from lib.sleeper import Sleeper


def random_colours(tree, end_time):
    colours = [
        Color('red'),
        Color('yellow'),
        Color('green'),
        Color('cyan'),
        Color('blue'),
        Color('magenta'),
    ]

    colours = [random.choice(colours) for p in tree]
    fade_to_multi(tree, colours)

    s = Sleeper()
    while end_time == 0 or time() < end_time:
        s.sleep(0.2)
        pixel = random.choice(tree)
        pixel.color = random.choice(colours)
