#! /usr/bin/python3
"""
Classe pyWinTools

    Classe responsavel pelo fluxo de telas do app.
    @autor: Thiago Serra <thiagonce@gmail.com>

"""
from Util import *
from BingWall import BingWall
from VPNCx import VPNCx
from criaAmostraBigFile import criaAmostraBigFile
import urllib.request

class pyWinTools():

    __versao = '3.0'

    @property
    def versao(self):
        return self.__versao

    @versao.setter
    def versao(self, value):
        self.__versao = value

    def __init__(self) -> None:
        self.splash()
        check()
        self.menu()

    def splash(self):
        clear()
        print()
        print('Py' * 40)
        print("--- pyWinTools - v.{}".format(self.versao))
        print("--- GitHub: @thiagoserra | https://github.com/thiagoserra/pyWinTools")
        print('pY' * 40)
        print()

    def menu(self, msg = ''):
        self.splash()
        print('*' * 80)
        print(' ' * 25, '*** OPÇÕES ***')
        print('*' * 80)
        print()
        print('-' * 45)
        print('-- [1]   Baixar WallPaper Bing do Dia')
        print('-- [2]   Baixar 20 últimos WallPapers Bing')
        print('-- [3]   Verficar servidores VPN CAIXA')
        print('-- [4]   Verficar meu IP Externo')
        print('-- [5]   Criar amostra de um arquivo GRANDE')

        print('-' * 45)
        print('-- [99]  Sair')
        if msg != '':
            print()
            print('-' * 45)
            print('[msg>] ', msg)
            print('-' * 80)
        print()

        obj = None
        op = str(input('[i] Informe uma opção válida: ')).strip()
        try:
            op = int(op)
        except ValueError:
            print('[x] Opção {} inválida!'.format(op))
            self.menu()

        if op == 1:
            msg = ''
            obj = BingWall()
            msg = obj.download_wallpaper()
            sleep(5)
            if not msg :
                msg = '[x] Erro executando rotina! (op 1)'
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 2:
            msg = ''
            obj = BingWall()
            msg = obj.download_old_wallpapers()
            sleep(5)
            if not msg :
                msg = '[x] Erro executando rotina! (op 2)'
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 3:
            msg = ''
            obj = VPNCx()
            msg = obj.consulta()
            sleep(5)
            if not msg :
                msg = '[x] Erro executando rotina! (op 3)'
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 4:
            msg = self.externalIp()
            if not msg :
                print('[x] Erro obtendo ip externo! (op 4)')
            else:
                msg = f' Meu IP Externo -> {msg}.'
            self.menu(msg)
        elif op == 5:
            obj = criaAmostraBigFile()
            msg = obj.copiar()
            sleep(5)
            if not msg :
                msg = '[x] Erro executando rotina! (op 5)'
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 99:
            self.splash()
            print('!' * 80)
            print('!!! Programa Finalizado !!!')
            print('!' * 80)
            print('!! bye ' * 2, '!!')
            sleep(3)
            sys.stdout.flush()
            os._exit(0)
        else:
            print('[x] Opção {} inválida!!!'.format(op))
            sleep(3)
            clear()
            self.menu()

        try:
            del(obj)
        except:
            pass

    def externalIp(self):
        ex_ip = ''
        try:
            ex_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            return str(ex_ip).strip()
        except:
            return False


n = pyWinTools()