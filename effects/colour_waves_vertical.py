from time import time

from colorzero import Color, Hue

from lib.fade import fade_to_multi
from lib.sleeper import Sleeper


def colour_waves_vertical(tree, end_time):
    rows = [
        [3, 2, 1, 0],
        [9, 8, 7],
        [13, 14, 15],
        [18, 17, 16],
        [10, 11, 12],
        [4, 5, 6],
        [21, 20, 19],
        [22, 23, 24],
    ]

    tree.updates_enabled = False
    colour = Color('red')
    colours = [(0, 0, 0) for p in tree]
    for row in rows:
        for n in row:
            colours[n] = colour
        colour += Hue(deg=30)
    fade_to_multi(tree, colours)

    # Rotate colours
    s = Sleeper()
    while end_time == 0 or time() < end_time:
        s.sleep(0.0025)
        for p in tree:
            c = p.color
            c += Hue(deg=-1)
            p.color = c
        tree.apply()
