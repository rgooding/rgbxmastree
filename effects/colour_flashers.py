from colorzero import Color, Hue

from lib.fade import fade_to_multi
from lib.flasher import Flasher
from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree


# colour cycle each row separately using a Flasher to control the colour

def colour_flashers(tree: RGBXmasTree, stop_func):
    rows = [
        [3],
        [2, 4, 9, 10, 21],
        [13, 18, 22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]
    # starting colour for each row
    colours = [
        Color('red'),
        Color('magenta'),
        Color('yellow'),
        Color('cyan'),
        Color('blue'),
    ]
    min_shift = 0
    max_shift = 90

    initial_colours = [(0, 0, 0) for p in tree]
    i = 0
    for row in rows:
        for n in row:
            initial_colours[n] = colours[i]
        i += 1

    fade_to_multi(tree, initial_colours)

    tree.updates_enabled = False

    flashers = []
    i = 0
    for _ in rows:
        flashers.append(Flasher(min_value=min_shift, max_value=max_shift, duration=2000))
        i += 1

    s = Sleeper()
    while stop_func is None or not stop_func():
        i = 0
        for row in rows:
            f = flashers[i]
            c = colours[i] + Hue(deg=f.value())
            for n in row:
                tree[n].color = c
            i += 1
        tree.apply()
        s.sleep(0.01)
