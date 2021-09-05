import unittest
import bpy
import main

class test_register(unittest.TestCase):
    def test_register(self):
        main.register()
        self.assertTrue(hasattr(bpy.types, bpy.ops.import_scene.mvr.idname()))
        self.assertTrue(hasattr(bpy.types, bpy.ops.export_scene.mvr.idname()))