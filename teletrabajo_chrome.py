from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
import pyautogui as gui
import subprocess
import vpn_pass
import constantes

def navegador_abrir():
    print("Inicializando el navegador.")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    navegador = webdriver.Chrome('./WebDrivers/chromedriver')
    return navegador

def navegador_cierre(browser):
    print('Terminar la sesion del navegador.')
    browser.quit()

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
    print("Enviando numero de linea.", constantes.LINEA)
    numero_linea = ver_existencia(browser, 'cphone', 'NAME')
    numero_linea.send_keys(constantes.LINEA)
    print("Aguardar PIN enviado a la linea.")

def cargar_pin(browser):
    numero_pin = ver_existencia(browser, 'pin', 'NAME')
    pin = input('PIN:')
    numero_pin.send_keys(pin)

def activar_vpn(browser):
    print("Procesando habilitacion del VPN.")
    activar_forti = ver_existencia(browser, "fo1")
    activar_forti.click()
    
def habilitar_vpn(browser):
    sleep(2)
    obj = browser.switch_to.alert
    msg=obj.text
    print ("Estado:", msg)
    sleep(1)
    obj.accept()
    sleep(1)
    navegador_cierre(browser)

def iniciar_forti():
    try:
        print('VPN: Inicio de la aplicacion Forti Client.')
        subprocess.Popen(constantes.DIRECTORIO_FORTI)
    except Exception as e:
        print('VPN: Fallo el inicio de Forti Client.', e)

def intento_teclado():
    try:
        print('VPN: Aguardando que la ventana del Forti Cient se visualice.')
        forti = []
        while forti == []:
            forti = gui.getWindowsWithTitle('FortiClient -- The Security Fabric Agent')
            sleep(1)
        print('VPN: Listo, cargando los parametros de usuario y password.')
        sleep(2)
        gui.press('tab', interval=0.25)
        gui.press('tab', interval=0.25)
        gui.press('tab', interval=0.25)
        gui.write(vpn_pass.KEY, interval=0.05)
        gui.press('enter')
        sleep(11)
    except Exception as e:
        print('VPN: Fallo el intento de automatizar el teclado.')

def iniciar_remoto():
    try:
        print('VPN: Inicio de la aplicacion del escritorio remoto.')
        gui.keyDown('ctrl')
        gui.press('tab')
        gui.keyUp('ctrl')
        subprocess.Popen(constantes.DRIECTORIO_ESCRITORIO_REMOTO)
        sleep(1)
    except Exception as e:
        print('VPN: Fallo el inicio del escritorio remoto.', e)

if __name__ == "__main__":
    try:
        validar = False

        browser = navegador_abrir()

        print("Cargando sitio web.")
        browser.get(constantes.URL)
        siguiente(browser)
        
        cargar_linea(browser)
        siguiente(browser)

        siguiente(browser)
        
        cargar_pin(browser)
        siguiente(browser)

        activar_vpn(browser)
        habilitar_vpn(browser)

        iniciar_forti()

        intento_teclado()

        iniciar_remoto()
        print('Se completo la activacion VPN.')
    except Exception as error:
        print("ERROR GENERAL DEL PROCESO:","{}".format(error))
        browser.quit()
        
