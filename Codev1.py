###From TeCoEd###
###Based on Teleport idea###

import sys
import time
sys.path.append("./mcpi/api/python/mcpi")
import minecraft
mc = minecraft.Minecraft.create()

###imports the blocks 
block = 102 ###glass
air = 0
build = 1


def tardis():   ###builds the teleport machine
    pos = mc.player.getPos() ###players current position
    x = pos.x
    y = pos.y
    z = pos.z

    ###postiton of blocks
    x2 = x+3 
    y2 = y+4
    z2 = z +3

    print x2,y2,z2
    ###builds teleport-sets blocks
    mc.setBlocks(x, y, z, x2, y2, z2, block)
    mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air)

    ##moves the player into the box
    xm = (x2 + x) /2
    ym = (y2 + y-2) /2
    zm = (z2 + z) /2

    #print xm, ym, zm used to test pos

    mc.player.setPos(xm, ym, zm)
    time.sleep(5)
    teleport() ###move later

def teleport(): ###teleport the player
    
    ###select where you wish to tavel to
    x_new = input("Please select X location you wish to teleport to, ")
    y_new = input("Please select UP location you wish to teleport to, ")
    z_new = input("Please select Z location you wish to teleport to, ")

    mc.player.setPos(x_new, y_new, z_new)
    tardis()

while True:
    Go_build = raw_input("Please enter number")
    if build ==1:
        tardis()
        teleport()
        
    
