# Jacob Lambert
# CIS 510 Computer Graphics
# Homework 2
# Lego man kicking and chasing a ball 

import maya.cmds as cmds

# parent the hands to arms
cmds.parent('hand_L', 'arm_L')
cmds.parent('hand_R', 'arm_R')
cmds.currentTime(0)

# arm raise
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


# leg kick
cmds.currentTime(35)

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

# ball bounce
cmds.currentTime(50)

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

# lego run
cmds.currentTime(70)

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
