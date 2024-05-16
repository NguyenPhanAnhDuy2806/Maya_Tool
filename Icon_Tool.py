'''
Nguyen Phan Anh Duy
Icon_Tool.py

Desc:
        Basic Toolset

How to Run:

from importlib import reload 
import Icon_Tool
reload(Icon_Tool)
Icon_Tool.gui()

'''

import maya.cmds as cmds

###############################

# Define color_slider as a global variable
color_slider = None

###############################

def create_box(*args):
   box = cmds.curve(d=1, p=[(0.5, 0.5, 0.5),(0.5, 0.5, -0.5),(-0.5, 0.5, -0.5),(-0.5, 0.5, 0.5),(0.5, 0.5, 0.5),(0.5, -0.5, 0.5),
                        (0.5, -0.5, -0.5),(0.5, 0.5, -0.5),(-0.5, 0.5, -0.5),(-0.5, -0.5, -0.5),(0.5, -0.5, -0.5),(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),(-0.5, -0.5, -0.5),(-0.5, 0.5, -0.5),(-0.5, 0.5, 0.5),(-0.5, -0.5, 0.5)],
                        k=[i for i in range(17)])
   cmds.scale( 20, 20, 20, box, cp= True, absolute=True )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

###############################

def arrow_square(*args):
   arrow = cmds.curve(d=1, p=[(-10, 0, -10), (-10, 0, -30), (-20, 0, -30), (0, 0, -50), (20, 0, -30), (10, 0, -30),
                           (10, 0, -10), (30, 0, -10), (30, 0, -20), (50, 0, 0), (30, 0, 20), (30, 0, 10), (10, 0, 10),
                           (10, 0, 30), (20, 0, 30), (0, 0, 50), (-20, 0, 30), (-10, 0, 30), (-10, 0, 10), (-30, 0, 10),
                           (-30, 0, 20), (-50, 0, 0), (-30, 0, -20), (-30, 0, -10), (-10, 0, -10)],
                           k=[i for i in range(25)])

###############################

def circle(*args):
   cirlce_icon=cmds.circle( nr=(1, 0, 0), c=(0, 0, 0),r=2  )
   cmds.scale( 10, 10, 10, cirlce_icon, cp= True, absolute=True )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)
   cmds.delete(ch=True)

###############################

def half_cirlce(*args):
   half_cirlce_icon=cmds.circle( nr=(0, 0, 1), c=(0, 0, 0), sw=180, r=2 )
   cmds.scale( 10, 10, 10, half_cirlce_icon, cp= True, absolute=True )
   cmds.rotate( 0, 0, '-90deg', half_cirlce_icon, pivot=(0, 0, 0) )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)
   cmds.delete(ch=True)

##############################

def arrow(*args):
   arrow = cmds.curve(d=1, p=[(0, 0, 0), (0, 0, -30), (-10, 0, -30), (10, 0, -50), (30, 0, -30), (20, 0, -30), (20, 0, 0), (0, 0, 0)],
                           k=[i for i in range(8)])
   cmds.xform(cp=True)
   cmds.move( -10, 0, 25 )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

##############################

def pryamid(*args):
   pryamid_icon = cmds.curve(d=1, p=[(0, 10.2, 0), (-10.2, -10.2, 10.2), (10.2, -10.2, 10.2), (0, 10.2, 0), 
                              (10.2, -10.2, -10.2), (10.2, -10.2, 10.2), (10.2, -10.2, -10.2), (-10.2, -10.2, -10.2), 
                              (0, 10.2, 0), (-10.2, -10.2, 10.2), (-10.2, -10.2, -10.2)],
                           k=[i for i in range(11)])
   cmds.scale( 2, 2, 2, pryamid_icon, cp= True, absolute=True )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

##############################

def square(*args):
   square_icon = cmds.curve(d=1, p=[(0, 0, -20), (0, 0, 10), (30, 0, 10), (30, 0, -20), (0, 0, -20)],k=[i for i in range(5)])
   cmds.xform(cp=True)
   cmds.move( -15, 0, 5 )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

##############################

