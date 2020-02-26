'''
ByrdRigs Interface tool

import BR_InterfaceTool
reload (BR_InterfaceTool)
BR_InterfaceTool.gui()

'''

import pymel.core as pm
import maya.cmds as cmds

# Still needs the control tab with the icons 
# Working on the quad and biped setups

tab_bgc=(0.4718592, 0.13568, 239)
subTab_bgc = (0.4915200, 0.32256, 241)
window_bgc = (.2,.2,.2)
color_1 = (.141,.725,.627)
color_2 = (.078, .678, .557)
color_3 = (.059, .612, .749)
color_4 = (.059, .475, .616)
color_5 = (.059, .392, .663)
color_6 = (.224, .259, .894)
color_7 = (.475, .278, .925)
color_8 = (.447, .145, .965)
color_9 = (.475, .078, .678)
color_10 = (.529, .078, .678)


def gui():

	if pm.window('ByrdRigs_interface_toolset', q=1, exists=1):
		pm.deleteUI('ByrdRigs_interface_toolset')
		#ByrdRigs_interface_toolset
		

	win_width = 240
	window_object = pm.window('ByrdRigs_interface_toolset', title="ByrdRigs_interface_toolset", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()


	'''
	Clean Up Geo and Controls

	'''
	pm.frameLayout(w=win_width, label='Clean Up', bgc=(color_1), cl=True, cll=True, ann='Clean Up', cc=windowResize)
	pm.rowColumnLayout(w=win_width)
	pm.iconTextButton('delete_histroy', w=166, st='iconAndTextHorizontal', image1='DeleteHistory.png',label='Delete History', c=deleteHistory)
	pm.iconTextButton(w=166, st='iconAndTextHorizontal', image1='CenterPivot.png',label='Center Pivot', c=centerPivot)
	pm.iconTextButton(w=166, st='iconAndTextHorizontal', image1='FreezeTransform.png',label='Freeze Transforms', c=freezeTransform)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=(color_1), st='in')

	'''
	Visibility
	'''
	pm.frameLayout(w=win_width, label='Visibility', bgc=(color_2), cl=True, cll=True, ann='Change Visibility', cc=windowResize)
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='Show')
	pm.button(label='All', c=showAll)
	pm.button(label='None', c=showNone)
	pm.text(label='Poly Vis')
	pm.button(label='On', c=polyOn)
	pm.button(label='Off', c=polyOff)
	pm.text(label='Joints')
	pm.button(label='On', c=jointsOn)
	pm.button(label='Off', c=jointsOff)
	pm.text(label='X-Ray Joints')
	pm.button(label='On', c=xRayOn)
	pm.button(label='Off', c=xRayOff)
	pm.text(label='Wire Shaded')
	pm.button(label='On', c=wireOn)
	pm.button(label='Off', c=wireOff)
	pm.text(label='NURBS Curves')
	pm.button(label='On', c=curvesOn)
	pm.button(label='Off', c=curvesOff)
	pm.text(label='NURBS Surfaces')
	pm.button(label='On', c=surfacesOn)
	pm.button(label='Off', c=surfacesOff)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=(color_2), st='in')

	'''
	Tools
	'''
	pm.frameLayout(w=win_width, label='Tools', bgc=(color_3), cl=True, cll=True, ann='Different Tools', cc=windowResize)
	pm.columnLayout()
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinJoint.png', label='Create Joint Tool', c=jointTool)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinMirrorJoint_S.png', label='Mirror Joint Tool', c=mirrorTool)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='menuIconDisplay.png', label='Joint Size', c=jointSize)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinInsert.png', label='Insert Joint', c=insertJoint)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='menuIconDisplay.png', label='IK Handle Size', c=IkSize)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='hierarchy.png', label='Select Hierarchy', c=hierarchy)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='testNameTag.svg', label='Renamer', c=renamerWindow)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='circle.png', label='Curve Tool Window', c=curveWindow)
	pm.separator(w=win_width, bgc=(color_3), st='in')
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='IK Handle Tool')
	pm.button(label='RP', c=RP_IkHandle)
	pm.button(label='SC', c=SC_IkHandle)
	pm.text(label='Padding')
	pm.button(label='Jnt' , c=jointPadding)
	pm.button(label='Ctrl', c=ctrlPadding)
	# pm.text('Renamer')
	# pm.button(label='Jnt', c=jointRenamer)
	# pm.button(label='Ctrl',c=ctrlRenamer, ann='For control chains')

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=(color_4), st='in')
	
	'''
	Constraints
	'''
	pm.frameLayout(w=win_width, label='Constraints', bgc=(color_4), cl=True, cll=True, ann='Constraints', cc=windowResize)
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='Parent MO')
	pm.button(label='On', c=parentConstraint_on)
	pm.button(label='Off', c=parentConstraint_off)
	pm.text(label='Point MO')
	pm.button(label='On', c=pointConstraint_on)
	pm.button(label='Off', c=pointConstraint_off)
	pm.text(label='Orient MO')
	pm.button(label='On', c=orientConstraint_on)
	pm.button(label='Off', c=orientConstraint_off)
	pm.button(w=win_width, label='Pole Vector', c=poleVector)
	
	
	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=(color_4), st='in')


	'''
	Bipeds
	'''
	biped_layout = pm.frameLayout(w=win_width, label='Bipeds', bgc=(color_5), cl=True, cll=True, ann='Biped Tools', cc=windowResize)
	pm.frameLayout(w=win_width, label='Back (Based on 7 joints)', bgc=(color_6), cl=True, cll=True, cc=windowResize)
	pm.text(label='Step 1: Pad the back bind joints')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label='Step 2: Create a curve following the joints', w=win_width)
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label='Step 3: Parent the curve under back pad grp', w=win_width)
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label='Step 4: Duplicate the back bind joints twice', w=win_width)
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label='Step 5: Select pad and duplicated 01_bind', w=win_width)
	pm.text(label='joints')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label='Step 6: Hit the setup buttom', w=win_width)
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.button(label='Setup', w=win_width, c=backSetup)
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label='Step 7: Select the ikHandle and go to the')
	pm.text(label='advanced twist contols')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label="Step 8: Change the world up object to the")
	pm.text(label="first 'curveBind'")
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.text(label="Step 9: Change the world up object 2 to the")
	pm.text(label="second 'curveBind'")
	pm.setParent(biped_layout)

	pm.frameLayout(w=win_width, label='Neck (Based on 4 joints)', bgc=(color_7), cl=True, cll=True, cc=windowResize)
	pm.text(label='Select the neck bind joints', w=win_width)
	pm.button(label='Ik/Fk System', w=win_width, c=neckSetup)

	pm.setParent(biped_layout)

	pm.frameLayout(w=win_width, label='Arms', bgc=(color_8), cl=True, cll=True, cc=windowResize)
	pm.button(label='Arm IK/FK Joints', w=win_width, ann='Creates Arm ik/fk joints', c=bipedArm_joints)
	pm.text(label='Select the bind, ik, and fk joints', w=win_width)
	pm.button(label='IK/FK System', w=win_width, c=bipedArm_system)
	pm.button(label='Twist Setup Window', w=win_width, c=twistWindow)
	pm.setParent(biped_layout)

	pm.frameLayout(w=win_width, label='Legs', bgc=(color_9), cl=True, cll=True, cc=windowResize)
	pm.button(label='Leg IK/FK Joints', w=win_width, ann='Creates Leg ik/fk joints', c=bipedLeg_joints)
	pm.text(label='Select the bind, ik, and fk joints', w=win_width)
	pm.button(label='IK/FK System', w=win_width, c=bipedLeg_system)	
	pm.setParent(biped_layout)

	pm.frameLayout(w=win_width, label='Feet', bgc=(color_10), cl=True, cll=True, cc=windowResize)
	pm.text(label='RFL Prep - Move the locators', w=win_width)
	pm.button(label='Create Locators - Select the bind', w=win_width, c=rflPrep)
	pm.text(label='Select the foot icon and the heel locator', w=win_width)
	pm.button(label='RFL System', w=win_width, c=rflSystem)



	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=(color_5), st='in')

	'''
	Quadrupeds
	'''
	quad_layout = pm.frameLayout(w=win_width, label='Quadrupeds', bgc=(color_6), cl=True, cll=True, ann='Quadruped Tools', cc=windowResize )
	pm.setParent(quad_layout)
	pm.frameLayout(w=win_width, label='Hind Legs', bgc=(color_7), cl=True, cll=True, cc=windowResize)
	pm.text(label='orientation_h(Leg, LegIK, then LegFK)', w=win_width, al='center')
	pm.button(label='Hind IK/FK/Helper Joints',w=win_width, ann='Creates leg ik/fk/helper joint chains', c=quad_hLeg_joints)
	pm.text(label='Select the bind, ik, helper, and fk joints', w=win_width)
	pm.button(label='hLeg IK/FK System', w=win_width,  ann='Sets up the hind leg IK/FK systems', c=quad_hIKFK_system)
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='Leg SDKs')
	pm.button(label='lt', c=lt_hLeg_SDKs)
	pm.button(label='rt', c=rt_hLeg_SDKs)
	


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=(color_6), st='in')

	'''
	Zero Out Attributes
	'''
	pm.frameLayout(w=win_width, label='Zero Out', bgc=(color_7), cl=True, cll=True, ann='Zero Out the Attributes to defaults', cc=windowResize)
	pm.columnLayout()
	pm.button(label='Human Foot Attributes', w=win_width, c=setZeroHumanFoot, ann='Sets Custom Foot Attributes back to defaults')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.button(label='Human Hand Attributes', w=win_width, c=setZeroHumanHand, ann='Sets Custom Hand Attributes back to defaults')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.rowColumnLayout(nc=3, cw=[[1, 80], [2, 80],[3, 80]])
	pm.button(label='Translate', c=setZeroTr)
	pm.button(label='Rotate', c=setZeroRo)
	pm.button(label='Scale', c=setZeroSc)


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=(color_7), st='in') 

	pm.window('ByrdRigs_interface_toolset', e=1, wh=(240, 110), rtf=True)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

def deleteHistory(*args):
	pm.delete(ch=True)
	print 'History Deleted'

def centerPivot(*args):
	pm.xform(cpc=True)
	print 'Selected pivot centered.'

def freezeTransform(*agrs):
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	print 'Transform Frozen'

panel_1 = 'modelPanel1' 
panel_2 =  'modelPanel2' 
panel_3 = 'modelPanel3' 
panel_4 = 'modelPanel4'
# print 'Panel 1:', panel_1
# print 'Panel 2:', panel_2
# print 'Panel 3:', panel_3
# print 'Panel 4:', panel_4
show_1 = 'MainPane|viewPanes|modelPanel1|modelPanel1|menu14'
show_2 = 'MainPane|viewPanes|modelPanel2|modelPanel2|menu18'
show_3 = 'MainPane|viewPanes|modelPanel3|modelPanel3|menu22'
show_4 = 'MainPane|viewPanes|modelPanel4|modelPanel4|menu26'
# print 'Panel 1 Show menu:', show_1
# print 'Panel 2 Show menu:', show_2
# print 'Panel 3 Show menu:', show_3
# print 'Panel 4 Show menu:', show_4

def showAll(*args):
	print 'Show All'
	pm.modelEditor(panel_1, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_1, panel_1, "modelPanel1", "Playblast Display")

	pm.modelEditor(panel_2, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_2, panel_2, "modelPanel2", "Playblast Display")

	pm.modelEditor(panel_3, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_3, panel_3, "modelPanel3", "Playblast Display")

	pm.modelEditor(panel_4, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_4, panel_4, "modelPanel4", "Playblast Display")

def showNone(*args):
	print 'Show None'
	pm.modelEditor(panel_1, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_1, panel_1, "modelPanel1", "Playblast Display")

	pm.modelEditor(panel_2, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_2, panel_2, "modelPanel2", "Playblast Display")

	pm.modelEditor(panel_3, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_3, panel_3, "modelPanel3", "Playblast Display")

	pm.modelEditor(panel_4, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_4, panel_4, "modelPanel4", "Playblast Display")

def polyOn(*args):
	print 'Polygons visible'
	pm.modelEditor(panel_1, e=1, polymeshes=True)
	pm.modelEditor(panel_1, e=1, hos=True)
	pm.modelEditor(panel_2, e=1, polymeshes=True)
	pm.modelEditor(panel_2, e=1, hos=True)
	pm.modelEditor(panel_3, e=1, polymeshes=True)
	pm.modelEditor(panel_3, e=1, hos=True)
	pm.modelEditor(panel_4, e=1, polymeshes=True)
	pm.modelEditor(panel_4, e=1, hos=True)

