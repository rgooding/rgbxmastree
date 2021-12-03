from time import time, sleep

from colorzero import Color, Hue

from lib.fade import fade_to


# Basically the same as the huecycle example

def colour_cycle(tree, end_time):
    fade_to(tree, Color('red'))
    while end_time == 0 or time() < end_time:
        tree.color += Hue(deg=1)
        sleep(0.05)