def hand(*args):
   hand_icon = cmds.curve(d=1, p=[(-20, 0, 10),(-20, 0, -10),(-30, 0, -10),(-30, 0, 20),(-20, 0, 30),
                              (10, 0, 30),(20, 0, 20),(20, 0, -20),(10, 0, -20),(10, 0, 10),
                              (10, 0, -30),(0, 0, -30),(0, 0, 10), (0, 0, -40),(-10, 0, -40),(-10, 0, 0),
                              (-10, 0, -30),(-20, 0, -30),(-20, 0, -10)],k=[i for i in range(19)])

##############################

def jointLike_icon(*args):
   icon_circle_1 = cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),r=2)
   icon_circle_2 = cmds.circle( nr=(0, 0, 0), c=(0, 0, 0),r=2)
   icon_circle_3 = cmds.circle( nr=(1, 0, 0), c=(0, 0, 0),r=2)
   c_1 = cmds.listRelatives( icon_circle_1[0], s=True )
   c_2 = cmds.listRelatives( icon_circle_2[0], s=True )
   c_3 = cmds.listRelatives( icon_circle_3[0], s=True )
   group_node = cmds.group(empty=True, name="curve")
   cmds.parent(c_1,c_2,c_3,group_node,s=True,r=True)
   cmds.delete(icon_circle_1,icon_circle_2,icon_circle_3)
   cmds.scale( 5, 5, 5, group_node, cp= True, absolute=True )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

###############################

def cyclinder(*args):
   cyclinder_icon = cmds.curve(d=1, p=[(-1, 1, 0), (-0.707107, 1, 0.707107), (0, 1, 1), (0.707107, 1, 0.707107), (1, 1, 0), (0.707107, 1, -0.707107), 
                               (0, 1, -1), (-0.707107, 1, -0.707107), (-1, 1, 0), (-1, -1, 0), (-0.707107, -1, 0.707107), (0, -1, 1), (0.707107, -1, 0.707107), (1, -1, 0), (0.707107, -1, -0.707107), 
                               (0, -1, -1), (-0.707107, -1, -0.707107), (-1, -1, 0), (-0.707107, -1, 0.707107), (0, -1, 1), (0, 1, 1), (0.707107, 1, 0.707107), (1, 1, 0),
                               (1, -1, 0), (0.707107, -1, -0.707107), (0, -1, -1), (0, 1, -1)],
                               k=[i for i in range(27)])
   
   cmds.scale( 20, 20, 20, cyclinder_icon, cp= True, absolute=True )
   cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

###############################

def control_padding(*args):
   selected_control = cmds.ls(sl=True)
   
   # Create an mod group and match all transformation to the control
   control_mod = cmds.group(em=True)
   constraint = cmds.parentConstraint(selected_control, control_mod, mo=False)
   
   # group the mod group below the local group
   control_local = cmds.group(control_mod, n="local_01")
   cmds.delete(constraint)
   
   # group the selected control under the mod group
   cmds.parent(selected_control,control_mod)

########################################################

def set_curve_thickness(curve_name, thickness):
    # Check if the input curve exists
    if not cmds.objExists(curve_name):
        print(f"Curve '{curve_name}' does not exist.")
        return
    
    # Set the display curve thickness using the line width attribute
    cmds.setAttr(f"{curve_name}.lineWidth", thickness)

def apply_curve_thickness(*args):
    # Get thickness from UI
    thickness = float(cmds.textFieldGrp('thicknessSlider', q=True, text=True))
    
    # Get selected objects
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.error("No curve selected. Please select one or more NURBS curves.")
        return
    
    # Iterate over selected curves and set thickness
    for curve_name in selected_objects:
        set_curve_thickness(curve_name, thickness)

########################################################

def color_change(*args):
    global color_slider
    selected_curves = cmds.ls(sl=True)
    color_index = cmds.colorIndexSliderGrp(color_slider, query=True, value=True)
    for curve_name in selected_curves:
        cmds.setAttr(curve_name + ".overrideEnabled", 1)
        cmds.setAttr(curve_name + ".overrideColor", color_index - 1)

#########################################################

def parent_snap(*args):
   item_selection = cmds.ls(sl=1)
   driver = item_selection[::2]
   driven = item_selection[1::2]
   for x in range(len(driver)):
       constraint = cmds.parentConstraint(driver[x], driven[x], mo=False)
       cmds.delete(constraint)

