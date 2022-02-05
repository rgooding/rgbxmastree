import random

from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree


# random_sparkles based on the randomsparkles example

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def random_sparkles(tree: RGBXmasTree, stop_func):
    s = Sleeper()
    while stop_func is None or not stop_func():
        s.sleep(0.1)
        pixel = random.choice(tree)
        pixel.color = random_color()
