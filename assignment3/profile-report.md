# Profiling report

## Questions

A few questions below. We are not asking for lots of detail,
just 1-2 sentences each.

### Question 1

> which profiler produced the most useful output, and why?

I cant get line_profiler to work properly so obviosly I think numpy is better but I also think the cProfile produces the most useful output because it shows cumulative time which gives more insights, even though total time really shows how the code is optimized.

### Question 2

> Which implementations have the most useful profiling output, and why?

Perhaps numpy since it gives an in-depth insight on how it is better than python and shows specifially where it does it faster.

### Question 3

> Do any profiler+implementations produce seem to not work at all? If so, which?

The line_profiler does not work, but I also see that numba implementations get tottime 0s.

## profile output

<details>
<summary>cProfile output</summary>

```
python3 -m in3110_instapy.profiling
Begin cProfile
Profiling python color2gray with cprofile:
         9 function calls in 2.529 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    2.529    0.843    2.529    0.843 python_filters.py:9(python_color2gray)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 multiarray.py:85(empty_like)


Profiling numpy color2gray with cprofile:
         51 function calls in 0.013 seconds

   Ordered by: cumulative time
   List reduced from 15 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.012    0.004    0.013    0.004 numpy_filters.py:7(numpy_color2gray)
        3    0.001    0.000    0.001    0.000 shape_base.py:372(stack)
        3    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 shape_base.py:362(_stack_dispatcher)
        3    0.000    0.000    0.000    0.000 shape_base.py:455(<listcomp>)
        3    0.000    0.000    0.000    0.000 shape_base.py:443(<listcomp>)
        3    0.000    0.000    0.000    0.000 shape_base.py:207(_arrays_for_stack_dispatcher)
        3    0.000    0.000    0.000    0.000 shape_base.py:447(<setcomp>)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        9    0.000    0.000    0.000    0.000 {built-in method numpy.asanyarray}


Profiling numba color2gray with cprofile:
         9 function calls in 0.015 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.015    0.005    0.015    0.005 numba_filters.py:8(numba_color2gray)
        3    0.000    0.000    0.000    0.000 serialize.py:30(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling cython color2gray with cprofile:
         6 function calls in 0.270 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.270    0.090    0.270    0.090 cython_filters.py:27(cython_color2gray)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling python color2sepia with cprofile:
         2764809 function calls in 7.028 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    6.835    2.278    7.028    2.343 python_filters.py:30(python_color2sepia)
  2764800    0.193    0.000    0.193    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 multiarray.py:85(empty_like)


Profiling numpy color2sepia with cprofile:
         54 function calls in 0.033 seconds

   Ordered by: cumulative time
   List reduced from 11 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.029    0.010    0.033    0.011 numpy_filters.py:23(numpy_color2sepia)
        6    0.000    0.000    0.003    0.000 fromnumeric.py:2100(clip)
        6    0.000    0.000    0.003    0.000 fromnumeric.py:53(_wrapfunc)
        6    0.000    0.000    0.003    0.000 {method 'clip' of 'numpy.ndarray' objects}
        6    0.003    0.000    0.003    0.000 _methods.py:90(_clip)
        6    0.001    0.000    0.001    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        6    0.000    0.000    0.000    0.000 fromnumeric.py:2096(_clip_dispatcher)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numba color2sepia with cprofile:
         9 function calls in 0.014 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.014    0.005    0.014    0.005 numba_filters.py:29(numba_color2sepia)
        3    0.000    0.000    0.000    0.000 serialize.py:30(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling cython color2sepia with cprofile:
         6 function calls in 1.648 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    1.648    0.549    1.648    0.549 cython_filters.py:51(cython_color2sepia)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


End cProfile
Begin line_profiler
Profiling python color2gray with line_profiler:
Timer unit: 1e-09 s

Total time: 1.01572 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/python_filters.py
Function: python_color2gray at line 9

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     9                                           def python_color2gray(image: np.array) -> np.array:
    10                                               """Convert rgb pixel array to grayscale
    11
    12                                               Args:
    13                                                   image (np.array)
    14                                               Returns:
    15                                                   np.array: gray_image
    16                                               """
    17         1       4000.0   4000.0      0.0      gray_image = np.empty_like(image)
    18         1       1000.0   1000.0      0.0      height, width = image.shape[:2]
    19
    20       481      66000.0    137.2      0.0      for row in range(height):
    21    307680   36302000.0    118.0      3.6          for column in range(width):
    22    307200  191530000.0    623.5     18.9              red, green, blue = image[row, column][:3]
    23    307200  678149000.0   2207.5     66.8              gray_value = int(0.21 * red + 0.72 * green + 0.07 * blue)
    24
    25    307200  109668000.0    357.0     10.8              gray_image[row, column] = gray_value
    26
    27         1          0.0      0.0      0.0      return gray_image

Profiling numpy color2gray with line_profiler:
Timer unit: 1e-09 s

Total time: 0.004722 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/numpy_filters.py
Function: numpy_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def numpy_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15
    16         1    4161000.0    4e+06     88.1      gray_image = np.dot(image[..., :3], [0.21, 0.72, 0.07])
    17         1     162000.0 162000.0      3.4      gray_image = gray_image.astype(np.uint8)
    18         1     399000.0 399000.0      8.4      gray_image_3d = np.stack([gray_image, gray_image, gray_image], axis=-1)
    19
    20         1          0.0      0.0      0.0      return gray_image_3d

Profiling numba color2gray with line_profiler:
/Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/profiling.py:48: UserWarning: Adding a function with a __wrapped__ attribute. You may want to profile the wrapped function by adding numba_color2gray.__wrapped__ instead.
  profiler.add_function(filter)
/opt/homebrew/lib/python3.11/site-packages/line_profiler/line_profiler.py:75: UserWarning: Adding a function with a __wrapped__ attribute. You may want to profile the wrapped function by adding numba_color2gray.__wrapped__ instead.
  self.add_function(func)
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/numba_filters.py
Function: numba_color2gray at line 8

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     8                                           @jit(nopython=True, parallel=True)
     9                                           def numba_color2gray(image: np.array) -> np.array:
    10                                               """Convert rgb pixel array to grayscale
    11
    12                                               Args:
    13                                                   image (np.array)
    14                                               Returns:
    15                                                   np.array: gray_image
    16                                               """
    17                                               gray_image = np.empty_like(image)
    18                                               height, width = image.shape[:2]
    19
    20                                               for row in prange(height):
    21                                                   for column in prange(width):
    22                                                       red, green, blue = image[row, column][:3]
    23                                                       gray_value = int(0.21 * red + 0.72 * green + 0.07 * blue)
    24                                                       gray_image[row, column] = [gray_value, gray_value, gray_value]
    25
    26                                               return gray_image
```

