# simple-downsizer
A small python program that will resize pictures down to something more
suitable for including in email, etc.

This is a very simple python program that will resize images.  It resizes both the height and the width by the
same proportions, so the output image has the same aspect ratio as the input image.

## Usage

```
python downsizer.py input_file [output_file] [--maxwidth w] [--maxheight h] [--jpegquality q]
```

If you just specify the input file, it will create an output file with the name small-*input_file*
at a maximum height of 640 and a maximum width of 480.

You can, of course, specify your own output name. The input file and the output file do not need to be of the same type,
so the input can be .png and the output .jpg, for example.

The --maxwidth and --maxheight optional arguments allow you to control the size of the output file.  If only one is given,
then only that dimension will be used to produce the output image size.

The --jpegquality is used to control the jpeg compression level on the output image, if the output image is a jpeg.
The default value is 80.  If the image is not a jpeg, the value is ignored.

This only does one file at a time; the assumption is that you will wrap this in a bash script or similar
for bulk conversions.

This code is released to the public domain under creative commons zero licensing.


## Test case

The script downsizer_test.py does a very simple test of the code.


