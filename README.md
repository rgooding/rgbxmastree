# rgbxmastree

Some fun effects to use with the [3D RGB Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi).

I would recommend getting familiar with the [official examples](https://github.com/ThePiHut/rgbxmastree/tree/master/examples) before attempting to modify these.

## Getting Started

This has been tested on a Raspberry Pi 4 and ZeroW but it should be compatible with any model.

Make sure you have the required packages installed:

#### Raspberry Pi OS 11 (bullseye):
```bash
sudo apt install python3-gpiozero python3-pigpio pigpio
```

#### Raspberry Pi OS 12 (bookworm):
```bash
sudo apt install python3-gpiozero=1.6.2-1+b4 python3-pigpio pigpio
sudo apt-mark hold python3-gpiozero
```

Start pigpiod:
```bash
sudo systemctl start pigpiod
sudo systemctl enable pigpiod # if you want to start pigpiod on boot
```
Run the main script:
```bash
python3 main.py
```
The `main.py` script cycles through the effects, choosing another effect at random every 60-90 seconds.

## Notes
Most of this code was based on the examples found here https://github.com/ThePiHut/rgbxmastree/.

While working with the RGB Xmas Tree I have made a couple of observations that could be helpful to others:
* You must be sure to exit the example scripts cleanly with Ctrl+C or SIGINT, otherwise they will not close the tree object properly which can sometimes cause the tree to stop functioning correctly. The only solution to this seems to be to power cycle the Raspberry Pi.
* The LEDs are controlled through quite a slow SPI interface. This has two drawbacks:
  * Each time a single LED is changed the state for all LEDs must be sent to the tree
  * Updating the tree state takes a noticeable amount of time so it is best to keep updates to a minimum to ensure smooth effects

Overriding the pin factory to use the pigpio driver makes a huge improvement to the speed of the SPI interface, especially on the Pi Zero.
In my tests this improved the update time from 0.2 seonds to 0.01 seconds.

The `tree.py` module in this repository is heavily modified from the official version to provide some enhancements:
* The brightness can be set for individual pixels
* Updates can be disabled, allowing you to configure the pixel values then apply the changes all at once. To use this set `tree.updates_enabled = False` then call `tree.apply()` to update the state of the LEDs.
* Uses the `pigpio` SPI driver instead of the default (`rpigpio` I think) to improve update time.