def polyOff(*args):
	print 'Polygons hidden'
	pm.modelEditor(panel_1, e=1, polymeshes=False)
	pm.modelEditor(panel_1, e=1, hos=False)
	pm.modelEditor(panel_2, e=1, polymeshes=False)
	pm.modelEditor(panel_2, e=1, hos=False)
	pm.modelEditor(panel_3, e=1, polymeshes=False)
	pm.modelEditor(panel_3, e=1, hos=False)
	pm.modelEditor(panel_4, e=1, polymeshes=False)
	pm.modelEditor(panel_4, e=1, hos=False)

def jointsOn(*args):
	print 'Joints visible'
	pm.modelEditor(panel_1, e=1, joints = True)
	pm.modelEditor(panel_1, e=1, hos = True)
	pm.modelEditor(panel_2, e=1, joints = True)
	pm.modelEditor(panel_2, e=1, hos = True)
	pm.modelEditor(panel_3, e=1, joints = True)
	pm.modelEditor(panel_3, e=1, hos = True)
	pm.modelEditor(panel_4, e=1, joints = True)
	pm.modelEditor(panel_4, e=1, hos = True)

def jointsOff(*args):
	print 'Joints hidden'
	pm.modelEditor(panel_1, e=1, joints = False)
	pm.modelEditor(panel_1, e=1, hos = False)
	pm.modelEditor(panel_2, e=1, joints = False)
	pm.modelEditor(panel_2, e=1, hos = False)
	pm.modelEditor(panel_3, e=1, joints = False)
	pm.modelEditor(panel_3, e=1, hos = False)
	pm.modelEditor(panel_4, e=1, joints = False)
	pm.modelEditor(panel_4, e=1, hos = False)

def xRayOn(*args):
	print 'X-Ray Joints visible'
	pm.modelEditor(panel_1, e=1, jointXray = True)
	pm.modelEditor(panel_1, e=1, hos = True)
	pm.modelEditor(panel_2, e=1, jointXray = True)
	pm.modelEditor(panel_2, e=1, hos = True)
	pm.modelEditor(panel_3, e=1, jointXray = True)
	pm.modelEditor(panel_3, e=1, hos = True)
	pm.modelEditor(panel_4, e=1, jointXray = True)
	pm.modelEditor(panel_4, e=1, hos = True)

def xRayOff(*args):
	print 'X-Ray Joints hidden'
	pm.modelEditor(panel_1, e=1, jointXray = False)
	pm.modelEditor(panel_1, e=1, hos = False)
	pm.modelEditor(panel_2, e=1, jointXray = False)
	pm.modelEditor(panel_2, e=1, hos = False)
	pm.modelEditor(panel_3, e=1, jointXray = False)
	pm.modelEditor(panel_3, e=1, hos = False)
	pm.modelEditor(panel_4, e=1, jointXray = False)
	pm.modelEditor(panel_4, e=1, hos = False)

def wireOn(*args):
	print 'Wireframe on Shaded On'
	pm.mel.setWireframeOnShadedOption(True, panel_1)
	pm.mel.setWireframeOnShadedOption(True, panel_2)
	pm.mel.setWireframeOnShadedOption(True, panel_3)
	pm.mel.setWireframeOnShadedOption(True, panel_4)

def wireOff(*args):
	print 'Wireframe On Shaded Off'
	pm.mel.setWireframeOnShadedOption(False, panel_1)
	pm.mel.setWireframeOnShadedOption(False, panel_2)
	pm.mel.setWireframeOnShadedOption(False, panel_3)
	pm.mel.setWireframeOnShadedOption(False, panel_4)

def curvesOn(*args):
	print 'NURBS Curves visible'
	pm.modelEditor(panel_1, e=1, nurbsCurves=True)
	pm.modelEditor(panel_2, e=1, nurbsCurves=True)
	pm.modelEditor(panel_3, e=1, nurbsCurves=True)
	pm.modelEditor(panel_4, e=1, nurbsCurves=True)

def curvesOff(*args):
	print 'NURBS Curves hidden'
	pm.modelEditor(panel_1, e=1, nurbsCurves=False)
	pm.modelEditor(panel_2, e=1, nurbsCurves=False)
	pm.modelEditor(panel_3, e=1, nurbsCurves=False)
	pm.modelEditor(panel_4, e=1, nurbsCurves=False)

def surfacesOn(*args):
	print 'NURBS Surfaces visible'
	pm.modelEditor(panel_1, e=1, nurbsSurfaces=True)
	pm.modelEditor(panel_2, e=1, nurbsSurfaces=True)
	pm.modelEditor(panel_3, e=1, nurbsSurfaces=True)
	pm.modelEditor(panel_4, e=1, nurbsSurfaces=True)

def surfacesOff(*args):
	print 'NURBS Surfaces hidden'
	pm.modelEditor(panel_1, e=1, nurbsSurfaces=False)
	pm.modelEditor(panel_2, e=1, nurbsSurfaces=False)
	pm.modelEditor(panel_3, e=1, nurbsSurfaces=False)
	pm.modelEditor(panel_4, e=1, nurbsSurfaces=False)

def jointTool(*args):
	print 'Joint Tool Active.'
	pm.mel.JointTool()

def mirrorTool(*args):
	print 'Mirroring Joints'
	selection = pm.ls(sl=True) 
	for each in selection:
		pm.mirrorJoint(each, searchReplace=("lt", "rt"), mirrorYZ=1)

def jointSize(*args):
	print 'Changing Joint Size.'
	pm.mel.jdsWin()

def insertJoint(*args):
	print 'Joint Tool Active.'
	pm.mel.InsertJointTool()

def hierarchy(*args):
	print 'Hierarchy Selected'
	pm.mel.SelectHierarchy()

def renamerWindow(*args):
	import Quick_rename_tool
	reload (Quick_rename_tool)
	Quick_rename_tool.Quick_rename_tool()

	# Not my script, I downloaded it from highend3d.com I changed the colors though.

def curveWindow(*args):
	import BR_curve_tool
	reload (BR_curve_tool)
	BR_curve_tool.windowCreation()

def RP_IkHandle(*args):
	print 'RP IK Handle Tool.'
	pm.ikHandle()

def SC_IkHandle(*args):
	print 'SC IK Handle Tool.'
	pm.ikHandle(sol='ikSCsolver')

def IkSize(*args):
	print 'Changing IK Handle Size'
	pm.mel.ikHdsWin()

