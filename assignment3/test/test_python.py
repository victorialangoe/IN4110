from in3110_instapy.python_filters import python_color2gray, python_color2sepia

import numpy as np


def test_color2gray(image):
    """Tests if python_color2gray works the way it should do

    Args:
        image (any)
    Returns:
        None
    """
    gray_image = python_color2gray(image)

    assert isinstance(
        gray_image, np.ndarray
    ), "Assertion error: python_color2gray does not return a numpy array"

    assert (
        gray_image.shape == image.shape
    ), "Assertion error from test_color2gray: The shapes are not equal"
    assert (
        gray_image.dtype == np.uint8
    ), "Assertion error from test_color2gray: The gray image' dtype is supposed to be uint8"
    assert (
        gray_image.dtype == image.dtype
    ), "Assertion error from test_color2gray: The types are indifferent"

    expected_gray_value = int(
        0.21 * image[0, 0, 0] + 0.72 * image[0, 0, 1] + 0.07 * image[0, 0, 2]
    )

    assert np.allclose(
        gray_image[0, 0],
        [expected_gray_value, expected_gray_value, expected_gray_value],
    ), "Assertion error from test_color2gray: The two images are not equal"


def test_color2sepia(image):
    """Tests if python_color2sepia works the way it should do

    Args:
        image (any)
    Returns:
        None
    """
    sepia_image = python_color2sepia(image)

    assert isinstance(
        sepia_image, np.ndarray
    ), "python_color2sepia does not return a numpy array"

    assert (
        sepia_image.shape == image.shape
    ), "Assertion error from test_color2sepia: The shapes are not equal"
    assert (
        sepia_image.dtype == np.uint8
    ), "Assertion error from test_color2sepia: The sepia image's dtype is supposed to be uint8"
    assert (
        sepia_image.dtype == image.dtype
    ), "Assertion error from test_color2sepia: The types are indifferent"

    expected_pixel_value = [
        int(0.393 * image[0, 0, 0] + 0.769 * image[0, 0, 1] + 0.189 * image[0, 0, 2]),
        int(0.349 * image[0, 0, 0] + 0.686 * image[0, 0, 1] + 0.168 * image[0, 0, 2]),
        int(0.272 * image[0, 0, 0] + 0.534 * image[0, 0, 1] + 0.131 * image[0, 0, 2]),
    ]

    assert np.allclose(
        sepia_image[0, 0],
        expected_pixel_value,
    ), "Assertion error from test_color2sepia: The two images are not equal"
