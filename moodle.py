from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://login.iiit.ac.in/cas/login?service=https%3A%2F%2Fmoodle.iiit.ac.in%2Flogin%2Findex.php%3FauthCAS%3DCAS"
browser = webdriver.Safari(executable_path = "/usr/bin/safaridriver")    
browser.maximize_window()
browser.get(url)

f = open('.moodle_creds','r')
creds = f.readlines()
f.close()
user_name = creds[0][:len(creds[0])-2]
pass_word = creds[1]

username = browser.find_element_by_xpath("//input[@name='username']")
password = browser.find_element_by_xpath("//input[@name='password']")
login = browser.find_element_by_xpath("//input[@name='submit']")

username.send_keys(user_name)
password.send_keys(pass_word)
login.click()

