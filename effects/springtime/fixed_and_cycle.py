from colorzero import Hue

from lib.fade import fade_to_multi
from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree

green = (0, 0.6, 0)
pink = (0.8, 0.15, 0.3)


def green_and_cycle(tree: RGBXmasTree, stop_func):
    fixed_and_cycle(tree, stop_func, green, pink)


def pink_and_cycle(tree: RGBXmasTree, stop_func):
    fixed_and_cycle(tree, stop_func, pink, pink)


def fixed_and_cycle(tree: RGBXmasTree, stop_func, fixed_colour, cycle_start_colour):
    cycle_px = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23}

    start_colours = [(0.0, 0.0, 0.0) for _ in tree]
    i = 0
    for _ in tree:
        if i in cycle_px:
            start_colours[i] = cycle_start_colour
        else:
            start_colours[i] = fixed_colour
        i += 1
    fade_to_multi(tree, start_colours)

    tree.updates_enabled = False
    s = Sleeper()
    while stop_func is None or not stop_func():
        for i in cycle_px:
            tree[i].color += Hue(deg=1)
        tree.apply()
        s.sleep(0.05)
