# rgbxmastree

Some fun effects to use with the [3D RGB Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi).

## Getting Started

This has only been tested under Raspberry Pi OS 10 on a Raspberry Pi 4 but it should be compatible with any Raspberry Pi running Raspbian or Raspberry Pi OS.

Make sure you have the gpiozero library installed:
```bash
sudo apt install python3-gpiozero
```
Run the main script:
```bash
python3 main.py
```
The `main.py` script cycles through the effects, choosing another effect at random every 60-90 seconds.

## Notes
Most of this code was based on the examples found here https://github.com/ThePiHut/rgbxmastree/.

The `tree.py` module used here is modified with some enhancements:
* The brightness can be set for individual pixels
* Updates can be disabled, allowing you to configure the pixel values then apply the changes all at once. To use this set `tree.updates_enabled = False` then call `tree.apply()` to update the state of the LEDs.
