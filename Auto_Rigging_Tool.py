'''
Nguyen Phan Anh Duy
Auto_Rigging_Tool.py

Desc:
        Basic Toolset

How to Run:

from importlib import reload 
import Auto_Rigging_Tool
reload(Auto_Rigging_Tool)
Auto_Rigging_Tool.gui()

'''
import maya.cmds as cmds
def gui():
    scriptName = __name__    
    window_name = "Auto_armRig_Maker"

    
    if cmds.window(window_name, q=True, exists=True):
        cmds.deleteUI(window_name)    
    
    if cmds.windowPref(window_name, q=True, exists=True):
        cmds.windowPref(window_name, r=True)
    
    myWindow = cmds.window(window_name, title="Auto Arm Rig",widthHeight=(150, 325), resizeToFitChildren=True)
    main_layout = cmds.rowColumnLayout("Main Header")

    # Naming Option (option menu)
    
    cmds.text('naming_Text', l='Step 1: Set name options')
    cmds.rowColumnLayout(nc=4, cw=[(1,20),(2,40),(3,40),(4,50)])
    
    cmds.text('ori_Txt', label='Ori:')
    cmds.optionMenu('ori_Menu',cc=scriptName + '.colorChange()')
    cmds.menuItem(l="lt_")
    cmds.menuItem(l="rt_")
    cmds.menuItem(l="ct_")

    cmds.text('label_Txt', label='Label:')
    cmds.optionMenu('label_Menu')
    cmds.menuItem(l="arm")
    cmds.menuItem(l="leg")
    cmds.setParent(main_layout)
    cmds.separator('name_Sep', w=150, h=5, style='singleDash')

    # Set the rig type (radio button)
    cmds.text('rigType_Text', l='Step 2: Set rig type')
    cmds.radioButtonGrp("armType_Btn", labelArray3=('IK','FK','IKFK'),numberOfRadioButtons=3,columnWidth3=[50,50,50],select=3, cc=scriptName + '.armTypeVis()')
    cmds.separator( 'type_Sep', w=150, h=5, style='singleDash')

    # Set icon options (option menu)
    cmds.text('conSet_Text', l='Step 3: Set icon options')
    cmds.rowColumnLayout(nc=2, cw=[(1,90),(2,60)])
    cmds.text('ikStyle_Text', label='IK Icon:')
    cmds.optionMenu('ikIcon_Menu',cc=scriptName + '.iconChanger("ik")')
    cmds.menuItem(l="Box")
    cmds.menuItem(l="4 Arrows")
    cmds.menuItem(l="4 Pin")
    
    cmds.text('fkStyle_Text', label='FK Icon:')
    cmds.optionMenu('fkIcon_Menu',cc=scriptName + '.iconChanger("fk")')
    cmds.menuItem(l="Circle")
    cmds.menuItem(l="Turn Arrows")

    cmds.text('handStyle_Text', label='Hand Icon:')
    cmds.optionMenu('handIcon_Menu',cc=scriptName + '.iconChanger("hand")')
    cmds.menuItem(l="Circle")
    cmds.menuItem(l="Hand")

    cmds.text('pvStyle_Text', label='PoleVector Icon:')
    cmds.optionMenu('pvIcon_Menu',cc=scriptName + '.iconChanger("pv")')
    cmds.menuItem(l="Diamond")
    cmds.menuItem(l="Arrow")
    cmds.setParent(main_layout)
    cmds.button('testIcon_Btn', l="Make test icons to set scale", w=150, c=scriptName + '.armIconScale()')
    cmds.separator('style_Sep', w=150, h=5, style='singleDash')

    # Icon color (iconTextButton and colorSlider)
    cmds.text('armColor_Text', l='Icon Color by Ori')
    cmds.setParent(main_layout)
    cmds.colorIndexSliderGrp('armColor', w=150, h=20, cw2=(150,0), min=0, max=31, value=7)
    cmds.separator('color_Sep', w=150, h=5, style='singleDash')

    # Pole vector options (radio button)
    cmds.text('PV_Text', l='Step 4: Set IK elbow options')
    cmds.radioButtonGrp("addPVElbow_Btn", labelArray2=('Twist','Pole Vector'), numberOfRadioButtons=2, columnWidth2=[65,85],select=2,cc=scriptName + '.pvChanger()')
    cmds.separator( 'pv_Sep', w=150, h=5, style='singleDash')
    
    cmds.button('final_Btn', l="Finalize the Arm", w=150, c=scriptName + '.autoArmRig()')

    cmds.showWindow(myWindow)

###########################################################################

