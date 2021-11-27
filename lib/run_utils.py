import random
from time import time

from lib.tree import RGBXmasTree


def run_random(effect_funcs):
    tree = RGBXmasTree()
    try:
        while True:
            random.shuffle(effect_funcs)

            for f in effect_funcs:
                tree.updates_enabled = True
                tree.brightness = 0.04
                print("Running " + str(f))
                f(tree, time() + random.randrange(60, 90, 1))
    except KeyboardInterrupt:
        pass
    finally:
        tree.updates_enabled = True
        tree.off()
        tree.close()


def run_single(f, max_duration=0):
    tree = RGBXmasTree()
    try:
        tree.brightness = 0.04
        if max_duration > 0:
            end_time = time() + max_duration
        else:
            end_time = 0
        f(tree, end_time)
    except KeyboardInterrupt:
        pass
    finally:
        tree.updates_enabled = True
        tree.off()
        tree.close()
