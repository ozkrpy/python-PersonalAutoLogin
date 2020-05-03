# import webbrowser
# import bs4
# import requests

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

try:
    # webbrowser.open('http://inventwithpython.com/')

    # asume que geckodriver esta copiado en /path/to/python/Scripts, sino descargarlo (https://github.com/mozilla/geckodriver/releases) y depositarlo en /path/to/python/Scripts
    #browser = webdriver.Firefox()
    # browser.get('https://duckduckgo.com')
    # browser.get('https://seguridad.personal.com.py/teletrabajo/')
    # print(type(browser))
    # inputs = browser.find_element_by_tag_name('input')
    # print(inputs.text)
    # browser.quit()
    opts = Options()
    opts.headless = True
    browser = Firefox(options=opts)
    browser.get(
        'file:///C:\\Users\\ozkrp\\Downloads\\Teletrabajo\\teletrabajo.html')
    search_next = browser.find_element_by_id('nextBtn')
    # search_form.submit()
    # results = browser.find_elements_by_class_name('result__body')
    search_next.click()
    numero = browser.find_element_by_name('cphone')
    print(numero)
    numero.send_keys('595971325507')

    print('texto:', numero.text)
    browser.close()
    quit()
except Exception as error:
    paises = []
    print("{}".format(error))
