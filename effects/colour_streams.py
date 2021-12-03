import random
from time import sleep, time

from colorzero import Color, Hue

from lib.fade import fade_to_multi


def colour_streams(tree, end_time):
    stream_pixels = [
        [3, 2, 1, 0],
        [3, 4, 5, 6],
        [3, 9, 8, 7],
        [3, 10, 11, 12],
        [3, 13, 14, 15],
        [3, 18, 17, 16],
        [3, 21, 20, 19],
        [3, 22, 23, 24],
    ]

    main_brightness = 1
    stream_brightness = 4

    tree.updates_enabled = False
    initial_colours = []
    colour = Color('red')
    for p in tree:
        p.brightness_int = main_brightness
        initial_colours.append(colour)
        colour += Hue(deg=90)
    tree.apply()

    fade_to_multi(tree, initial_colours)

    while end_time == 0 or time() < end_time:
        # sleep for between 0.5 and 1.2 seconds
        sleep(random.randrange(5, 12, 1) / 10)

        stream = random.choice(stream_pixels)
        for i in stream:
            tree[i].color += Hue(deg=180)
            tree[i].brightness_int = stream_brightness
            tree.apply()
            sleep(0.05)
        sleep(0.1)
        for i in stream:
            tree[i].color += Hue(deg=-180)
            tree[i].brightness_int = main_brightness
            tree.apply()
            sleep(0.05)
