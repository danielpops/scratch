#!/usr/bin/env python2.7
import argparse

from PIL import Image
from random import randrange


def main():
    parser = argparse.ArgumentParser(description='Make it :triggered:')
    parser.add_argument('--image', type=str, help='Input image', required=True)
    parser.add_argument('--magnitude', type=int, help='Triggered magnitude', required=False, default=10)
    args = parser.parse_args()

    frames = []

    orig = Image.open(args.image)
    orig_w, orig_h = orig.size

    for i in range(10):
        triggered = Image.new(
            'RGBA', (orig_w + args.magnitude * 2, orig_h + args.magnitude * 2), (255,255,255,0))

        trig_w, trig_h = triggered.size

        pos_x = ((trig_w - orig_w) // 2) + randrange(-args.magnitude, args.magnitude)
        pos_y = ((trig_h - orig_h) // 2) + randrange(-args.magnitude, args.magnitude)

        triggered.paste(orig, (pos_x, pos_y), orig)
        frames.append(triggered)

    frames[0].save('{0}.triggered.gif'.format(args.image), format='GIF', disposal=3, append_images=frames[1:],
                   transparency=0, save_all=True, duration=60, loop=0)

if __name__ == '__main__':
    main()
