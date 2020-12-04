from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import constantes

class Bot():
    def __init__(self):   
        print('SELENIUM:', "Inicializando el navegador.")
        self.opts = Options()
        self.opts.headless = constantes.OCULTAR_NAVEGADOR
        if (constantes.FIREFOX_PERFIL != ''):
            self.opts.profile = constantes.FIREFOX_PERFIL
        self.browser = Firefox(options=self.opts)
        print('SELENIUM:', "Cargando sitio web.")
        self.browser.get(constantes.URL)
        self.button_next = self.browser.find_element_by_id('nextBtn')
        self.button_next.click()
        self.numero_linea = self.browser.find_element_by_name('cphone')
        self.numero_linea.send_keys(constantes.LINEA)
        # sleep(1)
        self.button_next.click()
        print('SELENIUM:', "Aguarda unos segundos para recepcionar el PIN.")
        sleep(4)
        self.button_next.click()
        self.numero_pin = self.browser.find_element_by_name('pin')
        # print('SELENIUM:', "PIN:", self.numero_pin)
        while (self.numero_pin==''):
            print('SELENIUM:', "no se detecto el campo PIN, reintentando.")
            sleep(1)
            self.numero_pin = self.browser.find_element_by_name('pin')
        self.pin = input('SELENIUM PIN:')
        self.numero_pin.send_keys(self.pin)
        sleep(1)
        self.button_next.click()
        try:
            self.wait = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "fo1"))
            )
            self.activar_forti = self.browser.find_element_by_id("fo1")
            sleep(4)
            self.activar_forti.click()
            sleep(2)
            self.obj = self.browser.switch_to.alert
            self.msg=self.obj.text
            print ('SELENIUM:', "Estado: "+self.msg)
            sleep(2)
            self.obj.accept()
            print('SELENIUM:', "Listo, ya se puede acceder al VPN.")
        except Exception as error:
            print('SELENIUM:', "No se activo la sesion VPN:","{}".format(error))
        self.browser.close()
        print('SELENIUM:', 'Ya se puede cerrar la aplicacion.')
try:
    init_bot = Bot()
except Exception as error:
    print('SELENIUM:', "ERROR GENERAL DEL PROCESO:","{}".format(error))
   
