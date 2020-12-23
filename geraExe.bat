@echo off
echo -------- Gerando executavel...
pyinstaller.exe --debug=bootloader --name pyWinTools --onefile --noupx --icon="icon.ico" pyWinTools.py
echo -------- Exe criado!
del pyWinTools.exe
echo -------- Copiando arquivo...
copy dist\pyWinTools.exe .
echo -------- Finalizado!