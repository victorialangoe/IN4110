import numpy.testing as nt
from in3110_instapy.cython_filters import cython_color2gray, cython_color2sepia
import numpy as np


def test_color2gray(image, reference_gray):
    """Tests if cython_color2gray works the way it should do

    Args:
        image (any), reference_gray (any)
    Returns:
        None
    """
    filtered = cython_color2gray(image)

    assert isinstance(
        filtered, np.ndarray
    ), "numpy_color2grey does not return a numpy array"

    assert (
        filtered.shape == reference_gray.shape
    ), "Assertion error from test_color2gray: The shapes are not equal"
    assert (
        filtered.dtype == np.uint8
    ), "Assertion error from test_color2gray: The gray image' dtype is supposed to be uint8"
    assert (
        filtered.dtype == image.dtype
    ), "Assertion error from test_color2gray: The types are indifferent"

    expected_gray_value = int(
        0.21 * image[0, 0, 0] + 0.72 * image[0, 0, 1] + 0.07 * image[0, 0, 2]
    )

    nt.assert_allclose(
        filtered[0, 0],
        expected_gray_value,
        err_msg="The two images are not equal",
    )


def test_color2sepia(image, reference_sepia):
    """Tests if cython_color2gray works the way it should do

    Args:
        image (any), reference_gray (any)
    Returns:
        None
    """
    filtered = cython_color2sepia(image)

    assert isinstance(
        filtered, np.ndarray
    ), "numpy_color2sepia does not return a numpy array"

    assert (
        filtered.shape == reference_sepia.shape
    ), "Assertion error from test_color2sepia: The shapes are not equal"
    assert (
        filtered.dtype == np.uint8
    ), "Assertion error from test_color2sepia: The sepia image's dtype is supposed to be uint8"
    assert (
        filtered.dtype == image.dtype
    ), "Assertion error from test_color2sepia: The types are indifferent"

    expected_pixel_value = [
        int(0.393 * image[0, 0, 0] + 0.769 * image[0, 0, 1] + 0.189 * image[0, 0, 2]),
        int(0.349 * image[0, 0, 0] + 0.686 * image[0, 0, 1] + 0.168 * image[0, 0, 2]),
        int(0.272 * image[0, 0, 0] + 0.534 * image[0, 0, 1] + 0.131 * image[0, 0, 2]),
    ]
    assert np.allclose(
        filtered[0, 0],
        expected_pixel_value,
    ), "Assertion error from test_color2sepia: The image does not have the expected sepia pixel value"
