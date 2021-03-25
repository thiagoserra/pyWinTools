#! /usr/bin/python3
"""
Util.py

    Set de funções usadas na coleção
    @autor: Thiago Serra <thiagonce@gmail.com>

"""
import os
import sys
import datetime as dt
from time import sleep, time

clear = lambda: os.system('cls')


def check():
    now = dt.datetime.now()
    vencimento = dt.datetime.strptime('31/03/2021', '%d/%m/%Y')
    if now >= vencimento:
        print('!' * 80)
        print('[i] Versão expirada. Baixe a nova versão!')
        print('!' * 80)
        print('!!! Programa Finalizado !!!')
        print('!' * 80)
        sys.stdout.flush()
        os._exit(0)


def formatarTimer(start, end):
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.5f}".format(int(hours), int(minutes), seconds)