def colorChange():
    ori_opt = cmds.optionMenu('ori_Menu', q=True, sl=True) 
    if ori_opt == 1:
        ori_color = 7
    if ori_opt == 2:
        ori_color = 14
    if ori_opt == 3:
        ori_color = 18
    cmds.colorIndexSliderGrp('armColor', e=True, v=ori_color)

def armTypeVis():
    armType = cmds.radioButtonGrp("armType_Btn", q=True, sl=True) 
    if armType == 1:
        ik_val = 1
        fk_val = 0
        ikfk_val = 0
    if armType == 2:
        ik_val = 0
        fk_val = 1
        ikfk_val = 0
    if armType == 3:
        ik_val = 1
        fk_val = 1
        ikfk_val = 1

    cmds.text('ikStyle_Text', e=True, vis=ik_val)
    cmds.optionMenu('ikIcon_Menu', e=True, vis=ik_val)
    
    cmds.text('fkStyle_Text', e=True, vis=fk_val)
    cmds.optionMenu('fkIcon_Menu', e=True, vis=fk_val)
    
    cmds.text('handStyle_Text', e=True, vis=ikfk_val)
    cmds.optionMenu('handIcon_Menu', e=True, vis=ikfk_val)
    
    cmds.text('pvStyle_Text', e=True, vis=ik_val)
    cmds.optionMenu('pvIcon_Menu', e=True, vis=ik_val)
    cmds.text('PV_Text', e=True, vis=ik_val)
    cmds.radioButtonGrp("addPVElbow_Btn", e=True, vis=ik_val)
    cmds.separator( 'pv_Sep', e=True, vis=ik_val)

def pvChanger():
    pvType = (cmds.radioButtonGrp('addPVElbow_Btn',q=True,sl=True)) - 1
    if(cmds.objExists('ARM_PV_SCALE_TEST_DONT_DELETE') == True):
        cmds.setAttr('ARM_PV_SCALE_TEST_DONT_DELETE.v', pvType)

def iconChanger(icon_type):
    menu_opt = cmds.optionMenu(icon_type + 'Icon_Menu', q=True, sl=True)
    upper_text = icon_type.upper()
    if(cmds.objExists('ARM_' + upper_text + '_SCALE_TEST_DONT_DELETE') == True):
        shape_list = cmds.listRelatives('ARM_' + upper_text + '_SCALE_TEST_DONT_DELETE', s=True,type='nurbsCurve')
        shape_len = len(shape_list)
        counter = 1
        while(counter<(shape_len+1)):
                if counter == menu_opt:
                        cmds.setAttr(shape_list[counter-1] + '.visibility', 1 )
                else:
                        cmds.setAttr(shape_list[counter-1] + '.visibility', 0 )

                counter = counter + 1

