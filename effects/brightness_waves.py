from time import time,sleep

from colorzero import Color

from lib.fade import fade_to
from lib.flasher import Flasher


def brightness_waves(tree, end_time):
    rows = [
        [3],
        [2, 4, 9, 10, 21],
        [13, 18, 22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]
    # starting brightness of each row
    brightnesses = [8, 4, 2, 1, 1, 1, 2, 4]
    # brightnesses = [31, 16, 8, 4, 1, 4, 8, 16]
    min_brightness = 1
    max_brightness = 8

    fade_to(tree, Color('blue'))
    tree.updates_enabled = False
    # tree.color = Color('blue')

    flashers = []
    i = 0
    for _ in rows:
        flashers.append(
            Flasher(min_value=min_brightness, max_value=max_brightness, start_value=brightnesses[i], duration=2000))
        i += 1

    while end_time == 0 or time() < end_time:
        i = 0
        for row in rows:
            f = flashers[i]
            for n in row:
                tree[n].brightness_int = f.value()
            i += 1
        tree.apply()
        sleep(0.01)
