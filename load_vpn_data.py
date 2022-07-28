import pyautogui as gui
from time import sleep
import subprocess
import vpn_pass
import constantes

def intento_click():
    gui.click(734, 575); 
    gui.write(vpn_pass.KEY)

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
            forti = gui.getWindowsWithTitle('FortiClient')
            sleep(1)
        sleep(1)
        print('VPN: Listo, cargando los parametros de usuario y password.')
        gui.press('tab', interval=0.25)
        gui.press('tab', interval=0.25)
        gui.press('tab', interval=0.25)
        gui.write(vpn_pass.KEY, interval=0.05)
        gui.press('tab', interval=0.25)
        gui.press('tab', interval=0.25)
        gui.press('enter')
        sleep(12)
    except Exception as e:
        print('VPN: Fallo el intento de automatizar el teclado.')


def iniciar_remoto():
    try:
        print('VPN: Inicio de la aplicacion del escritorio remoto.')
        gui.keyDown('ctrl')
        gui.press('tab')
        gui.keyUp('ctrl')
        subprocess.Popen(constantes.DRIECTORIO_ESCRITORIO_REMOTO
        )
        #sleep(1)
        print('VPN: Procesado.')
        exit()
        print('Adios.')

        # gui.press('return')
    except Exception as e:
        print('VPN: Fallo el inicio del escritorio remoto.', e)

if __name__=='__main__':
    iniciar_forti()
    intento_teclado()
    iniciar_remoto()
    exit()