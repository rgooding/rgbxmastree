from time import time, sleep


class Sleeper:
    """
    This provides a way to perform updates at regular intervals, accounting for the time it took to perform the operation
    Calling sleep() will sleep for the delay minus the time that sleep() was last called
    """
    last_tick: float

    def __init__(self):
        self.last_tick = time()

    def sleep(self, delay: float):
        target_time = self.last_tick + delay
        sleep_time = target_time - time()
        if sleep_time > 0:
            sleep(sleep_time)
        self.last_tick = time()
