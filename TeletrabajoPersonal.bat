echo off
echo BATCH: Accediendo al directorio...
cd C:\PrivateApps\Proyectos\python-PersonalAutoLogin\
echo BATCH: Ejecutar script...
python.exe .\teletrabajo_or.py
@REM echo BATCH: Iniciando FortiClient
@REM START C:\Users\oerm\AppData\Roaming\Microsoft\"Internet Explorer"\"Quick Launch"\"User Pinned"\TaskBar\"FortiClient VPN.lnk"
@REM START C:\Users\ozkrp\AppData\Roaming\Microsoft\"Internet Explorer"\"Quick Launch"\"User Pinned"\TaskBar\"FortiClient VPN.lnk"
@REM echo BATCH: Listo, se inicio la aplicacion VPN
@REM cd C:\PrivateApps\Proyectos\python-PersonalAutoLogin\
echo BATCH: Configurando VPN
python.exe .\load_vpn_data.py
