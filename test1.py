# from selenium import webdriver
# browser = webdriver.PhantomJS()
# browser.get('https://www.baidu.com')
# print(browser.current_url)
# # from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)





