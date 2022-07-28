echo off
echo BATCH: Accediendo al directorio...
cd C:\PrivateApps\Proyectos\python-PersonalAutoLogin\
echo BATCH: Ejecutar script...
@REM python.exe .\teletrabajo_chrome.py
@echo BATCH: Configurando VPN
python.exe .\load_vpn_data.py
@echo BATCH: Completado
exit 0
@echo Adios.