def armIconScale():
    global armRefPad
    #Variables
    armType = cmds.radioButtonGrp('armType_Btn',q=True, sl=True)
    ikShape = cmds.optionMenu('ikIcon_Menu',q=True, sl=True)
    fkShape = cmds.optionMenu('fkIcon_Menu',q=True, sl=True)
    pvShape = cmds.optionMenu('pvIcon_Menu',q=True, sl=True)
    handShape = cmds.optionMenu('handIcon_Menu',q=True, sl=True)
    pvType = (cmds.radioButtonGrp('addPVElbow_Btn', q=True, sl=True)) - 1
    selected = cmds.ls(sl=True,dag=True, type='joint')
    
    icon_test_list = []
    
    #Creating the IK icon
    # cube
    ik_box = cmds.curve(n='ik_arm_box_curve',d=1, p=[(0.5, 0.5, 0.5),(0.5, 0.5, -0.5),(-0.5, 0.5, -0.5),(-0.5, 0.5, 0.5),(0.5, 0.5, 0.5),(0.5, -0.5, 0.5),
                        (0.5, -0.5, -0.5),(0.5, 0.5, -0.5),(-0.5, 0.5, -0.5),(-0.5, -0.5, -0.5),(0.5, -0.5, -0.5),(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),(-0.5, -0.5, -0.5),(-0.5, 0.5, -0.5),(-0.5, 0.5, 0.5),(-0.5, -0.5, 0.5)],
                        k=[i for i in range(17)])
    cmds.scale(2, 2, 2, ik_box)
    ik_box_List = cmds.listRelatives( ik_box, s=True )
    
    # 4 Arrows
    ik_arrows = cmds.curve(n='ik_arm_4arrows_curve',d=1, p=[(-10, 0, -10), (-10, 0, -30), (-20, 0, -30), (0, 0, -50), (20, 0, -30), (10, 0, -30),
                           (10, 0, -10), (30, 0, -10), (30, 0, -20), (50, 0, 0), (30, 0, 20), (30, 0, 10), (10, 0, 10),
                           (10, 0, 30), (20, 0, 30), (0, 0, 50), (-20, 0, 30), (-10, 0, 30), (-10, 0, 10), (-30, 0, 10),
                           (-30, 0, 20), (-50, 0, 0), (-30, 0, -20), (-30, 0, -10), (-10, 0, -10)],
                           k=[i for i in range(25)])
    
    cmds.setAttr(ik_arrows + '.rotateZ',-90)
    cmds.scale(0.1, 0.1, 0.1, ik_arrows)
    cmds.makeIdentity(ik_arrows,a=True, t=1, r=1, s=1, n=0, pn=1)
    ik_arrows_List = cmds.listRelatives( ik_arrows, s=True )
    
    # 4 Pin
    points = [(0.57, 0, -0.00002), (0.42, 0.15, -0.00002), (0.27, 0, -0.00001), (0.42, -0.15, -0.00002), (0.57, 0, -0.00002), (0.42, 0, -0.15), (0.27, 0, -0.00001), (0.42, 0, 0.15), (0.57, 0, -0.00002), (0.42, 0.15, -0.00002), (0.27, 0, -0.00001), (-0.27, 0, 0.00001), (-0.42, -0.15, 0.15), (-0.57, -0.00009, 0.00002), (-0.42, -0.15, -0.15), (-0.27, 0, 0.00001), (-0.42, 0.15, 0.00002), (-0.57, -0.00009, 0.00002), (-0.42, -0.15, 0.00002), (-0.27, 0, 0.00001), (0, 0, 0), (-0.00001, 0, 0.27), (0.00014, 0.15, 0.42), (0, 0, 0.57), (0.00017, -0.15, 0.42), (-0.00001, 0, 0.27), (-0.15, 0, 0.42), (0, 0, 0.57), (0.15, -0.00006, 0.42), (-0.00001, 0, 0.27), (-0.00003, 0, -0.27), (-0.00006, 0.15, -0.42), (-0.00004, 0, -0.57), (-0.00001, -0.15, -0.42), (-0.00003, 0, -0.27), (-0.15, 0, -0.42), (-0.00004, 0, -0.57), (0.15, -0.00006, -0.42)]
    ik_4pin = cmds.curve(n='ik_arm_4pin_curve',p=points, per=False, d=1, k=[i for i in range(len(points))])
    cmds.rotate( 0, 0, '-90deg', ik_4pin, pivot=(0, 0, 0) )
    cmds.setAttr(ik_4pin + '.rotateY', 90)
    cmds.makeIdentity(ik_4pin,a=True, t=1, r=1, s=1, n=0, pn=1)
    ik_4pin_List = cmds.listRelatives( ik_4pin, s=True )

    #empty group
    ik_ctrl= cmds.group(empty=True, n='ARM_IK_SCALE_TEST_DONT_DELETE')
    cmds.parent(ik_box_List[0], ik_arrows_List[0], ik_4pin_List[0], ik_ctrl, r=True, s=True)
    cmds.delete(ik_box,ik_arrows,ik_4pin)
    
    # Setting visibility
    
    if ikShape == 1:
        cmds.setAttr(ik_arrows_List[0] + '.visibility', 0)
        cmds.setAttr(ik_4pin_List[0] + '.visibility', 0)
    if ikShape == 2:
        cmds.setAttr(ik_box_List[0] + '.visibility', 0)
        cmds.setAttr(ik_4pin_List[0] + '.visibility', 0)
    if ikShape == 3:
        cmds.setAttr(ik_box_List[0] + '.visibility', 0)
        cmds.setAttr(ik_arrows_List[0] + '.visibility', 0)
    
    # Positioning the control
    tempCONST = cmds.parentConstraint(selected[1], ik_ctrl, mo=False)
    cmds.delete(tempCONST)
    tempCONST = cmds.parentConstraint(selected[-1], ik_ctrl, mo=False)
    cmds.delete(tempCONST)
    tempCONST= cmds.parentConstraint(selected[-1], ik_ctrl, mo=True)
    cmds.delete(tempCONST)

    icon_test_list.append(ik_ctrl)

    # Creating the FK icon
    # Circle
    fk_circle = cmds.circle( n='fk_arm_circle_curve', nr=(1, 0, 0), sw=360, c=(0, 0, 0),r=1,d=3,ut=0,tol=0.01,s=12)
    fk_circle_List = cmds.listRelatives(fk_circle, s=True)

    # Turn Arrow
    fk_turn = cmds.curve(d=1, p=[(1, 0, 0), (3, 0, -3), (5, 0, 0), (4, 0, 0), (4, 0, 4), (2, 0, 6), (-4, 0, 6), (-6, 0, 4), (-6, 0, 0), (-7, 0, 0), (-5, 0, -3), (-3, 0, 0), (-4, 0, 0), (-4, 0, 3), (-3, 0, 4), (1, 0, 4), (2, 0, 3), (2, 0, 0), (1, 0, 0), (3, 0, -3), (5, 0, 0), (4, 0, 0)], k=[i for i in range(22)])
    cmds.rotate( 0, '180deg', '90deg', fk_turn, pivot=(0, 0, 0) )
    cmds.makeIdentity(fk_turn, apply=True, t=1, r=1, s=1, n=0, pn=1)
    fk_turn_List = cmds.listRelatives(fk_turn, s=True)
    
    # empty group
    fk_ctrl = cmds.group(empty=True, n='ARM_FK_SCALE_TEST_DONT_DELETE')
    cmds.parent(fk_circle_List[0], fk_turn_List[0], fk_ctrl, r=True, s=True)
    cmds.delete(fk_circle,fk_turn)
    
    # Visibility
    if fkShape == 1:
        cmds.setAttr(fk_turn_List[0] + '.visibility', 0)
    if fkShape == 2:
        cmds.setAttr(fk_circle_List[0] + '.visibility', 0)    
    
    # Positioning icon
    tempCONST= cmds.parentConstraint(selected[0], fk_ctrl, mo=False)
    cmds.delete(tempCONST)
    icon_test_list.append(fk_ctrl)

    # Creating the PV icon
    # PV diamond
    pvDmd= cmds.curve(n='pv_dmnd_curve',d=1,p=[(0.0, -0.6630844559737615, 0.3329378246071956), (0.0, 4.6887170106272334e-07, 0.9960227494526567), (0.6630849248454597, 4.6887170106272334e-07, 0.33293782460719706), (0.0, -0.6630844559737615, 0.3329378246071956), (-0.6630849248454603, 4.6887170106272334e-07, 0.33293782460719706), (0.0, 4.6887170106272334e-07, 0.9960227494526567), (0.0, 0.6630844559737585, 0.33293782460719706), (-0.6630849248454603, 4.6887170106272334e-07, 0.33293782460719706), (0.0, 0.6630844559737585, 0.33293782460719706), (0.6630849248454597, 4.6887170106272334e-07, 0.33293782460719706), (0.0, 4.6887170106272334e-07, 0.9960227494526567), (0.0, 0.6630844559737585, 0.33293782460719706), (0.0, 0.6630844559737585, -0.3333176106856275), (0.6630849248454597, -4.6887170398374584e-07, -0.3329378246071942), (0.0, -0.00038025495013438904, -0.9960227494526552), (0.0, -0.6630844559737615, -0.3325580385287608), (0.6630849248454597, -4.6887170398374584e-07, -0.3329378246071942), (0.6630849248454597, 4.6887170106272334e-07, 0.33293782460719706), (0.0, -0.6630844559737615, 0.3329378246071956), (0.0, -0.6630844559737615, -0.3325580385287608), (-0.6630849248454603, -4.6887170398374584e-07, -0.3329378246071942), (-0.6630849248454603, 4.6887170106272334e-07, 0.33293782460719706), (-0.6630849248454603, -4.6887170398374584e-07, -0.3329378246071942), (0.0, 0.6630844559737585, -0.3333176106856275), (0.6630849248454597, -4.6887170398374584e-07, -0.3329378246071942), (0.0, -0.6630844559737615, -0.3325580385287608), (-0.6630849248454603, -4.6887170398374584e-07, -0.3329378246071942), (0.0, -0.00038025495013438904, -0.9960227494526552), (0.0, -0.6630844559737615, -0.3325580385287608), (0.6630849248454597, -4.6887170398374584e-07, -0.3329378246071942), (0.0, -0.00038025495013438904, -0.9960227494526552), (0.0, 0.6630844559737585, -0.3333176106856275), (-0.6630849248454603, -4.6887170398374584e-07, -0.3329378246071942), (0.0, -0.00038025495013438904, -0.9960227494526552)],k=[i for i in range(34)])
    pv_dmd_List = cmds.listRelatives(pvDmd, s=True)
    # PV arrow
    pvArrow = cmds.curve(n='pv_arrow_curve',d=1, p=[(0, 10.2, 0), (-10.2, -10.2, 10.2), (10.2, -10.2, 10.2), (0, 10.2, 0), (10.2, -10.2, -10.2), (10.2, -10.2, 10.2), (10.2, -10.2, -10.2), (-10.2, -10.2, -10.2), (0, 10.2, 0), (-10.2, -10.2, 10.2), (-10.2, -10.2, -10.2)],k=[i for i in range(11)])
    cmds.rotate( '90deg', 0, 0, pvArrow, pivot=(0, 0, 0) )
    cmds.scale(0.08, 0.08, 0.08, pvArrow)
    cmds.xform(pvArrow, pivots= [0,0,0], ws=True)
    cmds.makeIdentity(pvArrow, apply=True, t=1, r=1, s=1, n=0, pn=1)
    pv_arrow_List = cmds.listRelatives(pvArrow, s=True)

    # empty group
    pvIcon = cmds.group(empty=True, n='ARM_PV_SCALE_TEST_DONT_DELETE')
    cmds.parent(pv_dmd_List[0], pv_arrow_List[0], pvIcon, r=True, s=True)
    cmds.delete(pvDmd,pvArrow)

    # Visibility 
    if pvShape == 1:
        cmds.setAttr(pv_arrow_List[0] + '.visibility', 0)
    if pvShape == 2:
        cmds.setAttr(pv_dmd_List[0] + '.visibility', 0)   
    icon_test_list.append(pvIcon)

    # Making the hand icon
    # Circle
    handCircle= cmds.circle( n='hand_circle_curve', nr=(0, 1, 0), sw=360, c=(0, 0, 0),r=1,d=3,ut=0,tol=0.01,s=16)
    cmds.makeIdentity(handCircle, apply=True, t=1, r=1, s=1, n=0, pn=1)    
    handCircle_List = cmds.listRelatives(handCircle, s=True)

    # COG
    handCOG = cmds.curve(d=1, p=[(-20, 0, 10),(-20, 0, -10),(-30, 0, -10),(-30, 0, 20),(-20, 0, 30),(10, 0, 30),(20, 0, 20),(20, 0, -20),(10, 0, -20),(10, 0, 10),(10, 0, -30),(0, 0, -30),(0, 0, 10), (0, 0, -40),(-10, 0, -40),(-10, 0, 0),(-10, 0, -30),(-20, 0, -30),(-20, 0, -10)],k=[i for i in range(19)])
    cmds.rotate( 0, '-90deg', 0, handCOG, pivot=(0, 0, 0) )
    cmds.scale(0.1, 0.1, 0.1, handCOG)
    cmds.xform(handCOG, pivots= [0,0,0], ws=True)
    cmds.makeIdentity(handCOG, apply=True, t=1, r=1, s=1, n=0, pn=1)
    handCOG_List = cmds.listRelatives(handCOG, s=True)
    
    # empty group    
    handIcon = cmds.group(empty=True, n='ARM_HAND_SCALE_TEST_DONT_DELETE')
    cmds.parent(handCircle_List[0], handCOG_List[0], handIcon, r=True, s=True)
    cmds.delete(handCircle,handCOG)
    
    # Visibility 
    if handShape == 1:
        cmds.setAttr(handCOG_List[0] + '.visibility', 0)
    if handShape == 2:
        cmds.setAttr(handCircle_List[0] + '.visibility', 0) 
    
    # Positioning the control
    tempCONST = cmds.parentConstraint(selected[1], handIcon, mo=False)
    cmds.delete(tempCONST)
    tempCONST = cmds.parentConstraint(selected[-1], handIcon, mo=False)
    cmds.delete(tempCONST)
    icon_test_list.append(handIcon)

    # Getting the pole vector loocation
    pvLoc1 = cmds.spaceLocator(p=(0,0,0), name='pv1_local_loc')[0]
    cmds.setAttr('pv1_local_locShape.visibility', 0)
    pvPad1 = cmds.group(pvLoc1, name='pv1_local_pad')
    pvPad2 = cmds.group(pvIcon, name='pv2_pos_pad')
    pvPad1Main = cmds.group(pvPad1,pvPad2, name='pv1_main_pad')

    cmds.pointConstraint(selected[0],selected[-1],pvPad1, mo=False)
    cmds.aimConstraint(selected[0],pvPad1,mo=False,weight=1, aimVector=(-1,0,0), upVector=(0,1,0),worldUpType='objectrotation',worldUpObject=pvPad1Main)
    cmds.pointConstraint(selected[1],pvLoc1, skip=["y","z"], mo=False)
    cmds.pointConstraint(selected[1], pvPad2, mo=False)
    cmds.parentConstraint(selected[0], pvPad1Main, mo=True)
    cmds.aimConstraint(pvLoc1,pvPad2,mo=False,weight=1, aimVector=(0,0,1), upVector=(0,1,0),worldUpType='objectrotation',worldUpObject=pvLoc1)

    for each in ['.tx','.ty','.rx','.ry','.rz']:
        cmds.setAttr(pvIcon + each, lock=True, keyable=False, channelBox=False)

    # Visibility for main controls
    if armType == 1:
        cmds.setAttr(ik_ctrl + '.v', 1)
        cmds.setAttr(fk_ctrl + '.v', 0)
        cmds.setAttr(handIcon + '.v', 0)
        cmds.setAttr(pvIcon + '.v', pvType)
    if armType == 2:
        cmds.setAttr(ik_ctrl + '.v', 0)
        cmds.setAttr(pvIcon + '.v', 0)
        cmds.setAttr(fk_ctrl + '.v', 1)
        cmds.setAttr(handIcon + '.v', 0)
    if armType == 3:
        cmds.setAttr(ik_ctrl + '.v', 1)
        cmds.setAttr(pvIcon + '.v', pvType)
        cmds.setAttr(fk_ctrl + '.v', 1)
        cmds.setAttr(handIcon + '.v', 1)
  
    # Parenting all the preset arm rig
    armRefPad = cmds.group(empty=True, n='arm_refRig_pad')
    cmds.parent( ik_ctrl, fk_ctrl, pvPad1Main, handIcon, armRefPad )
    
    # settinng default scale value for the icons
    jointVal= cmds.getAttr(selected[1] + '.tx')
    finalVal= jointVal / 4
    for each in icon_test_list:
        cmds.scale( finalVal, finalVal, finalVal, each, relative=True)

