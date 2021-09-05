import unittest
import bpy
import main

class test_unregister(unittest.TestCase):
    def test_unregister(self):
        main.unregister()
        self.assertFalse(hasattr(bpy.types, bpy.ops.import_scene.mvr.idname()))
        self.assertFalse(hasattr(bpy.types, bpy.ops.export_scene.mvr.idname()))