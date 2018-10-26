# Jacob Lambert
# CIS 510 Computer Graphics
# Homework 2
# bouncing ball 

import maya.cmds as cmds

ctime = cmds.currentTime(query=True)

cmds.select('ball')

cmds.setAttr('ball.ty', 0)
cmds.setAttr('ball.tz', 0)
cmds.setAttr('ball.rx', 0)
cmds.setAttr('ball.ry', 0)
cmds.setAttr('ball.rz', 0)
cmds.setKeyframe()
cmds.keyTangent('ball', inTangentType='linear', outTangentType='linear', time=(ctime,ctime))

ctime += 25
cmds.currentTime(ctime)
cmds.setAttr('ball.ty', 10)
cmds.setKeyframe(at='translateY')

ctime += 25
cmds.currentTime(ctime)
cmds.setAttr('ball.ty', 0)
cmds.setKeyframe(at='translateY')
cmds.keyTangent('ball', inTangentType='linear', outTangentType='linear', time=(ctime,ctime))

ctime += 15
cmds.currentTime(ctime)
cmds.setAttr('ball.ty', 6)
cmds.setKeyframe(at='translateY')

ctime += 15
cmds.currentTime(ctime)
cmds.setAttr('ball.ty', 0)
cmds.setKeyframe(at='translateY')
cmds.keyTangent('ball', inTangentType='linear', outTangentType='linear', time=(ctime,ctime))

ctime += 5
cmds.currentTime(ctime)
cmds.setAttr('ball.ty', 2)
cmds.setKeyframe(at='translateY')

ctime += 5
cmds.currentTime(ctime)
cmds.setAttr('ball.ty', 0)
cmds.setKeyframe(at='translateY')
cmds.keyTangent('ball', inTangentType='linear', outTangentType='linear', time=(ctime,ctime))

ctime += 5
cmds.currentTime(ctime)
cmds.setAttr('ball.tz', 80)
cmds.setAttr('ball.ty', 0)
cmds.setAttr('ball.rx', 1500)
cmds.setAttr('ball.ry', 1200)
cmds.setAttr('ball.rz', 1200)
cmds.setKeyframe()
