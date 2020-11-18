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
    "version": (1,1,0)
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
class ArrayCollection_UID_Jxinghfv(bpy.types.PropertyGroup):
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
class SNA_OT_Operator_98c4d27eee(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_98c4d27eee"
    bl_label = "Change Solidify Thickness"
    bl_description = "My Operators description"
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
        layout.prop(bpy.context.active_object.modifiers[r"Kolup Ops Solidify"], 'thickness', emboss=True, text=r"Thickness", slider=True)
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=250)
        
    
    
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
    
    
def register_keymap_e33311bc2a():
    global addon_keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    
    kmi = km.keymap_items.new(idname="wm.call_menu",type="Q",value="PRESS",shift=True,ctrl=False,alt=False,any=False,repeat=False)
    kmi.properties.name = "SNA_MT_fe85d3d0af"
    addon_keymaps.append((km, kmi))
    
class SNA_OT_Operator_d8be4ac788(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_d8be4ac788"
    bl_label = "Toggle Bevel"
    bl_description = "Adds or Removes Bevel"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index = 0
            for_execute_node_1 = 0
            for_execute_node_index_1 = 0
            for for_execute_node_index_1, for_execute_node_1 in enumerate(bpy.context.active_object.modifiers):
                pass
                if (for_execute_node_1.name==r"Kolup Ops Bevel"):
                    pass
                    bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index = int((float(bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index)+1.0))
                    
                else:
                    pass
                    
                
            if (bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index>0):
                pass
                bpy.ops.scripting_nodes.sna_ot_operator_dcb31ad3d8('INVOKE_DEFAULT')
                
            else:
                pass
                bpy.ops.scripting_nodes.sna_ot_operator_a8ed88c43c('INVOKE_DEFAULT')
                
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_Operator_dcb31ad3d8(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_dcb31ad3d8"
    bl_label = "Remove Bevel"
    bl_description = "Removes the Kolup Ops Bevel"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.ops.object.modifier_remove('INVOKE_DEFAULT', modifier=r"Kolup Ops Bevel", report=False)
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
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
            bpy.context.active_object.modifiers[int((float(len(bpy.context.active_object.modifiers))-1.0))].name = r"Kolup Ops Solidify"
            bpy.ops.scripting_nodes.sna_ot_operator_98c4d27eee('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_Operator_1c2a223581(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_1c2a223581"
    bl_label = "Toggle Solidify"
    bl_description = "My Operators description"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index = 0
            for_execute_node_2 = 0
            for_execute_node_index_2 = 0
            for for_execute_node_index_2, for_execute_node_2 in enumerate(bpy.context.active_object.modifiers):
                pass
                if (for_execute_node_2.name==r"Kolup Ops Solidify"):
                    pass
                    bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index = int((float(bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index)+1.0))
                    
                else:
                    pass
                    
                
            if (bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.index>0):
                pass
                bpy.ops.scripting_nodes.sna_ot_operator_7f0b63b3eb('INVOKE_DEFAULT')
                
            else:
                pass
                bpy.ops.scripting_nodes.sna_ot_operator_a0d60c05e4('INVOKE_DEFAULT')
                
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_Operator_7f0b63b3eb(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_7f0b63b3eb"
    bl_label = "Remove Solidify"
    bl_description = "Removes the Kolup Ops Solidify Modifier"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.ops.object.modifier_remove('INVOKE_DEFAULT', modifier=r"Kolup Ops Solidify", report=False)
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
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
            bpy.context.active_object.modifiers[int((float(len(bpy.context.active_object.modifiers))-1.0))].name = r"Kolup Ops Bevel"
            bpy.context.active_object.modifiers[int((float(len(bpy.context.active_object.modifiers))-1.0))].harden_normals = True
            bpy.context.active_object.modifiers[int((float(len(bpy.context.active_object.modifiers))-1.0))].miter_outer = get_enum_identifier(bpy.context.active_object.modifiers[int((float(len(bpy.context.active_object.modifiers))-1.0))].bl_rna.properties['miter_outer'].enum_items, r"Arc")
            bpy.context.active_object.modifiers[int((float(len(bpy.context.active_object.modifiers))-1.0))].limit_method = get_enum_identifier(bpy.context.active_object.modifiers[int((float(len(bpy.context.active_object.modifiers))-1.0))].bl_rna.properties['limit_method'].enum_items, r"Angle")
            bpy.data.meshes[bpy.context.active_object.data.name].use_auto_smooth = True
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_OT_BTN_f338244368(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_f338244368'
    bl_label = r"Add/Remove Solidify"
    bl_description = r"Adds / Removes Solidify"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_1c2a223581('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
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
            if (len(bpy.context.active_object.modifiers)>0):
                pass
                bpy.ops.object.modifier_move_to_index('INVOKE_DEFAULT', modifier=r"Kolup Ops Bevel", index=int((float(len(bpy.context.active_object.modifiers))-1.0)))
                
            else:
                pass
                
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
class SNA_MT_fe85d3d0af(bpy.types.Menu):
    bl_label = "Kolup Ops"
    bl_idname = "SNA_MT_fe85d3d0af"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_f338244368",text=r"Add/Remove Solidify",emboss=True,depress=True,icon="MOD_SOLIDIFY")
        layout.menu("SNA_MT_21f45cbf38",text=r"Solidify Options",icon="PLAY")
        layout.separator(factor=1.0)
        layout.operator("scripting_nodes.sna_ot_btn_10d01b29f6",text=r"Add/Remove Bevel",emboss=True,depress=False,icon="MOD_BEVEL")
        layout.menu("SNA_MT_dec1fac416",text=r"Bevel Options",icon="PLAY")
        layout.separator(factor=1.0)
        if bpy.data.meshes[bpy.context.active_object.data.name].use_auto_smooth:
            pass
            layout.prop(bpy.data.meshes[bpy.context.active_object.data.name], 'use_auto_smooth', toggle=True, emboss=True, text=r"Auto Smooth", icon="OUTLINER_OB_LIGHT")
            layout.prop(bpy.data.meshes[bpy.context.active_object.data.name], 'auto_smooth_angle', emboss=True, text=r"Auto Smooth Angle", slider=False)
        else:
            pass
            layout.prop(bpy.data.meshes[bpy.context.active_object.data.name], 'use_auto_smooth', toggle=True, emboss=True, text=r"Auto Smooth", icon="LIGHT_DATA")
        layout.separator(factor=1.0)
        layout.menu("SNA_MT_4b8066c5e7",text=r"Utilities",icon="HIDE_OFF")
    
    
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
    
    
class SNA_OT_BTN_10d01b29f6(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_10d01b29f6'
    bl_label = r"Add/Remove Bevel"
    bl_description = r"Adds / Removes Bevel"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_d8be4ac788('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROPERTIES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Store the addons variables
class GeneratedAddonProperties_UID_Jxinghfv(bpy.types.PropertyGroup):
    set_default: bpy.props.BoolProperty(default=True)
    def update_index(self, context):
        pass

    index: bpy.props.IntProperty(name='index', description='', default=0, subtype='NONE', update=update_index)

# Check and set if the variable default values
@persistent
def check_variables(dummy):
    if bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.set_default:
        bpy.context.scene.sn_generated_addon_properties_UID_Jxinghfv.set_default = False
        set_variables()

# Set the addons array variables
def set_variables():
    pass





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# REGISTER / UNREGISTER
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def register():
    # Register variables
    bpy.utils.register_class(ArrayCollection_UID_Jxinghfv)
    bpy.utils.register_class(GeneratedAddonProperties_UID_Jxinghfv)
    bpy.types.Scene.sn_generated_addon_properties_UID_Jxinghfv = bpy.props.PointerProperty(type=GeneratedAddonProperties_UID_Jxinghfv)
    bpy.app.handlers.load_post.append(check_variables)

    bpy.utils.register_class(SNA_OT_Operator_98c4d27eee)
    bpy.utils.register_class(SNA_MT_21f45cbf38)
    register_keymap_e33311bc2a()
    bpy.utils.register_class(SNA_OT_Operator_d8be4ac788)
    bpy.utils.register_class(SNA_OT_Operator_dcb31ad3d8)
    bpy.utils.register_class(SNA_OT_Operator_a0d60c05e4)
    bpy.utils.register_class(SNA_OT_Operator_1c2a223581)
    bpy.utils.register_class(SNA_OT_Operator_7f0b63b3eb)
    bpy.utils.register_class(SNA_OT_Operator_a8ed88c43c)
    bpy.utils.register_class(SNA_OT_BTN_f338244368)
    bpy.utils.register_class(SNA_MT_dec1fac416)
    bpy.utils.register_class(SNA_OT_BTN_35165c1dc4)
    bpy.utils.register_class(SNA_OT_Operator_c55a258b12)
    bpy.utils.register_class(SNA_MT_fe85d3d0af)
    bpy.utils.register_class(SNA_MT_4b8066c5e7)
    bpy.utils.register_class(SNA_OT_BTN_10d01b29f6)

def unregister():
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # Unregister variables
    bpy.utils.unregister_class(ArrayCollection_UID_Jxinghfv)
    bpy.utils.unregister_class(GeneratedAddonProperties_UID_Jxinghfv)
    del bpy.types.Scene.sn_generated_addon_properties_UID_Jxinghfv
    bpy.app.handlers.load_post.remove(check_variables)

    bpy.utils.unregister_class(SNA_OT_Operator_98c4d27eee)
    bpy.utils.unregister_class(SNA_MT_21f45cbf38)
    bpy.utils.unregister_class(SNA_OT_Operator_d8be4ac788)
    bpy.utils.unregister_class(SNA_OT_Operator_dcb31ad3d8)
    bpy.utils.unregister_class(SNA_OT_Operator_a0d60c05e4)
    bpy.utils.unregister_class(SNA_OT_Operator_1c2a223581)
    bpy.utils.unregister_class(SNA_OT_Operator_7f0b63b3eb)
    bpy.utils.unregister_class(SNA_OT_Operator_a8ed88c43c)
    bpy.utils.unregister_class(SNA_OT_BTN_f338244368)
    bpy.utils.unregister_class(SNA_MT_dec1fac416)
    bpy.utils.unregister_class(SNA_OT_BTN_35165c1dc4)
    bpy.utils.unregister_class(SNA_OT_Operator_c55a258b12)
    bpy.utils.unregister_class(SNA_MT_fe85d3d0af)
    bpy.utils.unregister_class(SNA_MT_4b8066c5e7)
    bpy.utils.unregister_class(SNA_OT_BTN_10d01b29f6)