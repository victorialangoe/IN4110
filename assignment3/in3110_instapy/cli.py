"""Command-line (script) interface to instapy"""
from __future__ import annotations

import argparse
import sys
import time

import in3110_instapy
import numpy as np
from PIL import Image

from in3110_instapy.timing import time_one

from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
    runtime: bool = False,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)
    if scale != 1:
        image = image.resize((int(image.width * scale), int(image.height * scale)))

    # Apply the filter
    filtered_function = in3110_instapy.get_filter(
        filter=filter, implementation=implementation
    )

    image_array = np.array(image)

    if runtime:
        avg_runtime = time_one(filtered_function, image_array, calls=3)
        print(f"Average time over 3 runs: {avg_runtime:.4f}s")
        filtered = filtered_function(image_array)
    else:
        filtered = filtered_function(image_array)

    filtered = filtered_function(image_array)

    if out_file:
        filtered.save(out_file)
    else:
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    print("Instapy is running...")

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    parser.add_argument(
        "filter",
        choices=["color2gray", "color2sepia"],
        help="Choose 'color2gray' or 'color2sepia'",
    )
    parser.add_argument(
        "implementation",
        choices=["python", "numpy", "numba", "cython"],
        help="Choose implementation: 'python', 'numpy', 'numba', or 'cython'",
    )

    parser.add_argument(
        "-sc", "--scale", type=float, default=1, help="Scale to resize the image"
    )

    # Optional task
    parser.add_argument(
        "-r",
        "--runtime",
        action="store_true",
        help="Track the time of your chosen implementation using '-r' or '--runtime'",
    )

    args = parser.parse_args(argv)

    run_filter(
        args.file, args.out, args.implementation, args.filter, args.scale, args.runtime
    )


if __name__ == "__main__":
    main()
