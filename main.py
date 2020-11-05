from selenium import webdriver
import time
import yaml

# open your configuration file see example_config.yml
with open(r'.cfg.yml') as file:
    cfg = yaml.safe_load(file)

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
login_button  = browser.find_elements_by_xpath(cfg['xpath_login_click'])[0]
login_button.click()

# close the log in form in case needed
# browser.find_elements_by_xpath('xpath_login_close')[0].click()

