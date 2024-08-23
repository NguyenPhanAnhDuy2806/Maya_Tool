'''
Nguyen Phan Anh Duy
Icon_Replace_Tool.py

Desc:
        Basic Toolset

How to Run:

from importlib import reload 
import Icon_Replace_Tool
reload(Icon_Replace_Tool)
Icon_Replace_Tool.gui()

'''

import maya.cmds as cmds

# Check and delete existing window
if cmds.window("WiWi", exists=True):
    cmds.deleteUI("WiWi")

# GUI creation
def gui():
    global icon_menu 
    myWindow = cmds.window("WiWi", t="Icon Replace Tool", widthHeight=(300, 300), resizeToFitChildren=True)
    main_layout = cmds.rowColumnLayout()
    icon_menu = cmds.optionMenu(label='New Icon:', changeCommand=iconMake)
    cmds.menuItem(label='Box')
    cmds.menuItem(label='4 Arrows')
    cmds.menuItem(label='Circle')
    cmds.menuItem(label='Pyramid')
    cmds.button('testIcon_Btn', l="Replace Icon", w=150, c=replaceIcon)
    cmds.showWindow(myWindow)

# Create icon based on selection
def iconMake(selection):
    global new_ctrl
    # Check if the 'New_Icon' group already exists and delete it
    if cmds.objExists('New_Icon'):
        cmds.delete('New_Icon')

    # Create an empty group for the new icon
    new_ctrl = cmds.group(empty=True, n='New_Icon')

    # Create icon based on the selected menu item
    if selection == "Box":
        box = cmds.curve(d=1, p=[(0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5),
                          (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5),
                          (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5),
                          (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5),
                          (-0.5, -0.5, 0.5)], k=[i for i in range(17)])
        cmds.scale(150, 150, 150, box, r=True)
        cmds.makeIdentity(box, a=True, t=1, r=1, s=1, n=0, pn=1)
        box_List = cmds.listRelatives(box, s=True)
        if box_List:
            cmds.parent(box_List[0], new_ctrl, r=True, s=True)
        cmds.delete(box)

    elif selection == "4 Arrows":
        arrows_4 = cmds.curve(d=1, p=[(-10, 0, -10), (-10, 0, -30), (-20, 0, -30), (0, 0, -50), 
                            (20, 0, -30), (10, 0, -30), (10, 0, -10), (30, 0, -10), (30, 0, -20), (50, 0, 0), 
                            (30, 0, 20), (30, 0, 10), (10, 0, 10), (10, 0, 30), (20, 0, 30), (0, 0, 50), 
                            (-20, 0, 30), (-10, 0, 30), (-10, 0, 10), (-30, 0, 10), (-30, 0, 20), 
                            (-50, 0, 0), (-30, 0, -20), (-30, 0, -10), (-10, 0, -10)], k=[i for i in range(25)])
        cmds.setAttr(arrows_4 + '.rotateZ', -90)
        cmds.scale(5, 5, 5, arrows_4, r=True)
        cmds.makeIdentity(arrows_4, a=True, t=1, r=1, s=1, n=0, pn=1)
        arrows_4_List = cmds.listRelatives(arrows_4, s=True)
        if arrows_4_List:
            cmds.parent(arrows_4_List[0], new_ctrl, r=True, s=True)
        cmds.delete(arrows_4)

    elif selection == "Circle":
        circle_icon = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), r=2)
        cmds.scale(50, 50, 50, circle_icon[0], r=True)
        cmds.makeIdentity(circle_icon[0], a=True, t=1, r=1, s=1, n=0, pn=1)
        circle_List = cmds.listRelatives(circle_icon[0], s=True)
        if circle_List:
            cmds.parent(circle_List[0], new_ctrl, r=True, s=True)
        cmds.delete(circle_icon[0])

    elif selection == "Pyramid":
        pyramid_icon = cmds.curve(d=1, p=[(0, 10.2, 0), (-10.2, -10.2, 10.2), (10.2, -10.2, 10.2), 
                                          (0, 10.2, 0), (10.2, -10.2, -10.2), (10.2, -10.2, 10.2), 
                                          (10.2, -10.2, -10.2), (-10.2, -10.2, -10.2), (0, 10.2, 0), 
                                          (-10.2, -10.2, 10.2), (-10.2, -10.2, -10.2)], k=[i for i in range(11)])
        cmds.scale(10, 10, 10, pyramid_icon, r=True)
        cmds.makeIdentity(pyramid_icon, a=True, t=1, r=1, s=1, n=0, pn=1)
        pyramid_List = cmds.listRelatives(pyramid_icon, s=True)
        if pyramid_List:
            cmds.parent(pyramid_List[0], new_ctrl, r=True, s=True)
        cmds.delete(pyramid_icon)

def replaceIcon(*args):
    # Get the selected transforms
    selected_objects = cmds.ls(sl=True)
    if not selected_objects:
        cmds.warning("No objects selected")
        return

    for obj in selected_objects:
        # Position the control
        constraint = cmds.parentConstraint(obj, new_ctrl, mo=False)
        cmds.delete(constraint)
        cmds.makeIdentity(new_ctrl, a=True, t=1, r=1, s=1, n=0, pn=1)

        # List the shape nodes with full paths
        new_ctrl_shape = cmds.listRelatives(new_ctrl, s=True, fullPath=True)
        selected_obj_shape = cmds.listRelatives(obj, s=True, fullPath=True)

        if new_ctrl_shape and selected_obj_shape:
            # Parent the new shape under the selected transform node
            cmds.parent(new_ctrl_shape, obj, shape=True, relative=True)

            # Delete the original shape of the selected object
            cmds.delete(selected_obj_shape)

            # Delete the original transform node
            cmds.delete(new_ctrl)

    # Cleanup the new control
    if cmds.objExists('New_Icon'):
        cmds.delete('New_Icon')