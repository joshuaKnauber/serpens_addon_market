# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This addon was generated with the Visual Scripting Addon.
# You can find the addon under https://blendermarket.com/products/serpens
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
sn_tree_name = "QuickFrame"
addon_keymaps = []

bl_info = {
    "name": "QuickFrame",
    "author": "Brennan Currier",
    "description": "Quickly add a frame in node editors",
    "location": "",
    "doc_url": "",
    "warning": "",
    "category": "Node Editor",
    "blender": (2,80,0),
    "version": (1,0,0)
}


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# IMPORTS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import bpy
from bpy.app.handlers import persistent


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# UTILITY FUNCTIONS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def sn_print(*text):
    text = ', '.join(map(str, text))
    print(text) # actual print command
    try: # try to find the area in which the addon is opened and add the print text
        for area in bpy.context.screen.areas:
            if area.type == "NODE_EDITOR":
                if area.spaces[0].node_tree:
                    if area.spaces[0].node_tree.bl_idname == "ScriptingNodesTree":
                        if sn_tree_name == area.spaces[0].node_tree.name:
                            bpy.context.scene.sn_properties.print_texts.add().text = str(text)

        for area in bpy.context.screen.areas:
            area.tag_redraw()
    except: pass
    
def get_enum_identifier(enumItems, name):
    for item in enumItems:
        if item.name == name:
            return item.identifier
            
    return ''
    
def get_python_filepath():
    path = os.path.dirname(bpy.data.filepath)
    try:
        __file__
        exported = True
    except:
        exported = False
    if exported:
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    return path


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CODE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class SNA_OT_Operator_b8d5040b7d(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_operator_b8d5040b7d'
    bl_label = 'Quick Frame'
    bl_description = 'Add a frame to the node editors'
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.ops.node.add_node(type="NodeFrame", use_transform=True)
            
        except Exception as exc:
            self.report({"ERROR"},message="There was an error when running this operation! It has been printed to the console.")
            print("START ERROR | Node Name: Create Operator | (If you are this addons developer you might want to report this to the Serpens team) ")
            print("")
            print(exc)
            print("")
            print("END ERROR - - - - ")
            print("")
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
def register_keymap_3670e0c410():
    global addon_keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    
    km = kc.keymaps.new(name="Node Editor", space_type="NODE_EDITOR")
    
    kmi = km.keymap_items.new(idname="scripting_nodes.sna_ot_operator_b8d5040b7d",type="F",value="PRESS",shift=False,ctrl=True,alt=False,any=False,repeat=False)
    addon_keymaps.append((km, kmi))
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROPERTIES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# REGISTER / UNREGISTER
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def register():
    bpy.utils.register_class(SNA_OT_Operator_b8d5040b7d)
    register_keymap_3670e0c410()

def unregister():
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(SNA_OT_Operator_b8d5040b7d)