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

    # this image should already have a transparent background
    # if it doesn't, then learn to use Preview
    orig = Image.open(args.image)
    orig_w, orig_h = orig.size

    # trans MUST be zero, or first position in palette, for slack to respect gif transparency
    trans = 0
    disp = 3
    palette = []

    color_not_in_original_image = (255, 0, 0, 0)

    for i in range(10):
        triggered = Image.new('RGBA', (orig_w + args.magnitude, orig_h + args.magnitude), color_not_in_original_image)

        trig_w, trig_h = triggered.size

        pos_x = randrange(0, args.magnitude)
        pos_y = randrange(0, args.magnitude)

        triggered.alpha_composite(orig, (pos_x, pos_y))
        trig_conv = triggered.convert(mode='P')
        trig_conv_palette = trig_conv.getpalette()

        if i == 0:
            # debug statement to make sure that chosen color for trans is in first position of palette
            print trig_conv_palette
            palette = trig_conv_palette

        frames.append(triggered)

    frames[0].save('{0}.triggered.gif'.format(args.image), format='GIF', disposal=disp, append_images=frames[1:],
                   transparency=trans, save_all=True, duration=50, loop=0)

if __name__ == '__main__':
    main()

