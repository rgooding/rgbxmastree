from colorzero import Color

from effects.colour_waves import colour_waves
from effects.springtime.fixed_and_cycle import green_and_cycle, pink_and_cycle
from effects.springtime.pink_and_white import pink_and_white
from lib.run_utils import run_random
from lib.tree import RGBXmasTree


def colour_waves_spring(tree: RGBXmasTree, stop_func):
    colour_waves(tree, stop_func, Color(0.8, 0.15, 0.3))


if __name__ == '__main__':
    run_random([
        green_and_cycle,
        pink_and_cycle,
        pink_and_white,
        colour_waves_spring
    ])
