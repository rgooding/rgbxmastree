from effects.brightness_waves import brightness_waves
from effects.colour_cycle import colour_cycle
from effects.colour_waves import colour_waves
from effects.colour_waves_vertical import colour_waves_vertical
from effects.random_sparkles import random_sparkles
from effects.sparkles import sparkles
from effects.streams import streams
from lib.run_utils import run_random

if __name__ == '__main__':
    # run_single(colour_waves)

    run_random([
        brightness_waves,
        colour_cycle,
        colour_waves,
        colour_waves_vertical,
        random_sparkles,
        sparkles,
        streams,
    ])