def jointPadding(*args):
	'''
	This creates a world orientated pad on the root joint.

	import byrdCheyenne_riggingTools
	reload(byrdCheyenne_riggingTools)
	byrdCheyenne_riggingTools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:' , selected 
	root_joint = selected[0]

	# Create empty group
	# empty=True will create an empty group 
	# 
	pad = pm.group(empty=True)

	# Move group to joint.
	# 	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transformation on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def ctrlPadding(*args):
	selected = pm.ls(selection=True)
	#print 'Current Selected:' , selected 
	root_joint = selected[0]

	local = pm.group(empty=True)
	temp_constraint =pm.parentConstraint(root_joint, local)
	pm.delete(temp_constraint)
	pm.parent(root_joint, local)
	local_name = root_joint.replace('_icon', '_local')
	# print(local_name)
	local.rename(local_name)

def parentConstraint_on(*args):
	print 'Parent Constraint with Maintain Offset On'
	selection = pm.ls(sl=True)
	pm.parentConstraint(selection, mo=True)

def parentConstraint_off(*args):
	print 'Parent Constraint with Maintain Offset Off'
	selection = pm.ls(sl=True)
	pm.parentConstraint(selection, mo=False)

def pointConstraint_on(*args):
	print 'Point Constraint with Maintain Offset On'
	selection = pm.ls(sl=True)
	pm.pointConstraint(selection, mo=True)

def pointConstraint_off(*args):
	print 'Point Constraint with Maintain Offset Off'
	selection = pm.ls(sl=True)
	pm.pointConstraint(selection, mo=False)

def orientConstraint_on(*args):
	print 'Orient Constraint with Maintain Offset On'
	selection = pm.ls(sl=True)
	pm.orientConstraint(selection, mo=True)

def orientConstraint_off(*args):
	print 'Orient Constraint with Maintain Offset Off'
	selection = pm.ls(sl=True)
	pm.orientConstraint(selection, mo=False)

def poleVector(*args):
	print 'Pole Vector Constraint'
	selection = pm.ls(sl=True)
	driver = selection[0]
	driven = selection[1]
	pm.poleVectorConstraint(driver, driven)

def backSetup(*args):
	import BR_7Joint_backSetup
	reload (BR_7Joint_backSetup)
	BR_7Joint_backSetup.back()

def neckSetup(*args):
	import BR_4Joint_neckSetup
	reload (BR_4Joint_neckSetup)
	BR_4Joint_neckSetup.neck()

def bipedArm_joints(*args):
	joint_system = pm.ls(selection=True, dag=True)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	# print 'Root Joint:', root_joint
	# print 'Joint 2:', joint_2
	# print 'Joint 3:', joint_3
	pm.duplicate(root_joint)
	ik_joints = pm.ls(selection=True, dag=True)
	ik_root_joint = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	# print 'Ik Root Joint:', ik_root_joint
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3

	ik_joint_name = root_joint.replace('bind', 'ik')
	ik_root_joint.rename(ik_joint_name)

	ik_joint_name = joint_2.replace('bind', 'ik')
	ik_joint_2.rename(ik_joint_name)

	ik_joint_name = joint_3.replace('waste', 'ik')
	ik_joint_3.rename(ik_joint_name)
	

	pm.duplicate(ik_root_joint)
	fk_joints = pm.ls(selection=True, dag=True)
	fk_root_joint = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	# print 'Ik Root Joint:', fk_root_joint
	# print 'Ik Joint 2:', fk_joint_2
	# print 'Ik Joint 3:', fk_joint_3

	fk_joint_name = root_joint.replace('bind', 'fk')
	fk_root_joint.rename(fk_joint_name)

	fk_joint_name = joint_2.replace('bind', 'fk')
	fk_joint_2.rename(fk_joint_name)

	fk_joint_name = joint_3.replace('waste', 'fk')
	fk_joint_3.rename(fk_joint_name)

def bipedArm_system(*args):
	joint_systems = pm.ls(selection=True)
	
	arm_root = joint_systems[0]
	ik_root = joint_systems[1]
	fk_root = joint_systems[2]

	arm_joints = pm.ls(arm_root, dag=True)
	ik_joints = pm.ls(ik_root, dag=True)
	fk_joints = pm.ls(fk_root, dag=True)
	print 'Arm System:', arm_joints
	print 'IK System:', ik_joints
	print 'FK Systems:', fk_joints

	arm_root_joint = pm.ls(arm_joints[0])
	arm_joint_2 = pm.ls(arm_joints[1])
	arm_joint_3 = pm.ls(arm_joints[2])
	# print 'Arm root joint:', arm_root_joint
	# print '2nd arm joint:', arm_joint_2 
	# print '3rd arm joint:', arm_joint_3
	
	ik_root_joint = pm.ls(ik_joints[0])
	ik_joint_2 = pm.ls(ik_joints[1])
	ik_joint_3 = pm.ls(ik_joints[2])
	# print 'IK Arm root joint:', ik_root_joint
	# print '2nd ik joint:', ik_joint_2 
	# print '3rd ik joint:', ik_joint_3

	fk_root_joint = pm.ls(fk_joints[0])
	fk_joint_2 = pm.ls(fk_joints[1])
	fk_joint_3 = pm.ls(fk_joints[2])
	# print 'FK Arm root joint:', fk_root_joint
	# print '2nd fk joint:', fk_joint_2 
	# print '3rd fk joint:', fk_joint_3

	orient_blend_1 = pm.orientConstraint(ik_root_joint, fk_root_joint, arm_root_joint)
	orient_blend_2 = pm.orientConstraint(ik_joint_2, fk_joint_2, arm_joint_2)


	pm.xform(ik_joint_2, ro= [0, 5, 0])
	pm.joint(ik_joint_2, spa=1, ch=1, e=1)
	pm.xform(ik_joint_2, ro= [0, 0, 0])

	pm.select(ik_root_joint, ik_joint_3)
	ikh = pm.ikHandle()[0]

	ikh_name = ik_root.replace('01_ik', 'ikh')
	ikh.rename(ikh_name)

	'''
	Create the arm icon
	'''
	arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	temp_constraint = pm.pointConstraint(arm_joint_3, arm_icon)
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()

	pm.parent(ikh, arm_icon)

	'''
	Rename arm icon
	'''
	arm_icon_name = arm_root.replace('01_bind', 'icon')
	arm_icon.rename(arm_icon_name)


	'''
	Create the elbow icon.
	'''

	elbow_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
	pm.select('curve1.cv[0]', 'curve1.cv[6]', 'curve1.cv[12]', 'curve1.cv[18]', 'curve1.cv[24]', r=1)
	pm.cmds.move(0, -0.982783, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[22]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[23]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[19]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[20]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[16]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[17]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[13]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[14]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[10]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[11]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[7]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[8]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[4]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[5]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[1]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[2]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	
	pm.select(elbow_icon)
	centerPivot(elbow_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the elbow icon.
	'''
	temp_constraint = pm.pointConstraint(arm_joint_2, elbow_icon)
	pm.delete(temp_constraint)
	freezeTransform(elbow_icon)
	pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
	freezeTransform(elbow_icon)

	'''
	Rename elbow icon
	'''
	elbow_icon_name = arm_root.replace('arm_01_bind', 'elbow_icon')
	elbow_icon.rename(elbow_icon_name)

	'''
	Create the pole vector for the elbow
	'''
	pm.poleVectorConstraint(elbow_icon, ikh)


	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_pad_1)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_1, fk_pad_1)
	pm.select(fk_icon_1)
	freezeTransform()


	fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 2:', fk_icon_2
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_icon_2)
	pm.delete(temp_constraint)
	fk_pad_2 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_pad_2)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_2, fk_pad_2)
	pm.select(fk_icon_2)
	freezeTransform()
	pm.parent(fk_pad_2, fk_icon_1)

	'''
	Rename the icons and the pads
	'''
	fk_icon1_name = fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name)

	'''
	Orient constraaint the icons to the fk joints
	'''
	pm.orientConstraint(fk_icon_1, fk_root_joint)
	pm.orientConstraint(fk_icon_2, fk_joint_2)


	'''
	Create the IK/FK switch
	'''
	ikfk_shape_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	ikfk_shape_2 = pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)
	ikfk_shape_3 = pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)
	ikfk_shape_4 = pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)

	shape_name_1 = arm_root.replace('arm_01_bind', 'ikfk_curve1') 
	# print 'Shape 1 Name:', shape_name_1
	ikfk_shape_1.rename(shape_name_1)
	
	shape_name_2 = arm_root.replace('arm_01_bind', 'ikfk_curve2') 
	# print 'Shape 2 Name:', shape_name_2
	ikfk_shape_2.rename(shape_name_2)

	shape_name_3 = arm_root.replace('arm_01_bind', 'ikfk_curve3') 
	# print 'Shape 3 Name:', shape_name_3
	ikfk_shape_3.rename(shape_name_3)
	
	shape_name_4 = arm_root.replace('arm_01_bind', 'ikfk_curve4') 
	# print 'Shape 4 Name:', shape_name_4
	ikfk_shape_4.rename(shape_name_4)

	arm_switch = pm.group(empty=True)
	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4, arm_switch)
	shapes = pm.ls(selection=True, dag=True)
	curveShape_1 = shapes[1]
	curveShape_2 = shapes[3]
	curveShape_3 = shapes[5]
	curveShape_4 = shapes[7]
	arm_switch_grp = shapes[8]
	# print 'Curve Shape 1:', curveShape_1
	# print 'Curve Shape 2:', curveShape_2
	# print 'Curve Shape 3:', curveShape_3
	# print 'Curve Shape 4:', curveShape_4
	# print 'Switch:', arm_switch_grp
	pm.select(ikfk_shape_2, ikfk_shape_3)

	pm.cmds.scale(0.768, 0.768, 0.768)
	freezeTransform()

	pm.parent(curveShape_1, curveShape_2, curveShape_3, curveShape_4, arm_switch, s=1, r=1)
	pm.delete(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	pm.cmds.move(0, 0, 3, arm_switch + '.scalePivot', arm_switch + '.rotatePivot', rpr=1)

	pm.xform(arm_switch, ro=[0,0,90], scale=[1.5,1.5,1.5])
	freezeTransform(arm_switch)
	temp_constraint = pm.pointConstraint(arm_joint_3, arm_switch, mo=0, w=1)
	pm.delete(temp_constraint)
	freezeTransform()
	switch_name = arm_root.replace('01_bind', 'IkFk_switch')
	arm_switch.rename(switch_name)
	pm.pointConstraint(arm_joint_3, arm_switch, mo=0, w=1)
	deleteHistory()

	'''
	Add IkFk attribute
	'''
	pm.addAttr(arm_switch, ln="IkFk", max=1, dv=0, at='double', min=0)
	arm_switch.IkFk.set(e=1, keyable=True)

	arm_switch.tx.set(lock=True, channelBox=False, keyable=False)
	arm_switch.ty.set(lock=True, channelBox=False, keyable=False)
	arm_switch.tz.set(lock=True, channelBox=False, keyable=False)
	arm_switch.rx.set(lock=True, channelBox=False, keyable=False)
	arm_switch.ry.set(lock=True, channelBox=False, keyable=False)
	arm_switch.rz.set(lock=True, channelBox=False, keyable=False)
	arm_switch.sx.set(lock=True, channelBox=False, keyable=False)
	arm_switch.sy.set(lock=True, channelBox=False, keyable=False)
	arm_switch.sz.set(lock=True, channelBox=False, keyable=False)
 	arm_switch.v.set(lock=True, channelBox=False, keyable=False)
 	ik_root.v.set(0)
 	fk_root.v.set(0)

	'''
	Rt SDKs
	'''
	if pm.objExists('rt_arm_01_bind_orientConstraint1.rt_arm_01_fkW1'):
		arm_switch.IkFk.set(0)
		pm.setAttr(orient_blend_1 + '.rt_arm_01_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_arm_01_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_arm_01_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(1)
		pm.setAttr(orient_blend_1 + '.rt_arm_01_fkW1', 1)
		pm.setAttr(orient_blend_1 + '.rt_arm_01_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_arm_01_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_arm_01_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0)
		arm_icon.v.set(1)
		fk_pad_1.v.set(0)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(1)
		arm_icon.v.set(0)
		fk_pad_1.v.set(1)
		elbow_icon.v.set(0)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0.01)
		arm_icon.v.set(1)
		fk_pad_1.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0.99)
		arm_icon.v.set(1)
		fk_pad_1.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
	else:
		print 'The right arm is not done'

	if pm.objExists('rt_arm_02_bind_orientConstraint1.rt_arm_02_fkW1'):
		arm_switch.IkFk.set(0)
		pm.setAttr(orient_blend_2 + '.rt_arm_02_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_arm_02_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_arm_02_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(1)
		pm.setAttr(orient_blend_2 + '.rt_arm_02_fkW1', 1)
		pm.setAttr(orient_blend_2 + '.rt_arm_02_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_arm_02_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_arm_02_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0)
	else:
		print 'The right arm is not done'

 	'''
 	Lt SDKs
 	'''
	if pm.objExists('lt_arm_01_bind_orientConstraint1.lt_arm_01_fkW1'):
		arm_switch.IkFk.set(0)
		pm.setAttr(orient_blend_1 + '.lt_arm_01_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_arm_01_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_arm_01_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(1)
		pm.setAttr(orient_blend_1 + '.lt_arm_01_fkW1', 1)
		pm.setAttr(orient_blend_1 + '.lt_arm_01_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_arm_01_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_arm_01_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0)
		arm_icon.v.set(1)
		fk_pad_1.v.set(0)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(1)
		arm_icon.v.set(0)
		fk_pad_1.v.set(1)
		elbow_icon.v.set(0)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0.01)
		arm_icon.v.set(1)
		fk_pad_1.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0.99)
		arm_icon.v.set(1)
		fk_pad_1.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= arm_switch + '.IkFk')
	else:
		print 'The left arm is not done'


	if pm.objExists('lt_arm_02_bind_orientConstraint1.lt_arm_02_fkW1'):
		arm_switch.IkFk.set(0)
		pm.setAttr(orient_blend_2 + '.lt_arm_02_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_arm_02_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_arm_02_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(1)
		pm.setAttr(orient_blend_2 + '.lt_arm_02_fkW1', 1)
		pm.setAttr(orient_blend_2 + '.lt_arm_02_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_arm_02_ikW0', currentDriver= arm_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_arm_02_fkW1', currentDriver= arm_switch + '.IkFk')
		arm_switch.IkFk.set(0)

	else:
		print 'The left arm is not done'

def twistWindow(*args):
	import Arm_twist_window
	reload (Arm_twist_window)
	Arm_twist_window.gui()

def bipedLeg_joints(*args):
	joint_system = pm.ls(selection=True, dag=True)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	joint_4 = joint_system[3]
	joint_5 = joint_system[4]
	# print 'Root Joint:', root_joint
	# print 'Joint 2:', joint_2
	# print 'Joint 3:', joint_3
	# print 'Joint 4:', joint_4
	# print 'Joint 5:', joint_5
	pm.duplicate(root_joint)
	ik_joints = pm.ls(selection=True, dag=True)
	ik_root_joint = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	ik_joint_4 = ik_joints[3]
	ik_joint_5 = ik_joints[4]
	# print 'Ik Root Joint:', ik_root_joint
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3
	# print 'Ik Joint 4:', ik_joint_4
	# print 'Ik Joint 5:', ik_joint_5

	ik_joint_name = root_joint.replace('bind', 'ik')
	ik_root_joint.rename(ik_joint_name)

	ik_joint_name = joint_2.replace('bind', 'ik')
	ik_joint_2.rename(ik_joint_name)

	ik_joint_name = joint_3.replace('bind', 'ik')
	ik_joint_3.rename(ik_joint_name)

	ik_joint_name = joint_4.replace('bind', 'ik')
	ik_joint_4.rename(ik_joint_name)

	ik_joint_name = joint_5.replace('waste', 'ik')
	ik_joint_5.rename(ik_joint_name)

	pm.duplicate(ik_root_joint)
	fk_joints = pm.ls(selection=True, dag=True)
	fk_root_joint = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	fk_joint_4 = fk_joints[3]
	fk_joint_5 = fk_joints[4]
	# print 'Ik Root Joint:', fk_root_joint
	# print 'Ik Joint 2:', fk_joint_2
	# print 'Ik Joint 3:', fk_joint_3
	# print 'Ik Joint 4:', fk_joint_4
	# print 'Ik Joint 5:', fk_joint_5

	fk_joint_name = root_joint.replace('bind', 'fk')
	fk_root_joint.rename(fk_joint_name)

	fk_joint_name = joint_2.replace('bind', 'fk')
	fk_joint_2.rename(fk_joint_name)

	fk_joint_name = joint_3.replace('bind', 'fk')
	fk_joint_3.rename(fk_joint_name)

	fk_joint_name = joint_4.replace('bind', 'fk')
	fk_joint_4.rename(fk_joint_name)

	fk_joint_name = joint_5.replace('waste', 'fk')
	fk_joint_5.rename(fk_joint_name)

def bipedLeg_system(*args):
	joint_systems = pm.ls(selection=True)
	
	leg_root = joint_systems[0]
	ik_root = joint_systems[1]
	fk_root = joint_systems[2]

	leg_joints = pm.ls(leg_root, dag=True)
	ik_joints = pm.ls(ik_root, dag=True)
	fk_joints = pm.ls(fk_root, dag=True)

	print 'Leg System:', leg_joints
	print 'IK System:', ik_joints
	print 'FK Systems:', fk_joints

	leg_root_joint = pm.ls(leg_joints[0])
	leg_joint_2 = pm.ls(leg_joints[1])
	leg_joint_3 = pm.ls(leg_joints[2])
	leg_joint_4 = pm.ls(leg_joints[3])
	leg_joint_5 = pm.ls(leg_joints[4])
	# print 'Leg root joint:', leg_root_joint
	# print '2nd leg joint:', leg_joint_2 
	# print '3rd leg joint:', leg_joint_3
	# print '4th leg joint:', leg_joint_4
	# print '5th leg joint:', leg_joint_5
	ik_root_joint = pm.ls(ik_joints[0])
	ik_joint_2 = pm.ls(ik_joints[1])
	ik_joint_3 = pm.ls(ik_joints[2])
	ik_joint_4 = pm.ls(ik_joints[3])
	ik_joint_5 = pm.ls(ik_joints[4])
	# print 'Leg root joint:', ik_root_joint
	# print '2nd ik joint:', ik_joint_2 
	# print '3rd ik joint:', ik_joint_3
	# print '4th ik joint:', ik_joint_4
	# print '5th ik joint:', ik_joint_5
	fk_root_joint = pm.ls(fk_joints[0])
	fk_joint_2 = pm.ls(fk_joints[1])
	fk_joint_3 = pm.ls(fk_joints[2])
	fk_joint_4 = pm.ls(fk_joints[3])
	fk_joint_5 = pm.ls(fk_joints[4])
	# print 'Leg root joint:', fk_root_joint
	# print '2nd fk joint:', fk_joint_2 
	# print '3rd fk joint:', fk_joint_3
	# print '4th fk joint:', fk_joint_4
	# print '5th fk joint:', fk_joint_5

	orient_blend_1 = pm.orientConstraint(ik_root_joint, fk_root_joint, leg_root_joint)
	orient_blend_2 = pm.orientConstraint(ik_joint_2, fk_joint_2, leg_joint_2)
	orient_blend_3 = pm.orientConstraint(ik_joint_3, fk_joint_3, leg_joint_3)
	orient_blend_4 = pm.orientConstraint(ik_joint_4, fk_joint_4, leg_joint_4)

	'''
	Create the ik handles
	'''

	pm.select(ik_root_joint, ik_joint_3)
	ikh_1 = pm.ikHandle()[0]
	pm.select(ik_joint_3, ik_joint_4)
	ikh_2 = pm.ikHandle(sol='ikSCsolver')[0]
	pm.select(ik_joint_4, ik_joint_5)
	ikh_3 =pm.ikHandle(sol='ikSCsolver')[0]

	'''
	Remane the ikh 
	'''
	ikh_name_1 = ik_root.replace('01_ik', 'ikh')
	ikh_1.rename(ikh_name_1)
	ikh_name_2 = ikh_1.replace('leg', 'ball')
	ikh_2.rename(ikh_name_2)
	ikh_name_3 = ikh_2.replace('ball', 'toe')
	ikh_3.rename(ikh_name_3)

	'''
	Create the foot icon
	'''
	footCurve_1 = pm.curve(p=[(-1.67422e-06, 0, 2.182925), (-0.13416, 0, 2.16342), (-0.266779, 0, 2.095529), (-0.395472, 0, 1.99807), (-0.518993, 0, 1.858632), (-0.636496, 0, 1.679268), (-0.737632, 0, 1.452024), (-0.819474, 0, 1.166445), (-0.846144, 0, 0.821387), (-0.824602, 0, 0.556128), (-0.749206, 0, 0.167213), (-0.673656, 0, -0.127237), (-0.597808, 0, -0.419587), (-0.545054, 0, -0.746104), (-0.544891, 0, -1.097217), (-0.571904, 0, -1.448294), (-0.512279, 0, -1.753435), (-0.393271, 0, -1.92306), (-0.266839, 0, -2.035747), (-0.133965, 0, -2.097731), (0, 0, -2.120128), (0.133965, 0, -2.097731), (0.266839, 0, -2.035747), (0.393271, 0, -1.92306), (0.512279, 0, -1.753435), (0.571904, 0, -1.448294), (0.544891, 0, -1.097217), (0.545054, 0, -0.746104), (0.597807, 0, -0.419586), (0.673656, 0, -0.127237), (0.749207, 0, 0.167214), (0.824602, 0, 0.556128), (0.846144, 0, 0.82139), (0.819474, 0, 1.166447), (0.737631, 0, 1.452029), (0.636486, 0, 1.679267), (0.519008, 0, 1.858641), (0.395504, 0, 1.9981), (0.266596, 0, 2.09545), (0.134293, 0, 2.163449), (-1.67422e-06, 0, 2.182925)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 38], d=3)
	footCurve_2 = pm.curve(p=[(-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217)], k=[0, 0, 0, 1, 2, 3, 3, 3], d=3)

	foot_icon = pm.group(empty=True)

	pm.select(footCurve_1, footCurve_2, foot_icon)
	foot_shapes = pm.ls(sl=True, dag=True)
	curveShape_1 = foot_shapes[1]
	curveShape_2 = foot_shapes[3]
	foot_icon_grp = foot_shapes[4]
	pm.parent(curveShape_1, curveShape_2, foot_icon, s=1, r=1)
	pm.delete(footCurve_1, footCurve_2)
	pm.xform(foot_icon, scale= [3.5, 3.5, 3.5])
	pm.select(foot_icon)
	freezeTransform()

	'''
	Move the foot icon
	'''
	temp_constraint = pm.pointConstraint(ik_joint_3, foot_icon)
	pm.delete(temp_constraint)
	foot_icon.ty.set(0)
	foot_icon.tz.set(6)
	pm.select(foot_icon)
	freezeTransform()
	

	'''
	Rename the foot icon
	'''
	foot_icon_name = leg_root.replace('leg_01_bind', 'foot_icon')
	foot_icon.rename(foot_icon_name)

	'''
	Add foot attrs
	'''
	pm.select(foot_icon)
	bipedFootAttrs()

	'''
	Parent the ikhs under the foot icon
	'''
	pm.parent(ikh_1, ikh_2, ikh_3, foot_icon)

	'''
	Move the pivot of the foot icon
	'''
	pm.select(leg_joint_3, foot_icon)
	selection = pm.ls(sl=True)
	driver_pivot = selection[0]
	driven_pivot = selection[1]
	driver_translation = driver_pivot.getTranslation(ws=True)
	driven_pivot.setPivots(driver_translation, ws=True)

	'''
	Create the knee icon.
	'''

	knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
	pm.select('curve1.cv[0]', 'curve1.cv[6]', 'curve1.cv[12]', 'curve1.cv[18]', 'curve1.cv[24]', r=1)
	pm.cmds.move(0, -0.982783, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[22]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[23]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[19]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[20]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[16]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[17]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[13]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[14]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[10]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[11]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[7]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[8]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[4]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[5]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[1]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[2]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	
	pm.select(knee_icon)
	centerPivot(knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(leg_joint_2, knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(knee_icon)
	pm.xform(knee_icon, t=[0,0,15], scale=[.5, .5, .5], ro=[-90, 0, 0])
	freezeTransform()

	'''
	Pole vector constraint.
	'''
	pm.poleVectorConstraint(knee_icon, ikh_1)

	'''
	Rename the knee icon
	'''
	knee_name = leg_root.replace('leg_01_bind', 'knee_icon')
	knee_icon.rename(knee_name)

	'''
	FK Setup
	'''

	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_pad_1)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_1, fk_pad_1)
	pm.select(fk_icon_1)
	freezeTransform()


	fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 2:', fk_icon_2
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_icon_2)
	pm.delete(temp_constraint)
	fk_pad_2 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_pad_2)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_2, fk_pad_2)
	pm.select(fk_icon_2)
	freezeTransform()
	pm.parent(fk_pad_2, fk_icon_1)

	fk_icon_3 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 3:', fk_icon_3
	temp_constraint = pm.parentConstraint(fk_joint_3, fk_icon_3)
	pm.delete(temp_constraint)
	fk_pad_3 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_joint_3, fk_pad_3)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_3, fk_pad_3)
	pm.select(fk_icon_3)
	freezeTransform()
	pm.parent(fk_pad_3, fk_icon_2)
	
	fk_icon_4 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 4:', fk_icon_4
	temp_constraint = pm.parentConstraint(fk_joint_4, fk_icon_4)
	pm.delete(temp_constraint)
	fk_pad_4 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_joint_4, fk_pad_4)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_4, fk_pad_4)
	pm.select(fk_icon_4)
	freezeTransform()
	pm.parent(fk_pad_4, fk_icon_3)

	'''
	Rename the icons and the pads
	'''
	fk_icon1_name = fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_icon3_name = fk_icon_2.replace('02', '03')
	fk_icon_3.rename(fk_icon3_name)
	
	fk_icon4_name = fk_icon_3.replace('03', '04')
	fk_icon_4.rename(fk_icon4_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name)

	fk_pad3_name = fk_icon_3.replace('icon', 'local')
	fk_pad_3.rename(fk_pad3_name)

	fk_pad4_name = fk_icon_4.replace('icon', 'local')
	fk_pad_4.rename(fk_pad4_name)

	'''
	Orient constrain the icons to the joints
	'''
	pm.orientConstraint(fk_icon_1, fk_root_joint)
	pm.orientConstraint(fk_icon_2, fk_joint_2)
	pm.orientConstraint(fk_icon_3, fk_joint_3)
	pm.orientConstraint(fk_icon_4, fk_joint_4)

	'''
	Create the IKFK switch 
	'''

	ikfk_shape_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	ikfk_shape_2 = pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)
	ikfk_shape_3 = pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)
	ikfk_shape_4 = pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)

	shape_name_1 = leg_root.replace('leg_01_bind', 'ikfk_curve1') 
	# print 'Shape 1 Name:', shape_name_1
	ikfk_shape_1.rename(shape_name_1)
	
	shape_name_2 = leg_root.replace('leg_01_bind', 'ikfk_curve2') 
	# print 'Shape 2 Name:', shape_name_2
	ikfk_shape_2.rename(shape_name_2)

	shape_name_3 = leg_root.replace('leg_01_bind', 'ikfk_curve3') 
	# print 'Shape 3 Name:', shape_name_3
	ikfk_shape_3.rename(shape_name_3)
	
	shape_name_4 = leg_root.replace('leg_01_bind', 'ikfk_curve4') 
	# print 'Shape 4 Name:', shape_name_4
	ikfk_shape_4.rename(shape_name_4)

	leg_switch = pm.group(empty=True)
	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4, leg_switch)
	shapes = pm.ls(selection=True, dag=True)
	curveShape_1 = shapes[1]
	curveShape_2 = shapes[3]
	curveShape_3 = shapes[5]
	curveShape_4 = shapes[7]
	leg_switch_grp = shapes[8]
	# print 'Curve Shape 1:', curveShape_1
	# print 'Curve Shape 2:', curveShape_2
	# print 'Curve Shape 3:', curveShape_3
	# print 'Curve Shape 4:', curveShape_4
	# print 'Switch:', leg_switch_grp
	pm.select(ikfk_shape_2, ikfk_shape_3)

	pm.cmds.scale(0.768, 0.768, 0.768)
	freezeTransform()

	pm.parent(curveShape_1, curveShape_2, curveShape_3, curveShape_4, leg_switch, s=1, r=1)
	pm.delete(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	pm.cmds.move(0, 0, 3, leg_switch + '.scalePivot', leg_switch + '.rotatePivot', rpr=1)

	pm.xform(leg_switch, ro=[0,0,90], scale=[1.5,1.5,1.5])
	freezeTransform(leg_switch)
	temp_constraint = pm.pointConstraint(leg_joint_3, leg_switch, mo=0, w=1)
	pm.delete(temp_constraint)
	freezeTransform()
	switch_name = leg_root.replace('01_bind', 'IkFk_switch')
	leg_switch.rename(switch_name)
	pm.pointConstraint(leg_joint_3, leg_switch, mo=0, w=1)
	deleteHistory()

	'''
	Add IkFk attribute
	'''
	pm.addAttr(leg_switch, ln="IkFk", max=1, dv=0, at='double', min=0)
	leg_switch.IkFk.set(e=1, keyable=True)

	leg_switch.tx.set(lock=True, channelBox=False, keyable=False)
	leg_switch.ty.set(lock=True, channelBox=False, keyable=False)
	leg_switch.tz.set(lock=True, channelBox=False, keyable=False)
	leg_switch.rx.set(lock=True, channelBox=False, keyable=False)
	leg_switch.ry.set(lock=True, channelBox=False, keyable=False)
	leg_switch.rz.set(lock=True, channelBox=False, keyable=False)
	leg_switch.sx.set(lock=True, channelBox=False, keyable=False)
	leg_switch.sy.set(lock=True, channelBox=False, keyable=False)
	leg_switch.sz.set(lock=True, channelBox=False, keyable=False)
 	leg_switch.v.set(lock=True, channelBox=False, keyable=False)
 	ik_root.v.set(0)
 	fk_root.v.set(0)

 	
	'''
 	Lt SDKs
 	'''
 	if pm.objExists('lt_leg_01_bind_orientConstraint1.lt_leg_01_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_1 + '.lt_leg_01_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_1 + '.lt_leg_01_fkW1', 1)
		pm.setAttr(orient_blend_1 + '.lt_leg_01_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
		foot_icon.v.set(1)
		fk_pad_1.v.set(0)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		foot_icon.v.set(0)
		fk_pad_1.v.set(1)
		knee_icon.v.set(0)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.01)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.99)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
	else:
		print 'The left leg is not done'
	if pm.objExists('lt_leg_02_bind_orientConstraint1.lt_leg_02_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_2 + '.lt_leg_02_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_2 + '.lt_leg_02_fkW1', 1)
		pm.setAttr(orient_blend_2 + '.lt_leg_02_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The left leg is not done'

	if pm.objExists('lt_leg_03_bind_orientConstraint1.lt_leg_03_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_3 + '.lt_leg_03_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_3 + '.lt_leg_03_fkW1', 1)
		pm.setAttr(orient_blend_3 + '.lt_leg_03_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The left leg is not done'

	if pm.objExists('lt_leg_04_bind_orientConstraint1.lt_leg_04_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_4 + '.lt_leg_04_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_4 + '.lt_leg_04_fkW1', 1)
		pm.setAttr(orient_blend_4 + '.lt_leg_04_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The left leg is not done'

	'''
 	Rt SDKs
 	'''
 	if pm.objExists('rt_leg_01_bind_orientConstraint1.rt_leg_01_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_1 + '.rt_leg_01_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_1 + '.rt_leg_01_fkW1', 1)
		pm.setAttr(orient_blend_1 + '.rt_leg_01_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
		foot_icon.v.set(1)
		fk_pad_1.v.set(0)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		foot_icon.v.set(0)
		fk_pad_1.v.set(1)
		knee_icon.v.set(0)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.01)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.99)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
	else:
		print 'The right leg is not done'
	if pm.objExists('rt_leg_02_bind_orientConstraint1.rt_leg_02_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_2 + '.rt_leg_02_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_2 + '.rt_leg_02_fkW1', 1)
		pm.setAttr(orient_blend_2 + '.rt_leg_02_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The right leg is not done'

	if pm.objExists('rt_leg_03_bind_orientConstraint1.rt_leg_03_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_3 + '.rt_leg_03_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_3 + '.rt_leg_03_fkW1', 1)
		pm.setAttr(orient_blend_3 + '.rt_leg_03_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The right leg is not done'

	if pm.objExists('rt_leg_04_bind_orientConstraint1.rt_leg_04_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_4 + '.rt_leg_04_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_4 + '.rt_leg_04_fkW1', 1)
		pm.setAttr(orient_blend_4 + '.rt_leg_04_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The right leg is not done'

def rflPrep(*args):
	name_selection = pm.ls(sl=True, dag=True)
	root_joint = name_selection[0]
	joint_2 = name_selection[1]
	joint_3 = name_selection[2]
	joint_4 = name_selection[3]
	joint_5 = name_selection[4]
	'''
	Create the locators
	'''
	loc1 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 1:', loc1

	loc2 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 2:', loc2
	pm.xform(loc2, t=[-3, 0, 10])

	loc3 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 3:', loc3
	pm.xform(loc3, t=[3, 0, 10])
	
	loc4 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 4:', loc4
	pm.xform(loc4, t=[0, 0, 14])

	loc5 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 5:', loc5 
	pm.xform(loc5, t=[0, 0, 10])

	loc6 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 6:', loc6 
	pm.xform(loc6, t=[0, 7, 2])

	locs = pm.select(loc1, loc2, loc3, loc4, loc5, loc6)
	freezeTransform(locs)

	pm.parent(loc2, loc1)
	pm.parent(loc3, loc2)
	pm.parent(loc4, loc3)
	pm.parent(loc5, loc4)
	pm.parent(loc6, loc5)

	'''
	Rename the locs
	'''
	loc_name = root_joint.replace('leg_01_bind', 'heel_loc')
	loc1.rename(loc_name)
	loc_name = loc1.replace('heel', 'innerBank')
	loc2.rename(loc_name)
	loc_name = loc2.replace('inner', 'outer')
	loc3.rename(loc_name)
	loc_name = loc1.replace('heel', 'toe')
	loc4.rename(loc_name)
	loc_name = loc4.replace('toe', 'ball')
	loc5.rename(loc_name)
	loc_name = loc5.replace('ball', 'ankle')
	loc6.rename(loc_name)

def rflSystem(*args):
	rflSelection = pm.ls(sl=True)
	selection_1 = rflSelection[0]
	selection_2 = rflSelection[1]
	# print 'rfl selection', rflSelection
	# print 'selection 1', selection_1
	# print 'selection 2', selection_2

	foot_icon = pm.ls(selection_1, dag=True)
	locs = pm.ls(selection_2, dag=True)

	ikh_1 = foot_icon[3]
	ikh_2 = foot_icon[5]
	ikh_3 = foot_icon[6]
	# print 'ikh 1', ikh_1
	# print 'ikh 2', ikh_2
	# print 'ikh 3', ikh_3

	loc1 = locs[0]
	loc2 = locs[2]
	loc3 = locs[4]
	loc4 = locs[6]
	loc5 = locs[8]
	loc6 = locs[10]
	# print 'loc 1', loc1
	# print 'loc 2', loc2
	# print 'loc 3', loc3
	# print 'loc 4', loc4
	# print 'loc 5', loc5
	# print 'loc 6', loc6
	pm.select(loc1)
	freezeTransform()
	
	'''
	Create and rename the heel rot clamp
	'''
	heel_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = loc1.replace('loc', 'rot_clamp')
	heel_rot_clamp.rename(clamp_name)
	print 'Heel rot clamp:', heel_rot_clamp

	ball_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = heel_rot_clamp.replace('heel', 'ball')
	ball_rot_clamp.rename(clamp_name)
	print 'Ball rot clamp:', ball_rot_clamp

	footBtoS_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = heel_rot_clamp.replace('heel_rot', 'footBtoS')
	footBtoS_clamp.rename(clamp_name)
	print 'Foot BtoS clamp:', footBtoS_clamp

	footBtoS_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = footBtoS_clamp.replace('clamp', 'percent')
	footBtoS_percent.rename(clamp_name)
	print 'Foot BtoS perect:', footBtoS_percent

	foot_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = selection_1.replace('icon', 'roll_mult')
	foot_roll_mult.rename(clamp_name)
	print 'Foot roll mult:', foot_roll_mult

	toeTap_invert_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = selection_1.replace('foot_icon', 'toeTap_invert_mult')
	toeTap_invert_mult.rename(clamp_name)

	rflSetupPartA()

	ball_0toB_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = footBtoS_percent.replace('footBtoS', 'ball_0toB')
	ball_0toB_percent.rename(clamp_name)
	print 'Ball ball 0toB percent:', ball_0toB_percent

	foot_invert_percent = pm.shadingNode('plusMinusAverage', asUtility=1)
	clamp_name = selection_1.replace('icon', 'invert_percent')
	foot_invert_percent.rename(clamp_name)
	print 'Foot invert percent:', foot_invert_percent

	ball_percent_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = foot_roll_mult.replace('foot_roll', 'ball_percent' )
	ball_percent_mult.rename(clamp_name)
	print 'ball percent mult:', ball_percent_mult

	clamp_name = heel_rot_clamp.replace('heel_rot', 'ball_0toB')
	ball_rot_clamp.rename(clamp_name)
	print 'Ball rot clamp:', ball_rot_clamp

	ball_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = ball_percent_mult.replace('percent', 'roll')
	ball_roll_mult.rename(clamp_name)
	print 'ball roll mult:', ball_roll_mult

	rflSetupPartB()

	pm.parent(ikh_2, loc5)
	pm.parent(ikh_1, loc6)

	'''
	Lean
	'''
	pm.connectAttr('lt_foot_icon.lean', loc5 + '.rz', f=1)

	'''
	Toe Spin
	'''
	pm.connectAttr('lt_foot_icon.toeSpin', loc4 + '.ry', f=1)

def bipedFootAttrs(*args):
	if pm.objExists('lt_foot_icon'):
		pm.addAttr('|lt_foot_icon', ln="roll", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.roll', e=1, keyable=True)
		pm.addAttr('|lt_foot_icon', ln="bendLimitAngle", dv=45, at='double')
		pm.setAttr('|lt_foot_icon.bendLimitAngle', e=1, keyable=True)
		pm.addAttr('|lt_foot_icon', ln="toeStraightAngle", dv=75, at='double')
		pm.setAttr('|lt_foot_icon.toeStraightAngle', e=1, keyable=True)
		pm.addAttr('|lt_foot_icon', ln="tilt", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.tilt', e=1, keyable=True)
		pm.addAttr('|lt_foot_icon', ln="lean", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.lean', e=1, keyable=True)
		pm.addAttr('|lt_foot_icon', ln="toeSpin", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.toeSpin', e=1, keyable=True)
		pm.addAttr('|lt_foot_icon', ln="toeTap", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.toeTap', e=1, keyable=True)

	else:
		print "Lt foot icon donesn't exists"

	if pm.objExists('rt_foot_icon'):
		pm.addAttr('|rt_foot_icon', ln="roll", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.roll', e=1, keyable=True)
		pm.addAttr('|rt_foot_icon', ln="bendLimitAngle", dv=45, at='double')
		pm.setAttr('|rt_foot_icon.bendLimitAngle', e=1, keyable=True)
		pm.addAttr('|rt_foot_icon', ln="toeStraightAngle", dv=75, at='double')
		pm.setAttr('|rt_foot_icon.toeStraightAngle', e=1, keyable=True)
		pm.addAttr('|rt_foot_icon', ln="tirt", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.tirt', e=1, keyable=True)
		pm.addAttr('|rt_foot_icon', ln="lean", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.lean', e=1, keyable=True)
		pm.addAttr('|rt_foot_icon', ln="toeSpin", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.toeSpin', e=1, keyable=True)
		pm.addAttr('|rt_foot_icon', ln="toeTap", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.toeTap', e=1, keyable=True)

	else:
		print "Rt foot icon donesn't exists"

def rflSetupPartA(*args):
	if pm.objExists('lt_heel_rot_clamp'):
		pm.connectAttr('lt_foot_icon.roll', 'lt_heel_rot_clamp.inputR', f=1)
		pm.setAttr("lt_heel_rot_clamp.minR", -90)
		pm.connectAttr('lt_heel_rot_clamp.outputR', 'lt_heel_loc.rotateX', f=1)
		pm.connectAttr('lt_foot_icon.roll', 'lt_ball_rot_clamp.inputR', f=1)
		pm.setAttr("lt_ball_rot_clamp.maxR", 90)
		pm.connectAttr('lt_ball_rot_clamp.outputR', 'lt_ball_loc.rotateX', f=1)

		pm.connectAttr('lt_foot_icon.toeStraightAngle', 'lt_footBtoS_clamp.maxR', f=1)
		pm.connectAttr('lt_foot_icon.bendLimitAngle', 'lt_footBtoS_clamp.minR', f=1)
		pm.connectAttr('lt_foot_icon.roll', 'lt_footBtoS_clamp.inputR', f=1)

		pm.connectAttr('lt_footBtoS_clamp.maxR', 'lt_footBtoS_percent.oldMaxX', f=1)
		pm.connectAttr('lt_footBtoS_clamp.minR', 'lt_footBtoS_percent.oldMinX', f=1)
		pm.setAttr("lt_footBtoS_percent.maxX", 1)
		pm.connectAttr('lt_footBtoS_clamp.inputR', 'lt_footBtoS_percent.valueX', f=1)

		pm.connectAttr('lt_footBtoS_percent.outValueX', 'lt_foot_roll_mult.input1X', f=1)
		pm.connectAttr('lt_footBtoS_clamp.inputR', 'lt_foot_roll_mult.input2X', f=1)
		pm.connectAttr('lt_foot_roll_mult.outputX', 'lt_toe_loc.rotateX', f=1)

		pm.mel.CBdeleteConnection("lt_ball_loc.rx")

		pm.connectAttr('lt_foot_icon.bendLimitAngle', 'lt_ball_rot_clamp.maxR', f=1)

		pm.setDrivenKeyframe('lt_innerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setDrivenKeyframe('lt_outerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setAttr("lt_foot_icon.tilt", -90)
		pm.setAttr("lt_innerBank_loc.rotateZ", 90)
		pm.setDrivenKeyframe('lt_innerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setAttr("lt_foot_icon.tilt", 90)
		pm.setAttr("lt_outerBank_loc.rotateZ", -90)
		pm.setDrivenKeyframe('lt_outerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setAttr("lt_foot_icon.tilt", 0)

		'''
		Toe Tap Setup
		'''
		toeTap_pad = pm.group(empty=True, n='lt_toeTap_pivot')
		temp_constraint = pm.parentConstraint('lt_leg_04_bind', toeTap_pad)
		pm.delete(temp_constraint)
		pm.makeIdentity(toeTap_pad, apply=True, t=1, r=1, s=1, n=0, pn=1)
		pm.parent('lt_toe_ikh', toeTap_pad)
		pm.parent(toeTap_pad, 'lt_toe_loc')
		pm.setAttr('lt_toeTap_invert_mult.input2X', -1)
		pm.connectAttr('lt_foot_icon.toeTap', 'lt_toeTap_invert_mult.input1X', f=1)
		pm.connectAttr('lt_toeTap_invert_mult.input1X', 'lt_toeTap_pivot.rotateX', f=1)

			
	else:
		print 'RFL not set up'

def rflSetupPartB(*agrs):
	if  pm.objExists('lt_ball_0toB_percent'):
		pm.connectAttr('lt_ball_0toB_clamp.maxR', 'lt_ball_0toB_percent.oldMaxX', f=1)
		pm.connectAttr('lt_ball_0toB_clamp.minR', 'lt_ball_0toB_percent.oldMinX', f=1)
		pm.setAttr("lt_ball_0toB_percent.maxX", 1)
		pm.connectAttr('lt_ball_0toB_clamp.inputR', 'lt_ball_0toB_percent.valueX', f=1)

		pm.setAttr('lt_foot_invert_percent.input1D[0]', 1)
		pm.setAttr('lt_foot_invert_percent.input1D[1]', 1)
		pm.connectAttr('lt_footBtoS_percent.outValueX', 'lt_foot_invert_percent.input1D[1]', f=1)
		pm.setAttr("lt_foot_invert_percent.operation", 2)

		pm.connectAttr('lt_ball_0toB_percent.outValueX', 'lt_ball_percent_mult.input1X', f=1)
		pm.connectAttr('lt_foot_invert_percent.output1D', 'lt_ball_percent_mult.input2X', f=1)

		pm.connectAttr('lt_ball_percent_mult.outputX', 'lt_ball_roll_mult.input1X', f=1)
		pm.connectAttr('lt_foot_icon.roll', 'lt_ball_roll_mult.input2X', f=1)
		pm.connectAttr('lt_ball_roll_mult.outputX', 'lt_ball_loc.rotateX', f=1)
	else:
		print 'RFL not set up'

def quadHind_fkLeg_icons():
	'''
	Input
	What are we working on?
	The root joint of the hind fk leg
	'''

	joint_systems = pm.ls(selection=True)

	leg_root = joint_systems[0]
	ik_root = joint_systems[1]
	helper_root = joint_systems[2]
	fk_root = joint_systems[3]

	leg_joints = pm.ls(leg_root, dag=True)
	ik_joints = pm.ls(ik_root, dag=True)
	helper_joints = pm.ls(helper_root, dag=True)
	fk_joints = pm.ls(fk_root, dag=True)

	print 'Leg System:', leg_joints
	print 'IK System:', ik_joints
	print 'Helper System:', helper_joints
	print 'FK Systems:', fk_joints

	leg_root_joint = pm.ls(leg_joints[0])
	leg_joint_2 = pm.ls(leg_joints[1])
	leg_joint_3 = pm.ls(leg_joints[2])
	leg_joint_4 = pm.ls(leg_joints[3])
	leg_joint_5 = pm.ls(leg_joints[4])
	leg_joint_6 = pm.ls(leg_joints[5])
	# print 'Leg root joint:', leg_root_joint
	# print '2nd leg joint:', leg_joint_2 
	# print '3rd leg joint:', leg_joint_3
	# print '4th leg joint:', leg_joint_4
	# print '5th leg joint:', leg_joint_5
	# print '6th leg joint:', leg_joint_6

	ik_root_joint = pm.ls(ik_joints[0])
	ik_joint_2 = pm.ls(ik_joints[1])
	ik_joint_3 = pm.ls(ik_joints[2])
	ik_joint_4 = pm.ls(ik_joints[3])
	ik_joint_5 = pm.ls(ik_joints[4])
	ik_joint_6 = pm.ls(ik_joints[5])
	# print 'Leg root joint:', ik_root_joint
	# print '2nd ik joint:', ik_joint_2 
	# print '3rd ik joint:', ik_joint_3
	# print '4th ik joint:', ik_joint_4
	# print '5th ik joint:', ik_joint_5
	# print '6th ik joint:', ik_joint_6

	helper_root_joint = pm.ls(helper_joints[0])
	helper_joint_2 = pm.ls(helper_joints[1])
	helper_joint_3 = pm.ls(helper_joints[2])
	helper_joint_4 = pm.ls(helper_joints[3])
	# print 'Leg root joint:', helper_root_joint
	# print '2nd helper joint:', helper_joint_2 
	# print '3rd helper joint:', helper_joint_3
	# print '4th helper joint:', helper_joint_4


	fk_root_joint = pm.ls(fk_joints[0])
	fk_joint_2 = pm.ls(fk_joints[1])
	fk_joint_3 = pm.ls(fk_joints[2])
	fk_joint_4 = pm.ls(fk_joints[3])
	fk_joint_5 = pm.ls(fk_joints[4])
	fk_joint_6 = pm.ls(fk_joints[5])
	# print 'Leg root joint:', fk_root_joint
	# print '2nd fk joint:', fk_joint_2 
	# print '3rd fk joint:', fk_joint_3
	# print '4th fk joint:', fk_joint_4
	# print '5th fk joint:', fk_joint_5
	# print '6th fk joint:', fk_joint_6

	'''
	Local Controls 
	'''

	'''
	Control 1 - root_joint
	'''
	# Create a control


	# Custom Orb Icon
	orbCurve_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	orbCurve_2 = pm.duplicate(rr=1)[0]
	orbCurve_2.rx.set(45)
	orbCurve_3 = pm.duplicate(rr=1)[0]
	orbCurve_3.rx.set(90)
	orbCurve_4 = pm.duplicate(rr=1)[0]
	orbCurve_4.ry.set(45)
	orbCurve_5 = pm.duplicate(rr=1)[0]
	orbCurve_5.ry.set(-45)
	pm.makeIdentity(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5, n=0,s=1,r=1,t=1, apply=True,pn=1)
	orbIcon = pm.group(empty=True)
	temp_grp = pm.group(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5)

	orbShapes = pm.ls(sl=True, dag=True)
	shape_1 = orbShapes[2]
	shape_2 = orbShapes[4]
	shape_3 = orbShapes[6]
	shape_4 = orbShapes[8]
	shape_5 = orbShapes[10]
	#print 'Shape 1:', shape_1

	pm.parent(shape_1, shape_2, shape_3, shape_4, shape_5, orbIcon, s=1, r=1)
	pm.delete(temp_grp)

	icon_name = leg_root.replace('bind', 'fk_icon')
	orbIcon.rename(icon_name)


	#  Create a group
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad
	print 'Orb Created', orbIcon
	print 'Local Pad 1 Created', local_pad_1
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient constrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(orbIcon, leg_root_joint)




	print 'Orb 1 Renamed', orbIcon

	# Renaming Pad
	pad_1 = local_pad_1
	pad_1_name = fk_root.replace('01_fk', '01_fk_local')
	pad_1.rename(pad_1_name)

	print 'Local Pad 1 Renamed', local_pad_1

	pm.parent(orbIcon, local_pad_1)

	'''
	Control 2
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad
	print 'Control 2 Created', control_icon_2
	print 'Local Pad 2 Created', local_pad_2
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_2, fk_joint_2)

	# Renaming Icon
	# control_icon_2
	icon_2 = control_icon_2
	icon_2_name = fk_root.replace('01_fk', '02_fk_icon')
	icon_2.rename(icon_2_name)

	print 'Icon 2 Renamed', control_icon_2

	# Renaming Pad
	pad_2 = local_pad_2
	pad_2_name = fk_root.replace('01_fk', '02_fk_local')
	pad_2.rename(pad_2_name)

	print 'Local Pad 2 Renamed', local_pad_2

	''' 
	Parent controls together
	'''
	# Pad 2 -> control 1
	pm.parent(local_pad_2, orbIcon)

	'''
	Control 3
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad
	print 'Control 3 Created', control_icon_3
	print 'Local Pad 3 Created', local_pad_3
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_3, local_pad_3)
	pm.delete(temp_constraint)




	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_3, fk_joint_3)

	# Renaming Icon
	# control_icon_3
	icon_3 = control_icon_3
	icon_3_name = fk_root.replace('01_fk', '03_fk_icon')
	icon_3.rename(icon_3_name)

	print 'Icon 3 Renamed', control_icon_3

	# Renaming Pad
	pad_3 = local_pad_3
	pad_3_name = fk_root.replace('01_fk', '03_fk_local')
	pad_3.rename(pad_3_name)

	print 'Local Pad 3 Renamed', local_pad_3


	''' 
	Parent controls together
	'''
	# Pad 3 -> control 1
	pm.parent(local_pad_3, control_icon_2)
	
def ik_jointRenamer():
	'''
	Get Selected
	'''
	joint_chain = pm.ls(selection=True, dag=True)

	'''
	Figure out naming convention
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'ik'

	'''
	Loop through the joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0},{1}IK,0{2};{3}'.format(ori, system_name, count, suffix)
		#  Rename joints
		current_joint.rename(new_name)
	new_name = '{0},{1}IK,0{2};{3}'.format(ori,system_name,count, 'ik')

def fk_jointRenamer():
	'''
	Get Selected
	'''
	joint_chain = pm.ls(selection=True, dag=True)

	'''
	Figure out naming convention
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'fk'

	'''
	Loop through the joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0},{1}FK,0{2};{3}'.format(ori, system_name, count, suffix)
		#  Rename joints
		current_joint.rename(new_name)
	new_name = '{0},{1}FK,0{2};{3}'.format(ori,system_name,count, 'fk')

def quad_hLeg_joints(*args):
	joint_system = pm.ls(selection=True, dag=True)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	joint_4 = joint_system[3]
	joint_5 = joint_system[4]
	joint_6 = joint_system[5]
	

	pm.duplicate(rr=1)
	ik_hJointRenamer()
	pm.duplicate(rr=1)
	fk_hJointRenamer()
	pm.duplicate(rr=1)
	helper_hJointRenamer()

def ik_hJointRenamer():
	'''
	Get Selected
	'''
	joint_chain = pm.ls(selection=True, dag=True)

	'''
	Figure out naming convention
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'ik'

	'''
	Loop through the joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0},h{1}IK,0{2};{3}'.format(ori, system_name, count, suffix)
		#  Rename joints
		current_joint.rename(new_name)
	new_name = '{0},h{1}IK,0{2};{3}'.format(ori,system_name,count, 'ik')

def fk_hJointRenamer():
	'''
	Get Selected
	'''
	joint_chain = pm.ls(selection=True, dag=True)

	'''
	Figure out naming convention
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'fk'

	'''
	Loop through the joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0},h{1}FK,0{2};{3}'.format(ori, system_name, count, suffix)
		#  Rename joints
		current_joint.rename(new_name)
	new_name = '{0},h{1}FK,0{2};{3}'.format(ori,system_name,count, 'fk')

def helper_hJointRenamer():
	'''
	Get Selected
	'''
	joint_chain = pm.ls(selection=True, dag=True)

	'''
	Figure out naming convention
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'helper'

	'''
	Loop through the joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0},{1},0{2};{3}'.format(ori, system_name, count, suffix)
		#  Rename joints
		current_joint.rename(new_name)
	new_name = '{0},{1},0{2};{3}'.format(ori,system_name,count, 'helper')

	joint_system = pm.ls(selection=True, dag=True)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	joint_4 = joint_system[3]
	joint_5 = joint_system[4]
	joint_6 = joint_system[5]
	pm.delete(joint_5)

def quad_hIKFK_system(*args):
	joint_systems = pm.ls(selection=True)
	
	leg_root = joint_systems[0]
	ik_root = joint_systems[1]
	helper_root = joint_systems[2]
	fk_root = joint_systems[3]

	leg_joints = pm.ls(leg_root, dag=True)
	ik_joints = pm.ls(ik_root, dag=True)
	helper_joints = pm.ls(helper_root, dag=True)
	fk_joints = pm.ls(fk_root, dag=True)

	print 'Leg System:', leg_joints
	print 'IK System:', ik_joints
	print 'Helper System:', helper_joints
	print 'FK Systems:', fk_joints

	leg_root_joint = pm.ls(leg_joints[0])
	leg_joint_2 = pm.ls(leg_joints[1])
	leg_joint_3 = pm.ls(leg_joints[2])
	leg_joint_4 = pm.ls(leg_joints[3])
	leg_joint_5 = pm.ls(leg_joints[4])
	leg_joint_6 = pm.ls(leg_joints[5])
	# print 'Leg root joint:', leg_root_joint
	# print '2nd leg joint:', leg_joint_2 
	# print '3rd leg joint:', leg_joint_3
	# print '4th leg joint:', leg_joint_4
	# print '5th leg joint:', leg_joint_5
	# print '6th leg joint:', leg_joint_6

	ik_root_joint = pm.ls(ik_joints[0])
	ik_joint_2 = pm.ls(ik_joints[1])
	ik_joint_3 = pm.ls(ik_joints[2])
	ik_joint_4 = pm.ls(ik_joints[3])
	ik_joint_5 = pm.ls(ik_joints[4])
	ik_joint_6 = pm.ls(ik_joints[5])
	# print 'Leg root joint:', ik_root_joint
	# print '2nd ik joint:', ik_joint_2 
	# print '3rd ik joint:', ik_joint_3
	# print '4th ik joint:', ik_joint_4
	# print '5th ik joint:', ik_joint_5
	# print '6th ik joint:', ik_joint_6

	helper_root_joint = pm.ls(helper_joints[0])
	helper_joint_2 = pm.ls(helper_joints[1])
	helper_joint_3 = pm.ls(helper_joints[2])
	helper_joint_4 = pm.ls(helper_joints[3])
	# print 'Leg root joint:', helper_root_joint
	# print '2nd helper joint:', helper_joint_2 
	# print '3rd helper joint:', helper_joint_3
	# print '4th helper joint:', helper_joint_4


	fk_root_joint = pm.ls(fk_joints[0])
	fk_joint_2 = pm.ls(fk_joints[1])
	fk_joint_3 = pm.ls(fk_joints[2])
	fk_joint_4 = pm.ls(fk_joints[3])
	fk_joint_5 = pm.ls(fk_joints[4])
	fk_joint_6 = pm.ls(fk_joints[5])
	# print 'Leg root joint:', fk_root_joint
	# print '2nd fk joint:', fk_joint_2 
	# print '3rd fk joint:', fk_joint_3
	# print '4th fk joint:', fk_joint_4
	# print '5th fk joint:', fk_joint_5
	# print '6th fk joint:', fk_joint_6

	'''
	Orient constraint the IK/FK system with the bind.
	'''
	pm.orientConstraint(ik_root_joint, fk_root_joint, leg_root_joint, mo=0, w=1)
	pm.orientConstraint(ik_joint_2, fk_joint_2, leg_joint_2, mo=0, w=1)
	pm.orientConstraint(ik_joint_3, fk_joint_3, leg_joint_3, mo=0, w=1)
	pm.orientConstraint(ik_joint_4, fk_joint_4, leg_joint_4, mo=0, w=1)
	pm.orientConstraint(ik_joint_5, fk_joint_5, leg_joint_5, mo=0, w=1)

	'''
	Create the ikHandles
	'''
	pm.select(ik_root_joint, ik_joint_3)
	ikh_1 = pm.ikHandle(n='leg_ikh')[0]
	pm.select(ik_joint_3, ik_joint_4)
	ikh_2 = pm.ikHandle(sol='ikSCsolver', n='ankle_ikh')[0]
	pm.select(ik_joint_4, ik_joint_5)
	ikh_3 = pm.ikHandle(sol='ikSCsolver', n='ball_ikh')[0]
	pm.select(ik_joint_5, ik_joint_6)
	ikh_4 = pm.ikHandle(sol='ikSCsolver', n='toe_ikh')[0]
	pm.select(helper_root, helper_joint_4)
	ikh_5 = pm.ikHandle(n='helper_ikh')[0]

	'''
	Create the foot icon
	'''
	foot_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	pm.xform(scale=[2,0,4])
	temp_constraint = pm.pointConstraint(leg_joint_4, 'curve1')
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()

	'''
	Rename the foot icon
	'''
	foot_name = leg_root.replace('hLeg_01_bind', 'hFoot_icon')
	foot_icon.rename(foot_name)

	'''
	Parent the ikHandles under the foot icon.
	'''

	pm.parent(ikh_1, ikh_2, ikh_3, ikh_4, ikh_5, foot_icon)

	ikh_5.twist.set(180)


	'''
	Create the knee icon.
	'''

	knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
	pm.select('curve1.cv[0]', 'curve1.cv[6]', 'curve1.cv[12]', 'curve1.cv[18]', 'curve1.cv[24]', r=1)
	pm.cmds.move(0, -0.982783, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[22]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[23]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[19]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[20]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[16]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[17]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[13]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[14]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[10]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[11]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[7]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[8]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[4]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[5]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[1]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[2]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	
	
	centerPivot(knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(leg_joint_3, knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(knee_icon)
	pm.xform(knee_icon, t=[0,0,-30], scale=[3, 3, 3], ro=[90, 0, 0])
	freezeTransform(knee_icon)

	'''
	Pole vector constraint. 
	'''

	
	pm.poleVectorConstraint(knee_icon, ikh_1)
	pm.poleVectorConstraint(knee_icon, ikh_5)

	'''
	Rename the knee
	'''
	knee_name = leg_root.replace('hLeg_01_bind', 'knee_icon')
	knee_icon.rename(knee_name)
	'''
	Thigh Icon
	'''
	'''
	Create orb icon
	'''
	# Custom Orb Icon
	orbCurve2_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	orbCurve2_2 = pm.duplicate(rr=1)[0]
	orbCurve2_2.rx.set(45)
	orbCurve2_3 = pm.duplicate(rr=1)[0]
	orbCurve2_3.rx.set(90)
	orbCurve2_4 = pm.duplicate(rr=1)[0]
	orbCurve2_4.ry.set(45)
	orbCurve2_5 = pm.duplicate(rr=1)[0]
	orbCurve2_5.ry.set(-45)
	pm.makeIdentity(orbCurve2_1, orbCurve2_2, orbCurve2_3, orbCurve2_4, orbCurve2_5, n=0,s=1,r=1,t=1, apply=True,pn=1)
	ik_thigh_icon = pm.group(empty=True)
	temp_grp = pm.group(orbCurve2_1, orbCurve2_2, orbCurve2_3, orbCurve2_4, orbCurve2_5)

	orb2Shapes = pm.ls(sl=True, dag=True)
	shape2_1 = orb2Shapes[2]
	shape2_2 = orb2Shapes[4]
	shape2_3 = orb2Shapes[6]
	shape2_4 = orb2Shapes[8]
	shape2_5 = orb2Shapes[10]
	#print 'Shape 1:', shape_1

	pm.parent(shape2_1, shape2_2, shape2_3, shape2_4, shape2_5, ik_thigh_icon, s=1, r=1)
	pm.delete(temp_grp)

	'''
	Move the icon
	'''
	temp_constraint = pm.parentConstraint(ik_root_joint, ik_thigh_icon)
	pm.delete(temp_constraint)
	freezeTransform(ik_thigh_icon)
	# pm.xform(ik_thigh_icon, t=[0, 0, -10], scale=[3, 3, 3])



	'''
	Pad the icon
	'''

	ik_thigh_pad = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(ik_root_joint, ik_thigh_pad)
	pm.delete(temp_constraint)
	pm.parent(ik_thigh_icon, ik_thigh_pad)
	freezeTransform()

	# Rename Icon
	ik_thigh_icon_name = leg_root.replace('hLeg_01_bind', 'thigh_icon')
	ik_thigh_icon.rename(ik_thigh_icon_name)

	# Renaming Pad
	ik_thigh_pad_name = ik_thigh_icon.replace('icon', 'local')
	ik_thigh_pad.rename(ik_thigh_pad_name)

	'''
	Create the IK/FK switch
	'''
	pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))

	pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)

	pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)

	pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)


	pm.rename('nurbsCircle1', 'ikfk_curve1')
	pm.rename('curve1', 'ikfk_curve2')
	pm.rename('curve2', 'ikfk_curve3')
	pm.rename('curve3', 'ikfk_curve4')

	shape_1 = 'ikfk_curveShape1'
	shape_2 = 'ikfk_curveShape2'
	shape_3 = 'ikfk_curveShape3'
	shape_4 = 'ikfk_curveShape4'
	switch = pm.group(empty=True)
	print 'Shape 1:', shape_1
	print 'Switch:', switch


	pm.select(shape_2, shape_3)

	pm.cmds.scale(0.768552, 0.768552, 0.768552)
	pm.makeIdentity(n=0, s=1, r=1, t=1, apply=True, pn=1)



	pm.parent(shape_1, shape_2, shape_3, shape_4, switch, s=1, r=1)

	pm.makeIdentity(n=0, s=1, r=1, t=1, apply=True, pn=1)
	shape_1 = 'ikfk_curve1'
	shape_2 = 'ikfk_curve2'
	shape_3 = 'ikfk_curve3'
	shape_4 = 'ikfk_curve4'
	pm.delete(shape_1, shape_2, shape_3, shape_4)

	pm.select(switch, r=1)
	pm.cmds.move(0, 0, 3, switch + '.scalePivot', switch + '.rotatePivot', rpr=1)

	pm.xform(switch, ro=[0,0,90], scale=[2,2,2])
	freezeTransform(switch)
	temp_constraint = pm.pointConstraint(leg_joint_4, switch, mo=0, w=1)
	pm.delete(temp_constraint)
	freezeTransform()
	pm.pointConstraint(leg_joint_4, switch, mo=0, w=1)
	deleteHistory()

	'''
	Add IkFk attribute
	'''
	pm.addAttr(switch, ln="IkFk", max=10, dv=0, at='double', min=0)
	switch.IkFk.set(e=1, keyable=True)

	switch.tx.set(lock=True, channelBox=False, keyable=False)
	switch.ty.set(lock=True, channelBox=False, keyable=False)
	switch.tz.set(lock=True, channelBox=False, keyable=False)
	switch.rx.set(lock=True, channelBox=False, keyable=False)
	switch.ry.set(lock=True, channelBox=False, keyable=False)
	switch.rz.set(lock=True, channelBox=False, keyable=False)
	switch.sx.set(lock=True, channelBox=False, keyable=False)
	switch.sy.set(lock=True, channelBox=False, keyable=False)
	switch.sz.set(lock=True, channelBox=False, keyable=False)
 	switch.v.set(lock=True, channelBox=False, keyable=False)

	'''
	Fk set up
	'''
	
	'''

	Create a hierarchy based upon given system

	Select root joint and execute function.

	# import fk_hQ_legSetUp
	# reload(fk_hQ_legSetUp)
	# fk_hQ_legSetUp.fk_hQ_leg()
	'''

	# print 'Hierarchy Selected'

	'''
	Local Controls 
	'''

	'''
	Control 1 - root_joint
	'''
	'''
	Create orb icon
	'''
	# Custom Orb Icon
	orbCurve_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	orbCurve_2 = pm.duplicate(rr=1)[0]
	orbCurve_2.rx.set(45)
	orbCurve_3 = pm.duplicate(rr=1)[0]
	orbCurve_3.rx.set(90)
	orbCurve_4 = pm.duplicate(rr=1)[0]
	orbCurve_4.ry.set(45)
	orbCurve_5 = pm.duplicate(rr=1)[0]
	orbCurve_5.ry.set(-45)
	pm.makeIdentity(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5, n=0,s=1,r=1,t=1, apply=True,pn=1)
	fk_thigh_icon = pm.group(empty=True)
	temp_grp = pm.group(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5)

	orbShapes = pm.ls(sl=True, dag=True)
	shape_1 = orbShapes[2]
	shape_2 = orbShapes[4]
	shape_3 = orbShapes[6]
	shape_4 = orbShapes[8]
	shape_5 = orbShapes[10]
	#print 'Shape 1:', shape_1

	pm.parent(shape_1, shape_2, shape_3, shape_4, shape_5, fk_thigh_icon, s=1, r=1)
	pm.delete(temp_grp)

	icon_name = leg_root.replace('bind', 'fk_icon')
	fk_thigh_icon.rename(icon_name)


	'''
	Move the icon
	'''
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_thigh_icon)
	pm.delete(temp_constraint)
	pm.makeIdentity(fk_thigh_icon, n=0,s=1,r=1,t=1, apply=True,pn=1)

	'''
	Pad the icon
	'''

	fk_thigh_pad = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_thigh_pad)
	pm.delete(temp_constraint)
	pm.parent(fk_thigh_icon, fk_thigh_pad)
	freezeTransform()

	# Renaming Pad

	fk_thigh_pad_name = fk_thigh_icon.replace('icon', 'local')
	fk_thigh_pad.rename(fk_thigh_pad_name)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(fk_thigh_icon, fk_root_joint)


	'''
	Control 2
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad
	print 'Control 2 Created', control_icon_2
	print 'Local Pad 2 Created', local_pad_2
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_2, fk_joint_2)

	# Renaming Icon
	# control_icon_2
	icon_2 = control_icon_2
	icon_2_name = fk_thigh_icon.replace('01', '02')
	icon_2.rename(icon_2_name)

	print 'Icon 2 Renamed', control_icon_2

	# Renaming Pad
	pad_2 = local_pad_2
	pad_2_name = control_icon_2.replace('icon', 'local')
	pad_2.rename(pad_2_name)

	print 'Local Pad 2 Renamed', local_pad_2

	''' 
	Parent controls together
	'''
	# Pad 2 -> control 1
	pm.parent(local_pad_2, fk_thigh_icon)

	'''
	Control 3
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad
	print 'Control 3 Created', control_icon_3
	print 'Local Pad 3 Created', local_pad_3
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_3, local_pad_3)
	pm.delete(temp_constraint)


	# Orient constgrain the joint to the control
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, fk_joint_3)

	# Renaming Icon
	control_icon_3
	icon_3 = control_icon_3
	icon_3_name = control_icon_2.replace('02', '03')
	icon_3.rename(icon_3_name)

	print 'Icon 3 Renamed', control_icon_3

	# Renaming Pad
	pad_3 = local_pad_3
	pad_3_name = control_icon_3.replace('icon', 'local')
	pad_3.rename(pad_3_name)

	print 'Local Pad 3 Renamed', local_pad_3


	''' 
	Parent controls together
	'''
	# Pad 3 -> control 1
	pm.parent(local_pad_3, control_icon_2)

	'''
	Control 4
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_4 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_4 = pm.group()

	# Output control and pad
	print 'Control 4 Created', control_icon_4
	print 'Local Pad 4 Created', local_pad_4
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_4, local_pad_4)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_4, fk_joint_4)

	# Renaming Icon
	# control_icon_4
	icon_4 = control_icon_4
	icon_4_name = control_icon_3.replace('03', '04')
	icon_4.rename(icon_4_name)

	# print 'Icon 4 Renamed', control_icon_4

	# Renaming Pad
	pad_4 = local_pad_4
	pad_4_name = control_icon_4.replace('icon', 'local')
	pad_4.rename(pad_4_name)

	# print 'Local Pad 4 Renamed', local_pad_4


	''' 
	Parent controls together
	'''
	# Pad 4 -> control 1
	pm.parent(local_pad_4, control_icon_3)


	'''
	Control 5
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_5 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_5 = pm.group()

	# Output control and pad
	print 'Control 5 Created', control_icon_5
	print 'Local Pad 5 Created', local_pad_5
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_5, local_pad_5)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	temp_constraint = pm.orientConstraint(control_icon_5, fk_joint_5)


	# Renaming Icon
	# control_icon_5
	icon_5 = control_icon_5
	icon_5_name = control_icon_4.replace('04', '05')
	icon_5.rename(icon_5_name)

	print 'Icon 5 Renamed', control_icon_5

	# Renaming Pad
	pad_5 = local_pad_5
	pad_5_name = control_icon_5.replace('icon', 'local')
	pad_5.rename(pad_5_name)

	print 'Local Pad 5 Renamed', local_pad_5


	''' 
	Parent controls together
	'''
	# Pad 5 (Last) -> control 1
	pm.parent(local_pad_5, control_icon_4)

	pm.setAttr("lt_hLeg_01_ik.visibility", 0)
	pm.setAttr("lt_leg_01_helper.visibility", 0)
	pm.setAttr("lt_hLeg_01_fk.visibility", 0)

	'''
	Create the locators
	'''
	# pm.CreateLocator()
	loc1 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 1:', loc1

	# pm.CreateLocator()
	loc2 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 2:', loc2

	# pm.CreateLocator()
	loc3 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 3:', loc3

	'''
	Point constraint the locs to the joints.
	'''

	temp_constraint = pm.pointConstraint(leg_joint_4, loc1)
	pm.delete(temp_constraint)
	freezeTransform(loc1)

	temp_constraint = pm.pointConstraint(leg_joint_5, loc2)
	pm.delete(temp_constraint)
	freezeTransform(loc2)

	temp_constraint = pm.pointConstraint(leg_joint_6, loc3)
	pm.delete(temp_constraint)
	freezeTransform(loc3)

	'''
	Parent the locs under the foot icon.
	'''
	pm.parent(loc1, loc2, loc3, foot_icon)

	'''
	Create the flex pivot and offset.
	'''

	flex_pivot = pm.group(empty=True)
	flex_offset = pm.group(empty=True)

	flex_pivot_name = leg_root.replace('hLeg_01_bind', 'flex_pivot')
	flex_pivot.rename(flex_pivot_name)

	flex_offset_name = flex_pivot.replace('pivot', 'offset')
	flex_offset.rename(flex_offset_name)


	temp_constraint = pm.pointConstraint(loc1, flex_pivot)
	pm.delete(temp_constraint)
	pm.makeIdentity(flex_pivot, n=0, s=1, r=1, t=1, apply=True, pn=1)


	temp_constraint = pm.pointConstraint(loc1, flex_offset)
	pm.delete(temp_constraint)
	freezeTransform(flex_offset)

	pm.parent(ikh_1, ikh_2, flex_pivot)
	pm.parent(flex_pivot, flex_offset)

	'''
	Create the toeTap pivot.
	'''

	toeTap_pivot = pm.group(empty=True)

	temp_constraint = pm.pointConstraint(loc2, toeTap_pivot)
	pm.delete(temp_constraint)
	freezeTransform(toeTap_pivot)

	toeTap_name = flex_pivot.replace('flex', 'toeTap')
	toeTap_pivot.rename(toeTap_name)

	pm.parent(ikh_4, toeTap_pivot)

	pm.parentConstraint(helper_joint_4, flex_offset, mo=1, w=1)

	'''
	Add custom attributes.
	'''
	pm.addAttr(foot_icon, ln="flex", dv=0, at='double')
	foot_icon.flex.set(e=1, keyable=True)
	pm.addAttr(foot_icon, ln="swivel", dv=0, at='double')
	foot_icon.swivel.set(e=1, keyable=True)
	pm.addAttr(foot_icon, ln="toeTap", dv=0, at='double')
	foot_icon.toeTap.set(e=1, keyable=True)
	pm.addAttr(foot_icon, ln="toeTip", dv=0, at='double')
	foot_icon.toeTip.set(e=1, keyable=True)

	'''
	Connect the flex attribute
	'''
	pm.connectAttr(foot_icon + '.flex', flex_pivot.rx, f=1)

	'''
	Connect the toeTap attribute.
	'''
	pm.connectAttr(foot_icon + '.toeTap', toeTap_pivot.rx, f=1)

	'''
	Parent the pivots under the foot icon.
	'''
	pm.parent(toeTap_pivot, flex_offset, foot_icon )

	ikfk_name = foot_icon.replace('hFoot_icon', 'IkFk_switch')
	switch.rename(ikfk_name)

def lt_hLeg_SDKs(*args):
	switch = 'lt_IkFk_switch'
	foot_icon = 'lt_hFoot_icon'
	pm.setAttr("lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)
	pm.setAttr("lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1", 1)
	pm.setAttr("lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1", 1)
	pm.setAttr("lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1", 1)
	pm.setAttr("lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1", 1)
	pm.setAttr("lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1", 1)
	pm.setAttr("lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)
	pm.setAttr('lt_hLeg_01_fk_local.visibility', 0)
	pm.setDrivenKeyframe('lt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)	
	pm.setAttr("lt_hLeg_01_fk_local.visibility", 1)
	pm.setAttr("lt_thigh_local.visibility", 0)
	pm.setAttr("lt_hFoot_icon.visibility", 0)
	pm.setDrivenKeyframe('lt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)

def rt_hLeg_SDKs(*args):
	switch = 'rt_IkFk_switch'
	foot_icon = 'rt_hFoot_icon'
	pm.setAttr("rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)
	pm.setAttr("rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1", 1)
	pm.setAttr("rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1", 1)
	pm.setAttr("rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1", 1)
	pm.setAttr("rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1", 1)
	pm.setAttr("rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1", 1)
	pm.setAttr("rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)
	pm.setAttr('rt_hLeg_01_fk_local.visibility', 0)
	pm.setDrivenKeyframe('rt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)	
	pm.setAttr("rt_hLeg_01_fk_local.visibility", 1)
	pm.setAttr("rt_thigh_local.visibility", 0)
	pm.setAttr("rt_hFoot_icon.visibility", 0)
	pm.setDrivenKeyframe('rt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)

def setZeroHumanFoot(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".roll"), lock=0)
		pm.setAttr((str(current) + ".roll"), 0)
		pm.setAttr((str(current) + ".bendLimitAngle"), lock=0)
		pm.setAttr((str(current) + ".bendLimitAngle"), 45)
		pm.setAttr((str(current) + ".toeStraightAngle"), lock=0)
		pm.setAttr((str(current) + ".toeStraightAngle"), 75)
		pm.setAttr((str(current) + ".tilt"), lock=0)
		pm.setAttr((str(current) + ".tilt"), 0)
		pm.setAttr((str(current) + ".lean"), lock=0)
		pm.setAttr((str(current) + ".lean"), 0)
		pm.setAttr((str(current) + ".toeSpin"), lock=0)
		pm.setAttr((str(current) + ".toeSpin"), 0)
		pm.setAttr((str(current) + ".toeTap"), lock=0)
		pm.setAttr((str(current) + ".toeTap"), 0)

def setZeroHumanHand(*args):

	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".All_Curl"), lock=0)
		pm.setAttr((str(current) + ".All_Curl"), 0)
		pm.setAttr((str(current) + ".All_Spread"), lock=0)
		pm.setAttr((str(current) + ".All_Spread"), 0)
		pm.setAttr((str(current) + ".Thumb_Drop"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Drop"), 0)
		pm.setAttr((str(current) + ".Thumb_Root"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Root"), 0)
		pm.setAttr((str(current) + ".Thumb_Mid"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Mid"), 0)
		pm.setAttr((str(current) + ".Thumb_End"), lock=0)
		pm.setAttr((str(current) + ".Thumb_End"), 0)
		pm.setAttr((str(current) + ".Index_Root"), lock=0)
		pm.setAttr((str(current) + ".Index_Root"), 0)
		pm.setAttr((str(current) + ".Index_Mid"), lock=0)
		pm.setAttr((str(current) + ".Index_Mid"), 0)
		pm.setAttr((str(current) + ".Index_End"), lock=0)
		pm.setAttr((str(current) + ".Index_End"), 0)
		pm.setAttr((str(current) + ".Mid_Root"), lock=0)
		pm.setAttr((str(current) + ".Mid_Root"), 0)
		pm.setAttr((str(current) + ".Mid_Mid"), lock=0)
		pm.setAttr((str(current) + ".Mid_Mid"), 0)
		pm.setAttr((str(current) + ".Mid_End"), lock=0)
		pm.setAttr((str(current) + ".Mid_End"), 0)
		pm.setAttr((str(current) + ".Ring_Root"), lock=0)
		pm.setAttr((str(current) + ".Ring_Root"), 0)
		pm.setAttr((str(current) + ".Ring_Mid"), lock=0)
		pm.setAttr((str(current) + ".Ring_Mid"), 0)
		pm.setAttr((str(current) + ".Ring_End"), lock=0)
		pm.setAttr((str(current) + ".Ring_End"), 0)
		pm.setAttr((str(current) + ".Pinky_Root"), lock=0)
		pm.setAttr((str(current) + ".Pinky_Root"), 0)
		pm.setAttr((str(current) + ".Pinky_Mid"), lock=0)
		pm.setAttr((str(current) + ".Pinky_Mid"), 0)
		pm.setAttr((str(current) + ".Pinky_End"), lock=0)
		pm.setAttr((str(current) + ".Pinky_End"), 0)
		pm.setAttr((str(current) + ".Thumb_Spread"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Spread"), 0)
		pm.setAttr((str(current) + ".Index_Spread"), lock=0)
		pm.setAttr((str(current) + ".Index_Spread"), 0)
		pm.setAttr((str(current) + ".Middle_Spread"), lock=0)
		pm.setAttr((str(current) + ".Middle_Spread"), 0)
		pm.setAttr((str(current) + ".Ring_Spread"), lock=0)
		pm.setAttr((str(current) + ".Ring_Spread"), 0)
		pm.setAttr((str(current) + ".Pinky_Spread"), lock=0)
		pm.setAttr((str(current) + ".Pinky_Spread"), 0)

def setZeroTr(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".translateX"), lock=0)
		pm.setAttr((str(current) + ".translateX"), 0)
		pm.setAttr((str(current) + ".translateY"), lock=0)
		pm.setAttr((str(current) + ".translateY"), 0)
		pm.setAttr((str(current) + ".translateZ"), lock=0)
		pm.setAttr((str(current) + ".translateZ"), 0)

def setZeroRo(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".rotateX"), lock=0)
		pm.setAttr((str(current) + ".rotateX"), 0)
		pm.setAttr((str(current) + ".rotateY"), lock=0)
		pm.setAttr((str(current) + ".rotateY"), 0)
		pm.setAttr((str(current) + ".rotateZ"), lock=0)
		pm.setAttr((str(current) + ".rotateZ"), 0)

def setZeroSc(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".scaleX"), lock=0)
		pm.setAttr((str(current) + ".scaleX"), 1)
		pm.setAttr((str(current) + ".scaleY"), lock=0)
		pm.setAttr((str(current) + ".scaleY"), 1)
		pm.setAttr((str(current) + ".scaleZ"), lock=0)
		pm.setAttr((str(current) + ".scaleZ"), 1)


def windowResize(*args):
	if pm.window('ByrdRigs_interface_toolset', q=1, exists=1):
		pm.window('ByrdRigs_interface_toolset', e=1, wh=(240, 110), rtf=True)
	else:
		pm.warming('ByrdRigs_interface_toolset does not exist')