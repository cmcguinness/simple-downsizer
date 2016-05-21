from downsizer import *
import os

# Test cases ...



inname_png = os.path.join('test_images', 'red_people.png')
inname_jpg = os.path.join('test_images', 'red_people.jpg')

crossname_png = os.path.join('test_images', 'x_red_people.png')
crossname_jpg = os.path.join('test_images', 'x_red_people.jpg')

width_name = os.path.join('test_images', 'w_red_people.png')
height_name = os.path.join('test_images', 'h_red_people.png')

quality_name = os.path.join('test_images', 'q_red_people.jpg')

full_name = os.path.join('test_images', 'f_red_people.jpg')

# Single file tests, all input files...
main([inname_png])
main([inname_jpg])

# Double file tests, cross formats
main([inname_png, crossname_jpg])
main([inname_jpg, crossname_png])


# width only
main([inname_png, width_name, '--maxwidth', '200'])

# height only
main([inname_png, height_name, '--maxheight', '200'])

# quality test
main([inname_png, quality_name, '--jpegquality', '30']) # That should be horrible!

# Full test ...
main([inname_png, full_name, '--maxwidth', '200', '--maxheight', '200', '--jpegquality', '30'])

