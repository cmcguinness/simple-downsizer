"""
    World's simplest image resizer (well maybe not simplest)

    Charles McGuinness

    Released to the public domain under CC0


"""
import sys
import cv2
import argparse
import os
import numpy as np

def unAlpha(image):
    """
    Put image onto a white background if it has alpha.  This is a bit
    awkward.  I'll spend time later on to figure out how to do this better.

    Unfortunately, the stock COLOR_BGRA2BGR just drops it on black, which
    seems generally to be the wrong thing to do.

    TODO: Should add options to control matte color
    TODO: Handle monochrome images with alpha
    """
    allwhite = np.zeros((image.shape[0], image.shape[1], 3), dtype=float)
    allwhite[:,:] = 255

    alpha1 = image[:,:,3].astype(float)/255
    alpha =  np.zeros((image.shape[0], image.shape[1], 3), dtype=float)
    for c in range(3):
        alpha[:,:,c] = alpha1

    beta = 1.0 - alpha
    # place our RGBA image onto a white background
    source = image[:,:,0:3].astype(float)

    merged = source * alpha + allwhite*beta

    return merged.astype(np.uint8)


def resizer(input_name, output_name, max_width, max_height, jpeq_quality):
    try:
        big_image = cv2.imread(input_name, -1)
    except Exception as e:
        print("downsizer.py: Could not read {}: error {}".format(input_name,e))
        sys.exit(-1)

    fraction_width = max_width / (big_image.shape[1])
    fraction_height = max_height / (big_image.shape[0])

    resize_fraction = min(fraction_height, fraction_width)

    small_image = cv2.resize(big_image, (0, 0), fx=resize_fraction, fy=resize_fraction)

    if output_name.upper().endswith(('.JPG')) or output_name.upper().endswith(('.JPEG')) or output_name.upper().endswith(('.JPE')):
        if len(small_image.shape) == 3 and small_image.shape[2] == 4: # Set alpha to white...
            small_image = unAlpha(small_image)
        cv2.imwrite(output_name, small_image, [int(cv2.IMWRITE_JPEG_QUALITY), jpeq_quality])
    else:
        cv2.imwrite(output_name, small_image)

def parse_args(command_line):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Presumably large input image to be downsized")
    parser.add_argument("output_file", nargs='?', default=None, help="Optional name of output file")
    parser.add_argument('-w', '--maxwidth', type=int, default=None, help='Maximum width of the image')
    parser.add_argument('-t', '--maxheight', type=int, default=None, help='Maximum height of the image')
    parser.add_argument('-q', '--jpegquality', type=int, default=80, help='If output is a jpeg, quality to write it at')

    return parser.parse_args(command_line)

def main(command_line):

    args = parse_args(command_line)
    #   Start with figuring out what to resize the image to....

    #   Defaults, probably not the most satisfactory...
    max_width = 640.0
    max_height = 480.0

    if args.maxwidth is not None and args.maxheight is None:
        max_width = float(args.maxwidth)
        max_height = float(sys.maxsize)  # just a large number so width is the controlling factor

    if args.maxwidth is None and args.maxheight is not None:
        max_width = float(sys.maxsize)  # just a large number so height is the controlling factor
        max_height = float(args.maxheight)

    if args.maxwidth is not None and args.maxheight is not None:
        max_width = float(args.maxwidth)
        max_height = float(args.maxheight)

    if args.output_file is None:
        small_name = os.path.join(os.path.dirname(args.input_file), 'small-' + os.path.basename(args.input_file))
    else:
        small_name = args.output_file

    resizer(args.input_file, small_name, max_width, max_height, args.jpegquality)


if __name__ == "__main__":
    main(sys.argv[1:])