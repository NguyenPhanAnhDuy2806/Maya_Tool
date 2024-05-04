'''
Nguyen Phan Anh Duy
Rigging_ToolBox.py

Desc:
        Basic Toolset

How to Run:

from importlib import reload 
import Rigging_ToolBox
reload(Rigging_ToolBox)
Rigging_ToolBox.gui()

'''

import maya.cmds as cmds
import maya.mel as mel

if cmds.window("WiWi", exists=True):
    cmds.deleteUI("WiWi")
def gui():
    myWindow = cmds.window("WiWi", t="Duy's ToolBox", widthHeight=(300, 300), resizeToFitChildren=True)
    cmds.columnLayout(adj=True, rowSpacing=5)
    
    cmds.text(h = 20, label='Command')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=3)
    cmds.button(h=25,w=100, label='Center Pivot', c=center_pivot)
    cmds.button(h=25,w=100, label='Delete History', c=delete_history)
    cmds.button(h=25,w=100, label='Freeze Transform', c=freeze_transform)
    cmds.setParent('..')
    
    cmds.text(label='Select')
    cmds.rowColumnLayout(numberOfColumns=3)
    cmds.setParent('..')
    cmds.button(h=25, label='Select Hierarchy', c=select_hierarchy)
    
    cmds.text(label='Renaming')
    cmds.rowColumnLayout(numberOfColumns=3)
    cmds.text(label= "Ori")
    cmds.text(label= "Name")
    cmds.text(label= "Suffix")
    global ori_text, name_text, suffix_text
    ori_text = cmds.textField(w=100)
    name_text = cmds.textField(w=100)
    suffix_text = cmds.textField(w=100)
    
    cmds.setParent('..')
    cmds.button(h=30, label='Renamer', c=renamer)
    cmds.button(h=30, label='Renamer Joints', c=renamer_jnt)
    cmds.button(h=30, label='Renamer Joints Ren', c=renamer_jnt_ren)
    cmds.showWindow(myWindow)
###########################################################################
def center_pivot(*args):
    cmds.xform(cp=True)

def delete_history(*args):
    cmds.delete(ch=True)

def freeze_transform(*args):
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

def select_hierarchy(*args):
    cmds.select(hi=True)

def renamer(*args):
    
    print("Selected have been renamed")

    #ori_name_suffix_count

    ori = cmds.textField(ori_text, q = True, text = True)
    name = cmds.textField(name_text, q = True, text = True)
    suffix = cmds.textField(suffix_text, q = True, text = True)
    count = 1

    #Get selected.
    selected = cmds.ls(sl=True)

    print(selected)

    for current in selected:
        new_name = '{0}_{1}_{2}_{3:02d}'.format(ori, name, suffix, count)
        print(new_name)

        cmds.rename(current, new_name)

        count = count + 1

def renamer_jnt(*args):
    
    print("Selected have been renamed")

    #ori_name_suffix_count

    ori = cmds.textField(ori_text, q = True, text = True)
    name = cmds.textField(name_text, q = True, text = True)
    suffix = cmds.textField(suffix_text, q = True, text = True)
    count = 1

    #Get selected.
    selected = cmds.ls(sl=True, dag = True)

    last_joint = ''

    print(selected)

    for current in selected:
        new_name = '{0}_{1}_{2}_{3:02d}'.format(ori, name, suffix, count)
        print(new_name)

        cmds.rename(current, new_name)
        last_joint = new_name
        count = count + 1

    new_name = '{0}_{1}_{2}_{3:02d}'.format(ori, name, "waste", count-1)
    print(last_joint, new_name)
    cmds.rename(last_joint, new_name)

def renamer_jnt_ren(*args):
    
    print("Selected have been renamed")

    #ori_name_suffix_count

    ori = cmds.textField(ori_text, q = True, text = True)
    name = cmds.textField(name_text, q = True, text = True)
    suffix = cmds.textField(suffix_text, q = True, text = True)
    count = 1

    #Get selected.
    selected = cmds.ls(sl=True, dag = True)
    cmds.select(selected, add=True)

    # renameSelectionList("renProcess")
    mel.eval('renameSelectionList("renProcess")')

    selected = cmds.ls(sl=True)

    last_joint = ''
    for current in selected:
        new_name = '{0}_{1}_{2}_{3:02d}'.format(ori, name, suffix, count)
        print(current, new_name)

        cmds.rename(current, new_name)
        last_joint = new_name
        count = count + 1
    new_name = '{0}_{1}_{2}_{3:02d}'.format(ori, name, "waste", count-1)
    print(last_joint, new_name)
    cmds.rename(last_joint, new_name)