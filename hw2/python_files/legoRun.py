# Jacob Lambert
# CIS 510 Computer Graphics
# Homework 2
# Lego man run in place for 70 frames
# assume hadns already parented to arms

import maya.cmds as cmds

def rotate_limbs(angle):
  
  cmds.select('arm_L')
  cmds.setAttr('arm_L.rx', angle)
  cmds.setKeyframe(at='rotateX')

  cmds.select('arm_R')
  cmds.setAttr('arm_R.rx', -angle)
  cmds.setKeyframe(at='rotateX')

  cmds.select('left_L')
  cmds.setAttr('left_L.rx', -angle)
  cmds.setKeyframe(at='rotateX')

  cmds.select('leg_R')
  cmds.setAttr('leg_R.rx', angle)
  cmds.setKeyframe(at='rotateX')

def change_height(height):

  cmds.select('Lego_Group')
  cmds.setAttr('Lego_Group.ty', height);
  cmds.setKeyframe(at='translateY')
  
ctime = cmds.currentTime(query=True)

cmds.select('Lego_Group')
cmds.setAttr('Lego_Group.tz', 0)
cmds.setKeyframe(at='translateZ')

for index in range(1, 5):

  rotate_limbs(0)
  change_height(0)

  ctime += 5
  cmds.currentTime(ctime)
  rotate_limbs(90)
  change_height(3)
  
  ctime += 5
  cmds.currentTime(ctime)
  rotate_limbs(0)
  change_height(0)

  ctime += 5
  cmds.currentTime(ctime)
  rotate_limbs(-90)
  change_height(3)

  ctime += 5
  cmds.currentTime(ctime)


rotate_limbs(0)
change_height(0)

cmds.select('Lego_Group')
cmds.setAttr('Lego_Group.tz', 65)
cmds.setKeyframe(at='translateZ')
