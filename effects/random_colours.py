import random

from colorzero import Color

from lib.fade import fade_to_multi
from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree


# Like random_sparkles but uses a preset list of colours

def random_colours(tree: RGBXmasTree, stop_func):
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
    while stop_func is None or not stop_func():
        s.sleep(0.2)
        pixel = random.choice(tree)
        pixel.color = random.choice(colours)
