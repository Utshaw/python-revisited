#!/usr/bin/env python3
import webbrowser, sys, pyperclip

# sys.argv # ['mapit.py', 'Valencia', 'St.']

if len(sys.argv) > 1:
    # ['mapit.py', 'Valencia', 'St.']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


webbrowser.open("https://www.google.com/maps/place/" + address)

