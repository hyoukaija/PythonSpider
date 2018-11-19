import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

total_page = 0
bace_url = sys.argv[1]
title = ''

browser = webdriver.Chrome()
browser.get(bace_url)

def get_url(url):
    try:
        browser.get(url)
        time.sleep(5)
        cover = browser.find_elements_by_css_selector('ul.cube-list > li > a.cover')
        for key in cover:
            with open(title+'.txt','a') as f:
                f.write(key.get_attribute('href')+'\n')
    except:
        browser.close()

def get_total_page():
    try:
        global total_page
        total_page = int(browser.find_element_by_class_name('be-pager-total').text[2:-3])
    except:
        total_page = 1

def get_name():
    global title
    title = browser.find_element_by_id('h-name').text

if __name__ == "__main__":
    get_total_page()
    get_name()
    try:
        for i in range(1,total_page+1):
            get_url(bace_url+'?page=' + str(i))
    finally:
        browser.close()
    os.mkdir(title)
    os.system('annie -o ' + title + '/' ' -F '+title+'.txt')


        

