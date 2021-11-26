from colorzero import Color
from time import sleep,time
import random
from run_utils import run_single, register_effect


def sparkles(tree, end_time):
    main_colour = Color('blue')
    sparkle_colours = [
        #Color('cyan'),
        Color('white'),
        #Color('yellow'),
    ]
    flash_time = 0.1

    tree.color = main_colour
    
    tree.updates_enabled = False
    while end_time == 0 or time() < end_time:
        # sleep for between 0.3 and 0.7 seconds
        sleep(random.randrange(3, 7, 1) / 10)
        # flash a random pixel
        p = random.choice(tree)
        old_b = p.brightness
        p.color = random.choice(sparkle_colours)
        p.brightness = old_b * 2
        tree.apply(True)
        sleep(flash_time)
        p.color = main_colour
        p.brightness = old_b
        tree.apply(True)


if __name__ == '__main__':
    run_single(sparkles)
else:
    register_effect(sparkles)
