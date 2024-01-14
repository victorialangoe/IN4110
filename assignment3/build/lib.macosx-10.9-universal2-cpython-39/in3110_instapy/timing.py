from __future__ import annotations

import time
from typing import Callable
import os

from in3110_instapy import get_filter, io

from PIL import Image
import numpy as np


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    # run the filter function `calls` times
    # return the _average_ time of one call
    ...


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    image = Image.open(filename)
    image_array = np.array(image)
    print(f"Showing original picture")
    Image.fromarray(image_array).show()

    height, width = image.size
    print(f"Dimensions for {filename}: {height} x {width}")
    report_string = f"Dimensions for {filename}: {height} x {width}\n"

    filter_names = ["color2gray", "color2sepia"]
    implementations = ["python", "numpy", "numba"]

    for filter_name in filter_names:
        start_time = time.time()
        reference_filter_function = get_filter(
            filter=filter_name, implementation="python"
        )
        reference_filter = reference_filter_function(image_array)
        Image.fromarray(reference_filter).show()

        reference_time = time.time() - start_time
        print(
            f"\nReference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})"
        )
        report_string += f"\nReference (pure Python) filter time {filter_name}: {reference_time:.3f}s (calls={calls})\n"

        for implementation in implementations[1:]:
            filter_function = get_filter(
                filter=filter_name, implementation=implementation
            )
            start_time = time.time()
            filter_function(image_array)
            filter_time = time.time() - start_time
            speedup = reference_time / filter_time
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )
            report_string += f"Timing: {implementation} {filter_name}: {filter_time:.3f}s (speedup={speedup:.2f}x)\n"

    with open("in3110_instapy/timing-report.txt", "w") as f:
        f.write(report_string)


if __name__ == "__main__":
    # run as `python -m in3110_instapy.timing`
    make_reports()
