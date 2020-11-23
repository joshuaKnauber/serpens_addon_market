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
sn_tree_name = "kolup_ops"
addon_keymaps = []

bl_info = {
    "name": "kolup_ops",
    "author": "kolupsy",
    "description": "basic hardsurface modeling tools (Shift+Q to open up menu)",
    "location": "",
    "doc_url": "",
    "warning": "",
    "category": "General",
    "blender": (2,90,0),
    "version": (1,2,0)
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

def report_sn_error(self,error):
    self.report({"ERROR"},message="There was an error when running this operation! It has been printed to the console.")
    print("START ERROR | Node Name: ",self.name," | (If you are this addons developer you might want to report this to the Serpens team) ")
    print("")
    print(error)
    print("")
    print("END ERROR - - - - ")
    print("")
    
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

def cast_int(cast):
    int_string = ""
    if type(cast) == str:
        for char in cast:
            if char.isnumeric():
                int_string+=char
    else:
        return cast[0]
    if int_string.isnumeric():
        int_string = int(int_string)
        return int_string
    return 0

def cast_float(cast):
    float_string = ""
    if type(cast) == str:
        for char in cast:
            if char.isnumeric() or char == ".":
                float_string+=char
    else:
        return cast[0]
    if float_string != "" and float_string != ".":
        float_string = float(float_string)
        return float_string
    return 0
    
def cast_vector(cast):
    if type(cast) == bool:
        if cast:
            return (1.0, 1.0, 1.0)
        else:
            return (0.0, 0.0, 0.0)
    elif type(cast) == int:
        return (float(cast), float(cast), float(cast))
    elif type(cast) == float:
        return (cast, cast, cast)
    elif type(cast) == str:
        cast = cast_float(cast)
        return (cast, cast, cast)
    return (0, 0, 0)

def cast_four_vector(cast, four):
    if type(cast) == bool:
        if cast:
            return (1.0, 1.0, 1.0, four)
        else:
            return (0.0, 0.0, 0.0, four)
    elif type(cast) == int:
        return (float(cast), float(cast), float(cast), four)
    elif type(cast) == float:
        return (cast, cast, cast, four)
    elif type(cast) == str:
        cast = cast_float(cast)
        return (cast, cast, cast, four)
    return (0, 0, 0)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CLASSES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # Create Array Collection for use in PROPERTIES
class ArrayCollection_UID_Yzrkrwfk(bpy.types.PropertyGroup):
    string: bpy.props.StringProperty()
    string_filepath: bpy.props.StringProperty(subtype='FILE_PATH')
    string_dirpath: bpy.props.StringProperty(subtype='DIR_PATH')
    bool: bpy.props.BoolProperty()

    int: bpy.props.IntProperty()
    int_pixel: bpy.props.IntProperty(subtype="PIXEL")
    int_unsigned: bpy.props.IntProperty(subtype="UNSIGNED")
    int_percentage: bpy.props.IntProperty(subtype="PERCENTAGE")
    int_factor: bpy.props.IntProperty(subtype="FACTOR")
    int_angle: bpy.props.IntProperty(subtype="ANGLE")
    int_time: bpy.props.IntProperty(subtype="TIME")
    int_distance: bpy.props.IntProperty(subtype="DISTANCE")

    float: bpy.props.FloatProperty()
    float_pixel: bpy.props.FloatProperty(subtype="PIXEL")
    float_unsigned: bpy.props.FloatProperty(subtype="UNSIGNED")
    float_percentage: bpy.props.FloatProperty(subtype="PERCENTAGE")
    float_factor: bpy.props.FloatProperty(subtype="FACTOR")
    float_angle: bpy.props.FloatProperty(subtype="ANGLE")
    float_time: bpy.props.FloatProperty(subtype="TIME")
    float_distance: bpy.props.FloatProperty(subtype="DISTANCE")

    vector: bpy.props.FloatVectorProperty()
    four_vector: bpy.props.FloatVectorProperty(size=4)
    color: bpy.props.FloatVectorProperty(subtype='COLOR')
    four_color: bpy.props.FloatVectorProperty(subtype='COLOR', size=4)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CODE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class SNA_OT_Operator_a0d60c05e4(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_a0d60c05e4"
    bl_label = "Add Solidify"
    bl_description = "adds a Solidify Modifier to the active Object"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            op_reset_context = context.area.type
            context.area.type = "VIEW_3D"
            bpy.ops.object.modifier_add('INVOKE_DEFAULT', type='SOLIDIFY')
            context.area.type = op_reset_context
            bpy.context.active_object.modifiers[-1].name = r"Kolup Ops Solidify"
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_MT_21f45cbf38(bpy.types.Menu):
    bl_label = "Solidify Options"
    bl_idname = "SNA_MT_21f45cbf38"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Solidify"], 'thickness', emboss=True, text=r"Change Thickness", slider=True)
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Solidify"], 'use_flip_normals', toggle=True, emboss=True, text=r"Flipped Normals", icon="NORMALS_FACE")
    
    
class SNA_OT_Operator_a8ed88c43c(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_a8ed88c43c"
    bl_label = "Add Bevel"
    bl_description = "My Operators description"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.ops.object.modifier_add('INVOKE_DEFAULT', type='BEVEL')
            bpy.context.active_object.modifiers[-1].name = r"Kolup Ops Bevel"
            bpy.context.active_object.modifiers[-1].harden_normals = True
            bpy.context.active_object.modifiers[-1].miter_outer = get_enum_identifier(bpy.context.active_object.modifiers[-1].bl_rna.properties['miter_outer'].enum_items, r"Arc")
            bpy.context.active_object.modifiers[-1].limit_method = get_enum_identifier(bpy.context.active_object.modifiers[-1].bl_rna.properties['limit_method'].enum_items, r"Angle")
            bpy.data.meshes[bpy.context.active_object.data.name].use_auto_smooth = True
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_MT_dec1fac416(bpy.types.Menu):
    bl_label = "Bevel Options"
    bl_idname = "SNA_MT_dec1fac416"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Bevel"], 'width', emboss=True, text=r"Bevel Amount", slider=True)
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Bevel"], 'segments', emboss=True, text=r"Segments", slider=True)
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Bevel"], 'harden_normals', toggle=True, emboss=True, text=r"Harden Normals")
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Bevel"], 'angle_limit', emboss=True, text=r"Angle Limit", slider=False)
        layout.separator(factor=1.0)
        layout.operator("scripting_nodes.sna_ot_btn_35165c1dc4",text=r"Push To Bottom",emboss=True,depress=False,icon="MODIFIER")
    
    
class SNA_OT_BTN_35165c1dc4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_35165c1dc4'
    bl_label = r"Push To Bottom"
    bl_description = r"Pushes the Bevel Modifier to the bottom of the modifier stack"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_c55a258b12('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_10d01b29f6(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_10d01b29f6'
    bl_label = r"Remove Bevel"
    bl_description = r"Removes Bevel"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.object.modifier_remove('INVOKE_DEFAULT', modifier=r"Kolup Ops Bevel", report=False)
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_4ccd1f07b1(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_4ccd1f07b1'
    bl_label = r"Add Bevel"
    bl_description = r"Adds Bevel"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_a8ed88c43c('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_f338244368(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_f338244368'
    bl_label = r"Remove Solidify"
    bl_description = r"Removes Solidify"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.object.modifier_remove('INVOKE_DEFAULT', modifier=r"Kolup Ops Solidify", report=False)
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_d4f137e128(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_d4f137e128'
    bl_label = r"Add Solidify"
    bl_description = r"Adds Solidify"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_a0d60c05e4('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_MT_4b8066c5e7(bpy.types.Menu):
    bl_label = "Utilities"
    bl_idname = "SNA_MT_4b8066c5e7"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.prop(bpy.context.active_object, 'show_wire', toggle=True, emboss=True, text=r"Toggle Wireframe")
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Bevel"], 'show_viewport', toggle=True, emboss=True, text=r"Toggle Bevel")
    
    
def register_keymap_74beacf7b9():
    global addon_keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    
    kmi = km.keymap_items.new(idname="scripting_nodes.sna_ot_operator_cf12fd245a",type="Q",value="PRESS",shift=True,ctrl=False,alt=False,any=False,repeat=False)
    addon_keymaps.append((km, kmi))
    
def register_keymap_e33311bc2a():
    global addon_keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    
    kmi = km.keymap_items.new(idname="wm.call_menu",type="Q",value="RELEASE",shift=True,ctrl=False,alt=False,any=False,repeat=False)
    kmi.properties.name = "SNA_MT_fe85d3d0af"
    addon_keymaps.append((km, kmi))
    
class SNA_MT_fe85d3d0af(bpy.types.Menu):
    bl_label = "Kolup Ops"
    bl_idname = "SNA_MT_fe85d3d0af"
    
    @classmethod
    def poll(cls, context):
        return bool(bpy.context.active_object)
    
    def draw(self, context):
        layout = self.layout
        if len(bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array) == 0:
            pass
            layout.label(text=r"Standard Tools", icon="TOOL_SETTINGS")
            if bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.has_solidify:
                pass
                layout.operator("scripting_nodes.sna_ot_btn_f338244368",text=r"Remove Solidify",emboss=True,depress=True,icon="X")
                layout.menu("SNA_MT_21f45cbf38",text=r"Solidify Options",icon="PLAY")
                layout.separator(factor=1.0)
            else:
                pass
                layout.operator("scripting_nodes.sna_ot_btn_d4f137e128",text=r"Add Solidify",emboss=True,depress=True,icon="MOD_SOLIDIFY")
            if bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.has_bevel:
                pass
                layout.operator("scripting_nodes.sna_ot_btn_10d01b29f6",text=r"Remove Bevel",emboss=True,depress=False,icon="X")
                layout.menu("SNA_MT_dec1fac416",text=r"Bevel Options",icon="PLAY")
                layout.separator(factor=1.0)
            else:
                pass
                layout.operator("scripting_nodes.sna_ot_btn_4ccd1f07b1",text=r"Add Bevel",emboss=True,depress=True,icon="MOD_BEVEL")
            if bpy.data.meshes[bpy.context.active_object.data.name].use_auto_smooth:
                pass
                layout.prop(bpy.data.meshes[bpy.context.active_object.data.name], 'use_auto_smooth', toggle=True, emboss=True, text=r"Auto Smooth", icon="OUTLINER_OB_LIGHT")
                layout.prop(bpy.data.meshes[bpy.context.active_object.data.name], 'auto_smooth_angle', emboss=True, text=r"Auto Smooth Angle", slider=False)
            else:
                pass
                layout.prop(bpy.data.meshes[bpy.context.active_object.data.name], 'use_auto_smooth', toggle=True, emboss=True, text=r"Auto Smooth", icon="LIGHT_DATA")
            layout.separator(factor=1.0)
            layout.menu("SNA_MT_4b8066c5e7",text=r"Utilities",icon="HIDE_OFF")
        else:
            pass
            layout.label(text=r"Multi-Object Tools", icon="MOD_OPACITY")
            layout.menu("SNA_MT_7d272e059f",text=r"Booleans",icon="MOD_BOOLEAN")
    
    
class SNA_OT_BTN_df1a56d376(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_df1a56d376'
    bl_label = r"Difference Boolean"
    bl_description = r""
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.boolean_type = r"Difference"
            bpy.ops.scripting_nodes.sna_ot_operator_a6232a1f24('EXEC_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_a140a90c88(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_a140a90c88'
    bl_label = r"Union Boolean"
    bl_description = r""
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.boolean_type = r"Union"
            bpy.ops.scripting_nodes.sna_ot_operator_a6232a1f24('EXEC_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7120938023(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7120938023'
    bl_label = r"Intersect Boolean"
    bl_description = r""
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.boolean_type = r"Intersect"
            bpy.ops.scripting_nodes.sna_ot_operator_a6232a1f24('EXEC_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_MT_7d272e059f(bpy.types.Menu):
    bl_label = "Booleans"
    bl_idname = "SNA_MT_7d272e059f"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_df1a56d376",text=r"Difference Boolean",emboss=True,depress=True,icon="SELECT_SUBTRACT")
        layout.operator("scripting_nodes.sna_ot_btn_a140a90c88",text=r"Union Boolean",emboss=True,depress=True,icon="SELECT_EXTEND")
        layout.operator("scripting_nodes.sna_ot_btn_7120938023",text=r"Intersect Boolean",emboss=True,depress=True,icon="SELECT_INTERSECT")
        layout.operator("scripting_nodes.sna_ot_btn_d758b588e9",text=r"Slice Boolean",emboss=True,depress=True,icon="SELECT_DIFFERENCE")
    
    
class SNA_OT_Operator_d786ee5000(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_d786ee5000"
    bl_label = "Update Selected Inactive"
    bl_description = "My Operators description"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array.clear()
            for_execute_node_5 = 0
            for_execute_node_index_5 = 0
            for for_execute_node_index_5, for_execute_node_5 in enumerate(bpy.context.scene.objects):
                pass
                if for_execute_node_5.select_get() and (for_execute_node_5.name!=bpy.context.active_object.name):
                    pass
                    bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array.add().string = for_execute_node_5.name
                    bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array.move(len(bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array)-1, 0)
                    
                else:
                    pass
                    
                
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_BTN_d758b588e9(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_d758b588e9'
    bl_label = r"Slice Boolean"
    bl_description = r""
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_ee8a4054e2('EXEC_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_Operator_a6232a1f24(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_a6232a1f24"
    bl_label = "Add Standard Boolean"
    bl_description = "Adds one of the standard boolean operations"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_d786ee5000('EXEC_DEFAULT')
            repeat_execute_node_1 = 0
            for repeat_execute_node_1 in range(len(bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array)):
                pass
                bpy.ops.object.modifier_add('INVOKE_DEFAULT', type='BOOLEAN')
                bpy.context.active_object.modifiers[-1].name = r"Kolup Ops Boolean - " + bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array[repeat_execute_node_1].string
                bpy.context.active_object.modifiers[-1].object = bpy.context.scene.objects[bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array[repeat_execute_node_1].string]
                bpy.context.active_object.modifiers[-1].operation = get_enum_identifier(bpy.context.active_object.modifiers[-1].bl_rna.properties['operation'].enum_items, bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.boolean_type)
                bpy.context.scene.objects[bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array[repeat_execute_node_1].string].display_type = get_enum_identifier(bpy.context.scene.objects[bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array[repeat_execute_node_1].string].bl_rna.properties['display_type'].enum_items, r"Wire")
                bpy.context.scene.objects[bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array[repeat_execute_node_1].string].parent = bpy.context.active_object
                bpy.data.meshes[bpy.context.scene.objects[bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.selected_inactive_array[repeat_execute_node_1].string].data.name].use_auto_smooth = True
                bpy.ops.scripting_nodes.sna_ot_operator_c55a258b12('EXEC_DEFAULT')
                
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_Operator_ee8a4054e2(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_ee8a4054e2"
    bl_label = "Add Slice Boolean"
    bl_description = "Adds a custom Slice Boolean"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            pass
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_Operator_c55a258b12(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_c55a258b12"
    bl_label = "Push Bevel to Bottom"
    bl_description = "My Operators description"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            if (len(bpy.context.active_object.modifiers)>0) and bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.has_bevel:
                pass
                
            else:
                pass
                
            bpy.ops.object.modifier_move_to_index('INVOKE_DEFAULT', modifier=r"Kolup Ops Bevel", index=int((float(len(bpy.context.active_object.modifiers))-1.0)))
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_Operator_cf12fd245a(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_cf12fd245a"
    bl_label = "Update Properties for Active Object"
    bl_description = "My Operators description"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return bool(bpy.context.active_object)
        
    def execute(self, context):
        try:
            pass
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index = 0
            for_execute_node_3 = 0
            for_execute_node_index_3 = 0
            for for_execute_node_index_3, for_execute_node_3 in enumerate(bpy.context.active_object.modifiers):
                pass
                if (for_execute_node_3.name==r"Kolup Ops Bevel"):
                    pass
                    bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index = int((float(bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index)+1.0))
                    
                else:
                    pass
                    
                
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.has_bevel = (bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index>0)
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index = 0
            for_execute_node_4 = 0
            for_execute_node_index_4 = 0
            for for_execute_node_index_4, for_execute_node_4 in enumerate(bpy.context.active_object.modifiers):
                pass
                if (for_execute_node_4.name==r"Kolup Ops Solidify"):
                    pass
                    bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index = int((float(bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index)+1.0))
                    
                else:
                    pass
                    
                
            bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.has_solidify = (bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.index>0)
            bpy.ops.scripting_nodes.sna_ot_operator_d786ee5000('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROPERTIES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Store the addons variables
class GeneratedAddonProperties_UID_Yzrkrwfk(bpy.types.PropertyGroup):
    set_default: bpy.props.BoolProperty(default=True)
    def update_boolean_type(self, context):
        pass
    def update_index(self, context):
        pass
    def update_has_bevel(self, context):
        pass
    def update_has_solidify(self, context):
        pass

    boolean_type: bpy.props.StringProperty(name='boolean_type', description='', default='', subtype='NONE', update=update_boolean_type)
    selected_inactive_array: bpy.props.CollectionProperty(type=ArrayCollection_UID_Yzrkrwfk)
    index: bpy.props.IntProperty(name='index', description='', default=0, subtype='NONE', update=update_index)
    has_bevel: bpy.props.BoolProperty(name='has_bevel', description='', default=False, update=update_has_bevel)
    has_solidify: bpy.props.BoolProperty(name='has_solidify', description='', default=False, update=update_has_solidify)

# Check and set if the variable default values
@persistent
def check_variables(dummy):
    if bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.set_default:
        bpy.context.scene.sn_generated_addon_properties_UID_Yzrkrwfk.set_default = False
        set_variables()

# Set the addons array variables
def set_variables():
    pass





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# REGISTER / UNREGISTER
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def register():
    # Register variables
    bpy.utils.register_class(ArrayCollection_UID_Yzrkrwfk)
    bpy.utils.register_class(GeneratedAddonProperties_UID_Yzrkrwfk)
    bpy.types.Scene.sn_generated_addon_properties_UID_Yzrkrwfk = bpy.props.PointerProperty(type=GeneratedAddonProperties_UID_Yzrkrwfk)
    bpy.app.handlers.load_post.append(check_variables)

    bpy.utils.register_class(SNA_OT_Operator_a0d60c05e4)
    bpy.utils.register_class(SNA_MT_21f45cbf38)
    bpy.utils.register_class(SNA_OT_Operator_a8ed88c43c)
    bpy.utils.register_class(SNA_MT_dec1fac416)
    bpy.utils.register_class(SNA_OT_BTN_35165c1dc4)
    bpy.utils.register_class(SNA_OT_BTN_10d01b29f6)
    bpy.utils.register_class(SNA_OT_BTN_4ccd1f07b1)
    bpy.utils.register_class(SNA_OT_BTN_f338244368)
    bpy.utils.register_class(SNA_OT_BTN_d4f137e128)
    bpy.utils.register_class(SNA_MT_4b8066c5e7)
    register_keymap_74beacf7b9()
    register_keymap_e33311bc2a()
    bpy.utils.register_class(SNA_MT_fe85d3d0af)
    bpy.utils.register_class(SNA_OT_BTN_df1a56d376)
    bpy.utils.register_class(SNA_OT_BTN_a140a90c88)
    bpy.utils.register_class(SNA_OT_BTN_7120938023)
    bpy.utils.register_class(SNA_MT_7d272e059f)
    bpy.utils.register_class(SNA_OT_Operator_d786ee5000)
    bpy.utils.register_class(SNA_OT_BTN_d758b588e9)
    bpy.utils.register_class(SNA_OT_Operator_a6232a1f24)
    bpy.utils.register_class(SNA_OT_Operator_ee8a4054e2)
    bpy.utils.register_class(SNA_OT_Operator_c55a258b12)
    bpy.utils.register_class(SNA_OT_Operator_cf12fd245a)

def unregister():
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # Unregister variables
    bpy.utils.unregister_class(ArrayCollection_UID_Yzrkrwfk)
    bpy.utils.unregister_class(GeneratedAddonProperties_UID_Yzrkrwfk)
    del bpy.types.Scene.sn_generated_addon_properties_UID_Yzrkrwfk
    bpy.app.handlers.load_post.remove(check_variables)

    bpy.utils.unregister_class(SNA_OT_Operator_a0d60c05e4)
    bpy.utils.unregister_class(SNA_MT_21f45cbf38)
    bpy.utils.unregister_class(SNA_OT_Operator_a8ed88c43c)
    bpy.utils.unregister_class(SNA_MT_dec1fac416)
    bpy.utils.unregister_class(SNA_OT_BTN_35165c1dc4)
    bpy.utils.unregister_class(SNA_OT_BTN_10d01b29f6)
    bpy.utils.unregister_class(SNA_OT_BTN_4ccd1f07b1)
    bpy.utils.unregister_class(SNA_OT_BTN_f338244368)
    bpy.utils.unregister_class(SNA_OT_BTN_d4f137e128)
    bpy.utils.unregister_class(SNA_MT_4b8066c5e7)
    bpy.utils.unregister_class(SNA_MT_fe85d3d0af)
    bpy.utils.unregister_class(SNA_OT_BTN_df1a56d376)
    bpy.utils.unregister_class(SNA_OT_BTN_a140a90c88)
    bpy.utils.unregister_class(SNA_OT_BTN_7120938023)
    bpy.utils.unregister_class(SNA_MT_7d272e059f)
    bpy.utils.unregister_class(SNA_OT_Operator_d786ee5000)
    bpy.utils.unregister_class(SNA_OT_BTN_d758b588e9)
    bpy.utils.unregister_class(SNA_OT_Operator_a6232a1f24)
    bpy.utils.unregister_class(SNA_OT_Operator_ee8a4054e2)
    bpy.utils.unregister_class(SNA_OT_Operator_c55a258b12)
    bpy.utils.unregister_class(SNA_OT_Operator_cf12fd245a)