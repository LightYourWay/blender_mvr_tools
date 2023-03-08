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
from . ui.import_mvr_menu import *
from . ui.export_mvr_menu import *

# Add to a menu
def menu_func_export(self, context):
    self.layout.operator(ExportMvrMenu.bl_idname, text="My Virtual Rig (.mvr)")


def menu_func_import(self, context):
    self.layout.operator(ImportMvrMenu.bl_idname, text="My Virtual Rig (.mvr)")

def register():
    bpy.utils.register_class(ImportMvrMenu)
    bpy.utils.register_class(ExportMvrMenu)

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ImportMvrMenu)
    bpy.utils.unregister_class(ExportMvrMenu)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    print("Registering.")
    register()