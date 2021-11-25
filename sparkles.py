from colorzero import Color
from time import sleep,time
import random

def sparkles(tree, end_time):
    main_colour = Color('blue')
    sparkle_colours = [
        #Color('cyan'),
        Color('white'),
        #Color('yellow'),
    ]
    flash_time = 0.1

    tree.color = main_colour
    
    while end_time == 0 or time() < end_time:
        # sleep for between 0.3 and 0.7 seconds
        sleep(random.randrange(3, 7, 1) / 10)
        # flash a random pixel
        p = random.choice(tree)
        p.color = random.choice(sparkle_colours)
        sleep(flash_time)
        p.color = main_colour
