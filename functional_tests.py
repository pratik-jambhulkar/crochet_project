from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost')

assert 'Django' in browser.title

browser.quit()