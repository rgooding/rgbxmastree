from colorzero import Color

from lib.fade import fade_to_multi
from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree


def colour_swap(tree: RGBXmasTree, stop_func):
    colours = (Color('red'), Color('green'))

    start_colours = [(0, 0, 0) for _ in tree]
    i = 0
    for _ in tree:
        start_colours[i] = colours[i % 2]
        i += 1
    fade_to_multi(tree, start_colours)

    # swap colours
    j = 0
    s = Sleeper()
    while stop_func is None or not stop_func():
        s.sleep(3)
        j += 1
        j = j % 2
        new_colours = [(0, 0, 0) for _ in tree]
        i = 0
        for _ in tree:
            new_colours[i] = colours[(i + j) % 2]
            i += 1
        fade_to_multi(tree, new_colours, duration=0.25)