def orient_snap(*args):
   item_selection = cmds.ls(sl=1)
   driver = item_selection[::2]
   driven = item_selection[1::2]
   for x in range(len(driver)):
       constraint = cmds.orientConstraint(driver[x], driven[x], mo=False)
       cmds.delete(constraint)

def point_snap(*args):
   item_selection = cmds.ls(sl=1)
   driver = item_selection[::2]
   driven = item_selection[1::2]
   for x in range(len(driver)):
       constraint = cmds.pointConstraint(driver[x], driven[x], mo=False)
       cmds.delete(constraint)

#########################################################

cirlce_image_path = r'D:\1\2023\scripts\Image\Circle.png'
box_image_path = r'D:\1\2023\scripts\Image\Square.png'
four_arrow_image_path = r'D:\1\2023\scripts\Image\Four_Arrow.png'
half_circle_arrow_image_path = r'D:\1\2023\scripts\Image\Half_Circle.png'
one_arrow_image_path = r'D:\1\2023\scripts\Image\One_Arrow.png'
pyramid_image_path = r'D:\1\2023\scripts\Image\Pyramid.png'
square_image_path = r'D:\1\2023\scripts\Image\2D_Square.png'
hand_image_path = r'D:\1\2023\scripts\Image\Hand.png'
jointlike_image_path = r'D:\1\2023\scripts\Image\3D_Joint.png'
cyclinder_image_path = r'D:\1\2023\scripts\Image\Cyclinder.png'

###############################

def gui():
    global color_slider
    window_name = "IconTool"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)    
    
    window = cmds.window(window_name, title="Icon Tool",widthHeight=(300, 300), resizeToFitChildren=True)
    cmds.columnLayout(adjustableColumn=True)
    cmds.rowColumnLayout( numberOfColumns=6 )

    cmds.text(label="2D Shape ", align='right')

    cmds.symbolButton(w=75,h=75,image=cirlce_image_path,command=circle)
    cmds.symbolButton(w=75,h=75,image=four_arrow_image_path,command=arrow_square)
    cmds.symbolButton(w=75,h=75,image=half_circle_arrow_image_path,command=half_cirlce)
    cmds.symbolButton(w=75,h=75,image=one_arrow_image_path,command=arrow)
    cmds.symbolButton(w=75,h=75,image=square_image_path,command=square)

    cmds.text(h=20, label="3D Shape ", align='right')

    cmds.symbolButton(w=75,h=75,image=box_image_path,command=create_box)
    cmds.symbolButton(w=75,h=75,image=pyramid_image_path,command=pryamid)
    cmds.symbolButton(w=75,h=75,image=jointlike_image_path,command=jointLike_icon)
    cmds.symbolButton(w=75,h=75,image=cyclinder_image_path,command=cyclinder)
    cmds.symbolButton(w=75,h=75,image=hand_image_path,command=hand)
    
    cmds.setParent('..')
    cmds.separator( height=10, style='singleDash' )
    cmds.text(h=20, label="Create Pad", align='center')
    cmds.button(label='Pad', command=control_padding)
    cmds.separator( height=10, style='singleDash' )
    cmds.text(h=15,label='Snapping Type')
    cmds.rowColumnLayout(numberOfRows=1)
    cmds.button(h=30,w=150, label='Parent Snap', c=parent_snap)
    cmds.button(h=30,w=150, label='Orient Snap', c=orient_snap)
    cmds.button(h=30,w=150, label='Point Snap', c=point_snap)
    cmds.setParent('..')
    
    cmds.separator( height=10, style='singleDash' )
    cmds.text(h=20, label='Enter the desired icon thickness:')
    cmds.floatSliderGrp('thicknessSlider', label='Thickness:', field=True, minValue=1, maxValue=10.0, value=1.0, adjustableColumn2=True)   
    cmds.button(label='Apply', command=apply_curve_thickness)  
    
    cmds.separator( height=10, style='singleDash' )
    cmds.text(h=20,label="Change Curve Color")
    cmds.columnLayout(adjustableColumn=True,rowSpacing=5)
    color_slider = cmds.colorIndexSliderGrp(label="Color Index", min=1, max=31, value=1, changeCommand=color_change) 

    cmds.showWindow(window)
