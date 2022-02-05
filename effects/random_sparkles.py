import random
from time import time


# random_sparkles based on the randomsparkles example
from lib.sleeper import Sleeper


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def random_sparkles(tree, end_time):
    s = Sleeper()
    while end_time == 0 or time() < end_time:
        s.sleep(0.1)
        pixel = random.choice(tree)
        pixel.color = random_color()
