import random
from time import sleep, time


# random_sparkles based on the randomsparkles example

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def random_sparkles(tree, end_time):
    while end_time == 0 or time() < end_time:
        sleep(0.01)
        pixel = random.choice(tree)
        pixel.color = random_color()
