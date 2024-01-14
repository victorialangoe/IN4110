"""Cython implementation of filter functions"""
from __future__ import annotations

# cimport numpy as cnp


import cython as C
import numpy as np
from PIL import Image

from in3110_instapy.io import read_image, display, write_image


if not C.compiled:
    raise ImportError(
        "Cython module not compiled! Check setup.py and make sure this package has been installed, not just imported in-place, e.g. `pip install --editable .`."
    )

from cython.cimports.libc.stdint import uint8_t  # noqa


# we may need a 'const uint8_t' type to make sure we accept 'read-only' arrays
const_uint8_t = C.typedef("const uint8_t")
float64_t = C.typedef(C.double)


def cython_color2gray(image):
    """Convert rgb pixel array to grayscale

    Args:
        image (any)
    Returns:
        np.array: gray_image
    """
    height: C.int = image.shape[0]
    width: C.int = image.shape[1]
    gray_image: np.ndarray = np.empty((height, width), dtype=np.uint8)

    for row in range(height):
        for column in range(width):
            red: C.int = image[row, column, 0]
            green: C.int = image[row, column, 1]
            blue: C.int = image[row, column, 2]
            gray_value: C.int = int(0.21 * red + 0.72 * green + 0.07 * blue)

            gray_image[row, column] = gray_value

    return gray_image


def cython_color2sepia(image):
    """Convert rgb pixel array to sepia

    Args:
        image (any)
    Returns:
        np.array: gray_image
    """
    height: C.int = image.shape[0]
    width: C.int = image.shape[1]
    sepia_image: np.ndarray = np.empty((height, width, 3), dtype=np.uint8)
    sepia_matrix: np.ndarray = np.array(
        [
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131],
        ],
        dtype=np.float64,
    )

    for row in range(height):
        for column in range(width):
            red: C.int = image[row, column, 0]
            green: C.int = image[row, column, 1]
            blue: C.int = image[row, column, 2]
            sepia_r: C.int = int(
                red * sepia_matrix[0][0]
                + green * sepia_matrix[0][1]
                + blue * sepia_matrix[0][2]
            )
            sepia_g: C.int = int(
                red * sepia_matrix[1][0]
                + green * sepia_matrix[1][1]
                + blue * sepia_matrix[1][2]
            )
            sepia_b: C.int = int(
                red * sepia_matrix[2][0]
                + green * sepia_matrix[2][1]
                + blue * sepia_matrix[2][2]
            )
            sepia_image[row, column] = [
                min(sepia_r, 255),
                min(sepia_g, 255),
                min(sepia_b, 255),
            ]
    return sepia_image
