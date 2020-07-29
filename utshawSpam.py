#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

def getPage(url, paramName, paramValue):
    """
    GET request on a URL
    """
    
    payload = {paramName: paramValue}
    r = requests.get(url, params=payload, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    print(r.url) 
    if r.ok:            # if status code is less than 400 then returns True otherwise False
        print(r.text)

getPage('https://www.bing.com/search', 'q', 'Farhan Tanvir Utshaw')