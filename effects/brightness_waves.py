from colorzero import Color

from lib.fade import fade_to
from lib.flasher import Flasher
from lib.sleeper import Sleeper


def brightness_waves(tree, stop_func=None):
    rows = [
        [3],
        [2, 4, 9, 10, 21],
        [13, 18, 22],
        [1, 5, 8, 11, 14, 17, 20, 23],
        [0, 6, 7, 12, 15, 16, 19, 24],
    ]
    min_brightness = 1
    max_brightness = 8

    fade_to(tree, Color('blue'))
    tree.updates_enabled = False

    flashers = []
    i = 0
    for _ in rows:
        flashers.append(
            Flasher(min_value=min_brightness, max_value=max_brightness, duration=2000, time_offset=i * 400))
        i += 1

    s = Sleeper()
    while stop_func is None or not stop_func():
        i = 0
        for row in rows:
            f = flashers[i]
            for n in row:
                tree[n].brightness_int = int(f.value())
            i += 1
        tree.apply()
        s.sleep(0.01)
