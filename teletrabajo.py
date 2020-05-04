from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # asume que geckodriver esta copiado en /path/to/python/Scripts, sino descargarlo (https://github.com/mozilla/geckodriver/releases) y depositarlo en /path/to/python/Scripts
    # opts = Options()
    # opts.headless = True
    browser = Firefox()#options=opts)
    # Cargar la pagina de Teletrabajo, y buscar el boton 'Siguiente/Acepto'.
    browser.get(
        'https://seguridad.personal.com.py/teletrabajo/'
    )
    button_next = browser.find_element_by_id('nextBtn')
    # Clic en Siguiente para pasar al step2: Pantalla para ingresar el numero de linea.
    button_next.click()
    # Obtiene el campo de numero de linea, y envia los digitos.
    numero_linea = browser.find_element_by_name('cphone')
    numero_linea.send_keys('595971325507')
    # Clic en Siguiente para pasar al step3: Pantalla de notificacion que se envio el SMS.
    button_next.click()
    # Darle un tiempo para que se recepcione el SMS.
    time.sleep(10)
    # Clic en Siguiente para pasar al step4: Pantalla para ingresar el pin.
    button_next.click()
    # Ingresar el pin recibido en el celular.
    pin = input('PIN:')
    numero_pin = browser.find_element_by_name('pin')
    numero_pin.send_keys(pin)
    # Clic en Siguiente para pasar al step5: Pantalla para ingresar cantidad de horas.
    button_next.click()
    # Setear la cantidad de horas a loguearse en el vpn.
    numero_horas = browser.find_element_by_name('dd')
    numero_horas.send_keys(10)
    # Clic en Siguiente para pasar al step6: Pantalla para inicializar el Forti.
    button_next.click()
    # Clic en inicializar y habilitar la conexion VPN.
    inicializar_forti = browser.find_element_by_id('fo1')
    inicializar_forti.clic()
    # Cierra la sesion y mata el proceso.
    browser.close()
    quit()
except Exception as error:
    print("{}".format(error))