</details>

<details>
<summary>line_profiler output</summary>

python3 -m in3110_instapy.profiling
Begin cProfile
Profiling python color2gray with cprofile:
9 function calls in 2.534 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
3 2.534 0.845 2.534 0.845 python_filters.py:9(python_color2gray)
3 0.000 0.000 0.000 0.000 {method 'disable' of '\_lsprof.Profiler' objects}
3 0.000 0.000 0.000 0.000 multiarray.py:85(empty_like)

Profiling numpy color2gray with cprofile:
51 function calls in 0.014 seconds

Ordered by: cumulative time
List reduced from 15 to 10 due to restriction <10>

ncalls tottime percall cumtime percall filename:lineno(function)
3 0.012 0.004 0.014 0.005 numpy_filters.py:7(numpy_color2gray)
3 0.001 0.000 0.001 0.000 shape_base.py:372(stack)
3 0.000 0.000 0.000 0.000 {method 'astype' of 'numpy.ndarray' objects}
3 0.000 0.000 0.000 0.000 shape_base.py:362(\_stack_dispatcher)
3 0.000 0.000 0.000 0.000 shape_base.py:207(\_arrays_for_stack_dispatcher)
3 0.000 0.000 0.000 0.000 shape_base.py:447(<setcomp>)
3 0.000 0.000 0.000 0.000 shape_base.py:455(<listcomp>)
3 0.000 0.000 0.000 0.000 shape_base.py:443(<listcomp>)
3 0.000 0.000 0.000 0.000 {built-in method builtins.hasattr}
9 0.000 0.000 0.000 0.000 {built-in method numpy.asanyarray}

