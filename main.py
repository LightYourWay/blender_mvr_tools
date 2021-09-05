# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import zipfile
import os
import shutil

from bpy_extras.io_utils import (
    ImportHelper,
    ExportHelper
)

from bpy.props import (
    StringProperty
)

class ImportMVR(bpy.types.Operator, ImportHelper):
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

class ExportMVR(bpy.types.Operator, ExportHelper):
    """Export to 3DS file format (.3ds)"""
    bl_idname = "export_scene.mvr"
    bl_label = 'Export MVR'

    filename_ext = ".mvr"
    filter_glob: StringProperty(
        default="*.mvr",
        options={'HIDDEN'},
    )

    def execute(self, context):
        keywords = self.as_keywords()
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
        

        return {'FINISHED'}


# Add to a menu
def menu_func_export(self, context):
    self.layout.operator(ExportMVR.bl_idname, text="My virtual Rig (.mvr)")


def menu_func_import(self, context):
    self.layout.operator(ImportMVR.bl_idname, text="My virtual Rig (.mvr)")

def register():
    bpy.utils.register_class(ImportMVR)
    bpy.utils.register_class(ExportMVR)

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ImportMVR)
    bpy.utils.unregister_class(ExportMVR)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    print("Registering.")
    register()