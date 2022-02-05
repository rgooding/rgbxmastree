from colorzero import Color, Hue

from lib.fade import fade_to
from lib.sleeper import Sleeper
from lib.tree import RGBXmasTree


# Basically the same as the huecycle example

def colour_cycle(tree: RGBXmasTree, stop_func):
    fade_to(tree, Color('red'))
    s = Sleeper()
    while stop_func is None or not stop_func():
        tree.color += Hue(deg=1)
        s.sleep(0.05)