def ikSetup(armType, oriName, labelName, iconColor, selected):
    global ik_joints, ikIconPick, newPVIcon
    # Variables
    pvType= cmds.radioButtonGrp("addPVElbow_Btn", q=True, sl=True)
    if armType == 3:
        ik_joints = []
        new_dup = cmds.duplicate(selected[0],rc=True)
        dup_list = cmds.ls(new_dup, dag=True, type='joint')
        counter = 1
        for each in dup_list:
            new_name = cmds.rename(each, oriName + labelName + '_IK' + str(counter) + '_waste')
            ik_joints.append(new_name)
            counter = counter + 1
    else:
        ik_joints = selected

    # Set up new IK control
    cmds.setAttr('ARM_IK_SCALE_TEST_DONT_DELETE.overrideEnabled', 1)
    cmds.setAttr('ARM_IK_SCALE_TEST_DONT_DELETE.overrideColor', (iconColor - 1))
    for each in ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz']:
        cmds.setAttr('ARM_IK_SCALE_TEST_DONT_DELETE' + each, lock=False, channelBox=True)
        cmds.setAttr('ARM_IK_SCALE_TEST_DONT_DELETE' + each, keyable=True)
    findConst = cmds.listConnections('ARM_IK_SCALE_TEST_DONT_DELETE.tx')
    if findConst:
        cmds.delete(findConst)
    cmds.makeIdentity('ARM_IK_SCALE_TEST_DONT_DELETE', apply=True, t=1, r=1, s=1, n=0, pn=1)
    ikIconPick = cmds.rename('ARM_IK_SCALE_TEST_DONT_DELETE', oriName + labelName + '_IK_icon')

    # IK handle Setup
    ikGrpTest = cmds.objExists('ikHandles_pad')
    if not ikGrpTest:
        ikHandles_pad = cmds.group(empty=True, n='ikHandles_pad')
    else:
        ikHandles_pad = 'ikHandles_pad'
    cmds.setAttr(ikHandles_pad + '.v', 0)
    ik = cmds.ikHandle(sj=ik_joints[0], ee=ik_joints[-1], sol='ikRPsolver', name=oriName + labelName + '_ikHandle')
    cmds.setAttr(ik[0] + ".snapEnable", 0)
    cmds.parent(ikIconPick, w=True)

    # Set up the pole vector/twist
    if pvType == 1:
        cmds.addAttr(ikIconPick, ln='PV_Twist', at='double', dv=0, k=True)
        cmds.connectAttr(ikIconPick + '.PV_Twist', ik[0] + '.twist', force=True)
    elif pvType == 2:
        cmds.setAttr('ARM_PV_SCALE_TEST_DONT_DELETE.overrideEnabled', 1)
        cmds.setAttr('ARM_PV_SCALE_TEST_DONT_DELETE.overrideColor', (iconColor - 1))
        for each in ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz']:
            cmds.setAttr('ARM_PV_SCALE_TEST_DONT_DELETE' + each, lock=False, channelBox=True)
            cmds.setAttr('ARM_PV_SCALE_TEST_DONT_DELETE' + each, keyable=True)
        cmds.parent('ARM_PV_SCALE_TEST_DONT_DELETE', w=True)
        cmds.delete('pv1_main_pad')
        newPVIcon = cmds.rename('ARM_PV_SCALE_TEST_DONT_DELETE', oriName + labelName + '_PV_icon')
        cmds.makeIdentity(newPVIcon, apply=True, t=1, r=1, s=1, n=0, pn=0)

        cmds.poleVectorConstraint(newPVIcon, ik[0])
        for each in ['.rx', '.ry', '.rz', '.sx', '.sy', '.sz']:
            cmds.setAttr(newPVIcon + each, lock=True, keyable=False, channelBox=False)

    # Connecting the ikHandle to the icon
    cmds.parentConstraint(ikIconPick, ik[0], mo=True)
    cmds.parent(ik[0], ikHandles_pad)
    for each in ['.sx', '.sy', '.sz']:
        cmds.setAttr(ikIconPick + each, lock=True, keyable=True, channelBox=False)

