from tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree(brightness=0)
try:
    tree.on()
    for b in [0.0625, 0.125, 0.25, 0.5, 1.0]:
        for p in tree:
            p.brightness = b
            sleep(0.1)
finally:
    tree.off()
    tree.close()
    