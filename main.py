from tree import RGBXmasTree
from time import time
import random
from stripes_rotate import stripes_rotate
from sparkles import sparkles
from streams import streams


def main():
    funcs = [stripes_rotate, sparkles, streams]
#    funcs = [stripes_rotate]

    tree = RGBXmasTree()
    try:
        tree.brightness = 0.04

        while True:
            f = random.choice(funcs)
            print("Running " + str(f))
            f(tree, time() + 30)
    except KeyboardInterrupt:
        pass
    finally:
        tree.off()
        tree.close()


main()
