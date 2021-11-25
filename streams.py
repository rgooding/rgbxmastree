from colorzero import Color
from time import sleep,time
import random

def streams(tree, end_time):
    main_colour = Color('blue')
    stream_colour = Color('white')
    
    streams = [
        [3,2,1,0],
        [3,4,5,6],
        [3,9,8,7],
        [3,10,11,12],
        [3,15,14,13],
        [3,16,17,18],
        [3,21,20,19],
        [3,22,23,24],
    ]
    
    tree.color = main_colour

    si = 0
    while end_time == 0 or time() < end_time:
        # sleep for between 0.3 and 0.7 seconds
        #sleep(random.randrange(3, 7, 1) / 10)
        sleep(1)
        
        #stream = random.choice(streams)
        #stream = streams[0]
        stream = streams[si]
        for i in stream:
            tree[i].color = stream_colour
            sleep(0.05)
        sleep(0.1)
        for i in stream:
            tree[i].color = main_colour
            sleep(0.05)
        si = si + 1
        if si >= len(streams):
            si = 0
