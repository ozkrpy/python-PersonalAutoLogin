from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import constantes

def navegador_abrir():
    opts = Options()
    opts.headless = constantes.OCULTAR_NAVEGADOR
    if (constantes.FIREFOX_PERFIL != ''):
        opts.profile = constantes.FIREFOX_PERFIL
    navegador = Firefox(options=opts)
    return navegador

def ver_existencia(browser, buscar_elemento: str, criterio:str='ID'):
    wait = ''
    elemento_encontrado = ''
    validar = False
    i = 0
    while validar==False: 
        try:
            if criterio=='NAME':
                wait = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.NAME, buscar_elemento)))
                elemento_encontrado = browser.find_element_by_name(buscar_elemento)
                validar = True
            else:
                wait = WebDriverWait(browser, 10).until(
                    EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal']")))
                elemento_encontrado = browser.find_element_by_id(buscar_elemento)
                validar = True
            if validar:
                return elemento_encontrado
        except Exception as error:
            print('SELENIUM ERROR:', "No se detecto el elemento: "+buscar_elemento,"{}".format(error))
            validar = False
        i += 1
    return False

def siguiente(browser):
    boton_siguiente = ver_existencia(browser, 'nextBtn')
    boton_siguiente.click()

def cargar_linea(browser):
    numero_linea = ver_existencia(browser, 'cphone', 'NAME')
    numero_linea.send_keys(constantes.LINEA)

def cargar_pin(browser):
    numero_pin = ver_existencia(browser, 'pin', 'NAME')
    pin = input('SELENIUM PIN:')
    numero_pin.send_keys(pin)

def activar_vpn(browser):
    activar_forti = ver_existencia(browser, "fo1")
    activar_forti.click()
    
def habilitar_vpn(browser):
    sleep(2)
    obj = browser.switch_to.alert
    msg=obj.text
    print ('SELENIUM:', "Estado: "+msg)
    sleep(1)
    obj.accept()

try:
    validar = False
    print('SELENIUM:', "Inicializando el navegador.")
    browser = navegador_abrir()

    print('SELENIUM:', "Cargando sitio web.")
    browser.get(constantes.URL)
    siguiente(browser)
    
    print('SELENIUM:', "Enviando numero de linea.")
    cargar_linea(browser)
    siguiente(browser)

    print('SELENIUM:', "Aguardar PIN enviado a la linea.")
    siguiente(browser)
    
    print('SELENIUM:', "Escribir PIN.")
    cargar_pin(browser)
    siguiente(browser)

    print('SELENIUM:', "Activar y habilitar la VPN.")
    activar_vpn(browser)
    habilitar_vpn(browser)
    # sleep(10)
    
    browser.close()
    print('SELENIUM:', 'Ya se puede cerrar la aplicacion.')

except Exception as error:
    print('SELENIUM:', "ERROR GENERAL DEL PROCESO:","{}".format(error))
   
