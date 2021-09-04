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

from bpy_extras.io_utils import (
    ImportHelper,
    ExportHelper
)

from bpy.props import (
    StringProperty
)

bl_info = {
    "name": "MVR Import / Export",
    "author": "Felix Scheib, Lukas Runge",
    "version": (0, 0, 1),
    "blender": (2, 93, 4),
    "location": "File > Import | File > Export",
    "description": "Import / Export MVR e.g. for use in lighting control software",
    "warning": "I am not able to warn you yet, but this is under heavy development without ony knowledge.",
    "doc_url": "http://example.com/"
               "Scripts/Import-Export/MVR",
    "category": "Import-Export",
}

class ImportMVR(bpy.types.Operator, ImportHelper):
    """Import from 3DS file format (.3ds)"""
    bl_idname = "import_scene.mvr"
    bl_label = 'Import MVR'
    bl_options = {'UNDO'}

    filename_ext = ".mvr"
    filter_glob: StringProperty(default="*.mvr", options={'HIDDEN'})

    def execute(self, context):
        keywords = self.as_keywords()
        file = open(keywords["filepath"], "r")
        self.report({'INFO'}, file.read())
        file.close()

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
        file = open(keywords["filepath"], "w")
        try:
            file.write("Leben is toll :)")
            file.close()
            self.report({'INFO'}, "File saved")
            # get filename without extension
            filename_zip = os.path.splitext(keywords["filepath"])[0]
            # create zip file
            try:
                zip_file = zipfile.ZipFile(f'{filename_zip}.zip', "w")
                zip_file.write(keywords["filepath"], os.path.basename(keywords["filepath"]))
                zip_file.close()
                self.report({'INFO'}, "ZIP File saved")
            except:
                zip_file.close()
                self.report({'ERROR'}, "Could not create zip file")
        except:
            self.report({'ERROR'}, "File not saved")
        

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