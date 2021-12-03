from time import time, sleep

from colorzero import Color

from lib.fade import fade_to
from lib.flasher import Flasher


# Like brightness_waves but uses the colour value to change the brightness instead of the brightness property

def brightness_waves2(tree, end_time):
    rows = [
        [3],
        [2, 4, 9, 10, 21],
        [13, 18, 22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]
    # starting brightness of each row
    # brightnesses = [1.0, 0.5, 0.25, 0.1, 0.1, 0.1, 0.25, 0.5]
    brightnesses = [1.0, 0.5, 0.25, 0.125, 0.0635, 0.03, 0.01, 0.01]
    min_brightness = 0.1
    max_brightness = 1.0

    colour = Color('blue')
    fade_to(tree, colour)
    tree.updates_enabled = False

    flashers = []
    i = 0
    for _ in rows:
        flashers.append(
            Flasher(min_value=min_brightness, max_value=max_brightness, duration=2000, time_offset=i * 400))
        i += 1

    while end_time == 0 or time() < end_time:
        i = 0
        for row in rows:
            f = flashers[i]
            r, g, b = colour
            r *= f.value()
            g *= f.value()
            b *= f.value()
            for n in row:
                tree[n].color = Color(r, g, b)
            i += 1
        tree.apply()
        sleep(0.01)
