from selenium import webdriver
import time


browser = webdriver.Chrome()


def shimo_login(username, password):
    browser.get('https://shimo.im/login?from=home')
    browser.implicitly_wait(5)
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(username)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(password)
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    time.sleep(2)


username = '18980099169'
password = "******"
shimo_login(username, password)