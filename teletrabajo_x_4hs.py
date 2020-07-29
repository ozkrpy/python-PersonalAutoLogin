from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

try:
    print("Cargando sitio web.")
    # asume que geckodriver esta copiado en /path/to/python/Scripts, sino descargarlo (https://github.com/mozilla/geckodriver/releases) y depositarlo en /path/to/python/Scripts
    opts = Options()
    opts.headless = True
    browser = Firefox(options=opts)
    # Cargar la pagina de Teletrabajo, y buscar el boton 'Siguiente/Acepto'.
    browser.get(
        'https://seguridad.personal.com.py/teletrabajo/'
    )
    button_next = browser.find_element_by_id('nextBtn')
    # Clic en Siguiente para pasar al step2: Pantalla para ingresar el numero de linea.
    button_next.click()
    # Obtiene el campo de numero de linea, y envia los digitos.
    # linea = input('LINEA (59597XXXXXXX):')
    numero_linea = browser.find_element_by_name('cphone')
    numero_linea.send_keys('595971325507')
    # Clic en Siguiente para pasar al step3: Pantalla de notificacion que se envio el SMS.
    button_next.click()
    print("Aguarda unos segundos para recepcionar el PIN.")
    # Darle un tiempo para que se recepcione el SMS.
    sleep(3)
    # Clic en Siguiente para pasar al step4: Pantalla para ingresar el pin.
    button_next.click()
    # Ingresar el pin recibido en el celular.
    pin = input('PIN:')
    numero_pin = browser.find_element_by_name('pin')
    numero_pin.send_keys(pin)
    # Clic en Siguiente para pasar al step5: Pantalla para ingresar cantidad de horas.
    button_next.click()
    # Modificacion semana del 27/07/2020: se quito la cantidad de horas. Setear la cantidad de horas a loguearse en el vpn.
    # try:
    #     wait = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.NAME, "dd"))
    #     )
    #     numero_horas = browser.find_element_by_name('dd')
    #     sleep(2)
    #     numero_horas.send_keys(4)
    # except Exception as error:
    #     print("Error al intentar ingresar total de horas.")
    #     print("Mensaje:","{}".format(error))
    # Clic en Siguiente para pasar al step6: Pantalla para inicializar el Forti.
    # button_next.click()
    # Clic en iniciar y habilitar la conexion VPN.
    try:
        wait = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "fo1"))
        )
        activar_forti = browser.find_element_by_id("fo1")
        sleep(3)
        activar_forti.click()
        sleep(2)
        # Maneja el mensaje de alerta que aparece en la pagina tras el click.
        obj = browser.switch_to.alert
        msg=obj.text
        print ("Estado: "+ msg)
        sleep(1)
        obj.accept()
    except Exception as error:
        # print("No se pudo hacer clic en iniciar Forti desde la pagina.")
        print("Mensaje:","{}".format(error))
    # Cierra la sesion y mata el proceso.
    print("Listo, ya se puede acceder al VPN.")
    browser.close()
except Exception as error:
    print("{}".format(error))