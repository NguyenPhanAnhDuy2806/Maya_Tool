import maya.cmds as cmds

###############################

def color_change(*args):
    
    curve_name = cmds.ls(sl=True)
    color_index = cmds.colorIndexSliderGrp(color_slider, query=True, value=True)
    cmds.setAttr(curve_name[0] + ".overrideEnabled", 1)
    cmds.setAttr(curve_name[0] + ".overrideColor", color_index - 1)

###############################################################

window_name = "ColorChangeWindow"
if cmds.window(window_name, exists=True):
    cmds.deleteUI(window_name)

cmds.window(window_name, title="Change Curve Color")
cmds.columnLayout(adjustableColumn=True)
color_slider = cmds.colorIndexSliderGrp(label="Color Index", min=1, max=31, value=1,changeCommand=color_change)
cmds.showWindow(window_name)