"""
Util.py

    Set de funções usadas na coleção
    @autor: Thiago Serra <thiagonce@gmail.com>

"""

import os
import sys
import datetime as dt
from time import sleep

clear = lambda: os.system('cls')

def check():
    now = dt.datetime.now()
    vencimento = dt.datetime.strptime('31/01/2021', '%d/%m/%Y')
    if now >= vencimento:
        print('!' * 80)
        print('[i] Versão expirada. Baixe a nova versão!')
        print('!' * 80)
        print('!!! Programa Finalizado !!!')
        print('!' * 80)
        sys.stdout.flush()
        os._exit(0)
