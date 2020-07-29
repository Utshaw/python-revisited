#!/usr/bin/env python3
# Useful for web pages that require login, submit form etc
# You require firefox browser
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.bing.com/')
searchBox = browser.find_element_by_css_selector('#sb_form_q')
# elem.click() # click on the elem
searchBox.send_keys('Farhan Utshaw')
searchBox.submit()

elem = browser.find_element_by_css_selector('html')
print(elem.text)
# browser.back() # back button of browser
# browser.forward() # forward button of browser
# browser.refresh() # refresh browser
# browser.quit() # quit the browser
