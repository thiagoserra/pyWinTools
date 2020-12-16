@echo off
echo -------- Gerando executavel...
pyinstaller.exe --debug=bootloader --name VPNDisponivel --onefile --noupx --icon="icon.ico" servidores.py
echo -------- Exe criado!
echo -------- Copiando arquivo...
del ..\Executaveis\VPNDisponivel.exe
copy dist\VPNDisponivel.exe ..\Executaveis\
echo -------- Finalizado!