#!/usr/bin/env python3
# Controlling keyboard and mouse is called GUI Automation

# pip install PyAutoGUI
# sudo apt-get install python3-tk python3-dev
# (0.0) is the top left corner of the screen
# X-axis increases going to right, Y-axis increases going to down
import pyautogui
pyautogui.click(100, 100) # first move to some text editor
pyautogui.typewrite('Hello world\n', interval=0.2) # 0.2 seconds pause ater each character

# you can also press some keyboard keys using list of keys to press
# these keys can be found using:
pyKeys = pyautogui.KEYBOARD_KEYS
pyautogui.typewrite(['R', 'B', 'left', 'left', 'O', 'P'], interval=0.2)
pyautogui.press('f1') # will trigger help in most of the applications
pyautogui.hotkey('ctrl', 'o') # sequence of keys

# typewrite -> string of characters to type
# press -> press a single key
# hotkey -> for keyboard shortcuts