Profiling numba color2gray with cprofile:
9 function calls in 0.015 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
3 0.015 0.005 0.015 0.005 numba_filters.py:8(numba_color2gray)
3 0.000 0.000 0.000 0.000 serialize.py:30(\_numba_unpickle)
3 0.000 0.000 0.000 0.000 {method 'disable' of '\_lsprof.Profiler' objects}

Profiling cython color2gray with cprofile:
6 function calls in 0.270 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
3 0.270 0.090 0.270 0.090 cython_filters.py:27(cython_color2gray)
3 0.000 0.000 0.000 0.000 {method 'disable' of '\_lsprof.Profiler' objects}

Profiling python color2sepia with cprofile:
2764809 function calls in 6.966 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
3 6.773 2.258 6.966 2.322 python_filters.py:30(python_color2sepia)
2764800 0.193 0.000 0.193 0.000 {built-in method builtins.min}
3 0.000 0.000 0.000 0.000 {method 'disable' of '\_lsprof.Profiler' objects}
3 0.000 0.000 0.000 0.000 multiarray.py:85(empty_like)

Profiling numpy color2sepia with cprofile:
54 function calls in 0.033 seconds

Ordered by: cumulative time
List reduced from 11 to 10 due to restriction <10>

ncalls tottime percall cumtime percall filename:lineno(function)
3 0.029 0.010 0.033 0.011 numpy_filters.py:23(numpy_color2sepia)
6 0.000 0.000 0.002 0.000 fromnumeric.py:2100(clip)
6 0.000 0.000 0.002 0.000 fromnumeric.py:53(\_wrapfunc)
6 0.000 0.000 0.002 0.000 {method 'clip' of 'numpy.ndarray' objects}
6 0.002 0.000 0.002 0.000 \_methods.py:90(\_clip)
6 0.001 0.000 0.001 0.000 {method 'astype' of 'numpy.ndarray' objects}
3 0.000 0.000 0.000 0.000 {built-in method numpy.array}
6 0.000 0.000 0.000 0.000 {built-in method builtins.getattr}
6 0.000 0.000 0.000 0.000 fromnumeric.py:2096(\_clip_dispatcher)
3 0.000 0.000 0.000 0.000 {method 'disable' of '\_lsprof.Profiler' objects}

Profiling numba color2sepia with cprofile:
9 function calls in 0.014 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
3 0.014 0.005 0.014 0.005 numba_filters.py:29(numba_color2sepia)
3 0.000 0.000 0.000 0.000 serialize.py:30(\_numba_unpickle)
3 0.000 0.000 0.000 0.000 {method 'disable' of '\_lsprof.Profiler' objects}

Profiling cython color2sepia with cprofile:
6 function calls in 1.640 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
3 1.640 0.547 1.640 0.547 cython_filters.py:51(cython_color2sepia)
3 0.000 0.000 0.000 0.000 {method 'disable' of '\_lsprof.Profiler' objects}

End cProfile
Begin line_profiler
Profiling python color2gray with line_profiler:
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/python_filters.py
Function: python_color2gray at line 9

# Line # Hits Time Per Hit % Time Line Contents

     9                                           def python_color2gray(image: np.array) -> np.array:
    10                                               """Convert rgb pixel array to grayscale
    11
    12                                               Args:
    13                                                   image (np.array)
    14                                               Returns:
    15                                                   np.array: gray_image
    16                                               """
    17                                               gray_image = np.empty_like(image)
    18                                               height, width = image.shape[:2]
    19
    20                                               for row in range(height):
    21                                                   for column in range(width):
    22                                                       red, green, blue = image[row, column][:3]
    23                                                       gray_value = int(0.21 * red + 0.72 * green + 0.07 * blue)
    24
    25                                                       gray_image[row, column] = gray_value
    26
    27                                               return gray_image

