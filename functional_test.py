from selenium import webdriver
import re

browser = webdriver.Firefox()
browser.get('http://localhost:8000/dashapp')

#assert 'dashapp' in browser.find_elements(by, value)
body = browser.find_element_by_tag_name("body")
assert 'dashapp' in body.text