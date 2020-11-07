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

# config release date:
release_date = datetime(2020, 11, 18, 12, 0, 6, 0)

print('Press ctl + c to stop the program')
try:
    while not have_purchased:
        if datetime.now() < release_date:
            logging.debug(str(datetime.now()) + ': the product have not yet been released')
        else:
            have_stock = False
            try:
                page = urllib.request.urlopen('http://127.0.0.1:5000/')

                page.read() # without this line it won't work, dont know why yet.
                have_stock = bool(page.read())
                status = str(datetime.now()) + ' checking whether it is in stock, result is: ' + str(have_stock)
                logging.debug(status)
            except Exception as e:
                logging.warning(str(datetime.now()) + ': localhost:5000 is not available')
            # log and show the status of the program


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
                #browser.close()

        # pause every 60 to 120 seconds
        time.sleep(30 + random.randint(0, 3))
except KeyboardInterrupt:
    print('exited')
    pass