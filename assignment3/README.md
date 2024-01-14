# in3110_instapy

# Turn your Instagram into a beautiful canvas! This package puts either a grayscale or sepia filter on any .jpg image!

### Installation:

Install the package using pip. See [documentation for pip](https://pip.pypa.io/en/stable/) here.

    - pip install in3110_instapy

### You can also verify the installation by writing:

    - in3110_instapy --version

### How to run this package:

First you will need a .jpg image.

    - python3 -m in3110_instapy [YOUR_IMAGE.jpg] [FILTER] [IMPLEMENTATION]

FILTER: Choose between 'color2gray' or 'color2sepia'

IMPLEMENTATION: Select from 'python', 'numpy', 'numba', or 'cython'

### Additional flags

You can also add a extra flag '-r' or '--runtime' to calculate the average runtime for your chosen implementation. This is an example for how to use the flag

    - python3 -m in3110_instapy -r rain.jpg color2sepia python

### Help

If you need more help on running the package you can also write:

    - python3 -m in3110_instapy --help
