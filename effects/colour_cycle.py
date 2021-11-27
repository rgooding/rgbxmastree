from time import time, sleep

from colorzero import Color, Hue


# Basically the same as the huecycle example

def colour_cycle(tree, end_time):
    tree.color = Color('red')
    while end_time == 0 or time() < end_time:
        tree.color += Hue(deg=1)
        sleep(0.05)
