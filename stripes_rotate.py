from colorzero import Color, Hue
from time import time,sleep


def stripes_rotate(tree, end_time):
    rows = [
        [3],
        [2,4,9,10,21],
        [13,18,22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]

    colours = [
        Color('red'),
        Color('yellow'),
        Color('green'),
        Color('cyan'),
        Color('blue'),
        Color('magenta'),
    ]

    # Set initial colours
#    i = 0
#    for row in rows:
#        colour = colours[i]
#        for n in row:
#            tree[n].color = colour
#        i = i + 1

    colour = Color('red')
    for row in rows:
        for n in row:
            tree[n].color = colour
        colour += Hue(deg=60)
        
    # Rotate colours
    while end_time == 0 or time() < end_time:
        sleep(0.05)
        new_value = list(tree.value)
        for row in rows:
            for n in row:
                c = Color(new_value[n])
                c += Hue(deg=-5)
                r, g, b = c
                new_value[n] = (r, g, b)
        tree.value = tuple(new_value)
