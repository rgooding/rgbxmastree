from statistics import mean

from colorzero import Color
from gpiozero import SPIDevice, SourceMixin

max_brightness = 31


class Pixel:
    def __init__(self, parent, index, brightness=0.5):
        self.parent = parent
        self.index = index
        self._color = (0, 0, 0)
        self._brightness_int = int(brightness * max_brightness)

    @property
    def color(self):
        return Color(*self._color)

    @color.setter
    def color(self, c):
        r, g, b = c
        self._color = (r, g, b)
        self.parent._apply()

    @property
    def r(self):
        return self._color[0]

    @property
    def g(self):
        return self._color[1]

    @property
    def b(self):
        return self._color[2]

    @property
    def brightness(self):
        return self._brightness_int / max_brightness

    @brightness.setter
    def brightness(self, b):
        self.brightness_int = int(b * max_brightness)

    @property
    def brightness_int(self):
        return self._brightness_int

    @brightness_int.setter
    def brightness_int(self, b):
        self._brightness_int = b
        if self._brightness_int < 0:
            self._brightness_int = 0
        if self._brightness_int > max_brightness:
            self._brightness_int = max_brightness
        self.parent._apply()

    def on(self):
        self.color = (1, 1, 1)

    def off(self):
        self.color = (0, 0, 0)


class RGBXmasTree(SourceMixin, SPIDevice):
    def __init__(self, pixels=25, brightness=0.5, mosi_pin=12, clock_pin=25, *args, **kwargs):
        super(RGBXmasTree, self).__init__(mosi_pin=mosi_pin, clock_pin=clock_pin, *args, **kwargs)
        self._all = [Pixel(parent=self, index=i, brightness=brightness) for i in range(pixels)]
        self._brightness = brightness
        self.updates_enabled = True
        self.off()

    def __len__(self):
        return len(self._all)

    def __getitem__(self, index):
        return self._all[index]

    def __iter__(self):
        return iter(self._all)

    @property
    def value(self):
        # Not used, just to satisfy the abstract parent
        return True

    @property
    def color(self):
        average_r = mean(pixel.color[0] for pixel in self)
        average_g = mean(pixel.color[1] for pixel in self)
        average_b = mean(pixel.color[2] for pixel in self)
        return Color(average_r, average_g, average_b)

    @color.setter
    def color(self, c):
        was_enabled = self.updates_enabled
        self.updates_enabled = False
        for p in self:
            p.color = c
        self.updates_enabled = was_enabled
        self._apply()

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        was_enabled = self.updates_enabled
        self.updates_enabled = False
        for p in self:
            p.brightness = brightness
        self.updates_enabled = was_enabled
        self._brightness = brightness
        self._apply()

    def apply(self):
        self._apply(True)

    def _apply(self, force=False):
        if not (self.updates_enabled or force):
            return

        start_of_frame = [0] * 4
        end_of_frame = [0] * 5
        pixels = [[0b11100000 | p.brightness_int, int(p.b * 255), int(p.g * 255), int(p.r * 255)] for p in self]
        pixel_bytes = [i for p in pixels for i in p]
        data = start_of_frame + pixel_bytes + end_of_frame
        self._spi.transfer(data)

    def on(self):
        self.color = (1, 1, 1)

    def off(self):
        self.color = (0, 0, 0)

    def close(self):
        super(RGBXmasTree, self).close()


if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        tree.on()
    finally:
        tree.close()
