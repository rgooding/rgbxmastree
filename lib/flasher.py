from time import time


class Flasher:
    def __init__(self, min_value=1, max_value=8, duration=1000, time_offset=0):
        self.min = min_value
        self.max = max_value
        # flash duration in milliseconds (full cycle)
        self.dur = duration
        self.start_time = time() + (time_offset / 1000)

    def value(self):
        cycle_time = ((time() - self.start_time) * 1000) % self.dur
        half_dur = self.dur / 2
        if cycle_time < half_dur:
            # ascending
            f = cycle_time / half_dur
        else:
            # descending
            f = (half_dur - (cycle_time - half_dur)) / half_dur
        return self.min + (f * (self.max - self.min))
