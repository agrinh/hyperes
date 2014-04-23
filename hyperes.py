#!/usr/bin/python
"""
Takes one parameter, image_file_path. The script then creates a new hyperes
image and stores that in img_file_path.hyperes.jpg.
"""
from itertools import chain
from numpy import array


def hyperes(img):
    """
    Creates a new image with each subpixel as a black and white pixel.

    Will result in vertical lines unless image is mostly colorless.

    Parameters
    ----------
    img : numpy.array
        Image as numpy.array (MxNx3).

    Notes
    -----
    Assumes the subpixel layout is R G B R G B .... across all rows.

    Vertically the same rows are copied three times to avoid scewing of the
    image.
    """
    # chain the subpixels
    hyperes = [list(chain(*row)) for row in img]
    hyperes = list(chain(*zip(*[hyperes]*3)))   # copy each row three times
    return array(hyperes)

if __name__ == '__main__':
    import sys
    from scipy.misc import imread, imsave
    filename = sys.argv[1]
    img = imread(filename)
    img_hyperes = hyperes(img)
    imsave(filename+'.hyperes.jpg', img_hyperes)
