from colorzero import Color, Hue

from lib.fade import fade_to_multi
from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree


def colour_waves(tree: RGBXmasTree, stop_func):
    rows = [
        [3],
        [2, 4, 9, 10, 21],
        [13, 18, 22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
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
    while stop_func is None or not stop_func():
        s.sleep(0.0025)
        for p in tree:
            c = p.color
            c += Hue(deg=-1)
            p.color = c
        tree.apply()
