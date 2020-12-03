echo off
echo BATCH: Accediendo al directorio...
cd C:\PrivateApps\Proyectos\python-PersonalAutoLogin\
echo BATCH: Ejecutar script...
python.exe .\teletrabajo_or.py
echo BATCH: Iniciando FortiClient
START C:\Users\oerm\AppData\Roaming\Microsoft\"Internet Explorer"\"Quick Launch"\"User Pinned"\TaskBar\"FortiClient VPN.lnk"
echo BATCH: Listo, se inicio la aplicacion VPN
cd C:\PrivateApps\Proyectos\python-PersonalAutoLogin\
echo BATCH: Configurando VPN
python.exe .\load_vpn_data.py
echo BATCH: Iniciando el escritorio remoto
%windir%\system32\mstsc.exe