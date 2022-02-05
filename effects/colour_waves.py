from colorzero import Color, Hue

from lib.fade import fade_to_multi
from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree


def _colour_waves(tree: RGBXmasTree, stop_func, rows, start_colour=Color('red')):
    tree.updates_enabled = False
    colour = start_colour
    colours = [(0, 0, 0) for _ in tree]
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


def colour_waves_vertical(tree: RGBXmasTree, stop_func, start_colour=Color('red')):
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
    _colour_waves(tree, stop_func, rows, start_colour)


def colour_waves(tree: RGBXmasTree, stop_func, start_colour=Color('red')):
    rows = [
        [3],
        [2, 4, 9, 10, 21],
        [13, 18, 22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]
    _colour_waves(tree, stop_func, rows, start_colour)
