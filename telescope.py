#!/usr/bin/env python
"telescope.py - drive a telescope with nxt servos and gamepad control"

import pygame
import sys, signal
import time

import nxt.locator
from nxt.motor import Motor

sock = nxt.locator.find_one_brick()
brick = sock.connect()

pitch = Motor(brick, 0)
yaw = Motor(brick, 1)

pygame.joystick.init()
pygame.display.init()

jcount = pygame.joystick.get_count()
if jcount == 0 : raise 'No joystick detected'

for i in range(jcount) :
    js = pygame.joystick.Joystick(i)
    js.init()

while True:  
    ev = pygame.event.wait()
    if ev.type == pygame.JOYAXISMOTION and ev.joy == 0 :
        if ev.axis == 0 :
            yaw.run(ev.value * 10)
        elif ev.axis == 2 :
            pitch.run(ev.value * -5)
    elif ev.type == pygame.JOYBUTTONDOWN :
        pass
    elif ev.type == pygame.JOYBUTTONUP :
        if ev.button == 4 :
            yaw.stop()
            yaw.run(0)
            
            pitch.stop()
            pitch.run(0)
            
            sock.close()
            sys.exit(0)
