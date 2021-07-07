bl_info = {
    "name": "Multikey",
    "description": "change shape keys on multiple objects and keyframe them",
    "author": "Joseph Hansen",
    "version": (1, 1, 0),
    "blender": (2, 90, 0),
    "location": "3D View > Multikey",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "https://github.com/josephclaytonhansen/blender-multikey/",
    "tracker_url": "https://github.com/josephclaytonhansen/blender-multikey/",
    "category": "Animation"
}


import bpy
icons = True
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
def callback(scene, context):
    items=[]
    for collection in bpy.data.collections:
        items.append((collection.name, collection.name, ""))
    return items

def cframe(scene, context):
    frame = context.scene.frame_current
    return frame
    
class MyProperties(PropertyGroup):
    
    my_bool: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    my_float: FloatProperty(
        name = "",
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
        name = "",
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
        name = "",
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
        name = "",
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
        name = "",
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
        
    my_bool_f: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    my_float_f: FloatProperty(
        name = "",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )

    my_string_f: StringProperty(
        name="Key F",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )
    
    my_bool_g: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    my_float_g: FloatProperty(
        name = "",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )

    my_string_g: StringProperty(
        name="Key G",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )
    
    my_bool_h: BoolProperty(
        name="",
        description="Enable/disable this key",
        default = True
        )

    my_float_h: FloatProperty(
        name = "",
        description = "Value (0.0 to 0.1) of the shape key",
        default = 1,
        min = 0.00,
        max = 1.0
        )

    my_string_h: StringProperty(
        name="Key H",
        description="Name of the shape key (all objects must use identical shape key names)",
        default="",
        maxlen=64,
        )
    
    my_float_all: FloatProperty(
        name = "",
        description = "Value (0.0 to 0.1)",
        default = 0.60,
        min = 0.00,
        max = 1.0
        )

    my_enum: EnumProperty(
        name="Collection",
        description="Collection containing objects to shape key",
        items=callback
        )
    
    my_int: IntProperty(
        name="Frame",
        description="Frame to add keyframes",
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
        mytool.my_float_f = 1
        mytool.my_float_g = 1
        mytool.my_float_h = 1
        return {'FINISHED'}

class WM_OT_CurrentFrame(Operator):
    bl_label = "Get current frame"
    bl_description = "Get current frame"
    bl_idname = "wm.mk_currentframe"
    def execute(self,context):
        scene = context.scene
        mytool = scene.my_tool
        mytool.my_int = context.scene.frame_current
        return {'FINISHED'}
    
class WM_OT_AddKey(Operator):
    bl_label = "Add keyframes at frame"
    bl_description = "Add keyframes at frame for shapekeys"
    bl_idname = "wm.mk_addkey"
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        print("float value:", mytool.my_float)
        print("string value:", mytool.my_string)
        print("enum state:", mytool.my_enum)

        k_key = mytool.my_string
        k_val = mytool.my_float
        k_col = mytool.my_enum
        k_en = mytool.my_int
        k_e = mytool.my_bool
        
        k_keyb = mytool.my_string_b
        k_valb = mytool.my_float_b
        k_colb = mytool.my_enum
        k_enb = mytool.my_int
        k_eb = mytool.my_bool_b
        
        k_keyc = mytool.my_string_c
        k_valc = mytool.my_float_c
        k_colc = mytool.my_enum
        k_enc = mytool.my_int
        k_ec = mytool.my_bool_c
        
        k_keyd = mytool.my_string_d
        k_vald = mytool.my_float_d
        k_cold = mytool.my_enum
        k_end = mytool.my_int
        k_ed = mytool.my_bool_d
        
        k_keye = mytool.my_string_e
        k_vale = mytool.my_float_e
        k_cole = mytool.my_enum
        k_ene = mytool.my_int
        k_ee = mytool.my_bool_e
        
        k_keyf = mytool.my_string_f
        k_valf = mytool.my_float_f
        k_colf = mytool.my_enum
        k_enf = mytool.my_int
        k_ef = mytool.my_bool_f
        
        k_keyg = mytool.my_string_g
        k_valg = mytool.my_float_g
        k_colg = mytool.my_enum
        k_eng = mytool.my_int
        k_eg = mytool.my_bool_g
        
        k_keyh = mytool.my_string_h
        k_valh = mytool.my_float_h
        k_colh = mytool.my_enum
        k_enh = mytool.my_int
        k_eh = mytool.my_bool_h
        
        col = k_col        
        ob_l = bpy.context.selected_objects
        def ex(key,value,collection,framef, enabled):
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
                                    obj.data.shape_keys.key_blocks[key].keyframe_insert("value", frame=framef)
                                else:
                                    pass

                for obj in bpy.data.collections[col].all_objects:
                    obj.select_set(False)
            for ob in ob_l:
                ob.select_set(True)
                    
        ex(k_key, k_val, k_col, k_en, k_e)
        ex(k_keyb, k_valb, k_colb, k_enb, k_eb)
        ex(k_keyc, k_valc, k_colc, k_enc, k_ec)
        ex(k_keyd, k_vald, k_cold, k_end, k_ed)
        ex(k_keye, k_vale, k_cole, k_ene, k_ee)
        ex(k_keyf, k_valf, k_colf, k_enf, k_ef)
        ex(k_keyg, k_valg, k_colg, k_eng, k_eg)
        ex(k_keyh, k_valh, k_colh, k_enh, k_eh)
        
        return {'FINISHED'}

    

    
class WM_OT_ResetDown(Operator):
    bl_label = "Set all to 0"
    bl_description = "Set all keys (A-H) to 0"
    bl_idname = "wm.mk_resetdown"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        mytool.my_float = 0
        mytool.my_float_b = 0
        mytool.my_float_c = 0
        mytool.my_float_d = 0
        mytool.my_float_e = 0
        mytool.my_float_f = 0
        mytool.my_float_g = 0
        mytool.my_float_h = 0
        return {'FINISHED'}

class WM_OT_SetAll(Operator):
    bl_label = "Set all to:"
    bl_description = "Set all keys (A-H) to a value"
    bl_idname = "wm.mk_setall"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        mytool.my_float = mytool.my_float_all
        mytool.my_float_b = mytool.my_float_all
        mytool.my_float_c = mytool.my_float_all
        mytool.my_float_d = mytool.my_float_all
        mytool.my_float_e = mytool.my_float_all
        mytool.my_float_f = mytool.my_float_all
        mytool.my_float_g = mytool.my_float_all
        mytool.my_float_h = mytool.my_float_all
        return {'FINISHED'}

class WM_OT_Light(Operator):
    bl_label = "Toggle icons"
    bl_description = "Remove/show icons"
    bl_idname = "wm.mk_clean"
    
    def execute(self, context):
        global icons
        if icons:
            icons = False
        else:
            icons = True
        return {'FINISHED'}
    
class WM_OT_ClearNames(Operator):
    bl_label = "Clear key names"
    bl_description = "Delete key names"
    bl_idname = "wm.mk_clearnames"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        mytool.my_string = ""
        mytool.my_string_b = ""
        mytool.my_string_c = ""
        mytool.my_string_d = ""
        mytool.my_string_e = ""
        mytool.my_string_f = ""
        mytool.my_string_g = ""
        mytool.my_string_h = ""

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
        
        k_keyf = mytool.my_string_f
        k_valf = mytool.my_float_f
        k_colf = mytool.my_enum
        k_enf = mytool.my_bool_f
        
        k_keyg = mytool.my_string_g
        k_valg = mytool.my_float_g
        k_colg = mytool.my_enum
        k_eng = mytool.my_bool_g
        
        k_keyh = mytool.my_string_h
        k_valh = mytool.my_float_h
        k_colh = mytool.my_enum
        k_enh = mytool.my_bool_h
        
        col = k_col        
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
        ex(k_keyf, k_valf, k_colf, k_enf)
        ex(k_keyg, k_valg, k_colg, k_eng)
        ex(k_keyg, k_valg, k_colg, k_enh)
        
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
        global icons
        if icons:
            icon_dict = {0:"TRASH",1:"SHAPEKEY_DATA",2:"SHAPEKEY_DATA",3:"SHAPEKEY_DATA",4:"SHAPEKEY_DATA",5:"SHAPEKEY_DATA",6:"SHAPEKEY_DATA",
                         7:"OUTPUT",8:"OUTLINER_OB_GROUP_INSTANCE",9:"DECORATE_KEYFRAME",10:"KEY_HLT", 11:"SHAPEKEY_DATA", 12:"SHAPEKEY_DATA"}

        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        subcolumn = layout.column()
        if icons:
            layout.operator("wm.mk_clearnames", icon = icon_dict[0])
        else:
            layout.operator("wm.mk_clearnames")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string", icon = icon_dict[1])
        else:
            subrow.prop(mytool, "my_string")
        subrow.separator()
        subrow.prop(mytool, "my_float")
        subrow.separator()
        subrow.prop(mytool, "my_bool")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string_b", icon = icon_dict[2])
        else:
            subrow.prop(mytool, "my_string_b")
        subrow.separator()
        subrow.prop(mytool, "my_float_b")
        subrow.separator()
        subrow.prop(mytool, "my_bool_b")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string_c", icon = icon_dict[3])
        else:
            subrow.prop(mytool, "my_string_c")
        subrow.separator()
        subrow.prop(mytool, "my_float_c")
        subrow.separator()
        subrow.prop(mytool, "my_bool_c")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string_d", icon = icon_dict[4])
        else:
            subrow.prop(mytool, "my_string_d")
        subrow.separator()
        subrow.prop(mytool, "my_float_d")
        subrow.separator()
        subrow.prop(mytool, "my_bool_d")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string_e", icon = icon_dict[5])
        else:
            subrow.prop(mytool, "my_string_e")
        subrow.separator()
        subrow.prop(mytool, "my_float_e")
        subrow.separator()
        subrow.prop(mytool, "my_bool_e")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string_f", icon = icon_dict[6])
        else:
            subrow.prop(mytool, "my_string_f")
        subrow.separator()
        subrow.prop(mytool, "my_float_f")
        subrow.separator()
        subrow.prop(mytool, "my_bool_f")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string_g", icon = icon_dict[11])
        else:
            subrow.prop(mytool, "my_string_g")
        subrow.separator()
        subrow.prop(mytool, "my_float_g")
        subrow.separator()
        subrow.prop(mytool, "my_bool_g")
        subrow = layout.row(align=True)
        if icons:
            subrow.prop(mytool, "my_string_h", icon = icon_dict[12])
        else:
            subrow.prop(mytool, "my_string_h")
        subrow.separator()
        subrow.prop(mytool, "my_float_h")
        subrow.separator()
        subrow.prop(mytool, "my_bool_h")
        subrow = layout.row(align=True)
        subrow.operator("wm.mk_resetdown")
        subrow.separator()
        subrow.operator("wm.mk_resetup")
        subrow.separator()
        subrow.operator("wm.mk_setall")
        subrow.separator()
        subrow.prop(mytool, "my_float_all")
        subrow = layout.row(align=True)
        if icons:
            layout.operator("wm.mk_panel", icon = icon_dict[7])
        else:
            layout.operator("wm.mk_panel")
        subrow = layout.row(align=True)
        if icons:
            layout.prop(mytool, "my_enum", icon = icon_dict[8], text = "")
        else:
            layout.prop(mytool, "my_enum")
        layout.separator()
        layout.separator()
        layout.separator()
        subrow = layout.row(align=True)
        if icons:
            subrow.operator("wm.mk_currentframe", icon = icon_dict[9])
        else:
            subrow.operator("wm.mk_currentframe")
        subrow = layout.row(align=True)
        subrow.prop(mytool, "my_int")
        subrow.separator()
        if icons:
            subrow.operator("wm.mk_addkey", icon = icon_dict[10])
        else:
            subrow.operator("wm.mk_addkey")
        layout.separator()
        subrow =  layout.row(align=True)
        subrow.operator("wm.mk_clean")

        

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    MyProperties,
    WM_OT_HelloWorld,
    WM_OT_ResetDown,
    WM_OT_ResetUp,
    WM_OT_SetAll,
    WM_OT_CurrentFrame,
    WM_OT_ClearNames,
    WM_OT_AddKey,
    WM_OT_Light,
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
 
