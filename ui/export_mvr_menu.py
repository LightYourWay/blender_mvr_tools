import bpy
import zipfile
import os
import shutil

from bpy_extras.io_utils import ExportHelper

from bpy.props import (
    StringProperty,
    BoolProperty
)


class ExportMvrMenu(bpy.types.Operator, ExportHelper):
    """Export to 3DS file format (.3ds)"""
    bl_idname = "export_scene.mvr"
    bl_label = 'Export MVR'

    filename_ext = ".mvr"

    filter_glob: StringProperty(default="*.mvr", options={'HIDDEN'})

    use_selection_only: BoolProperty(
        name="Selected Objects",
        description="Export selected objects only",
        default=False,
    )

    use_3ds_format: BoolProperty(
        name=".3ds Format (legacy!)",
        description="Export Objects in .3ds Format (legacy option!)",
        default=False,
    )

    def execute(self, context):
        keywords = self.as_keywords()

        print(keywords)

        """
        mvr_path = keywords["filepath"]
        root_path = f'{os.path.dirname(keywords["filepath"])}/temp_mvr'
        os.makedirs(root_path)
        file = open(f'{root_path}/demo.txt', "w")
        try:
            file.write("Leben is noch toller :)")
            file.close()
            print("File saved")
            # create zip file
            try:
                zip_file = zipfile.ZipFile(keywords["filepath"], "w")
                zip_file.write(f'{root_path}/demo.txt', 'demo.txt')
                zip_file.close()
                print("ZIP File saved")
            except:
                zip_file.close()
                print("Could not create zip file")
        except:
            print("File not saved")
        shutil.rmtree(root_path)
        """
        return {'FINISHED'}