from colorzero import Color
from time import sleep,time
import random
from run_utils import run_single, register_effect


def streams(tree, end_time):
    main_colour = Color('blue')
    stream_colour = Color('white')
    
    streams = [
        [3,2,1,0],
        [3,4,5,6],
        [3,9,8,7],
        [3,10,11,12],
        [3,13,14,15],
        [3,18,17,16],
        [3,21,20,19],
        [3,22,23,24],
    ]
    
    tree.color = main_colour

    while end_time == 0 or time() < end_time:
        # sleep for between 0.5 and 1.2 seconds
        sleep(random.randrange(5, 12, 1) / 10)
        
        stream = random.choice(streams)
        for i in stream:
            tree[i].color = stream_colour
            sleep(0.05)
        sleep(0.1)
        for i in stream:
            tree[i].color = main_colour
            sleep(0.05)


if __name__ == '__main__':
    run_single(streams)
else:
    register_effect(streams)
