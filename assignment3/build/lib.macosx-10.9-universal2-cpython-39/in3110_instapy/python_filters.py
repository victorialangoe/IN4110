"""pure Python implementation of image filters"""
from __future__ import annotations

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    height, width = image.shape[:2]

    for row in range(height):
        for column in range(width):
            red, green, blue = image[row, column][:3]
            gray_value = int(0.21 * red + 0.72 * green + 0.07 * blue)

            gray_image[row, column] = [gray_value, gray_value, gray_value]

    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    height, width = image.shape[:2]
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    # Iterate through the pixels
    for row in range(height):
        for column in range(width):
            red, green, blue = image[row, column][:3]
            sepia_r = int(
                red * sepia_matrix[0][0]
                + green * sepia_matrix[0][1]
                + blue * sepia_matrix[0][2]
            )
            sepia_g = int(
                red * sepia_matrix[1][0]
                + green * sepia_matrix[1][1]
                + blue * sepia_matrix[1][2]
            )
            sepia_b = int(
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
