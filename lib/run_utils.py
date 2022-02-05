import random
from time import time

from lib.tree import RGBXmasTree


def run_random(effect_funcs, min_time=60, max_time=90):
    if len(effect_funcs) < 1:
        return
    if len(effect_funcs) == 1:
        run_single(effect_funcs[0])
        return

    tree = RGBXmasTree()
    try:
        while True:
            random.shuffle(effect_funcs)

            for f in effect_funcs:
                tree.updates_enabled = True
                tree.brightness_int = 1
                print("Running " + str(f))
                stop_time = time() + random.randrange(min_time, max_time, 1)
                f(tree, lambda: time() >= stop_time)
    except KeyboardInterrupt:
        pass
    finally:
        tree.updates_enabled = True
        tree.off()
        tree.close()


def run_single(f, max_duration=0):
    tree = RGBXmasTree()
    try:
        tree.brightness_int = 1
        if max_duration > 0:
            end_time = time() + max_duration

            def stop_func():
                return time() >= end_time
        else:
            stop_func = None
        f(tree, stop_func)
    except KeyboardInterrupt:
        pass
    finally:
        tree.updates_enabled = True
        tree.off()
        tree.close()
