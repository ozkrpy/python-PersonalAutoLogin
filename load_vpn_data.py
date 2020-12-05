import pyautogui as gui
from time import sleep
import vpn_pass

def intento_click():
    gui.click(734, 575); 
    gui.write(vpn_pass.KEY+'\n')

def intento_teclado():
    forti = []
    while forti == []:
        forti = gui.getWindowsWithTitle('FortiClient -- The Security Fabric Agent')
    sleep(1)
    gui.press('tab')
    gui.press('tab')
    gui.press('tab')
    gui.write(vpn_pass.KEY+'\n')

try:
    intento_teclado()
except Exception as e:
    print('Fallo el intento de automatizar el teclado.')