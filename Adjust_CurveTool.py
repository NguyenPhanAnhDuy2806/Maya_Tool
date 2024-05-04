'''
Nguyen Phan Anh Duy
Adjust_CurveTool.py

Desc:
        Adjust Curve Tool

How to Run:

from importlib import reload 
import Adjust_CurveTool
reload(Adjust_CurveTool)
Adjust_CurveTool.gui()

'''

import maya.cmds as cmds

# Define color_slider as a global variable
color_slider = None

########################################################

def create_proxy_attribute(*args):
    # Get the values from the text fields
    long_name = cmds.textField(long_name_field, query=True, text=True)
    proxy_source = cmds.textField(proxy_source_field, query=True, text=True)
    
    selected_objects = cmds.ls(sl=True)
    if selected_objects:
        selected_object = selected_objects[0]
        cmds.addAttr(selected_object, longName=long_name, proxy=proxy_source)
    else:
        cmds.warning("No object selected.")

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
def gui():
    global color_slider
    window_name = "AdjustCurveTool"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)    
    
    window = cmds.window(window_name, title="Adjust Curve Tool", resizeToFitChildren=True)
    cmds.columnLayout(adjustableColumn=True)
    
    cmds.rowColumnLayout(numberOfColumns=1)
    cmds.text(label="Attribute Name", rs=True)
    long_name_field = cmds.textField()
    cmds.text(label="Proxy Source:", rs=True)
    proxy_source_field = cmds.textField()
    cmds.button(label="Create", command=create_proxy_attribute)
    
    cmds.rowColumnLayout(numberOfColumns=1)
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label='Enter the desired thickness:')
    cmds.floatSliderGrp('thicknessSlider', label='Thickness:', field=True, minValue=1, maxValue=10.0, value=1.0, adjustableColumn2=True)   
    cmds.button(label='Apply', command=apply_curve_thickness)  
    
    cmds.text(label="Change Curve Color")
    cmds.columnLayout(adjustableColumn=True)
    color_slider = cmds.colorIndexSliderGrp(label="Color Index", min=1, max=31, value=1, changeCommand=color_change) 
    cmds.showWindow(window)
