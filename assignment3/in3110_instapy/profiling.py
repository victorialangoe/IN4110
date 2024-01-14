"""
Profiling (IN4110 only)
"""
from __future__ import annotations

import cProfile
import pstats
from pstats import SortKey

import in3110_instapy
import line_profiler

from in3110_instapy.cython_filters import cython_color2sepia

from . import io
from PIL import Image
import numpy as np


def profile_with_cprofile(filter, image, ncalls=3):
    """Profile filter(image) with line_profiler

    Statistics will be printed to stdout.

    Args:

        filter (callable): filter function
        image (ndarray): image to filter
        ncalls (int): number of repetitions to measure
    """
    profiler = cProfile.Profile()
    for _ in range(ncalls):
        profiler.runcall(filter, image)

    pstats.Stats(profiler).strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(10)


import line_profiler


def python_wrapper_color2sepia(image):
    return cython_color2sepia(image)


def profile_with_line_profiler(filter, image, ncalls=3):
    """Profile filter(image) with line_profiler

    Statistics will be printed to stdout.

    Args:
        filter (callable): filter function
        image (ndarray): image to filter
        ncalls (int): number of repetitions to measure
    """
    profiler = line_profiler.LineProfiler()

    # If the filter is the Cython function, use the Python wrapper
    if filter.__name__ == "cython_color2sepia":
        profiler.add_function(python_wrapper_color2sepia)
        filter_to_use = python_wrapper_color2sepia
    else:
        profiler.add_function(filter)
        filter_to_use = filter

    for _ in range(ncalls):
        filter_to_use(image)

    profiler.print_stats()


def run_profiles(profiler: str = "cprofile"):
    """Run profiles of every implementation

    Args:

        profiler (str): either 'line_profiler' or 'cprofile'
    """
    # Select which profile function to use
    if profiler == "line_profiler":
        profile_func = profile_with_line_profiler
    elif profiler.lower() == "cprofile":
        profile_func = profile_with_cprofile
    else:
        raise ValueError(f"{profiler=} must be 'line_profiler' or 'cprofile'")

    # construct a random 640x480 image
    image = io.random_image(640, 480)

    filter_names = ["color2gray", "color2sepia"]
    implementations = ["python", "numpy", "numba", "cython"]
    for filter_name in filter_names:
        for implementation in implementations:
            print(f"Profiling {implementation} {filter_name} with {profiler}:")
            filter = in3110_instapy.get_filter(filter_name, implementation)  #
            # call it once
            filter(image)
            profile_func(filter, image)


if __name__ == "__main__":
    print("Begin cProfile")
    run_profiles("cprofile")
    print("End cProfile")
    print("Begin line_profiler")
    run_profiles("line_profiler")
    print("End line_profiler")
