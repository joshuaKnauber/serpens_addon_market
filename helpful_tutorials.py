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
sn_tree_name = "NodeTree"
addon_keymaps = []

bl_info = {
    "name": "Helpful Tutorials",
    "author": "Takeshi_Tenma",
    "description": "This add on adds a dropdown in the 3d viewport that contains hyperlinks to several tutorials on youtube based on category as well as some extra's",
    "location": "VIEW3D_HD_header, Scene tab in properties",
    "doc_url": "",
    "warning": "This is not meant to be a tutorial in itself but a hub for several tutorials i think are useful to see especially for beginners. By no means though is this meant to replace going out and searching for the information yourself.",
    "category": "Links",
    "blender": (2,90,1),
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

def report_sn_error(error):
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


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CODE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class SNA_MT_58efd74310(bpy.types.Menu):
    bl_label = "Nodes"
    bl_idname = "SNA_MT_58efd74310"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_6424bd4090",text=r"Blender Shader Nodes For Beginners",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_ccb7872885",text=r"Nodes 4 Noobs",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_1cf089cc35",text=r"Blender 2.8 PBR Texturing for Beginners",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_fa8f12d666",text=r"Blender | What is the Node Editor?",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_9d189649aa",text=r"beginners guide to nodes in blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_5d69c1cd01",text=r"Intro to Shading - Blender 2.80 Fundamentals",emboss=True,depress=False)
        column = layout.column(align=True)
        column.enabled = True
        column.alert = False
        column.scale_x = 1.0
        column.scale_y = 1.0
        column.menu("SNA_MT_1f1ea40f22",text=r"Texturing",icon="TEXTURE")
        column.menu("SNA_MT_25f86f7073",text=r"Materials",icon="NODE_MATERIAL")
        column.menu("SNA_MT_8d1b506450",text=r"Compositing",icon="NODE_COMPOSITING")
    
    
class SNA_OT_BTN_5d69c1cd01(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_5d69c1cd01'
    bl_label = r"Intro to Shading - Blender 2.80 Fundamentals"
    bl_description = r"Blender Nodes tutorial by Blender"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=RRilLLyyn1Y")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_9d189649aa(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_9d189649aa'
    bl_label = r"beginners guide to nodes in blender"
    bl_description = r"Blender Nodes tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ETMoOhAgXiY&list=PLn3ukorJv4vsmEcCMDX-dpBceuv_GJFcB")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_1cf089cc35(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_1cf089cc35'
    bl_label = r"Blender 2.8 PBR Texturing for Beginners"
    bl_description = r"Blender Nodes tutorial by Jayanam"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=XI-pZshRp8g")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_ccb7872885(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ccb7872885'
    bl_label = r"Nodes 4 Noobs"
    bl_description = r"Blender Nodes tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=moKFSMJwpmE&list=PLn3ukorJv4vtnU_TaZob7QD6Q8d9C9Ki7")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_fa8f12d666(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_fa8f12d666'
    bl_label = r"Blender | What is the Node Editor?"
    bl_description = r"Blender Nodes tutorial by Rory Allen"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=5TcBWJva9aE")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_6424bd4090(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_6424bd4090'
    bl_label = r"Blender Shader Nodes For Beginners"
    bl_description = r"Blender Nodes tutorial by CGMatter"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=BNn0bk77XNQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_e701734fe7(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_e701734fe7'
    bl_label = r"3D Modeling a Sword for Complete Beginners"
    bl_description = r"Blender beginner tutorial by YanSculpt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=jBqYTgaFDxU&list=PLvPwLecDlWRD_VK_2INC1VQ18dZdpDwLi")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_07b66b8200(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_07b66b8200'
    bl_label = r"How to Model Anything in 3D - Modeling Fundamentals"
    bl_description = r"Modelling fundamentals by Flipped Normals"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=tTfIo_bezqw")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_9768ad084b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_9768ad084b'
    bl_label = r"Blender 2.8 Modeling Beginner Tutorial"
    bl_description = r"Blender beginner tutorial by Jayanam"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=RWhZQ-IaetU")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7b92864909(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7b92864909'
    bl_label = r"Create A Low Poly Well | Beginners Tutorial | Blender 2.8 | Easy"
    bl_description = r"Blender beginner tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=OlnkGCdtGEw")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_3fe0e15768(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_3fe0e15768'
    bl_label = r"Getting Started Modeling in BlenderGetting Started Modeling in Blender"
    bl_description = r"Blender beginner tutorial by The CG Essentials"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=x_Evla8aKAQ&list=PL0LADxPpmXN7xXkosUQM5zMq-R5Sm8GgU")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_af173989e0(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_af173989e0'
    bl_label = r"Beginner Modelling Chair Tutorial"
    bl_description = r"Blender beginner tutorial by Blender Guru"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Hf2esGA7vCc&list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_ada7bd35cc(bpy.types.Menu):
    bl_label = "Modelling"
    bl_idname = "SNA_MT_ada7bd35cc"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_af173989e0",text=r"Beginner Modelling Chair Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_e701734fe7",text=r"3D Modeling a Sword for Complete Beginners",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_07b66b8200",text=r"How to Model Anything in 3D - Modeling Fundamentals",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_9768ad084b",text=r"Blender 2.8 Modeling Beginner Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7b92864909",text=r"Create A Low Poly Well | Beginners Tutorial | Blender 2.8 | Easy",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_3fe0e15768",text=r"Getting Started Modeling in BlenderGetting Started Modeling in Blender",emboss=True,depress=False)
        layout.menu("SNA_MT_a67b6fd600",text=r"UV Map",icon="UV")
        layout.menu("SNA_MT_1f1ea40f22",text=r"Texturing",icon="TEXTURE")
    
    
class SNA_OT_BTN_70d51f3bb0(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_70d51f3bb0'
    bl_label = r"'Blender Beginner Tutorial series'"
    bl_description = r"Blender beginner tutorial by Blender Guru"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=NyJWoyVx_XI&list=PLjEaoINr3zgEq0u2MzVgAaHEBt--xLB6U")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_054d6eeaa2(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_054d6eeaa2'
    bl_label = r"'Blender 2.8 Complete Beginner Tutorial Course'"
    bl_description = r"Blender beginner tutorial by CG Geek"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ppASl6yaguU&list=PLrjIgEdKLivgpCMmFC0_sV60Y_Ftp-WLD")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_331efe1e71(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_331efe1e71'
    bl_label = r"'Blender 2.8 for beginners full course'"
    bl_description = r"Blender beginner tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=7MRonzqYJgw&list=PLn3ukorJv4vs_eSJUQPxBRaDS8PrVmIri")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_9e2ba6ff8d(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_9e2ba6ff8d'
    bl_label = r"'Blender 2.9 Beginner Tutorial Series'"
    bl_description = r"Blender beginner tutorial by CG Fast Track"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=bpvh-9H8S1g&list=PL8eKBkZzqDiU-qcoaghCz04sMitC1yx6k")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_8300fea05b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_8300fea05b'
    bl_label = r"'Blender 2.8 Beginner Tutorial Series'"
    bl_description = r"Blender beginner tutorial by CGBoost"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=j14b25SnYRY&list=PL3UWN2F2M2C8-zUjbFlbgtWPQa0NXBsp0")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_936cb33337(bpy.types.Menu):
    bl_label = "General"
    bl_idname = "SNA_MT_936cb33337"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_70d51f3bb0",text=r"'Blender Beginner Tutorial series'",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_054d6eeaa2",text=r"'Blender 2.8 Complete Beginner Tutorial Course'",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_331efe1e71",text=r"'Blender 2.8 for beginners full course'",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_9e2ba6ff8d",text=r"'Blender 2.9 Beginner Tutorial Series'",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_8300fea05b",text=r"'Blender 2.8 Beginner Tutorial Series'",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_1ee62085e6",text=r"'First Steps - Blender 2.80 Fundamentals'",emboss=True,depress=False)
    
    
class SNA_OT_BTN_1ee62085e6(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_1ee62085e6'
    bl_label = r"'First Steps - Blender 2.80 Fundamentals'"
    bl_description = r"Blender beginner tutorial by Blender"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=MF1qEhBSfq4&list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_c543a20639(bpy.types.Menu):
    bl_label = "Sculpting"
    bl_idname = "SNA_MT_c543a20639"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_f34bf1a3f1",text=r"Sculpting In Blender For Beginners - Tutorial Course",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_52a41e63ac",text=r"Blender - Sculpting Tutorials, Tips and Tricks",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_f913340d71",text=r"learn sculpting in blender 2.8",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_3df3be261c",text=r"Introduction to Sculpting in Blender 2.8 - Sculpting Essentials",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_66d89bf833",text=r"Sculpting in Blender 2.8 for Beginners",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_781b461ec9",text=r"Base Mesh Sculpting Tutorial in Blender 2.8 | Stylized | 1/2",emboss=True,depress=False)
        layout.menu("SNA_MT_b65df0d4f0",text=r"Retopology",icon="MESH_PLANE")
        layout.menu("SNA_MT_a67b6fd600",text=r"UV Map",icon="UV")
        layout.menu("SNA_MT_1f1ea40f22",text=r"Texturing",icon="TEXTURE")
    
    
class SNA_OT_BTN_52a41e63ac(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_52a41e63ac'
    bl_label = r"Blender - Sculpting Tutorials, Tips and Tricks"
    bl_description = r"Blender sculpting tutorial by YansSculpt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=wOjPUiDIAG8&list=PLvPwLecDlWRCdNEaf4WKmwpunv9EXSDIz")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_66d89bf833(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_66d89bf833'
    bl_label = r"Sculpting in Blender 2.8 for Beginners"
    bl_description = r"Blender sculpting tutorial by VeryHotShark"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=fnsJyTLdy3o&list=PLG5Njy_Tug4XN_Urdn64qkZ1HhAXBgSEj")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_f34bf1a3f1(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_f34bf1a3f1'
    bl_label = r"Sculpting In Blender For Beginners - Tutorial Course"
    bl_description = r"Blender sculpting tutorial by YansSculpt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=IG1IEpU5VAw&list=PLvPwLecDlWRCXSVh0nskG810BAerdz9DW")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_781b461ec9(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_781b461ec9'
    bl_label = r"Base Mesh Sculpting Tutorial in Blender 2.8 | Stylized | 1/2"
    bl_description = r"Blender sculpting tutorial by VeryHotShark"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=BJ6wUtR6cWo")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_f913340d71(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_f913340d71'
    bl_label = r"learn sculpting in blender 2.8"
    bl_description = r"Blender sculpting tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=lKY2FIy60nc&list=PLn3ukorJv4vvJM7tvjet4PP-LVjJx13oB")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_3df3be261c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_3df3be261c'
    bl_label = r"Introduction to Sculpting in Blender 2.8 - Sculpting Essentials"
    bl_description = r"Blender sculpting tutorial by Flipped Normals"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=A-Wq8K8icpQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_a67b6fd600(bpy.types.Menu):
    bl_label = "UV Map"
    bl_idname = "SNA_MT_a67b6fd600"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_a0f41e0584",text=r"UV Unwrapping - Blender 2.80 Fundamentals",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_82542b11c4",text=r"unwrapping in blender 2.8",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_828edf75d5",text=r"the complete guide to uv unwrapping in blender 2.8 step by steb beginner tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_83f1a6254f",text=r"Blender Intermediate UV Unwrapping Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_83ebbdc331",text=r"Blender 2.8 Unwrapping a Face Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_3398e99b37",text=r"Blender 2.8 Beginner Tutorial - Part 6: UV Unwrapping",emboss=True,depress=False)
    
    
class SNA_OT_BTN_3398e99b37(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_3398e99b37'
    bl_label = r"Blender 2.8 Beginner Tutorial - Part 6: UV Unwrapping"
    bl_description = r"UV map tutorial by CG Boost"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=xPoxqOcUzNQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_83ebbdc331(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_83ebbdc331'
    bl_label = r"Blender 2.8 Unwrapping a Face Tutorial"
    bl_description = r"UV map tutorial by VeryHotShark"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=iKpixDzilR4")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_83f1a6254f(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_83f1a6254f'
    bl_label = r"Blender Intermediate UV Unwrapping Tutorial"
    bl_description = r"UV map tutorial by Blender Guru"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=scPSP_U858k")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_82542b11c4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_82542b11c4'
    bl_label = r"unwrapping in blender 2.8"
    bl_description = r"UV map tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=bHLT5Xh_tzQ&list=PLn3ukorJv4vve0s-cq8VWS4jRQCdWSU3N")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_828edf75d5(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_828edf75d5'
    bl_label = r"the complete guide to uv unwrapping in blender 2.8 step by steb beginner tutorial"
    bl_description = r"UV map tutorial by BlenderMoney"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=KIzEkbNwd54")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_a0f41e0584(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_a0f41e0584'
    bl_label = r"UV Unwrapping - Blender 2.80 Fundamentals"
    bl_description = r"UV map tutorial by Blender"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Y7M-B6xnaEM")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_af9b1c9d99(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_af9b1c9d99'
    bl_label = r"Beginners Guide to Texturing 3D models"
    bl_description = r"Texturing tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=3g5YihV-fyA")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_1f1ea40f22(bpy.types.Menu):
    bl_label = "Texturing"
    bl_idname = "SNA_MT_1f1ea40f22"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_af9b1c9d99",text=r"Beginners Guide to Texturing 3D models",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_41ed7d8742",text=r"Blender 2.8 Beginner Texturing Painting Tutorial: Getting Started",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_3b1e6946f8",text=r"How To Setup PBR and Displacement in EEVEE AND Cycles [Blender 2.8]",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_10912391c0",text=r"Blender 2.8 Texturing Tutorials",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_eeecc0d2e1",text=r"Understanding Materials - Blender 2.8 Tutorial for Beginners (Eevee)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_ae329c47be",text=r"Texture Maps in Blender: How To",emboss=True,depress=False)
    
    
class SNA_OT_BTN_ae329c47be(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ae329c47be'
    bl_label = r"Texture Maps in Blender: How To"
    bl_description = r"Texturing tutorial by Derek Elliott"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=C7jACtwbApI")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_eeecc0d2e1(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_eeecc0d2e1'
    bl_label = r"Understanding Materials - Blender 2.8 Tutorial for Beginners (Eevee)"
    bl_description = r"Texturing tutorial by Chocofur"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=nBdGm_d_8XE&list=PLYVR0A4acpNYSCN-0f7f9TB8XgHKNmRhz")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_10912391c0(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_10912391c0'
    bl_label = r"Blender 2.8 Texturing Tutorials"
    bl_description = r"Texturing tutorial by Jayanam"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=mdcodiuIwXM&list=PLboXykqtm8dz857b3H0XqQTFDTWJKS_C5")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_3b1e6946f8(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_3b1e6946f8'
    bl_label = r"How To Setup PBR and Displacement in EEVEE AND Cycles [Blender 2.8]"
    bl_description = r"Texturing tutorial by BlenderBinge"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=UkU0-QeWUcU")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_41ed7d8742(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_41ed7d8742'
    bl_label = r"Blender 2.8 Beginner Texturing Painting Tutorial: Getting Started"
    bl_description = r"Texturing tutorial by SouthernShotty"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=vTYustK-XBk")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_b65df0d4f0(bpy.types.Menu):
    bl_label = "Retopology"
    bl_idname = "SNA_MT_b65df0d4f0"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_ef0d442ea4",text=r"learn retopology",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_585b5ee59b",text=r"How to Retopology a Face | Blender 2.8 Beginner Tutorial | Introduction",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_8c7d0accee",text=r"Blender 2.8 Retopology with Polybuild Tool",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_cc076d5ce9",text=r"Retopology Using New Polybuild Tool in Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_a5ef8716e4",text=r"Retopo in Blender - Retopologizing the Face",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_fdf10b8389",text=r"Retopology in Blender - Polybuild tool",emboss=True,depress=False)
    
    
class SNA_OT_BTN_fdf10b8389(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_fdf10b8389'
    bl_label = r"Retopology in Blender - Polybuild tool"
    bl_description = r"Retopology tutorial by Jamie Dunbar"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=l-sALvdn3FI")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_a5ef8716e4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_a5ef8716e4'
    bl_label = r"Retopo in Blender - Retopologizing the Face"
    bl_description = r"Retopology tutorial by Flipped Normals"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=OuFwUaS8y1I")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_cc076d5ce9(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_cc076d5ce9'
    bl_label = r"Retopology Using New Polybuild Tool in Blender"
    bl_description = r"Retopology tutorial by Flipped Normals"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=BEwEWKOH5ws")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_8c7d0accee(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_8c7d0accee'
    bl_label = r"Blender 2.8 Retopology with Polybuild Tool"
    bl_description = r"Retopology tutorial by Jayanam"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=U3sY3f6aKB8")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_585b5ee59b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_585b5ee59b'
    bl_label = r"How to Retopology a Face | Blender 2.8 Beginner Tutorial | Introduction"
    bl_description = r"Retopology tutorial by VeryHotShark"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=hWmb3Gn0xgA&list=PLG5Njy_Tug4VyJKWPB4dVs6AeT0mVwlvK")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_ef0d442ea4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ef0d442ea4'
    bl_label = r"learn retopology"
    bl_description = r"Retopology tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=6sE-p8PcHDo&list=PLn3ukorJv4vs8PQj8z_PMbZAVLFEhQF5L")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_a341274abf(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_a341274abf'
    bl_label = r"Advanced Materials in Blender 2.80 | Shader Editor Tutorial"
    bl_description = r"Material tutorial by Surface Studio"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=iVjnS5Z77Ww")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_25f86f7073(bpy.types.Menu):
    bl_label = "Materials"
    bl_idname = "SNA_MT_25f86f7073"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_92a0d3338c",text=r"6 Most BASIC Blender MATERIALS (Eevee and Cycles Tutorial)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_e539d4ccbd",text=r"Basic Metallic surface in Blender Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_94f18635a4",text=r"Blender 2.8 Beginner Tutorial - Part 8: Materials",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_f55b158822",text=r"Blender Beginner Modeling Chair Tutorial - Part 8: Texture Mapping",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_06e4b0b572",text=r"Blender - Abstract Text Design (Blender 2.8)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_a341274abf",text=r"Advanced Materials in Blender 2.80 | Shader Editor Tutorial",emboss=True,depress=False)
    
    
class SNA_OT_BTN_06e4b0b572(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_06e4b0b572'
    bl_label = r"Blender - Abstract Text Design (Blender 2.8)"
    bl_description = r"Material tutorial by Ducky 3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Gf4AWLPovB8&list=PLNShHVjao84dggD3JutR4kAfNZsNxRgzz")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_f55b158822(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_f55b158822'
    bl_label = r"Blender Beginner Modeling Chair Tutorial - Part 8: Texture Mapping"
    bl_description = r"Material tutorial by Blender Guru"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=zJ_AoS7wojk")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_94f18635a4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_94f18635a4'
    bl_label = r"Blender 2.8 Beginner Tutorial - Part 8: Materials"
    bl_description = r"Material tutorial by CGBoost"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=LpDbJduDibE")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_e539d4ccbd(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_e539d4ccbd'
    bl_label = r"Basic Metallic surface in Blender Tutorial"
    bl_description = r"Material tutorial by Steven Scott"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Mb-fTVMjCTI")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_92a0d3338c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_92a0d3338c'
    bl_label = r"6 Most BASIC Blender MATERIALS (Eevee and Cycles Tutorial)"
    bl_description = r"Material tutorial by Chocofur"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=CN9ggYpl9SU")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_8d1b506450(bpy.types.Menu):
    bl_label = "Compositing"
    bl_idname = "SNA_MT_8d1b506450"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_a25978a46a",text=r"How to use the Compositor in Blender 2.8 | Blender 2.81 Compositor for Post Processing",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_b82a8d3800",text=r"Introduction to Compositing in Blender 2.8",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7a1e59489c",text=r"Blender Tutorial: Compositing Techniques",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_6089952c99",text=r"How to composite renders in Blender 2.8+",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_e68862f916",text=r"Blender 2.8 Render Passes and VERY Basic Compositing [Old School but Beginner Friendly]",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7260d0ffd1",text=r"Blender Tutorial - 3D Compositing | How to Composite Your 3D Model on a Real Background",emboss=True,depress=False)
    
    
class SNA_OT_BTN_7260d0ffd1(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7260d0ffd1'
    bl_label = r"Blender Tutorial - 3D Compositing | How to Composite Your 3D Model on a Real Background"
    bl_description = r"Compositing tutorial by Aneesh Arts"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=OHhKbCE3aMI&t=504s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_e68862f916(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_e68862f916'
    bl_label = r"Blender 2.8 Render Passes and VERY Basic Compositing [Old School but Beginner Friendly]"
    bl_description = r"Compositing tutorial by BlenderBinge"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Sdaj9Y_1mOY")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_6089952c99(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_6089952c99'
    bl_label = r"How to composite renders in Blender 2.8+"
    bl_description = r"Compositing tutorial by Blender Brit"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Eka75kHHBrA")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7a1e59489c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7a1e59489c'
    bl_label = r"Blender Tutorial: Compositing Techniques"
    bl_description = r"Compositing tutorial by Amort Media"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=hprVvGtGqoY")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_b82a8d3800(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_b82a8d3800'
    bl_label = r"Introduction to Compositing in Blender 2.8"
    bl_description = r"Compositing tutorial by Flipped Normals"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=bF7RV1My41s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_a25978a46a(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_a25978a46a'
    bl_label = r"How to use the Compositor in Blender 2.8 | Blender 2.81 Compositor for Post Processing"
    bl_description = r"Compositing tutorial by RenderRides"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=W5KqXPCKBuI")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_be1d31e86a(bpy.types.Menu):
    bl_label = "Rigging"
    bl_idname = "SNA_MT_be1d31e86a"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_285c930f59",text=r"Blender 2.82 Speed Rigging Tutorials",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_5f1a08d39a",text=r"Blender 2.81 human meta rig",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_a76e73ebc3",text=r"Beginners Guide to Rigging",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_65e82f9343",text=r"Rigging Characters in Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7b1010cbe5",text=r"Rigify Tutorial Series",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7d27d1931a",text=r"Blender Basic Rigging Tutorial",emboss=True,depress=False)
        column = layout.column(align=False)
        column.enabled = True
        column.alert = False
        column.scale_x = 1.0
        column.scale_y = 1.0
        column.menu("SNA_MT_ea6e2df1f9",text=r"Weight Painting",icon="WPAINT_HLT")
        column.menu("SNA_MT_e4da156ce3",text=r"Animation",icon="ANIM")
        column.menu("SNA_MT_9f1460c853",text=r"Shapekeys",icon="SHAPEKEY_DATA")
        column.menu("SNA_MT_e225647cb7",text=r"Mechanical",icon="MODIFIER_DATA")
    
    
class SNA_OT_BTN_7d27d1931a(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7d27d1931a'
    bl_label = r"Blender Basic Rigging Tutorial"
    bl_description = r"Rigging tutorial by Markom3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=kxcOzTlBIsI")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7b1010cbe5(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7b1010cbe5'
    bl_label = r"Rigify Tutorial Series"
    bl_description = r"Rigging tutorial by CGDive"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=-JSFcSxsaTs&list=PLdcL5aF8ZcJv68SSdwxip33M7snakl6Dx")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_65e82f9343(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_65e82f9343'
    bl_label = r"Rigging Characters in Blender"
    bl_description = r"Rigging tutorial by Dikko"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=kkX50pkZT1s&list=PLL3OEv6vd5VA8_FBkeitaeqC0kbcrhMTC")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_a76e73ebc3(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_a76e73ebc3'
    bl_label = r"Beginners Guide to Rigging"
    bl_description = r"Rigging tutorial by Dikko"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=cxlPWv9giR4&list=PLL3OEv6vd5VCrqZiupP2m68qSWHYAjoiW")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_5f1a08d39a(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_5f1a08d39a'
    bl_label = r"Blender 2.81 human meta rig"
    bl_description = r"Rigging tutorial by PIXXO 3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=XHa2Y8zjtZQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_285c930f59(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_285c930f59'
    bl_label = r"Blender 2.82 Speed Rigging Tutorials"
    bl_description = r"Rigging tutorial by Royal Skies LLC"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=PFaqjwpGxOc&list=PLZpDYt0cyiusytIPAOTPRzsa4GK6LgY3_")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_ea6e2df1f9(bpy.types.Menu):
    bl_label = "Weight Painting"
    bl_idname = "SNA_MT_ea6e2df1f9"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_5299890bea",text=r"Blender [2.8/2.9] Character Weight Paint: #1 Vertex Groups (beginner tutorial)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_e1070147cc",text=r"Blender 2.82 : Weight Paint Introduction (Advice For Beginners)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_2e108ff0f4",text=r"weight painting/skinning | tutorial | Blender | Quick",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_62d9634c5f",text=r"Vertex Groups - Blender 2.80 Fundamentals",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_59b1c7c70c",text=r"Blender 2.8 Weight-Paint Transfer BEST Tutorial! [30 seconds]",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7d437a6321",text=r"The Basics of Weight Paint Mode (blender 2.8)",emboss=True,depress=False)
    
    
class SNA_OT_BTN_7d437a6321(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7d437a6321'
    bl_label = r"The Basics of Weight Paint Mode (blender 2.8)"
    bl_description = r"Weight painting tutorial by Ian Letarte"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=pMIwthFmr-Q")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_59b1c7c70c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_59b1c7c70c'
    bl_label = r"Blender 2.8 Weight-Paint Transfer BEST Tutorial! [30 seconds]"
    bl_description = r"Weight painting tutorial by Sayuri Artsy"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=iBLGKNRK4j4")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_62d9634c5f(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_62d9634c5f'
    bl_label = r"Vertex Groups - Blender 2.80 Fundamentals"
    bl_description = r"Weight painting tutorial by Blender"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=dKZrzG5r13g")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_2e108ff0f4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_2e108ff0f4'
    bl_label = r"weight painting/skinning | tutorial | Blender | Quick"
    bl_description = r"Weight painting tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Tl4qTgwQwYw")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_e1070147cc(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_e1070147cc'
    bl_label = r"Blender 2.82 : Weight Paint Introduction (Advice For Beginners)"
    bl_description = r"Weight painting tutorial by Royal Skies LLC"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=uWuE8Gnhuy4&list=PLZpDYt0cyiusytIPAOTPRzsa4GK6LgY3_&index=11")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_5299890bea(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_5299890bea'
    bl_label = r"Blender [2.8/2.9] Character Weight Paint: #1 Vertex Groups (beginner tutorial)"
    bl_description = r"Weight painting tutorial by CGDive"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=LPYs3pZEzPY&list=PLdcL5aF8ZcJsFEdlMJ7To0Iu9s-XCFV3W")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_b1561224a9(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_b1561224a9'
    bl_label = r"beginners guide to animation in 2.8"
    bl_description = r"Animation tutorial by Grant Abbitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=zp6kCe5Kmf4&list=PLn3ukorJv4vvHr6RMoXrZSMVqmOKlqbBR")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_8c598c42b5(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_8c598c42b5'
    bl_label = r"Blender 2.83 Speed Animating Tutorials"
    bl_description = r"Animation tutorial by Royal Skies LLC"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=fmFety2tSqI&list=PLZpDYt0cyiut1oZv6zyWgDnyBJu4U1jwJ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_31b8f36caf(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_31b8f36caf'
    bl_label = r"Blender 2.8 ANIMATION (Speed Tutorials)"
    bl_description = r"Animation tutorial by Royal Skies LLC"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=1l1LBCtyh-8&list=PLZpDYt0cyiuu7XqpZ8_rXJG9x26JK7UCr")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_1c4b4865fe(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_1c4b4865fe'
    bl_label = r"Become a PRO at Animation in 25 Minutes | Blender Tutorial"
    bl_description = r"Animation tutorial by CG Geek"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=_C2ClFO3FAY")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_caf450d917(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_caf450d917'
    bl_label = r"Introduction to Animation - Blender 2.8 Beginner Tutorial "
    bl_description = r"Animation tutorial by Chocofur"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=GGp4ytnxJJ0")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_ef5cf60f53(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ef5cf60f53'
    bl_label = r"ANIMATION For Absolute Beginners - Blender Tutorial"
    bl_description = r"Animation tutorial by Surface Studio"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=GM1Fc-NTDsg")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_e4da156ce3(bpy.types.Menu):
    bl_label = "Animation"
    bl_idname = "SNA_MT_e4da156ce3"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_b1561224a9",text=r"beginners guide to animation in 2.8",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_8c598c42b5",text=r"Blender 2.83 Speed Animating Tutorials",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_31b8f36caf",text=r"Blender 2.8 ANIMATION (Speed Tutorials)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_1c4b4865fe",text=r"Become a PRO at Animation in 25 Minutes | Blender Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_caf450d917",text=r"Introduction to Animation - Blender 2.8 Beginner Tutorial ",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_ef5cf60f53",text=r"ANIMATION For Absolute Beginners - Blender Tutorial",emboss=True,depress=False)
    
    
class SNA_OT_BTN_fb8d46d6e4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_fb8d46d6e4'
    bl_label = r"Blender 2.82 : Everything About Shape-Keys (In 2 Minutes!!!)"
    bl_description = r"Shapekey tutorial by Royal Skies LLC"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=CaHomz6gPWY&list=PLZpDYt0cyiusytIPAOTPRzsa4GK6LgY3_&index=23")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_4f4e1050cf(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_4f4e1050cf'
    bl_label = r"Corrective Shape Keys - Blender 2.8 Tutorial"
    bl_description = r"Shapekey tutorial by Danny Mac"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=1WmFaBlDBHs")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_6e901b0fa7(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_6e901b0fa7'
    bl_label = r"Blender 2.8 Character Animation: Shape Keys"
    bl_description = r"Shapekey tutorial by SouthernShotty"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=YDu6y_2jFg0")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_309bdc1249(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_309bdc1249'
    bl_label = r"Shape Keys Weight Paint Blender Tutorial"
    bl_description = r"Shapekey tutorial by Markom3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=GLeiWgr6jV4&t=11s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7f81ef39ee(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7f81ef39ee'
    bl_label = r"Creating an Advanced Face Rig Pt. 1 (Blender 2.6 Tutorial)"
    bl_description = r"Shapekey tutorial by CG Cookie (Old but gold)"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=waFkCM0yaD4")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_56395fbc1c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_56395fbc1c'
    bl_label = r"Easy Face Rig in Blender | Blender 2.8"
    bl_description = r"Shapekey tutorial by Team miracles"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=-tYuKOhc8D8")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_9f1460c853(bpy.types.Menu):
    bl_label = "Shapekeys"
    bl_idname = "SNA_MT_9f1460c853"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_fb8d46d6e4",text=r"Blender 2.82 : Everything About Shape-Keys (In 2 Minutes!!!)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_4f4e1050cf",text=r"Corrective Shape Keys - Blender 2.8 Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_6e901b0fa7",text=r"Blender 2.8 Character Animation: Shape Keys",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_309bdc1249",text=r"Shape Keys Weight Paint Blender Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7f81ef39ee",text=r"Creating an Advanced Face Rig Pt. 1 (Blender 2.6 Tutorial)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_56395fbc1c",text=r"Easy Face Rig in Blender | Blender 2.8",emboss=True,depress=False)
    
    
class SNA_MT_e225647cb7(bpy.types.Menu):
    bl_label = "Mechanical"
    bl_idname = "SNA_MT_e225647cb7"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_521cd399a1",text=r"How to Rig a Scifi Landing Gear in Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_8d96052eb7",text=r"Rigging in Blender - Advance Mech Knee with Piston Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_e8bd65556a",text=r"Machine & Piston | Let's Build It In Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_08ffd8430f",text=r"Robot Rigging Full",emboss=True,depress=False)
    
    
class SNA_OT_BTN_08ffd8430f(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_08ffd8430f'
    bl_label = r"Robot Rigging Full"
    bl_description = r"Mechanical rigging tutorial by Level Pixel Level"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=GKvJKV5fiIU&list=PLbjn7kaP877v6ByHd-fgek3kOmUYFOzR0")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_e8bd65556a(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_e8bd65556a'
    bl_label = r"Machine & Piston | Let's Build It In Blender"
    bl_description = r"Mechanical rigging tutorial by CG cookie"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=sPiVoH4Z5uI")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_8d96052eb7(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_8d96052eb7'
    bl_label = r"Rigging in Blender - Advance Mech Knee with Piston Tutorial"
    bl_description = r"Mechanical rigging tutorial by Markom3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=T-zcCd6-UWs&t=37s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_521cd399a1(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_521cd399a1'
    bl_label = r"How to Rig a Scifi Landing Gear in Blender"
    bl_description = r"Mechanical rigging tutorial by Markom3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=6BUgz7Lr1Ig&t=26s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_ce62d13a20(bpy.types.Menu):
    bl_label = "VFX"
    bl_idname = "SNA_MT_ce62d13a20"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.menu("SNA_MT_e478d20820",text=r"Motion Tracking",icon="CON_CAMERASOLVER")
        layout.menu("SNA_MT_d99c476702",text=r"Object Tracking",icon="CON_OBJECTSOLVER")
        layout.menu("SNA_MT_4ac467767a",text=r"Green Screen",icon="NODE_COMPOSITING")
        layout.menu("SNA_MT_5aeeb94253",text=r"VFX compositing",icon="NODE_COMPOSITING")
    
    
class SNA_OT_BTN_370d8639ca(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_370d8639ca'
    bl_label = r"Blender 2.8 Object tracking Vfx Tutorial /Object motion solver"
    bl_description = r"Object tracking tutorial by JAYJAY Fx"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ncyzGGAtImE&t=105s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_45dced150a(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_45dced150a'
    bl_label = r"Thor VFX Tutorial | Blender 2.9"
    bl_description = r"Object tracking tutorial by Alfie Vaughan"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=3wh5cV_B5tc")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_4543aaf4c5(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_4543aaf4c5'
    bl_label = r"Track, Match, Blend - 19 Object & Camera Track"
    bl_description = r"Object tracking tutorial by alcoholadicted"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=S6QY8BroHcc")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_557a0143bd(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_557a0143bd'
    bl_label = r"Blender 2.62 object tracking tutorial! HD"
    bl_description = r"Object tracking tutorial by Blendertrack (Old but it hasn't changed much)"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=QmYaRRhyivA")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_d99c476702(bpy.types.Menu):
    bl_label = "Object Tracking"
    bl_idname = "SNA_MT_d99c476702"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=r"Object Tracking isnt that hard but there arent alot of vids covering it, sorry")
        layout.operator("scripting_nodes.sna_ot_btn_370d8639ca",text=r"Blender 2.8 Object tracking Vfx Tutorial /Object motion solver",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_45dced150a",text=r"Thor VFX Tutorial | Blender 2.9",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_557a0143bd",text=r"Blender 2.62 object tracking tutorial! HD",emboss=True,depress=False)
    
    
class SNA_OT_BTN_740252500b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_740252500b'
    bl_label = r"Blender 2.8 VFX Tutorial | Green Screen"
    bl_description = r"Green screen tutorial by CG Geek"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=5ZpGpfQjzJA")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_8ff84a373b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_8ff84a373b'
    bl_label = r"Learn Green Screen Basics With Blender"
    bl_description = r"Green screen tutorial by CG Cookie"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=i_CiCjuG7y4")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_c97c6f8316(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_c97c6f8316'
    bl_label = r"Wild Tricks for Greenscreen in Blender"
    bl_description = r"Green screen tutorial by Ian Hubert"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=RxD6H3ri8RI&t=395s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_c924e44316(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_c924e44316'
    bl_label = r"Green Screen Effects in 1 Minute"
    bl_description = r"Green screen tutorial by CG Geek"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=lA6AuZYbLyQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_6b76726318(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_6b76726318'
    bl_label = r"Green Screen Effects in 1 Minute"
    bl_description = r"Green screen tutorial by CG Geek"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7877b96044(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7877b96044'
    bl_label = r"Invisibility Is Overrated"
    bl_description = r"Green screen tutorial by CGMatter"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=AHZQr9fwSjQ&t=86s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_4ac467767a(bpy.types.Menu):
    bl_label = "Green screen"
    bl_idname = "SNA_MT_4ac467767a"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_740252500b",text=r"Blender 2.8 VFX Tutorial | Green Screen",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_8ff84a373b",text=r"Learn Green Screen Basics With Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_c97c6f8316",text=r"Wild Tricks for Greenscreen in Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_c924e44316",text=r"Green Screen Effects in 1 Minute",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_6b76726318",text=r"Green Screen Effects in 1 Minute",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7877b96044",text=r"Invisibility Is Overrated",emboss=True,depress=False)
    
    
class SNA_OT_BTN_849747f4ec(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_849747f4ec'
    bl_label = r"Blender VFX: Fire Power Compositing"
    bl_description = r"Vfx compositing tutorial by Kenan Proffitt"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Lu0IcYyISqA&t=3s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_dd787dbf5d(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_dd787dbf5d'
    bl_label = r"Composite CGI Element Behind Real Glass - Blender VFX Tutorial (Full)"
    bl_description = r"Vfx compositing tutorial by InLightVFX"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=qdqV4oortP0")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_46fbe2709e(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_46fbe2709e'
    bl_label = r"Composite CGI Around Real Object - Blender VFX Tutorial (FULL)"
    bl_description = r"Vfx compositing tutorial by InLightVFX"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=fnAGtXMkRMY")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_eeb62fe1a5(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_eeb62fe1a5'
    bl_label = r"Hole In Wall - Blender VFX Tutorial (FULL)"
    bl_description = r"Vfx compositing tutorial by InLightVFX"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=1B-obCeZsBE")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_79e17c9586(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_79e17c9586'
    bl_label = r"Blender Tutorial - 3D Compositing | How to Composite Your 3D Model on a Real Background"
    bl_description = r"Vfx compositing tutorial by Aneesh Arts"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=OHhKbCE3aMI&t=1s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_327c689a02(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_327c689a02'
    bl_label = r"How to Realistically 3D Composite a Car in Blender | PART 1 (Shooting and Importing)"
    bl_description = r"Vfx compositing tutorial by Josiah Vaughan"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=hTk1sh8dZ8s&list=PLAVMCs-iBvp94L0Q3oj1F0ZoF-jdF82S6")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_5aeeb94253(bpy.types.Menu):
    bl_label = "VFX compositing"
    bl_idname = "SNA_MT_5aeeb94253"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_849747f4ec",text=r"Blender VFX: Fire Power Compositing",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_dd787dbf5d",text=r"Composite CGI Element Behind Real Glass - Blender VFX Tutorial (Full)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_46fbe2709e",text=r"Composite CGI Around Real Object - Blender VFX Tutorial (FULL)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_eeb62fe1a5",text=r"Hole In Wall - Blender VFX Tutorial (FULL)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_79e17c9586",text=r"Blender Tutorial - 3D Compositing | How to Composite Your 3D Model on a Real Background",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_327c689a02",text=r"How to Realistically 3D Composite a Car in Blender | PART 1 (Shooting and Importing)",emboss=True,depress=False)
    
    
class SNA_MT_e478d20820(bpy.types.Menu):
    bl_label = "Motion Tracking"
    bl_idname = "SNA_MT_e478d20820"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_46fb9ca286",text=r"Blender Motion Tracking Series",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_64de6cddd6",text=r"Add CGI Characters to Live Footage | Blender 2.8 VFX Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_1c57d98354",text=r"Blender Motion Tracking - Room Transformation!",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_b20977a867",text=r"Beginner Tutorial | The Basics of Camera Tracking in Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_db7545a0ee",text=r"Blender tracking tutorial: Add 3d buildings to Live action Footage",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_2f50c158a7",text=r"Blender Minecraft Earth Effect Series",emboss=True,depress=False)
    
    
class SNA_OT_BTN_2f50c158a7(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_2f50c158a7'
    bl_label = r"Blender Minecraft Earth Effect Series"
    bl_description = r"Motion tracking tutorial by CGMatter"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=G1HUGtSb7YA&list=PL4EqKJjrgoVTKPR01osooe5I_794b_gxP")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_db7545a0ee(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_db7545a0ee'
    bl_label = r"Blender tracking tutorial: Add 3d buildings to Live action Footage"
    bl_description = r"Motion tracking tutorial by Light Architect"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=7FltiqN8R9g")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_b20977a867(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_b20977a867'
    bl_label = r"Beginner Tutorial | The Basics of Camera Tracking in Blender"
    bl_description = r"Motion tracking tutorial by Falzon Tutorials"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=QIQ0G0Czf_U")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_1c57d98354(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_1c57d98354'
    bl_label = r"Blender Motion Tracking - Room Transformation!"
    bl_description = r"Motion tracking tutorial by Ian Hubert"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=lY8Ol2n4o4A")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_64de6cddd6(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_64de6cddd6'
    bl_label = r"Add CGI Characters to Live Footage | Blender 2.8 VFX Tutorial"
    bl_description = r"Motion tracking tutorial by CG Geek"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=hymtATx1QXw")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_46fb9ca286(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_46fb9ca286'
    bl_label = r"Blender Motion Tracking Series"
    bl_description = r"Motion tracking tutorial by CGMatter"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=WLSGG7sDEac&list=PL4EqKJjrgoVTCrjTOBHePGXHqFdqaPYyR")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_4f033b72f8(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_4f033b72f8'
    bl_label = r"Flip Fluids Add on"
    bl_description = r"Adding Flip fluid to blender"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=eaU9vb63lGw&t=51s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_816bc12f42(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_816bc12f42'
    bl_label = r"Khaos Add on"
    bl_description = r"Using the Khaos Add on to make explosions"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=Frb792dcn20")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_edb4954ab2(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_edb4954ab2'
    bl_label = r"Molecular add on (FREE)"
    bl_description = r"How to use the molecular add on in blender"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=iLDCr9734r8")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_593317f3ac(bpy.types.Menu):
    bl_label = "Add on sims"
    bl_idname = "SNA_MT_593317f3ac"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=r"Mix of paid and free add ons for blender sim")
        layout.operator("scripting_nodes.sna_ot_btn_4f033b72f8",text=r"Flip Fluids Add on",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_816bc12f42",text=r"Khaos Add on",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_edb4954ab2",text=r"Molecular add on (FREE)",emboss=True,depress=False)
    
    
class SNA_OT_BTN_3adf31b411(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_3adf31b411'
    bl_label = r"The New Blender Fluid Simulator is AWESOME - MantaFlow Tutorial"
    bl_description = r"Mantaflow tutorial by CG Geek"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=JYc_6fXEjw4&t=1s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_80e4faad8b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_80e4faad8b'
    bl_label = r"Tutorial - Beautiful Water Feature Fluid Simulation in Blender 2.82 and Mantaflow"
    bl_description = r"Mantaflow tutorial by Moby Motion"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=GlkbeIv6kBM&t=1s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_422d0941ed(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_422d0941ed'
    bl_label = r"Blender 2.8 | How to make a Fire and smoke Tornado | Mantaflow Simulation | TUTORIAL"
    bl_description = r"Mantaflow tutorial by Aria Faith Jones"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ej-q9AUEHLA")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_3d71198554(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_3d71198554'
    bl_label = r"Create Simple Explosion VFX in Blender Mantaflow - Iridesium"
    bl_description = r"Mantaflow tutorial by Iredesium"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=29yfS-icS3M&t=1238s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_0fd1488bee(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_0fd1488bee'
    bl_label = r"Blender Tutorial - How to Create Mist with Mantaflow (2.90)"
    bl_description = r"Mantaflow tutorial by Blender Made Easy"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=NxtztAKyPU0")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_1a988fee2e(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_1a988fee2e'
    bl_label = r"Blender Tutorial - Mantaflow Guides Smoke & Fluid Simulations"
    bl_description = r"Mantaflow tutorial by Blender Made Easy"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ldUwslQJ9NQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_61c6dc959d(bpy.types.Menu):
    bl_label = "Mantaflow"
    bl_idname = "SNA_MT_61c6dc959d"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_3adf31b411",text=r"The New Blender Fluid Simulator is AWESOME - MantaFlow Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_80e4faad8b",text=r"Tutorial - Beautiful Water Feature Fluid Simulation in Blender 2.82 and Mantaflow",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_422d0941ed",text=r"Blender 2.8 | How to make a Fire and smoke Tornado | Mantaflow Simulation | TUTORIAL",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_3d71198554",text=r"Create Simple Explosion VFX in Blender Mantaflow - Iridesium",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_0fd1488bee",text=r"Blender Tutorial - How to Create Mist with Mantaflow (2.90)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_1a988fee2e",text=r"Blender Tutorial - Mantaflow Guides Smoke & Fluid Simulations",emboss=True,depress=False)
    
    
class SNA_OT_BTN_87d890e21b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_87d890e21b'
    bl_label = r"Blender Tutorial - Cloth Simulation | Advance Simulation | Blender 2.9"
    bl_description = r"Cloth physics tutorial by Aneesh Arts"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=AbyfuW5Aocg")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_0c0459c092(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_0c0459c092'
    bl_label = r"Blender | Sewing A Fancy Dress In Blender | Beginners Tutorial"
    bl_description = r"Cloth physics tutorial by PIXXO 3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=0dmeiQDp5Ko")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_6ff4f3124c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_6ff4f3124c'
    bl_label = r"Create Believable Cloth With These Three Easy Features in Blender"
    bl_description = r"Cloth physics tutorial by CG Cookie"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=hoyrgeyNdCo")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_a71ebc7c0d(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_a71ebc7c0d'
    bl_label = r"Easy Cloth Simulation In Blender 2.82"
    bl_description = r"Cloth physics tutorial by pinkpocketTV"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=8FL9WANKoUg")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_89fe2dd4c0(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_89fe2dd4c0'
    bl_label = r"How to Quickly Sew Clothing in Blender 2.8 - Marvelous Designer for free?"
    bl_description = r"Cloth physics tutorial by Martin Klekner"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ywXILQnPWK4&t=229s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_4354f7c246(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_4354f7c246'
    bl_label = r"Blender 2.9 | How to make a Halloween Ghost Cloth Simulation + Easy Procedural Textures | TUTORIAL"
    bl_description = r"Cloth physics tutorial by Aria Faith Jones"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=VsK_8JeWRyw")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_053cc2b54b(bpy.types.Menu):
    bl_label = "Cloth"
    bl_idname = "SNA_MT_053cc2b54b"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_87d890e21b",text=r"Blender Tutorial - Cloth Simulation | Advance Simulation | Blender 2.9",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_0c0459c092",text=r"Blender | Sewing A Fancy Dress In Blender | Beginners Tutorial",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_6ff4f3124c",text=r"Create Believable Cloth With These Three Easy Features in Blender",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_a71ebc7c0d",text=r"Easy Cloth Simulation In Blender 2.82",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_89fe2dd4c0",text=r"How to Quickly Sew Clothing in Blender 2.8 - Marvelous Designer for free?",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_4354f7c246",text=r"Blender 2.9 | How to make a Halloween Ghost Cloth Simulation + Easy Procedural Textures | TUTORIAL",emboss=True,depress=False)
    
    
class SNA_OT_BTN_d3050f5026(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_d3050f5026'
    bl_label = r"Blender 2.8 Beginner Tutorial - Part 12: Rigid Body Simulation"
    bl_description = r"Rigid body tutorial by CG Boost"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=2C7lRSPVvHI")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7a24293c08(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7a24293c08'
    bl_label = r"Physics in Blender 2.8 for Absolute Beginners"
    bl_description = r"Rigid body tutorial by Surface Studio"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=KtjJfWlQ8oE")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_bfd069f9a9(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_bfd069f9a9'
    bl_label = r"Physics in Blender 2.8 for Absolute Beginners"
    bl_description = r"Rigid body tutorial by Surface Studio"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_0b9897b0d7(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_0b9897b0d7'
    bl_label = r"Destruction in Blender for Absolute Beginners"
    bl_description = r"Rigid body tutorial by Surface Studio"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ogWQs_7DU0Y&t=32s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_80107c6eb3(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_80107c6eb3'
    bl_label = r"Blender Destruction Beginner Tutorial | Revisited"
    bl_description = r"Rigid body tutorial by Surface Studio"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=zMhPrT0UWWs")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_ea4cc4c9da(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ea4cc4c9da'
    bl_label = r"Wrecking Ball Animation Tutorial [Blender 2.81]"
    bl_description = r"Rigid body tutorial by PIXXO 3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=nrYLALJKUsQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_403f6ad46c(bpy.types.Menu):
    bl_label = "Rigid Body"
    bl_idname = "SNA_MT_403f6ad46c"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_d3050f5026",text=r"Blender 2.8 Beginner Tutorial - Part 12: Rigid Body Simulation",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7a24293c08",text=r"Physics in Blender 2.8 for Absolute Beginners",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_bfd069f9a9",text=r"Physics in Blender 2.8 for Absolute Beginners",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_0b9897b0d7",text=r"Destruction in Blender for Absolute Beginners",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_80107c6eb3",text=r"Blender Destruction Beginner Tutorial | Revisited",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_ea4cc4c9da",text=r"Wrecking Ball Animation Tutorial [Blender 2.81]",emboss=True,depress=False)
    
    
class SNA_OT_BTN_aa12a38bad(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_aa12a38bad'
    bl_label = r"Blender Soft Body Settings Explained"
    bl_description = r"Soft body explanation by Xaero"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=4lqUxQ2XN4o&t=336s")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_bd1b712f89(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_bd1b712f89'
    bl_label = r"Blender - Easy Soft Body Animation in Blender 2.8"
    bl_description = r"Soft body tutorial by Ducky 3D"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=p8rEHCGfTNs")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_40d0e0e427(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_40d0e0e427'
    bl_label = r"Softbody/Jelly Tetris Tutorial | Blender 2.83"
    bl_description = r"Soft body tutorial by Inferno Arts"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=O4CeRusspIg")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_538e45c5d2(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_538e45c5d2'
    bl_label = r"Skin Wrinkling with Cloth and Soft Bodies in Blender!"
    bl_description = r"Soft body tutorial by Mr.Cheebs"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=YDrbyITWMGU")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_2d403a9f85(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_2d403a9f85'
    bl_label = r"[2.8] Blender Tutorial, Easy Soft Body Simulation, EEVEE"
    bl_description = r"Soft body tutorial by Olav3D Tutorials"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=LeO5eOunzeQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_54f0a34ad5(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_54f0a34ad5'
    bl_label = r"How to create a soft body in blender 2.8"
    bl_description = r"Soft body tutorial by 3DSchool"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=IxcR_s3_VMs")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_0da1e02149(bpy.types.Menu):
    bl_label = "Soft Body"
    bl_idname = "SNA_MT_0da1e02149"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_bd1b712f89",text=r"Blender - Easy Soft Body Animation in Blender 2.8",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_aa12a38bad",text=r"Blender Soft Body Settings Explained",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_40d0e0e427",text=r"Softbody/Jelly Tetris Tutorial | Blender 2.83",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_538e45c5d2",text=r"Skin Wrinkling with Cloth and Soft Bodies in Blender!",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_2d403a9f85",text=r"[2.8] Blender Tutorial, Easy Soft Body Simulation, EEVEE",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_54f0a34ad5",text=r"How to create a soft body in blender 2.8",emboss=True,depress=False)
    
    
class SNA_MT_99d37f1e9e(bpy.types.Menu):
    bl_label = "Simulations"
    bl_idname = "SNA_MT_99d37f1e9e"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        column = layout.column(align=False)
        column.enabled = True
        column.alert = False
        column.scale_x = 1.0
        column.scale_y = 1.0
        column.menu("SNA_MT_403f6ad46c",text=r"Rigid Body",icon="MESH_CUBE")
        column.menu("SNA_MT_0da1e02149",text=r"Soft Body",icon="MOD_SOFT")
        column.menu("SNA_MT_053cc2b54b",text=r"Cloth",icon="MOD_CLOTH")
        column.menu("SNA_MT_61c6dc959d",text=r"Mantaflow",icon="EXPERIMENTAL")
        column.menu("SNA_MT_593317f3ac",text=r"Add on sims",icon="ADD")
    
    
class SNA_MT_890ac45df7(bpy.types.Menu):
    bl_label = "Huberterian"
    bl_idname = "SNA_MT_890ac45df7"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_4bdba83a7a",text=r"Ian Hubert",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_ae3423f4ed",text=r"Blender Guru",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_d275c9f6e9",text=r"CG GEEK",emboss=True,depress=False)
        layout.menu("SNA_MT_2118bdfcfe",text=r"CG/Default")
        layout.operator("scripting_nodes.sna_ot_btn_2de3e09ab7",text=r"Ducky3D",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_e693cabc68",text=r"SouthernShotty",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7483d22c7c",text=r"AskNK",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_b7587817e7",text=r"InspirationTuts",emboss=True,depress=False)
    
    
class SNA_OT_BTN_b7587817e7(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_b7587817e7'
    bl_label = r"InspirationTuts"
    bl_description = r"Really helpful"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/channel/UCDdv3C21EFv7MxBMu70OExw")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7483d22c7c(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7483d22c7c'
    bl_label = r"AskNK"
    bl_description = r"Live updates in a literal sense"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/c/askNK")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_e693cabc68(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_e693cabc68'
    bl_label = r"SouthernShotty"
    bl_description = r"CLAY"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/c/SouthernShotty/videos")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_2de3e09ab7(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_2de3e09ab7'
    bl_label = r"Ducky3D"
    bl_description = r"LOOPS"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/channel/UCuNhGhbemBkdflZ1FGJ0lUQ")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_d275c9f6e9(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_d275c9f6e9'
    bl_label = r"CG GEEK"
    bl_description = r"The one that continued it"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/c/CGGeek/videos")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_ae3423f4ed(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ae3423f4ed'
    bl_label = r"Blender Guru"
    bl_description = r"The one that started it"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/user/AndrewPPrice/videos")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_4bdba83a7a(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_4bdba83a7a'
    bl_label = r"Ian Hubert"
    bl_description = r"Honestly a huge inspiration"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/c/mrdodobird/videos")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_576bb611e8(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_576bb611e8'
    bl_label = r"CGMatter"
    bl_description = r"Not DefaultCube"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/c/CGMatter/videos")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_b83f763f60(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_b83f763f60'
    bl_label = r"DefaultCube"
    bl_description = r"Not CGMatter"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/c/DefaultCube/videos")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_MT_2118bdfcfe(bpy.types.Menu):
    bl_label = "CG/Default"
    bl_idname = "SNA_MT_2118bdfcfe"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scripting_nodes.sna_ot_btn_576bb611e8",text=r"CGMatter",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_b83f763f60",text=r"DefaultCube",emboss=True,depress=False)
    
    
class SNA_MT_970e5e6257(bpy.types.Menu):
    bl_label = "Music"
    bl_idname = "SNA_MT_970e5e6257"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        layout.label(text=r"Some of my favorite sounds to relax and work to")
        layout.operator("scripting_nodes.sna_ot_btn_c2d9e1c083",text=r"Lo-fi for Witches (Only) [lofi / calm / chill beats]",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7e75fada45",text=r"CHON - Grow (Full Album Stream)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_7d7c74d9a4",text=r"CHON - Chon",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_ca9db7f27b",text=r"Valiant Hearts - Odyssey (2019)",emboss=True,depress=False)
        layout.operator("scripting_nodes.sna_ot_btn_93700b3e7a",text=r"Lo-fi for Ghosts (Only)",emboss=True,depress=False)
    
    
class SNA_OT_BTN_c2d9e1c083(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_c2d9e1c083'
    bl_label = r"Lo-fi for Witches (Only) [lofi / calm / chill beats]"
    bl_description = r"Lo-fi but spooky"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=4Hg1Kudd_x4")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_93700b3e7a(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_93700b3e7a'
    bl_label = r"Lo-fi for Ghosts (Only)"
    bl_description = r"Spoopy"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=2GjPQfdQfMY")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_ca9db7f27b(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ca9db7f27b'
    bl_label = r"Valiant Hearts - Odyssey (2019)"
    bl_description = r"Valient Hearts"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=ya7eSXJMcPU&list=PL2gGv1ZtPX58NY0HPDnzrHOi-efXx91A3")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7d7c74d9a4(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7d7c74d9a4'
    bl_label = r"CHON - Chon"
    bl_description = r"Self named album"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=FBiWjtlX4k0&list=OLAK5uy_nOtWtC11Qkz68rrUKMYtqVk5gzk7O7Dd4&index=1")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_OT_BTN_7e75fada45(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_7e75fada45'
    bl_label = r"CHON - Grow (Full Album Stream)"
    bl_description = r"Chon"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.wm.url_open(url="https://www.youtube.com/watch?v=-hwTK6hGreM&list=PLPnALZKB5h_CVj4LY9c0oHFA4JBXg8jC_")
            
        except Exception as exc:
            report_sn_error(exc)
        return {"FINISHED"}
        
class SNA_PT_5daec377f0(bpy.types.Panel):
    bl_label = "Tutorial"
    bl_idname = "SNA_PT_5daec377f0"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"
    bl_category = "Tutorials"
    bl_options = {"DEFAULT_CLOSED"}
    
    @classmethod
    def poll(cls, context):
        return True
    
    def draw_header(self, context):
        layout = self.layout
    
    def draw(self, context):
        layout = self.layout
        layout.menu("SNA_MT_936cb33337",text=r"General",icon="BOOKMARKS")
        layout.menu("SNA_MT_ada7bd35cc",text=r"Modelling",icon="MESH_CUBE")
        layout.menu("SNA_MT_c543a20639",text=r"Sculpting",icon="SCULPTMODE_HLT")
        layout.menu("SNA_MT_58efd74310",text=r"Nodes",icon="NODETREE")
        layout.menu("SNA_MT_be1d31e86a",text=r"Rigging",icon="GROUP_BONE")
        layout.menu("SNA_MT_ce62d13a20",text=r"VFX",icon="CON_CAMERASOLVER")
        layout.menu("SNA_MT_99d37f1e9e",text=r"Simulations",icon="MOD_FLUIDSIM")
        layout.menu("SNA_MT_890ac45df7",text=r"Helpful Channels",icon="CAMERA_STEREO")
        layout.menu("SNA_MT_970e5e6257",text=r"Relaxing music",icon="OUTLINER_OB_SPEAKER")
    
    
def add_to_panel_c36060f8e1(self, context):
    layout = self.layout
    layout.popover("SNA_PT_5daec377f0",text=r"Tutorials", icon="WORLD_DATA")
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROPERTIES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# REGISTER / UNREGISTER
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def register():
    bpy.utils.register_class(SNA_MT_58efd74310)
    bpy.utils.register_class(SNA_OT_BTN_5d69c1cd01)
    bpy.utils.register_class(SNA_OT_BTN_9d189649aa)
    bpy.utils.register_class(SNA_OT_BTN_1cf089cc35)
    bpy.utils.register_class(SNA_OT_BTN_ccb7872885)
    bpy.utils.register_class(SNA_OT_BTN_fa8f12d666)
    bpy.utils.register_class(SNA_OT_BTN_6424bd4090)
    bpy.utils.register_class(SNA_OT_BTN_e701734fe7)
    bpy.utils.register_class(SNA_OT_BTN_07b66b8200)
    bpy.utils.register_class(SNA_OT_BTN_9768ad084b)
    bpy.utils.register_class(SNA_OT_BTN_7b92864909)
    bpy.utils.register_class(SNA_OT_BTN_3fe0e15768)
    bpy.utils.register_class(SNA_OT_BTN_af173989e0)
    bpy.utils.register_class(SNA_MT_ada7bd35cc)
    bpy.utils.register_class(SNA_OT_BTN_70d51f3bb0)
    bpy.utils.register_class(SNA_OT_BTN_054d6eeaa2)
    bpy.utils.register_class(SNA_OT_BTN_331efe1e71)
    bpy.utils.register_class(SNA_OT_BTN_9e2ba6ff8d)
    bpy.utils.register_class(SNA_OT_BTN_8300fea05b)
    bpy.utils.register_class(SNA_MT_936cb33337)
    bpy.utils.register_class(SNA_OT_BTN_1ee62085e6)
    bpy.utils.register_class(SNA_MT_c543a20639)
    bpy.utils.register_class(SNA_OT_BTN_52a41e63ac)
    bpy.utils.register_class(SNA_OT_BTN_66d89bf833)
    bpy.utils.register_class(SNA_OT_BTN_f34bf1a3f1)
    bpy.utils.register_class(SNA_OT_BTN_781b461ec9)
    bpy.utils.register_class(SNA_OT_BTN_f913340d71)
    bpy.utils.register_class(SNA_OT_BTN_3df3be261c)
    bpy.utils.register_class(SNA_MT_a67b6fd600)
    bpy.utils.register_class(SNA_OT_BTN_3398e99b37)
    bpy.utils.register_class(SNA_OT_BTN_83ebbdc331)
    bpy.utils.register_class(SNA_OT_BTN_83f1a6254f)
    bpy.utils.register_class(SNA_OT_BTN_82542b11c4)
    bpy.utils.register_class(SNA_OT_BTN_828edf75d5)
    bpy.utils.register_class(SNA_OT_BTN_a0f41e0584)
    bpy.utils.register_class(SNA_OT_BTN_af9b1c9d99)
    bpy.utils.register_class(SNA_MT_1f1ea40f22)
    bpy.utils.register_class(SNA_OT_BTN_ae329c47be)
    bpy.utils.register_class(SNA_OT_BTN_eeecc0d2e1)
    bpy.utils.register_class(SNA_OT_BTN_10912391c0)
    bpy.utils.register_class(SNA_OT_BTN_3b1e6946f8)
    bpy.utils.register_class(SNA_OT_BTN_41ed7d8742)
    bpy.utils.register_class(SNA_MT_b65df0d4f0)
    bpy.utils.register_class(SNA_OT_BTN_fdf10b8389)
    bpy.utils.register_class(SNA_OT_BTN_a5ef8716e4)
    bpy.utils.register_class(SNA_OT_BTN_cc076d5ce9)
    bpy.utils.register_class(SNA_OT_BTN_8c7d0accee)
    bpy.utils.register_class(SNA_OT_BTN_585b5ee59b)
    bpy.utils.register_class(SNA_OT_BTN_ef0d442ea4)
    bpy.utils.register_class(SNA_OT_BTN_a341274abf)
    bpy.utils.register_class(SNA_MT_25f86f7073)
    bpy.utils.register_class(SNA_OT_BTN_06e4b0b572)
    bpy.utils.register_class(SNA_OT_BTN_f55b158822)
    bpy.utils.register_class(SNA_OT_BTN_94f18635a4)
    bpy.utils.register_class(SNA_OT_BTN_e539d4ccbd)
    bpy.utils.register_class(SNA_OT_BTN_92a0d3338c)
    bpy.utils.register_class(SNA_MT_8d1b506450)
    bpy.utils.register_class(SNA_OT_BTN_7260d0ffd1)
    bpy.utils.register_class(SNA_OT_BTN_e68862f916)
    bpy.utils.register_class(SNA_OT_BTN_6089952c99)
    bpy.utils.register_class(SNA_OT_BTN_7a1e59489c)
    bpy.utils.register_class(SNA_OT_BTN_b82a8d3800)
    bpy.utils.register_class(SNA_OT_BTN_a25978a46a)
    bpy.utils.register_class(SNA_MT_be1d31e86a)
    bpy.utils.register_class(SNA_OT_BTN_7d27d1931a)
    bpy.utils.register_class(SNA_OT_BTN_7b1010cbe5)
    bpy.utils.register_class(SNA_OT_BTN_65e82f9343)
    bpy.utils.register_class(SNA_OT_BTN_a76e73ebc3)
    bpy.utils.register_class(SNA_OT_BTN_5f1a08d39a)
    bpy.utils.register_class(SNA_OT_BTN_285c930f59)
    bpy.utils.register_class(SNA_MT_ea6e2df1f9)
    bpy.utils.register_class(SNA_OT_BTN_7d437a6321)
    bpy.utils.register_class(SNA_OT_BTN_59b1c7c70c)
    bpy.utils.register_class(SNA_OT_BTN_62d9634c5f)
    bpy.utils.register_class(SNA_OT_BTN_2e108ff0f4)
    bpy.utils.register_class(SNA_OT_BTN_e1070147cc)
    bpy.utils.register_class(SNA_OT_BTN_5299890bea)
    bpy.utils.register_class(SNA_OT_BTN_b1561224a9)
    bpy.utils.register_class(SNA_OT_BTN_8c598c42b5)
    bpy.utils.register_class(SNA_OT_BTN_31b8f36caf)
    bpy.utils.register_class(SNA_OT_BTN_1c4b4865fe)
    bpy.utils.register_class(SNA_OT_BTN_caf450d917)
    bpy.utils.register_class(SNA_OT_BTN_ef5cf60f53)
    bpy.utils.register_class(SNA_MT_e4da156ce3)
    bpy.utils.register_class(SNA_OT_BTN_fb8d46d6e4)
    bpy.utils.register_class(SNA_OT_BTN_4f4e1050cf)
    bpy.utils.register_class(SNA_OT_BTN_6e901b0fa7)
    bpy.utils.register_class(SNA_OT_BTN_309bdc1249)
    bpy.utils.register_class(SNA_OT_BTN_7f81ef39ee)
    bpy.utils.register_class(SNA_OT_BTN_56395fbc1c)
    bpy.utils.register_class(SNA_MT_9f1460c853)
    bpy.utils.register_class(SNA_MT_e225647cb7)
    bpy.utils.register_class(SNA_OT_BTN_08ffd8430f)
    bpy.utils.register_class(SNA_OT_BTN_e8bd65556a)
    bpy.utils.register_class(SNA_OT_BTN_8d96052eb7)
    bpy.utils.register_class(SNA_OT_BTN_521cd399a1)
    bpy.utils.register_class(SNA_MT_ce62d13a20)
    bpy.utils.register_class(SNA_OT_BTN_370d8639ca)
    bpy.utils.register_class(SNA_OT_BTN_45dced150a)
    bpy.utils.register_class(SNA_OT_BTN_4543aaf4c5)
    bpy.utils.register_class(SNA_OT_BTN_557a0143bd)
    bpy.utils.register_class(SNA_MT_d99c476702)
    bpy.utils.register_class(SNA_OT_BTN_740252500b)
    bpy.utils.register_class(SNA_OT_BTN_8ff84a373b)
    bpy.utils.register_class(SNA_OT_BTN_c97c6f8316)
    bpy.utils.register_class(SNA_OT_BTN_c924e44316)
    bpy.utils.register_class(SNA_OT_BTN_6b76726318)
    bpy.utils.register_class(SNA_OT_BTN_7877b96044)
    bpy.utils.register_class(SNA_MT_4ac467767a)
    bpy.utils.register_class(SNA_OT_BTN_849747f4ec)
    bpy.utils.register_class(SNA_OT_BTN_dd787dbf5d)
    bpy.utils.register_class(SNA_OT_BTN_46fbe2709e)
    bpy.utils.register_class(SNA_OT_BTN_eeb62fe1a5)
    bpy.utils.register_class(SNA_OT_BTN_79e17c9586)
    bpy.utils.register_class(SNA_OT_BTN_327c689a02)
    bpy.utils.register_class(SNA_MT_5aeeb94253)
    bpy.utils.register_class(SNA_MT_e478d20820)
    bpy.utils.register_class(SNA_OT_BTN_2f50c158a7)
    bpy.utils.register_class(SNA_OT_BTN_db7545a0ee)
    bpy.utils.register_class(SNA_OT_BTN_b20977a867)
    bpy.utils.register_class(SNA_OT_BTN_1c57d98354)
    bpy.utils.register_class(SNA_OT_BTN_64de6cddd6)
    bpy.utils.register_class(SNA_OT_BTN_46fb9ca286)
    bpy.utils.register_class(SNA_OT_BTN_4f033b72f8)
    bpy.utils.register_class(SNA_OT_BTN_816bc12f42)
    bpy.utils.register_class(SNA_OT_BTN_edb4954ab2)
    bpy.utils.register_class(SNA_MT_593317f3ac)
    bpy.utils.register_class(SNA_OT_BTN_3adf31b411)
    bpy.utils.register_class(SNA_OT_BTN_80e4faad8b)
    bpy.utils.register_class(SNA_OT_BTN_422d0941ed)
    bpy.utils.register_class(SNA_OT_BTN_3d71198554)
    bpy.utils.register_class(SNA_OT_BTN_0fd1488bee)
    bpy.utils.register_class(SNA_OT_BTN_1a988fee2e)
    bpy.utils.register_class(SNA_MT_61c6dc959d)
    bpy.utils.register_class(SNA_OT_BTN_87d890e21b)
    bpy.utils.register_class(SNA_OT_BTN_0c0459c092)
    bpy.utils.register_class(SNA_OT_BTN_6ff4f3124c)
    bpy.utils.register_class(SNA_OT_BTN_a71ebc7c0d)
    bpy.utils.register_class(SNA_OT_BTN_89fe2dd4c0)
    bpy.utils.register_class(SNA_OT_BTN_4354f7c246)
    bpy.utils.register_class(SNA_MT_053cc2b54b)
    bpy.utils.register_class(SNA_OT_BTN_d3050f5026)
    bpy.utils.register_class(SNA_OT_BTN_7a24293c08)
    bpy.utils.register_class(SNA_OT_BTN_bfd069f9a9)
    bpy.utils.register_class(SNA_OT_BTN_0b9897b0d7)
    bpy.utils.register_class(SNA_OT_BTN_80107c6eb3)
    bpy.utils.register_class(SNA_OT_BTN_ea4cc4c9da)
    bpy.utils.register_class(SNA_MT_403f6ad46c)
    bpy.utils.register_class(SNA_OT_BTN_aa12a38bad)
    bpy.utils.register_class(SNA_OT_BTN_bd1b712f89)
    bpy.utils.register_class(SNA_OT_BTN_40d0e0e427)
    bpy.utils.register_class(SNA_OT_BTN_538e45c5d2)
    bpy.utils.register_class(SNA_OT_BTN_2d403a9f85)
    bpy.utils.register_class(SNA_OT_BTN_54f0a34ad5)
    bpy.utils.register_class(SNA_MT_0da1e02149)
    bpy.utils.register_class(SNA_MT_99d37f1e9e)
    bpy.utils.register_class(SNA_MT_890ac45df7)
    bpy.utils.register_class(SNA_OT_BTN_b7587817e7)
    bpy.utils.register_class(SNA_OT_BTN_7483d22c7c)
    bpy.utils.register_class(SNA_OT_BTN_e693cabc68)
    bpy.utils.register_class(SNA_OT_BTN_2de3e09ab7)
    bpy.utils.register_class(SNA_OT_BTN_d275c9f6e9)
    bpy.utils.register_class(SNA_OT_BTN_ae3423f4ed)
    bpy.utils.register_class(SNA_OT_BTN_4bdba83a7a)
    bpy.utils.register_class(SNA_OT_BTN_576bb611e8)
    bpy.utils.register_class(SNA_OT_BTN_b83f763f60)
    bpy.utils.register_class(SNA_MT_2118bdfcfe)
    bpy.utils.register_class(SNA_MT_970e5e6257)
    bpy.utils.register_class(SNA_OT_BTN_c2d9e1c083)
    bpy.utils.register_class(SNA_OT_BTN_93700b3e7a)
    bpy.utils.register_class(SNA_OT_BTN_ca9db7f27b)
    bpy.utils.register_class(SNA_OT_BTN_7d7c74d9a4)
    bpy.utils.register_class(SNA_OT_BTN_7e75fada45)
    bpy.utils.register_class(SNA_PT_5daec377f0)
    bpy.types.VIEW3D_HT_header.prepend(add_to_panel_c36060f8e1)

def unregister():
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(SNA_MT_58efd74310)
    bpy.utils.unregister_class(SNA_OT_BTN_5d69c1cd01)
    bpy.utils.unregister_class(SNA_OT_BTN_9d189649aa)
    bpy.utils.unregister_class(SNA_OT_BTN_1cf089cc35)
    bpy.utils.unregister_class(SNA_OT_BTN_ccb7872885)
    bpy.utils.unregister_class(SNA_OT_BTN_fa8f12d666)
    bpy.utils.unregister_class(SNA_OT_BTN_6424bd4090)
    bpy.utils.unregister_class(SNA_OT_BTN_e701734fe7)
    bpy.utils.unregister_class(SNA_OT_BTN_07b66b8200)
    bpy.utils.unregister_class(SNA_OT_BTN_9768ad084b)
    bpy.utils.unregister_class(SNA_OT_BTN_7b92864909)
    bpy.utils.unregister_class(SNA_OT_BTN_3fe0e15768)
    bpy.utils.unregister_class(SNA_OT_BTN_af173989e0)
    bpy.utils.unregister_class(SNA_MT_ada7bd35cc)
    bpy.utils.unregister_class(SNA_OT_BTN_70d51f3bb0)
    bpy.utils.unregister_class(SNA_OT_BTN_054d6eeaa2)
    bpy.utils.unregister_class(SNA_OT_BTN_331efe1e71)
    bpy.utils.unregister_class(SNA_OT_BTN_9e2ba6ff8d)
    bpy.utils.unregister_class(SNA_OT_BTN_8300fea05b)
    bpy.utils.unregister_class(SNA_MT_936cb33337)
    bpy.utils.unregister_class(SNA_OT_BTN_1ee62085e6)
    bpy.utils.unregister_class(SNA_MT_c543a20639)
    bpy.utils.unregister_class(SNA_OT_BTN_52a41e63ac)
    bpy.utils.unregister_class(SNA_OT_BTN_66d89bf833)
    bpy.utils.unregister_class(SNA_OT_BTN_f34bf1a3f1)
    bpy.utils.unregister_class(SNA_OT_BTN_781b461ec9)
    bpy.utils.unregister_class(SNA_OT_BTN_f913340d71)
    bpy.utils.unregister_class(SNA_OT_BTN_3df3be261c)
    bpy.utils.unregister_class(SNA_MT_a67b6fd600)
    bpy.utils.unregister_class(SNA_OT_BTN_3398e99b37)
    bpy.utils.unregister_class(SNA_OT_BTN_83ebbdc331)
    bpy.utils.unregister_class(SNA_OT_BTN_83f1a6254f)
    bpy.utils.unregister_class(SNA_OT_BTN_82542b11c4)
    bpy.utils.unregister_class(SNA_OT_BTN_828edf75d5)
    bpy.utils.unregister_class(SNA_OT_BTN_a0f41e0584)
    bpy.utils.unregister_class(SNA_OT_BTN_af9b1c9d99)
    bpy.utils.unregister_class(SNA_MT_1f1ea40f22)
    bpy.utils.unregister_class(SNA_OT_BTN_ae329c47be)
    bpy.utils.unregister_class(SNA_OT_BTN_eeecc0d2e1)
    bpy.utils.unregister_class(SNA_OT_BTN_10912391c0)
    bpy.utils.unregister_class(SNA_OT_BTN_3b1e6946f8)
    bpy.utils.unregister_class(SNA_OT_BTN_41ed7d8742)
    bpy.utils.unregister_class(SNA_MT_b65df0d4f0)
    bpy.utils.unregister_class(SNA_OT_BTN_fdf10b8389)
    bpy.utils.unregister_class(SNA_OT_BTN_a5ef8716e4)
    bpy.utils.unregister_class(SNA_OT_BTN_cc076d5ce9)
    bpy.utils.unregister_class(SNA_OT_BTN_8c7d0accee)
    bpy.utils.unregister_class(SNA_OT_BTN_585b5ee59b)
    bpy.utils.unregister_class(SNA_OT_BTN_ef0d442ea4)
    bpy.utils.unregister_class(SNA_OT_BTN_a341274abf)
    bpy.utils.unregister_class(SNA_MT_25f86f7073)
    bpy.utils.unregister_class(SNA_OT_BTN_06e4b0b572)
    bpy.utils.unregister_class(SNA_OT_BTN_f55b158822)
    bpy.utils.unregister_class(SNA_OT_BTN_94f18635a4)
    bpy.utils.unregister_class(SNA_OT_BTN_e539d4ccbd)
    bpy.utils.unregister_class(SNA_OT_BTN_92a0d3338c)
    bpy.utils.unregister_class(SNA_MT_8d1b506450)
    bpy.utils.unregister_class(SNA_OT_BTN_7260d0ffd1)
    bpy.utils.unregister_class(SNA_OT_BTN_e68862f916)
    bpy.utils.unregister_class(SNA_OT_BTN_6089952c99)
    bpy.utils.unregister_class(SNA_OT_BTN_7a1e59489c)
    bpy.utils.unregister_class(SNA_OT_BTN_b82a8d3800)
    bpy.utils.unregister_class(SNA_OT_BTN_a25978a46a)
    bpy.utils.unregister_class(SNA_MT_be1d31e86a)
    bpy.utils.unregister_class(SNA_OT_BTN_7d27d1931a)
    bpy.utils.unregister_class(SNA_OT_BTN_7b1010cbe5)
    bpy.utils.unregister_class(SNA_OT_BTN_65e82f9343)
    bpy.utils.unregister_class(SNA_OT_BTN_a76e73ebc3)
    bpy.utils.unregister_class(SNA_OT_BTN_5f1a08d39a)
    bpy.utils.unregister_class(SNA_OT_BTN_285c930f59)
    bpy.utils.unregister_class(SNA_MT_ea6e2df1f9)
    bpy.utils.unregister_class(SNA_OT_BTN_7d437a6321)
    bpy.utils.unregister_class(SNA_OT_BTN_59b1c7c70c)
    bpy.utils.unregister_class(SNA_OT_BTN_62d9634c5f)
    bpy.utils.unregister_class(SNA_OT_BTN_2e108ff0f4)
    bpy.utils.unregister_class(SNA_OT_BTN_e1070147cc)
    bpy.utils.unregister_class(SNA_OT_BTN_5299890bea)
    bpy.utils.unregister_class(SNA_OT_BTN_b1561224a9)
    bpy.utils.unregister_class(SNA_OT_BTN_8c598c42b5)
    bpy.utils.unregister_class(SNA_OT_BTN_31b8f36caf)
    bpy.utils.unregister_class(SNA_OT_BTN_1c4b4865fe)
    bpy.utils.unregister_class(SNA_OT_BTN_caf450d917)
    bpy.utils.unregister_class(SNA_OT_BTN_ef5cf60f53)
    bpy.utils.unregister_class(SNA_MT_e4da156ce3)
    bpy.utils.unregister_class(SNA_OT_BTN_fb8d46d6e4)
    bpy.utils.unregister_class(SNA_OT_BTN_4f4e1050cf)
    bpy.utils.unregister_class(SNA_OT_BTN_6e901b0fa7)
    bpy.utils.unregister_class(SNA_OT_BTN_309bdc1249)
    bpy.utils.unregister_class(SNA_OT_BTN_7f81ef39ee)
    bpy.utils.unregister_class(SNA_OT_BTN_56395fbc1c)
    bpy.utils.unregister_class(SNA_MT_9f1460c853)
    bpy.utils.unregister_class(SNA_MT_e225647cb7)
    bpy.utils.unregister_class(SNA_OT_BTN_08ffd8430f)
    bpy.utils.unregister_class(SNA_OT_BTN_e8bd65556a)
    bpy.utils.unregister_class(SNA_OT_BTN_8d96052eb7)
    bpy.utils.unregister_class(SNA_OT_BTN_521cd399a1)
    bpy.utils.unregister_class(SNA_MT_ce62d13a20)
    bpy.utils.unregister_class(SNA_OT_BTN_370d8639ca)
    bpy.utils.unregister_class(SNA_OT_BTN_45dced150a)
    bpy.utils.unregister_class(SNA_OT_BTN_4543aaf4c5)
    bpy.utils.unregister_class(SNA_OT_BTN_557a0143bd)
    bpy.utils.unregister_class(SNA_MT_d99c476702)
    bpy.utils.unregister_class(SNA_OT_BTN_740252500b)
    bpy.utils.unregister_class(SNA_OT_BTN_8ff84a373b)
    bpy.utils.unregister_class(SNA_OT_BTN_c97c6f8316)
    bpy.utils.unregister_class(SNA_OT_BTN_c924e44316)
    bpy.utils.unregister_class(SNA_OT_BTN_6b76726318)
    bpy.utils.unregister_class(SNA_OT_BTN_7877b96044)
    bpy.utils.unregister_class(SNA_MT_4ac467767a)
    bpy.utils.unregister_class(SNA_OT_BTN_849747f4ec)
    bpy.utils.unregister_class(SNA_OT_BTN_dd787dbf5d)
    bpy.utils.unregister_class(SNA_OT_BTN_46fbe2709e)
    bpy.utils.unregister_class(SNA_OT_BTN_eeb62fe1a5)
    bpy.utils.unregister_class(SNA_OT_BTN_79e17c9586)
    bpy.utils.unregister_class(SNA_OT_BTN_327c689a02)
    bpy.utils.unregister_class(SNA_MT_5aeeb94253)
    bpy.utils.unregister_class(SNA_MT_e478d20820)
    bpy.utils.unregister_class(SNA_OT_BTN_2f50c158a7)
    bpy.utils.unregister_class(SNA_OT_BTN_db7545a0ee)
    bpy.utils.unregister_class(SNA_OT_BTN_b20977a867)
    bpy.utils.unregister_class(SNA_OT_BTN_1c57d98354)
    bpy.utils.unregister_class(SNA_OT_BTN_64de6cddd6)
    bpy.utils.unregister_class(SNA_OT_BTN_46fb9ca286)
    bpy.utils.unregister_class(SNA_OT_BTN_4f033b72f8)
    bpy.utils.unregister_class(SNA_OT_BTN_816bc12f42)
    bpy.utils.unregister_class(SNA_OT_BTN_edb4954ab2)
    bpy.utils.unregister_class(SNA_MT_593317f3ac)
    bpy.utils.unregister_class(SNA_OT_BTN_3adf31b411)
    bpy.utils.unregister_class(SNA_OT_BTN_80e4faad8b)
    bpy.utils.unregister_class(SNA_OT_BTN_422d0941ed)
    bpy.utils.unregister_class(SNA_OT_BTN_3d71198554)
    bpy.utils.unregister_class(SNA_OT_BTN_0fd1488bee)
    bpy.utils.unregister_class(SNA_OT_BTN_1a988fee2e)
    bpy.utils.unregister_class(SNA_MT_61c6dc959d)
    bpy.utils.unregister_class(SNA_OT_BTN_87d890e21b)
    bpy.utils.unregister_class(SNA_OT_BTN_0c0459c092)
    bpy.utils.unregister_class(SNA_OT_BTN_6ff4f3124c)
    bpy.utils.unregister_class(SNA_OT_BTN_a71ebc7c0d)
    bpy.utils.unregister_class(SNA_OT_BTN_89fe2dd4c0)
    bpy.utils.unregister_class(SNA_OT_BTN_4354f7c246)
    bpy.utils.unregister_class(SNA_MT_053cc2b54b)
    bpy.utils.unregister_class(SNA_OT_BTN_d3050f5026)
    bpy.utils.unregister_class(SNA_OT_BTN_7a24293c08)
    bpy.utils.unregister_class(SNA_OT_BTN_bfd069f9a9)
    bpy.utils.unregister_class(SNA_OT_BTN_0b9897b0d7)
    bpy.utils.unregister_class(SNA_OT_BTN_80107c6eb3)
    bpy.utils.unregister_class(SNA_OT_BTN_ea4cc4c9da)
    bpy.utils.unregister_class(SNA_MT_403f6ad46c)
    bpy.utils.unregister_class(SNA_OT_BTN_aa12a38bad)
    bpy.utils.unregister_class(SNA_OT_BTN_bd1b712f89)
    bpy.utils.unregister_class(SNA_OT_BTN_40d0e0e427)
    bpy.utils.unregister_class(SNA_OT_BTN_538e45c5d2)
    bpy.utils.unregister_class(SNA_OT_BTN_2d403a9f85)
    bpy.utils.unregister_class(SNA_OT_BTN_54f0a34ad5)
    bpy.utils.unregister_class(SNA_MT_0da1e02149)
    bpy.utils.unregister_class(SNA_MT_99d37f1e9e)
    bpy.utils.unregister_class(SNA_MT_890ac45df7)
    bpy.utils.unregister_class(SNA_OT_BTN_b7587817e7)
    bpy.utils.unregister_class(SNA_OT_BTN_7483d22c7c)
    bpy.utils.unregister_class(SNA_OT_BTN_e693cabc68)
    bpy.utils.unregister_class(SNA_OT_BTN_2de3e09ab7)
    bpy.utils.unregister_class(SNA_OT_BTN_d275c9f6e9)
    bpy.utils.unregister_class(SNA_OT_BTN_ae3423f4ed)
    bpy.utils.unregister_class(SNA_OT_BTN_4bdba83a7a)
    bpy.utils.unregister_class(SNA_OT_BTN_576bb611e8)
    bpy.utils.unregister_class(SNA_OT_BTN_b83f763f60)
    bpy.utils.unregister_class(SNA_MT_2118bdfcfe)
    bpy.utils.unregister_class(SNA_MT_970e5e6257)
    bpy.utils.unregister_class(SNA_OT_BTN_c2d9e1c083)
    bpy.utils.unregister_class(SNA_OT_BTN_93700b3e7a)
    bpy.utils.unregister_class(SNA_OT_BTN_ca9db7f27b)
    bpy.utils.unregister_class(SNA_OT_BTN_7d7c74d9a4)
    bpy.utils.unregister_class(SNA_OT_BTN_7e75fada45)
    bpy.utils.unregister_class(SNA_PT_5daec377f0)
    bpy.types.VIEW3D_HT_header.remove(add_to_panel_c36060f8e1)