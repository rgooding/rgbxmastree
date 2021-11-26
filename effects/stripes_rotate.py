from colorzero import Color, Hue
from time import time, sleep
from lib.run_utils import register_effect


def stripes_rotate(tree, end_time):
    rows = [
        [3],
        [2,4,9,10,21],
        [13,18,22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]

    colour = Color('red')
    for row in rows:
        for n in row:
            tree[n].color = colour
        colour += Hue(deg=30)
        
    # Rotate colours
    while end_time == 0 or time() < end_time:
        sleep(0.05)
        tree.updates_enabled = False
        for row in rows:
            for n in row:
                c = tree[n].color
                c += Hue(deg=-5)
                tree[n].color = c
        tree.updates_enabled = True
        tree.apply()


register_effect(stripes_rotate)
