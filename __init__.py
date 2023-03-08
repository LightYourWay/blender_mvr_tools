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

from .main import *

import importlib
from . import ui

importlib.reload(ui)

bl_info = {
    "name": "MVR Import / Export",
    "author": "Felix Scheib, Lukas Runge",
    "version": (0, 0, 1),
    "blender": (3, 4, 1),
    "location": "File > Import | File > Export",
    "description": "Import/Export of MVR (My Virtual Rig) Data. MVR is used in the event industry to exchange the data of stages and lighting devices.",
    "warning": "This AddOn is under heavy development.",
    "doc_url": "http://example.com/"
               "Scripts/Import-Export/MVR",
    "category": "Import-Export",
}

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    print("Registering.")
    register()