import random
from time import sleep, time

from colorzero import Color

from lib.fade import fade_to
from lib.sleeper import Sleeper


def streams(tree, end_time):
    main_colour = Color('blue')
    stream_colour = Color('white')

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

    fade_to(tree, main_colour)

    while end_time == 0 or time() < end_time:
        # sleep for between 0.5 and 1.2 seconds
        sleep(random.randrange(5, 12, 1) / 10)

        stream = random.choice(stream_pixels)
        s = Sleeper()
        for i in stream:
            tree[i].color = stream_colour
            s.sleep(0.05)
        s.sleep(0.1)
        for i in stream:
            tree[i].color = main_colour
            s.sleep(0.05)
