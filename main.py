from effects.brightness_waves2 import brightness_waves2
from effects.colour_cycle import colour_cycle
from effects.colour_flashers import colour_flashers
from effects.colour_streams import colour_streams
from effects.colour_swap import colour_swap
from effects.colour_waves import colour_waves
from effects.colour_waves_vertical import colour_waves_vertical
from effects.random_colours import random_colours
from effects.random_sparkles import random_sparkles
from effects.sparkles import sparkles
from effects.streams import streams
from lib.run_utils import run_random

if __name__ == '__main__':
    # run_single(colour_waves)

    run_random([
        brightness_waves2,
        colour_cycle,
        colour_flashers,
        colour_streams,
        colour_swap,
        colour_waves,
        colour_waves_vertical,
        random_colours,
        random_sparkles,
        sparkles,
        streams,
    ])
