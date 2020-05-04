# import webbrowser
# import bs4
# import requests

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # asume que geckodriver esta copiado en /path/to/python/Scripts, sino descargarlo (https://github.com/mozilla/geckodriver/releases) y depositarlo en /path/to/python/Scripts
    opts = Options()
    opts.headless = True
    browser = Firefox(options=opts)
    browser.get(
        'https://duckduckgo.com'
    )
    search_next = browser.find_element_by_name('q')
    search_next.send_keys('ozkrpy')
    search_next.submit()
    wait = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "links"))
    )
    results = browser.find_elements_by_id('links')
    # time.sleep(10)
    print(results[0].text) 
    pin = input('PIN:')
    print(pin)
    browser.close()
    quit()
except Exception as error:
    print("{}".format(error))


