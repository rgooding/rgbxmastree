from time import time

from colorzero import Color, Hue

from lib.fade import fade_to


# Basically the same as the huecycle example
from lib.sleeper import Sleeper


def colour_cycle(tree, end_time):
    fade_to(tree, Color('red'))
    s = Sleeper()
    while end_time == 0 or time() < end_time:
        tree.color += Hue(deg=1)
        s.sleep(0.05)
