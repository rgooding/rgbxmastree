from time import time


class Flasher:
    def __init__(self, min_value=1, max_value=8, start_value=1, duration=1000):
        self.min = min_value
        self.max = max_value
        self.start_value = start_value
        # flash duration in milliseconds (full cycle)
        self.dur = duration
        self.start_time = time()

    def value(self):
        cycle_time = ((time() - self.start_time) * 1000) % self.dur
        cycle_pos = cycle_time / self.dur
        half_cycle_range = self.max - self.min
        cycle_range = half_cycle_range * 2
        start_offset = self.start_value - self.min
        cycle_offset = ((cycle_range * cycle_pos) + start_offset) % cycle_range

        if cycle_offset > half_cycle_range:
            real_offset = half_cycle_range - (cycle_offset / 2)
        else:
            real_offset = cycle_offset

        real_value = self.min + real_offset
        if real_value < self.min:
            real_value = self.min
        if real_value > self.max:
            real_value = self.max
        return int(real_value)
