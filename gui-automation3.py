#!/usr/bin/env python3
# Controlling keyboard and mouse is called GUI Automation

# pip install PyAutoGUI
# sudo apt-get install python3-tk python3-dev
# (0.0) is the top left corner of the screen
# X-axis increases going to right, Y-axis increases going to down
import pyautogui
pyautogui.screenshot('screenshot.png') # returns a Pillow image object

image_to_search = "dropbox-gnome-bar-icon.png"
# print(pyautogui.locateOnScreen(image_to_search))


x_cordinate, y_cordinate, imageWidth, imageHeight = pyautogui.locateOnScreen(image_to_search) # returns a tuple if the image_to_search is found in the screen 
x_cordinate, y_cordinate = pyautogui.locateCenterOnScreen(image_to_search) # returns x,y co-ordinate of the matched image found on the screen
pyautogui.moveTo(x_cordinate, y_cordinate, duration=1)
pyautogui.click(x_cordinate, y_cordinate)
