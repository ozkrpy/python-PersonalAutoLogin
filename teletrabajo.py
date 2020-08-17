from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import constantes

class Bot():
    def __init__(self):    
        print("Cargando sitio web.")
        self.opts = Options()
        self.opts.headless = True
        self.browser = Firefox()#options=opts)
        self.browser.get(
            constantes.URL # 'https://s.personal.com.py/teletrabajo/'
        )
        self.button_next = self.browser.find_element_by_id('nextBtn')
        self.button_next.click()
        self.linea = input('LINEA (59597XXXXXXX):')
        self.numero_linea = self.browser.find_element_by_name('cphone')
        self.numero_linea.send_keys(self.linea)
        self.button_next.click()
        print("Aguarda unos segundos para recepcionar el PIN.")
        sleep(3)
        self.button_next.click()
        self.pin = input('PIN:')
        self.numero_pin = self.browser.find_element_by_name('pin')
        self.numero_pin.send_keys(self.pin)
        self.button_next.click()
        try:
            self.wait = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "fo1"))
            )
            self.activar_forti = self.browser.find_element_by_id("fo1")
            sleep(3)
            self.reconectarse = 's'
            while reconectarse.lower()=='s':
                self.activar_forti.click()
                sleep(2)
                self.obj = self.browser.switch_to.alert
                self.msg=obj.text
                print ("Estado: "+ msg)
                sleep(1)
                self.obj.accept()
                print("Listo, ya se puede acceder al VPN.")

                # NEED TO TEST THIS BLOCK: pop-up que solicita seleccionar FortiClient.
                # Find our target window
                # handle = page.driver.find_window("My window title")

                # # Close it
                # page.driver.browser.switch_to.window(handle)
                # page.driver.browser.close

                # # Have the Selenium driver point to another window
                # last_handle = page.driver.browser.window_handles.last
                # page.driver.browser.switch_to.window(last_handle)

                self.reconectarse = input('Reconectarse(s/n)?: ')
        except Exception as error:
            print("No se activo la sesion VPN:","{}".format(error))
        self.browser.close()
        print('Ya se puede cerrar la aplicacion.')
try:
    obj = Bot()
except Exception as error:
    print("ERROR GENERAL DEL PROCESO:","{}".format(error))
   