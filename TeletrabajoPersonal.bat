echo off
echo BATCH: Accediendo al directorio...
cd C:\PrivateApps\Proyectos\python-PersonalAutoLogin\
echo BATCH: Ejecutar script...
python.exe .\teletrabajo_or.py
echo BATCH: Configurando VPN
python.exe .\load_vpn_data.py
