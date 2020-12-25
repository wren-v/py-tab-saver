import webbrowser
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
url = 'chrome://inspect/#pages'

#driver = webdriver.Chrome(PATH)

webbrowser.open(url, new=2, autoraise=True)
