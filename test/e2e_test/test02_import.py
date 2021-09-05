import unittest
import bpy
import sys
import os
from contextlib import contextmanager
from contextlib import redirect_stdout
from io import StringIO

stdout = StringIO()

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class test_import(unittest.TestCase):
    def test_import(self):
        print('starting Import')

        # remember path to return to for later
        blend_path = bpy.path.abspath("//import.blend")

        # open *.blend file for testing
        bpy.ops.wm.open_mainfile(filepath=blend_path)

        # define dist path
        dist_path = bpy.path.abspath("//dist")
        
        # import test mvr file and capture output
        with captured_output() as (out, err):
            result = bpy.ops.import_scene.mvr(filepath = bpy.path.abspath("//import.mvr"))
        output = out.getvalue().strip()
        print(output)

        # save resulting *.blend file as artifact
        file_path = os.path.join(dist_path, "import.blend")
        try:
            os.remove(file_path)
        except OSError:
            pass
        bpy.ops.wm.save_as_mainfile(check_existing=False, filepath=file_path)

        # check if the file was loaded correctly
        self.assertEqual(output, 'Leben is noch toller :)')
        self.assertEqual(result, {'FINISHED'})
        
        # reopen original file
        bpy.ops.wm.open_mainfile(filepath=blend_path)
        print('>> ', end='', flush=True)