import pyautogui as gui
from time import sleep
import subprocess
import vpn_pass

def intento_click():
    gui.click(734, 575); 
    gui.write(vpn_pass.KEY+'\n')

def intento_teclado():
    print('VPN: Automatizando el teclado para cargar datos de usuario.')
    forti = []
    while forti == []:
        forti = gui.getWindowsWithTitle('FortiClient -- The Security Fabric Agent')
        sleep(1)
    sleep(1)
    gui.press('tab')
    gui.press('tab')
    gui.press('tab')
    gui.write(vpn_pass.KEY+'\n')

def iniciar_remoto():
    print('VPN: Inicio de la aplicacion del escritorio remoto.')
    subprocess.Popen('C:\\Windows\\System32\\mstsc.exe')

try:
    intento_teclado()
except Exception as e:
    print('VPN: Fallo el intento de automatizar el teclado.')

try: 
    iniciar_remoto()
except Exception as e:
    print('VPN: Fallo el inicio del escritorio remoto.', e)
   