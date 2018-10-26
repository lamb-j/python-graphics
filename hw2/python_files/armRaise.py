# Jacob Lambert
# CIS 510 Computer Graphics
# Homework 2
# Lego man arm raise 

import maya.cmds as cmds

ctime = cmds.currentTime(query=True)

cmds.select('arm_L')

cmds.setAttr('arm_L.rx', 0)
cmds.setKeyframe()

cmds.currentTime(ctime + 10)
cmds.setAttr('arm_L.rx', -90)
cmds.setKeyframe()
  
cmds.currentTime(ctime + 15)
cmds.setAttr('arm_L.rx', -180)
cmds.setKeyframe()

cmds.currentTime(ctime + 25)
cmds.setAttr('arm_L.rx', -180)
cmds.setKeyframe()

cmds.currentTime(ctime + 35)
cmds.setAttr('arm_L.rx', 0)
cmds.setKeyframe()
