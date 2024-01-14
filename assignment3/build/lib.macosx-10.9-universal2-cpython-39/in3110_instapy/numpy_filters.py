"""numpy implementation of image filters"""
from __future__ import annotations

import numpy as np

from in3110_instapy.io import display, read_image, write_image


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    gray_image = gray_image.astype(np.uint8)

    return gray_image


def numpy_color2sepia(image: np.array, k: float = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
        you may ignore it)

    Returns:
        np.array: sepia_image
    """
    sepia_matrix = np.array(
        [
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131],
        ]
    )
    sepia_image = np.dot(image[..., :3], sepia_matrix.T)
    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)

    return sepia_image