Profiling numpy color2gray with line_profiler:
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/numpy_filters.py
Function: numpy_color2gray at line 7

# Line # Hits Time Per Hit % Time Line Contents

     7                                           def numpy_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15
    16                                               gray_image = np.dot(image[..., :3], [0.21, 0.72, 0.07])
    17                                               gray_image = gray_image.astype(np.uint8)
    18                                               gray_image_3d = np.stack([gray_image, gray_image, gray_image], axis=-1)
    19
    20                                               return gray_image_3d

Profiling numba color2gray with line_profiler:
/Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/profiling.py:62: UserWarning: Adding a function with a **wrapped** attribute. You may want to profile the wrapped function by adding numba_color2gray.**wrapped** instead.
profiler.add_function(filter)
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/numba_filters.py
Function: numba_color2gray at line 8

# Line # Hits Time Per Hit % Time Line Contents

     8                                           @jit(nopython=True, parallel=True)
     9                                           def numba_color2gray(image: np.array) -> np.array:
    10                                               """Convert rgb pixel array to grayscale
    11
    12                                               Args:
    13                                                   image (np.array)
    14                                               Returns:
    15                                                   np.array: gray_image
    16                                               """
    17                                               gray_image = np.empty_like(image)
    18                                               height, width = image.shape[:2]
    19
    20                                               for row in prange(height):
    21                                                   for column in prange(width):
    22                                                       red, green, blue = image[row, column][:3]
    23                                                       gray_value = int(0.21 * red + 0.72 * green + 0.07 * blue)
    24                                                       gray_image[row, column] = [gray_value, gray_value, gray_value]
    25
    26                                               return gray_image

Profiling cython color2gray with line_profiler:
Timer unit: 1e-09 s

Profiling python color2sepia with line_profiler:
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/python_filters.py
Function: python_color2sepia at line 30

# Line # Hits Time Per Hit % Time Line Contents

    30                                           def python_color2sepia(image: np.array) -> np.array:
    31                                               """Convert rgb pixel array to sepia
    32
    33                                               Args:
    34                                                   image (any)
    35                                               Returns:
    36                                                   np.array: sepia_image
    37                                               """
    38                                               sepia_image = np.empty_like(image)
    39                                               height, width = image.shape[:2]
    40                                               sepia_matrix = [
    41                                                   [0.393, 0.769, 0.189],
    42                                                   [0.349, 0.686, 0.168],
    43                                                   [0.272, 0.534, 0.131],
    44                                               ]
    45
    46                                               for row in range(height):
    47                                                   for column in range(width):
    48                                                       red, green, blue = image[row, column][:3]
    49                                                       sepia_r = int(
    50                                                           red * sepia_matrix[0][0]
    51                                                           + green * sepia_matrix[0][1]
    52                                                           + blue * sepia_matrix[0][2]
    53                                                       )
    54                                                       sepia_g = int(
    55                                                           red * sepia_matrix[1][0]
    56                                                           + green * sepia_matrix[1][1]
    57                                                           + blue * sepia_matrix[1][2]
    58                                                       )
    59                                                       sepia_b = int(
    60                                                           red * sepia_matrix[2][0]
    61                                                           + green * sepia_matrix[2][1]
    62                                                           + blue * sepia_matrix[2][2]
    63                                                       )
    64                                                       sepia_image[row, column] = [
    65                                                           min(sepia_r, 255),
    66                                                           min(sepia_g, 255),
    67                                                           min(sepia_b, 255),
    68                                                       ]
    69
    70                                               return sepia_image

Profiling numpy color2sepia with line_profiler:
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/numpy_filters.py
Function: numpy_color2sepia at line 23

