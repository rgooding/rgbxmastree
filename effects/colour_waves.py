from time import time, sleep

from colorzero import Color, Hue


def colour_waves(tree, end_time):
    rows = [
        [3],
        [2, 4, 9, 10, 21],
        [13, 18, 22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]

    tree.updates_enabled = False
    colour = Color('red')
    for row in rows:
        for n in row:
            tree[n].color = colour
        colour += Hue(deg=30)
    tree.apply()

    # Rotate colours
    while end_time == 0 or time() < end_time:
        sleep(0.0025)
        for p in tree:
            c = p.color
            c += Hue(deg=-1)
            p.color = c
        tree.apply()
