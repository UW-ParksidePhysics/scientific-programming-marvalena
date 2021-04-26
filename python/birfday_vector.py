from vpython import *
# GlowScript 3.0 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-.5,-.3,-1)

scene.caption= """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

xaxis = cylinder(color=color.magenta, pos=vector(0,0,0), axis=vector(15,0,0), radius=0.3)
xlbl = label(pos=vector(15,0,0), text="x", color=color.magenta, opacity=0, height=30, box=0)
yaxis = cylinder(color=color.purple, pos=vector(0,0,0), axis=vector(0,15,0), radius=0.3)
ylbl = label(pos=vector(0,15,0), text="y", color=color.purple, opacity=0, height=30, box=0)
zaxis = cylinder(color=color.red, pos=vector(0,0,0), axis=vector(0,0,15), radius=0.3)
xlbl = label(pos=vector(0,0,15), text="z", color=color.red, opacity=0, height=30, box=0)

r = arrow(pos=vector(0,0,0), axis = vector(3,27,1), color=color.cyan, shaftwidth=0.8)
rlbl = label(pos = vector(3,27,1), text="3x+27y+1z", color = color.cyan, opacity = 0, height = 20, box = 0)
