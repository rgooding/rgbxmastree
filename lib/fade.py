from time import sleep

from colorzero import Color

default_fade_duration = 2


def fade_to(tree, c, duration=default_fade_duration):
    """Fade the whole tree from its current state to a single colour"""
    start_colours = []
    for p in tree:
        start_colours.append(p.color)

    r2, g2, b2 = c

    delay = 0.05
    steps = round(duration / delay)

    upd_was_enabled = tree.updates_enabled
    tree.updates_enabled = False
    for i in range(1, steps):
        idx = 0
        for p in tree:
            r1, g1, b1 = start_colours[idx]
            idx += 1
            dr = (r2 - r1) / steps
            dg = (g2 - g1) / steps
            db = (b2 - b1) / steps

            r = r1 + (i * dr)
            g = g1 + (i * dg)
            b = b1 + (i * db)
            p.color = Color(r, g, b)
        tree.apply()
        sleep(delay)

    tree.color = Color(r2, g2, b2)
    tree.apply()
    tree.updates_enabled = upd_was_enabled


def fade_to_multi(tree, dest_colours, duration=default_fade_duration):
    """Fade each pixel in the tree from its current state to the corresponding colour in dest_colours"""
    start_colours = []
    for p in tree:
        start_colours.append(p.color)

    delay = 0.05
    steps = round(duration / delay)

    upd_was_enabled = tree.updates_enabled
    tree.updates_enabled = False
    for i in range(1, steps):
        idx = 0
        for p in tree:
            r1, g1, b1 = start_colours[idx]
            r2, g2, b2 = dest_colours[idx]
            idx += 1
            dr = (r2 - r1) / steps
            dg = (g2 - g1) / steps
            db = (b2 - b1) / steps

            r = r1 + (i * dr)
            g = g1 + (i * dg)
            b = b1 + (i * db)
            p.color = Color(r, g, b)
        tree.apply()
        sleep(delay)

    i = 0
    for p in tree:
        p.color = dest_colours[i]
        i += 1
    tree.apply()
    tree.updates_enabled = upd_was_enabled
