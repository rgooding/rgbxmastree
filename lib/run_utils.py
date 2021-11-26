from lib.tree import RGBXmasTree
from time import time
import random


effect_funcs = []


def register_effect(f):
    global effect_funcs
    effect_funcs.append(f)


def run_multi():
    global effect_funcs
    funcs = effect_funcs

    tree = RGBXmasTree()
    try:
        tree.brightness = 0.04

        while True:
            f = random.choice(funcs)
            print("Running " + str(f))
            f(tree, time() + 30)
    except KeyboardInterrupt:
        pass
    finally:
        tree.off()
        tree.close()


def run_single(f):
    tree = RGBXmasTree()
    try:
        tree.brightness = 0.04
        f(tree, 0)
    except KeyboardInterrupt:
        pass
    finally:
        tree.off()
        tree.close()