def fkSetup(armType, oriName, labelName, iconColor, selected):
    global fk_joints, fk01_pad
    
    # Naming the joints
    if armType == 3:
        fk_joints = []
        new_dup = cmds.duplicate(selected[0],rc=True)
        dup_list = cmds.ls(new_dup, dag=True, type='joint')
        counter = 1
        for each in dup_list:
            new_name = cmds.rename(each, oriName + labelName + '_FK' + str(counter) + '_waste')
            fk_joints.append(new_name)
            counter = counter + 1
    else:
        fk_joints = cmds.ls(sl=True, dag=True, type='joint')
    
    # Identifying the fk icon if it's there
    cmds.setAttr('ARM_FK_SCALE_TEST_DONT_DELETE.overrideEnabled', 1)
    cmds.setAttr('ARM_FK_SCALE_TEST_DONT_DELETE.overrideColor', (iconColor - 1))
    for each in ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.v']:
        cmds.setAttr('ARM_FK_SCALE_TEST_DONT_DELETE' + each, lock=False, channelBox=True)
        cmds.setAttr('ARM_FK_SCALE_TEST_DONT_DELETE' + each, keyable=True)
    testScale = cmds.getAttr('ARM_FK_SCALE_TEST_DONT_DELETE.scaleY')
    findConst = cmds.listConnections('ARM_FK_SCALE_TEST_DONT_DELETE.tx')
    if findConst:
        cmds.delete(findConst)
    cmds.makeIdentity('ARM_FK_SCALE_TEST_DONT_DELETE', apply=True, t=1, r=1, s=1, n=0, pn=1)
    fkIconPick = cmds.rename('ARM_FK_SCALE_TEST_DONT_DELETE', oriName + labelName + '_FK_01_icon')

    # Padding the icon
    fk01_pad = cmds.group(empty=True, name=oriName + labelName + '_FK_01_pad')
    temp_const = cmds.parentConstraint(fk_joints[0], fk01_pad, mo=False)
    cmds.delete(temp_const)
    cmds.parent(fkIconPick, fk01_pad)
    cmds.makeIdentity(fkIconPick, apply=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parentConstraint(fkIconPick, fk_joints[0])

    # Create the 2nd icon
    fk_dup = cmds.duplicate(fkIconPick)
    fk2_icon = cmds.rename(fk_dup[0], oriName + labelName + '_FK_02_icon')
    fk2_pad = cmds.group(empty=True, name=oriName + labelName + '_FK_02_pad')

    temp_const = cmds.parentConstraint(fk_joints[1], fk2_pad, mo=False)
    cmds.delete(temp_const)
    cmds.parent(fk2_icon, fk2_pad)
    cmds.setAttr(fk2_icon + '.translate', 0, 0, 0)
    cmds.setAttr(fk2_icon + '.rotate', 0, 0, 0)
    cmds.parentConstraint(fk2_icon, fk_joints[1])

    for each in ['tx', 'ty', 'tz', 'rx', 'rz', 'sx', 'sy', 'sz']:
        cmds.setAttr(fk2_icon + '.' + each, lock=True, keyable=False, channelBox=False)
    cmds.parent(fk2_pad, fkIconPick)

    for each in ['tx', 'ty', 'tz', 'sx', 'sy', 'sz']:
        cmds.setAttr(fkIconPick + '.' + each, lock=True, keyable=False, channelBox=False)

def autoArmRig():
    #Variables
    armType = cmds.radioButtonGrp('armType_Btn',q=True, sl=True)
    selected = cmds.ls(sl=True, dag=True, type='joint')
    oriName = cmds.optionMenu('ori_Menu', q=True, v=True)
    labelName = cmds.optionMenu('label_Menu', q=True, v=True)
    iconColor = cmds.colorIndexSliderGrp('armColor', q=True, v=True)

    #Naming
    new_list = []
    counter = 1
    for each in selected:
        newJoint = cmds.rename(each, oriName + labelName + str(counter) + '_bind')
        counter = counter + 1
        new_list.append(newJoint)
    wasteName = new_list[-1].replace('_bind', '_waste')
    wasteFinal = cmds.rename(new_list[-1], wasteName)
    selected = cmds.ls(new_list[0], dag=True, type='joint')

    # Making a joint pad
    pad = cmds.group( name= oriName + labelName + 'pad', empty=True )
    temp = cmds.pointConstraint(selected[0], pad, mo=False)
    cmds.delete(temp)
    cmds.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parent(selected[0], pad)

    if armType == 1:
        ikSetup(armType, oriName, labelName, iconColor, selected)
    if armType == 2:
        fkSetup(armType, oriName, labelName, iconColor, selected)
    if armType == 3:
        ikSetup(armType, oriName, labelName, iconColor, selected)
        fkSetup(armType, oriName, labelName, iconColor, selected)

        ik_list = ik_joints
        fk_list = fk_joints

        switchConst1 = cmds.orientConstraint(ik_list[0], fk_list[0], selected[0])
        switchConst2 = cmds.orientConstraint(ik_list[1], fk_list[1], selected[1])

        #Adding hand icon and attr
        cmds.setAttr('ARM_HAND_SCALE_TEST_DONT_DELETE.overrideEnabled',1)
        cmds.setAttr('ARM_HAND_SCALE_TEST_DONT_DELETE.overrideColor',(iconColor-1))
        cmds.makeIdentity('ARM_HAND_SCALE_TEST_DONT_DELETE', apply=True, t=1, r=1, s=1, n=0, pn=1)
        handPick = cmds.rename('ARM_HAND_SCALE_TEST_DONT_DELETE', oriName + labelName + '_hand_icon')
        cmds.parent(handPick, w=True)
        cmds.addAttr(handPick, ln="IKFK_switch", at="double", min=0, max=1, dv=0, k=True)

        sel_len = len(selected)
        counter = 0
        while (counter<(sel_len-1)):
                cmds.setAttr(handPick + '.IKFK_switch', 0)
                print(selected[counter] + '_orientConstraint1')
                cmds.setAttr(selected[counter] + '_orientConstraint1' + '.' + ik_list[counter] + 'W0', 1)
                cmds.setAttr(selected[counter] + '_orientConstraint1' + '.' + fk_list[counter] + 'W1', 0)
                cmds.setDrivenKeyframe(selected[counter] + '_orientConstraint1' +'.' +  ik_list[counter] + 'W0', cd= handPick + '.IKFK_switch' )
                cmds.setDrivenKeyframe(selected[counter] + '_orientConstraint1' +'.' +  fk_list[counter] + 'W1', cd= handPick + '.IKFK_switch' )
                cmds.setAttr(handPick + '.IKFK_switch',1)
                cmds.setAttr(selected[counter] + '_orientConstraint1' + '.' + ik_list[counter] + 'W0', 0)
                cmds.setAttr(selected[counter] + '_orientConstraint1' + '.' + fk_list[counter] + 'W1', 1)
                cmds.setDrivenKeyframe(selected[counter] + '_orientConstraint1' +'.' +  ik_list[counter] + 'W0', cd= handPick + '.IKFK_switch' )
                cmds.setDrivenKeyframe(selected[counter] + '_orientConstraint1' +'.' +  fk_list[counter] + 'W1', cd= handPick + '.IKFK_switch' )
                cmds.setAttr(handPick + '.IKFK_switch',0)
                counter = counter + 1

        # adding the visibility swap
        cmds.setAttr( handPick + '.IKFK_switch', 0)
        cmds.setAttr( ikIconPick + '.visibility', 1)
        cmds.setAttr( newPVIcon + '.visibility', 1)
        cmds.setAttr( fk01_pad + '.visibility', 0)
        cmds.setDrivenKeyframe( fk01_pad + '.visibility', cd= handPick + '.IKFK_switch')
        cmds.setDrivenKeyframe( ikIconPick + '.visibility', cd= handPick + '.IKFK_switch')
        cmds.setDrivenKeyframe( newPVIcon + '.visibility', cd= handPick + '.IKFK_switch')
        cmds.setAttr( handPick + '.IKFK_switch', 1)
        cmds.setAttr( ikIconPick + '.visibility', 0)
        cmds.setAttr( newPVIcon + '.visibility', 0)
        cmds.setAttr( fk01_pad + '.visibility', 1)
        cmds.setDrivenKeyframe( fk01_pad + '.visibility', cd= handPick + '.IKFK_switch')
        cmds.setDrivenKeyframe( ikIconPick + '.visibility', cd= handPick + '.IKFK_switch')
        cmds.setDrivenKeyframe( newPVIcon + '.visibility', cd= handPick + '.IKFK_switch')
        cmds.setAttr( handPick + '.IKFK_switch', 0)

        cmds.setAttr(ikIconPick + '.visibility', lock=True, keyable=False, channelBox=False)
        cmds.setAttr(newPVIcon + '.visibility', lock=True, keyable=False, channelBox=False)
    if (cmds.objExists(armRefPad) == True):
        cmds.delete(armRefPad)