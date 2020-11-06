import urllib.request
from selenium import webdriver
import time
import yaml
import logging
from datetime import datetime
import random

# set the logging
logging.basicConfig(level=logging.DEBUG)

# open your configuration file see example_config.yml
with open(r'.cfg.yml') as file:
    cfg = yaml.safe_load(file)

have_purchased = False
while not have_purchased:
    page = urllib.request.urlopen('http://127.0.0.1:5000/')

    page.read() # without this line it won't work, dont know why yet.
    have_stock = bool(page.read())
    # log and show the status of the program
    status = str(datetime.now()) + ' checking whether it is in stock, result is: ' + str(have_stock)
    logging.debug(status)

    # if have stock, make purchase
    if have_stock:
        have_purchased = True
        # load website
        browser = webdriver.Chrome(cfg['webdriver'])
        browser.get(cfg['url'])

        # click the button to log in
        python_button = browser.find_elements_by_xpath(cfg['xpath_find_log_in'])[0]
        python_button.click()

        # fill in the user name
        browser.find_elements_by_xpath(cfg['xpath_user_name'])[0].send_keys(cfg['username'])
        # put delay to avoid bug
        time.sleep(2.5)

        # fill in password
        b = browser.find_elements_by_xpath(cfg['xpath_password'])[0]
        b.send_keys(cfg['password'])

        # click log in
        login_button = browser.find_elements_by_xpath(cfg['xpath_login_click'])[0]
        login_button.click()
        browser.close()

    # pause every 60 to 120 seconds
    time.sleep(60 + random.randint(0, 60))