#!/usr/bin/env python3
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
res.raise_for_status() # raise exception if error downloading the file; for success do nothing
print(res.text[:500])
playFile = open('Romeo&Juliet.txt', 'wb') # wb -> write binary mode (binary for maintaining unicode encoding)

for chunk in res.iter_content(100000): # 100k bytes per iteration
    playFile.write(chunk)

playFile.close()

