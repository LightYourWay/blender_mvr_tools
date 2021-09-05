# add path of *.blend file to search path for modules
# this is needed for correct 'relative import' of custom modules
# in case of automatic testing via github actions
import bpy
import sys
import os

# we get blend file path
filepath = bpy.data.filepath

# we get the directory relative to the blend file path
dir = os.path.dirname(filepath)

# we append our path to blender modules path
# we use if not statement to do this one time only
if not dir in sys.path:
    sys.path.append(dir)

if not os.path.dirname(dir) in sys.path:
    sys.path.append(os.path.dirname(dir))

# ---------------------------------------------------------------

import unittest

if __name__ == "__main__":
    sys.argv = [__file__] + (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    testsuite = unittest.TestLoader().discover('test/unit_test')
    unittest.TextTestRunner(verbosity=2).run(testsuite)