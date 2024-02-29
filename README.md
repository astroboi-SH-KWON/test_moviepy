# test_moviepy
test moviepy, conda install conda-forge::moviepy


# Setting up the Environment  
* conda create -n test_moviepy
* conda activate test_moviepy
* conda install conda-forge::python==3.9.0
* conda install conda-forge::moviepy==1.0.3

# Trouble shooting
* conda install anaconda::numpy==1.22.3
* Downgrade numpy version

Traceback (most recent call last):
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/__init__.py", line 23, in <module>
    from . import multiarray
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/multiarray.py", line 10, in <module>
    from . import overrides
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/overrides.py", line 6, in <module>
    from numpy.core._multiarray_umath import (
ImportError: dlopen(/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so, 0x0002): Library not loaded: @rpath/libcblas.3.dylib
  Referenced from: <47C3937E-13E1-3103-AB3D-5460F93E55D8> /Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so
  Reason: tried: '/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/../../../../libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/../../../../libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/bin/../lib/libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/bin/../lib/libcblas.3.dylib' (no such file), '/usr/local/lib/libcblas.3.dylib' (no such file), '/usr/lib/libcblas.3.dylib' (no such file, not in dyld cache)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/{username}/PycharmProjects/test_moviepy/merge_mp4_files.py", line 1, in <module>
    from moviepy.editor import *
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/moviepy/editor.py", line 24, in <module>
    import imageio
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/imageio/__init__.py", line 24, in <module>
    from .core import FormatManager, RETURN_BYTES
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/imageio/core/__init__.py", line 10, in <module>
    from .util import Image, Array, Dict, asarray, image_as_uint, urlopen
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/imageio/core/util.py", line 10, in <module>
    import numpy as np
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/__init__.py", line 140, in <module>
    from . import core
  File "/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/__init__.py", line 49, in <module>
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.9 from "/Users/{username}/anaconda3/envs/test_moviepy/bin/python"
  * The NumPy version is: "1.23.5"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: dlopen(/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so, 0x0002): Library not loaded: @rpath/libcblas.3.dylib
  Referenced from: <47C3937E-13E1-3103-AB3D-5460F93E55D8> /Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so
  Reason: tried: '/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/../../../../libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/lib/python3.9/site-packages/numpy/core/../../../../libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/bin/../lib/libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/{username}/anaconda3/envs/test_moviepy/lib/libcblas.3.dylib' (no such file), '/Users/{username}/anaconda3/envs/test_moviepy/bin/../lib/libcblas.3.dylib' (no such file), '/usr/local/lib/libcblas.3.dylib' (no such file), '/usr/lib/libcblas.3.dylib' (no such file, not in dyld cache)