# Line # Hits Time Per Hit % Time Line Contents

    23                                           def numpy_color2sepia(image: np.array, k: float = 1) -> np.array:
    24                                               """Convert rgb pixel array to sepia
    25
    26                                               Args:
    27                                                   image (np.array)
    28                                                   k (float): amount of sepia (optional)
    29
    30                                               The amount of sepia is given as a fraction, k=0 yields no sepia while
    31                                               k=1 yields full sepia.
    32
    33                                               (note: implementing 'k' is a bonus task,
    34                                                   you may ignore it)
    35
    36                                               Returns:
    37                                                   np.array: sepia_image
    38                                               """
    39                                               if k > 1 or k < 0:
    40                                                   raise ValueError(f"k needs to be within range 0 to 1. k is {k}")
    41
    42                                               sepia_matrix = np.array(
    43                                                   [
    44                                                       [0.393, 0.769, 0.189],
    45                                                       [0.349, 0.686, 0.168],
    46                                                       [0.272, 0.534, 0.131],
    47                                                   ]
    48                                               )
    49
    50                                               sepia_image = np.dot(image[..., :3], sepia_matrix.T)
    51                                               sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)
    52
    53                                               if k == 0:
    54                                                   return sepia_image
    55
    56                                               blended_image = k * sepia_image + (1 - k) * image[..., :3]
    57                                               blended_image = np.clip(blended_image, 0, 255).astype(np.uint8)
    58
    59                                               return blended_image

Profiling numba color2sepia with line_profiler:
/Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/profiling.py:62: UserWarning: Adding a function with a **wrapped** attribute. You may want to profile the wrapped function by adding numba_color2sepia.**wrapped** instead.
profiler.add_function(filter)
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/numba_filters.py
Function: numba_color2sepia at line 29

# Line # Hits Time Per Hit % Time Line Contents

    29                                           @jit(nopython=True, parallel=True)
    30                                           def numba_color2sepia(image: np.array) -> np.array:
    31                                               """Convert rgb pixel array to sepia
    32
    33                                               Args:
    34                                                   image (np.array)
    35                                               Returns:
    36                                                   np.array: sepia_image
    37                                               """
    38                                               sepia_image = np.empty_like(image)
    39                                               height, width = image.shape[:2]
    40                                               sepia_matrix = np.array(
    41                                                   [
    42                                                       [0.393, 0.769, 0.189],
    43                                                       [0.349, 0.686, 0.168],
    44                                                       [0.272, 0.534, 0.131],
    45                                                   ]
    46                                               )
    47
    48                                               for row in prange(height):
    49                                                   for column in prange(width):
    50                                                       red, green, blue = image[row, column][:3]
    51                                                       sepia_r = int(
    52                                                           red * sepia_matrix[0][0]
    53                                                           + green * sepia_matrix[0][1]
    54                                                           + blue * sepia_matrix[0][2]
    55                                                       )
    56                                                       sepia_g = int(
    57                                                           red * sepia_matrix[1][0]
    58                                                           + green * sepia_matrix[1][1]
    59                                                           + blue * sepia_matrix[1][2]
    60                                                       )
    61                                                       sepia_b = int(
    62                                                           red * sepia_matrix[2][0]
    63                                                           + green * sepia_matrix[2][1]
    64                                                           + blue * sepia_matrix[2][2]
    65                                                       )
    66                                                       sepia_image[row, column] = [
    67                                                           min(sepia_r, 255),
    68                                                           min(sepia_g, 255),
    69                                                           min(sepia_b, 255),
    70                                                       ]
    71
    72                                               return sepia_image

Profiling cython color2sepia with line_profiler:
Timer unit: 1e-09 s

Total time: 0 s
File: /Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment3/in3110_instapy/profiling.py
Function: python_wrapper_color2sepia at line 41

# Line # Hits Time Per Hit % Time Line Contents

    41                                           def python_wrapper_color2sepia(image):
    42                                               return cython_color2sepia(image)

End line_profiler

</details>
