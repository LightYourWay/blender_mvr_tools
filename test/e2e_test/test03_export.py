import unittest
import bpy
import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class test_export(unittest.TestCase):
    def test_export(self):
        print('starting Export')

        # open *.blend file for testing
        blend_path = bpy.path.abspath("//export.blend")
        bpy.ops.wm.open_mainfile(filepath=blend_path)

        with captured_output() as (out, err):
            result = bpy.ops.export_scene.mvr(filepath = bpy.path.abspath("//dist/export.mvr"))
        output = out.getvalue().strip()
        print(output)

        self.assertEqual(output, 'File saved\nZIP File saved')
        self.assertEqual(result, {'FINISHED'})

        print('>> ', end='', flush=True)