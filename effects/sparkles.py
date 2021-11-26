from colorzero import Color
from time import sleep,time
import random
from lib.run_utils import register_effect


def sparkles(tree, end_time):
    main_colour = Color('blue')
    main_brightness = 0.033
    sparkle_brightness = 0.125
    sparkle_colours = [
        Color('blue'),
        Color('cyan'),
        Color('white'),
    ]
    flash_time = 0.1

    tree.color = main_colour
    tree.brightness = main_brightness
    
    tree.updates_enabled = False
    while end_time == 0 or time() < end_time:
        # sleep for between 0.3 and 0.7 seconds
        sleep(random.randrange(3, 7, 1) / 10)
        # flash a random pixel
        p = random.choice(tree)
        p.color = random.choice(sparkle_colours)
        p.brightness = sparkle_brightness
        tree.apply()
        sleep(flash_time)
        p.color = main_colour
        p.brightness = main_brightness
        tree.apply()


register_effect(sparkles)
