bl_info = {
    "name": "Multikey",
    "description": "change shape keys on multiple objects and keyframe them",
    "author": "Joseph Hansen",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "3D View > Multikey",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
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

    

    my_float: FloatProperty(
        name = "Value",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )


    my_string: StringProperty(
        name="Key",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
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
        
        col = 'chelye_bt'
        ob_l = bpy.context.selected_objects
        for ob in ob_l:
            ob.select_set(False)
        for obj in bpy.data.collections[col].all_objects:
            obj.select_set(True)
            if hasattr(obj.data, "shape_keys"):
                if hasattr(obj.data.shape_keys, "key_blocks"):
                    for shape in obj.data.shape_keys.key_blocks:
                        if (shape.name == mytool.my_string):
                            shape.value = mytool.my_float
                        else:
                            pass
            else:
                continue
            for obj in bpy.data.collections[col].all_objects:
                obj.select_set(False)
        for ob in ob_l:
            ob.select_set(True)

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
 