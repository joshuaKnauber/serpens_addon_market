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
sn_tree_name = "Steven Scott Pie Menu"
addon_keymaps = []

bl_info = {
    "name": "Pie Menu",
    "author": "",
    "description": "Pie menu",
    "location": "",
    "doc_url": "",
    "warning": "",
    "category": "General",
    "blender": (2,83,6),
    "version": (1,1,4)
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
class SNA_OT_Operator_b6ba890604(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_operator_b6ba890604'
    bl_label = 'My Operator'
    bl_description = 'My Operators description'
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.context.active_object.show_name = not bpy.context.active_object.show_name
            
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
class SNA_MT_e9064c9c8d(bpy.types.Menu):
    bl_label = "My Menu"
    bl_idname = "SNA_MT_e9064c9c8d"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("scripting_nodes.sna_ot_btn_ef09fe8d65",text=r"Add Sphere",emboss=True,depress=False,icon="SPHERE")
        if bool(bpy.context.active_object):
            pass
            pie.operator("scripting_nodes.sna_ot_btn_e8138a4b7c",text=r"Display Name",emboss=True,depress=False)
        else:
            pass
            
    
    
class SNA_OT_BTN_ef09fe8d65(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ef09fe8d65'
    bl_label = r"Add Sphere"
    bl_description = r""
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.mesh.primitive_uv_sphere_add('INVOKE_DEFAULT', segments=32, ring_count=16, radius=1.0, calc_uvs=True, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), align='WORLD')
            
        except Exception as exc:
            self.report({"ERROR"},message="There was an error when running this operation! It has been printed to the console.")
            print("START ERROR | Node Name: Button | (If you are this addons developer you might want to report this to the Serpens team) ")
            print("")
            print(exc)
            print("")
            print("END ERROR - - - - ")
            print("")
        return {"FINISHED"}
        
def register_keymap_76d3be098f():
    global addon_keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    
    km = kc.keymaps.new(name="Window", space_type="EMPTY")
    
    kmi = km.keymap_items.new(idname="wm.call_menu_pie",type="P",value="PRESS",shift=True,ctrl=True,alt=False,any=False,repeat=False)
    kmi.properties.name = "SNA_MT_e9064c9c8d"
    addon_keymaps.append((km, kmi))
    
class SNA_OT_BTN_e8138a4b7c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_e8138a4b7c'
    bl_label = r"Display Name"
    bl_description = r""
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_b6ba890604('EXEC_DEFAULT')
            
        except Exception as exc:
            self.report({"ERROR"},message="There was an error when running this operation! It has been printed to the console.")
            print("START ERROR | Node Name: Button.001 | (If you are this addons developer you might want to report this to the Serpens team) ")
            print("")
            print(exc)
            print("")
            print("END ERROR - - - - ")
            print("")
        return {"FINISHED"}
        

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROPERTIES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# REGISTER / UNREGISTER
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def register():
    bpy.utils.register_class(SNA_OT_Operator_b6ba890604)
    bpy.utils.register_class(SNA_MT_e9064c9c8d)
    bpy.utils.register_class(SNA_OT_BTN_ef09fe8d65)
    register_keymap_76d3be098f()
    bpy.utils.register_class(SNA_OT_BTN_e8138a4b7c)

def unregister():
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(SNA_OT_Operator_b6ba890604)
    bpy.utils.unregister_class(SNA_MT_e9064c9c8d)
    bpy.utils.unregister_class(SNA_OT_BTN_ef09fe8d65)
    bpy.utils.unregister_class(SNA_OT_BTN_e8138a4b7c)