#!/usr/bin/env python3
# Controlling keyboard and mouse is called GUI Automation

# pip install PyAutoGUI
# sudo apt-get install python3-tk python3-dev
# (0.0) is the top left corner of the screen
# X-axis increases going to right, Y-axis increases going to down
import pyautogui
width, height = pyautogui.size() # screen resolution
print(str(width) + " x " + str(height)) 
xpos, ypos = pyautogui.position() # position of the mouse cursor
print(str(xpos), ", " + str(ypos))
pyautogui.moveTo(10, 10, duration=1.5) # cursor goes to (10, 10) absolute position in 1.5 seconds
pyautogui.moveRel(200, 10) # moves 200 x-offsets, 10 x-offsets from current cursor position
pyautogui.click(954, 0) # single click on 854, 0 absolute position
pyautogui.click() # clicks on current cursor position

# some more click methods
# pyautogui.doubleClick(954, 0)
# pyautogui.rightClick(954, 0)
# pyautogui.middleClick(954, 0)

