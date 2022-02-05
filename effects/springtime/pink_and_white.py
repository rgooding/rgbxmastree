import random
from time import sleep

from fade import fade_to
from lib.tree import RGBXmasTree


def pink_and_white(tree: RGBXmasTree, stop_func):
    pink = (0.8, 0.15, 0.3)
    white = (0.8, 0.8, 0.8)

    fade_to(tree, pink)
    while stop_func is None or not stop_func():
        pixel = random.choice(tree)
        if pixel.color == white:
            pixel.color = pink
        else:
            pixel.color = white
        sleep(0.5)
