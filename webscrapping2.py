#!/usr/bin/env python3
import bs4
import requests

myUrl = 'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994'
res = requests.get(myUrl, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup)
print(soup.select('#unqualifiedBuyBox > div > div.a-text-center.a-spacing-mini > span'))
