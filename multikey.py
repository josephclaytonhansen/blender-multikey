bl_info = {
    "name": "Multikey",
    "description": "change shape keys on multiple objects and keyframe them",
    "author": "Joseph Hansen",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "3D View > Multikey",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "https://github.com/josephclaytonhansen/blender-multikey/",
    "tracker_url": "https://github.com/josephclaytonhansen/blender-multikey/",
    "category": "Animation"
}


import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )


# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------

class MyProperties(PropertyGroup):
    
    my_bool: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    

    my_float: FloatProperty(
        name = "Value",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )


    my_string: StringProperty(
        name="Key A",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )
    
    my_bool_b: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    

    my_float_b: FloatProperty(
        name = "Value",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )


    my_string_b: StringProperty(
        name="Key B",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )
    
    my_bool_c: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    

    my_float_c: FloatProperty(
        name = "Value",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )


    my_string_c: StringProperty(
        name="Key C",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )

    my_bool_d: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    

    my_float_d: FloatProperty(
        name = "Value",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )


    my_string_d: StringProperty(
        name="Key D",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )
    
    my_bool_e: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    

    my_float_e: FloatProperty(
        name = "Value",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )


    my_string_e: StringProperty(
        name="Key E",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )
    
    my_float_all: FloatProperty(
        name = "Value",
        description = "Value (0.0 to 0.1)",
        default = 0.60,
        min = 0.00,
        max = 1.0
        )


    my_enum: EnumProperty(
        name="Collection",
        description="Collection containing objects to shape key",
        items=[ ('OP1', "Option 1", ""),
                ('OP2', "Option 2", ""),
                ('OP3', "Option 3", ""),
               ]
        )

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------
class WM_OT_ResetUp(Operator):
    bl_label = "Set all to 1"
    bl_description = "Set all keys (A-E) to 1"
    bl_idname = "wm.mk_resetup"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        mytool.my_float = 1
        mytool.my_float_b = 1
        mytool.my_float_c = 1
        mytool.my_float_d = 1
        mytool.my_float_e = 1
        return {'FINISHED'}
    
class WM_OT_ResetDown(Operator):
    bl_label = "Set all to 0"
    bl_description = "Set all keys (A-E) to 0"
    bl_idname = "wm.mk_resetdown"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        mytool.my_float = 0
        mytool.my_float_b = 0
        mytool.my_float_c = 0
        mytool.my_float_d = 0
        mytool.my_float_e = 0
        return {'FINISHED'}

class WM_OT_SetAll(Operator):
    bl_label = "Set all to value"
    bl_description = "Set all keys (A-E) to a value"
    bl_idname = "wm.mk_setall"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        mytool.my_float = mytool.my_float_all
        mytool.my_float_b = mytool.my_float_all
        mytool.my_float_c = mytool.my_float_all
        mytool.my_float_d = mytool.my_float_all
        mytool.my_float_e = mytool.my_float_all
        return {'FINISHED'}

class WM_OT_HelloWorld(Operator):
    bl_label = "Preview"
    bl_description = "Apply value to shapekeys"
    bl_idname = "wm.mk_panel"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        print("float value:", mytool.my_float)
        print("string value:", mytool.my_string)
        print("enum state:", mytool.my_enum)

        k_key = mytool.my_string
        k_val = mytool.my_float
        k_col = mytool.my_enum
        k_en = mytool.my_bool
        
        k_keyb = mytool.my_string_b
        k_valb = mytool.my_float_b
        k_colb = mytool.my_enum
        k_enb = mytool.my_bool_b
        
        k_keyc = mytool.my_string_c
        k_valc = mytool.my_float_c
        k_colc = mytool.my_enum
        k_enc = mytool.my_bool_c
        
        k_keyd = mytool.my_string_d
        k_vald = mytool.my_float_d
        k_cold = mytool.my_enum
        k_end = mytool.my_bool_d
        
        k_keye = mytool.my_string_e
        k_vale = mytool.my_float_e
        k_cole = mytool.my_enum
        k_ene = mytool.my_bool_e
        
        col = 'chelye_bt'
        
        ob_l = bpy.context.selected_objects
        def ex(key,value,collection,enabled):
            if(enabled == True):
                for ob in ob_l:
                    ob.select_set(False)
                for obj in bpy.data.collections[col].all_objects:
                    obj.select_set(True)
                    if hasattr(obj.data, "shape_keys"):
                        if hasattr(obj.data.shape_keys, "key_blocks"):
                            for shape in obj.data.shape_keys.key_blocks:
                                if (shape.name == key):
                                    shape.value = value
                                else:
                                    pass
                    else:
                        continue
                    for obj in bpy.data.collections[col].all_objects:
                        obj.select_set(False)
                for ob in ob_l:
                    ob.select_set(True)
                    
        ex(k_key, k_val, k_col, k_en)
        ex(k_keyb, k_valb, k_colb, k_enb)
        ex(k_keyc, k_valc, k_colc, k_enc)
        ex(k_keyd, k_vald, k_cold, k_end)
        ex(k_keye, k_vale, k_cole, k_ene)

        return {'FINISHED'}

# ------------------------------------------------------------------------
#    Menus
# ------------------------------------------------------------------------

class OBJECT_MT_CustomMenu(bpy.types.Menu):
    bl_label = "Select"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class OBJECT_PT_CustomPanel(Panel):
    bl_label = "MultiKey"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Multikey"
    bl_context = "objectmode"   


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        subcolumn = layout.column()
        subrow = layout.row(align=True)
        subrow.prop(mytool, "my_string", icon = "SHAPEKEY_DATA")
        subrow.separator()
        subrow.prop(mytool, "my_float")
        subrow.separator()
        subrow.prop(mytool, "my_bool")
        subrow = layout.row(align=True)
        subrow.prop(mytool, "my_string_b", icon = "SHAPEKEY_DATA")
        subrow.separator()
        subrow.prop(mytool, "my_float_b")
        subrow.separator()
        subrow.prop(mytool, "my_bool_b")
        subrow = layout.row(align=True)
        subrow.prop(mytool, "my_string_c", icon = "SHAPEKEY_DATA")
        subrow.separator()
        subrow.prop(mytool, "my_float_c")
        subrow.separator()
        subrow.prop(mytool, "my_bool_c")
        subrow = layout.row(align=True)
        subrow.prop(mytool, "my_string_d", icon = "SHAPEKEY_DATA")
        subrow.separator()
        subrow.prop(mytool, "my_float_d")
        subrow.separator()
        subrow.prop(mytool, "my_bool_d")
        subrow = layout.row(align=True)
        subrow.prop(mytool, "my_string_e", icon = "SHAPEKEY_DATA")
        subrow.separator()
        subrow.prop(mytool, "my_float_e")
        subrow.separator()
        subrow.prop(mytool, "my_bool_e")
        subrow = layout.row(align=True)
        subrow.operator("wm.mk_resetdown")
        subrow.separator()
        subrow.operator("wm.mk_resetup")
        subrow = layout.row(align=True)
        subrow.operator("wm.mk_setall")
        subrow.separator()
        subrow.prop(mytool, "my_float_all")
        layout.operator("wm.mk_panel", icon = "OUTPUT")
        subrow = layout.row(align=True)
        layout.prop(mytool, "my_enum", icon = "OUTLINER_OB_GROUP_INSTANCE")
        layout.separator()

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    MyProperties,
    WM_OT_HelloWorld,
    WM_OT_ResetDown,
    WM_OT_ResetUp,
    WM_OT_SetAll,
    OBJECT_MT_CustomMenu,
    OBJECT_PT_CustomPanel
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
 
