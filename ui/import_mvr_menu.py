import bpy
import zipfile

from bpy_extras.io_utils import ImportHelper

from bpy.props import StringProperty

class ImportMvrMenu(bpy.types.Operator, ImportHelper):
    """Import from 3DS file format (.3ds)"""
    bl_idname = "import_scene.mvr"
    bl_label = 'Import MVR'
    bl_options = {'UNDO'}

    filename_ext = ".mvr"
    filter_glob: StringProperty(default="*.mvr", options={'HIDDEN'})

    def execute(self, context):
        keywords = self.as_keywords()
        mvr_path = keywords['filepath']
        mvr_file = zipfile.ZipFile(mvr_path, 'r')
        print(mvr_file.read("demo.txt").decode("UTF-8"))

        return {'FINISHED'}