# Jacob Lambert
# CIS 510 Computer Graphics
# Homework 2
# Lego man Kick leg

import maya.cmds as cmds

ctime = cmds.currentTime(query=True)
cmds.select('leg_R')

cmds.setAttr('leg_R.rx', 0)
cmds.setKeyframe()

cmds.currentTime(ctime + 10)
cmds.setAttr('leg_R.rx', 90)
cmds.setKeyframe()
  
cmds.currentTime(ctime + 20)
cmds.setAttr('leg_R.rx', -90)
cmds.setKeyframe()

cmds.currentTime(ctime + 30)
cmds.setAttr('leg_R.rx', 0)
cmds.setKeyframe()
