from selenium import webdriver
import time
import yaml

with open(r'.cfg.yml') as file:
    cfg = yaml.safe_load(file)

browser = webdriver.Chrome(cfg['webdriver'])
browser.get(cfg['url'])

python_button = browser.find_elements_by_xpath(cfg['xpath_find_log_in'])[0]
python_button.click()

browser.find_elements_by_xpath(cfg['xpath_user_name'])[0].send_keys(cfg['username'])
time.sleep(2.5)
b = browser.find_elements_by_xpath(cfg['xpath_password'])[0]
b.send_keys(cfg['password'])

login_button  = browser.find_elements_by_xpath(cfg['xpath_login_click'])[0]
login_button.click()

browser.find_elements_by_xpath('xpath_login_close')[0].click()

