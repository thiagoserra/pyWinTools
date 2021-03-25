#! /usr/bin/python3
"""
Classe pyWinTools

    Classe responsavel pelo fluxo de telas do app.
    @autor: Thiago Serra <thiagonce@gmail.com>

"""
from Util import *
from bingwall import bingwall
from VPNCx import VPNCx
from criaAmostraBigFile import criaAmostraBigFile
from NetWork import NetWork


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
        print('_' * 80)
        print('Py' * 40)
        print('-' * 80)
        print("--- pyWinTools - v.{}".format(self.versao))
        print("--- GitHub: @thiagoserra | https://github.com/thiagoserra/pyWinTools")
        print('_' * 80)
        print('pY' * 40)
        print('-' * 80)

    def menu(self, msg = ''):
        self.splash()
        print(' ' * 20, '*** ESCOLHA ENTRE AS OPÇÕES ***')
        print('-' * 80)
        print('-- [1]   Baixar WallPaper Bing do Dia')
        print('-- [2]   Baixar "x" últimos WallPapers Bing')
        print('-- [3]   Verficar Servidores VPN CAIXA')
        print('-- [4]   Criar Amostra de um arquivo GRANDE')
        print('-- [5]   Verficar meu IP Externo')
        print('-- [6]   Verificar Interfaces de Rede')
        print('-- [7]   Verificar dados da rede Wifi')
        print('-' * 45)
        print('-- [99]  Sair')
        print('-' * 45)
        if msg != '':
            print('[msg>] ', msg)
            print('-' * 80)
        print()

        obj = None
        op = str(input('[?] Informe uma opção válida: ')).strip()
        try:
            op = int(op)
        except ValueError:
            print('[x] Opção {} inválida!'.format(op))
            sleep(2)
            self.menu()

        if op == 1:
            msg = ''
            obj = bingwall()
            msg = obj.download_wallpaper()
            sleep(5)
            if not msg :
                msg = '[x] Erro executando rotina! (op 1)'
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 2:
            msg = ''
            max = str(input('[?] Quantos papeis de parede deseja baixar? [1 a 20]: '))
            try:
                max = int(max.strip())
                if max < 0 or max > 20:
                    max = False
            except ValueError:
                max = False
            obj = bingwall()
            msg = obj.download_old_wallpapers(max)
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
        elif op == 5:
            obj = NetWork()
            msg = obj.externalIp()
            if not msg :
                print('[x] Erro obtendo ip externo! (op 4)')
            else:
                msg = f' Meu IP Externo -> {msg}.'
            self.menu(msg)
        elif op == 6:
            obj = NetWork()
            msg = obj.show_networks()
            input('[?] Tecle em qualquer tecla para continuar...')
            if not msg :
                print('[x] Erro obtendo dados de rede! (op 5)')
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 4:
            obj = criaAmostraBigFile()
            msg = obj.copiar()
            sleep(5)
            if not msg :
                msg = '[x] Erro executando rotina! (op 6)'
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 7:
            obj = NetWork()
            msg = obj.show_wifi_data()
            input('[?] Tecle em qualquer tecla para continuar...')
            if not msg :
                print('[x] Erro obtendo dados de rede! (op 5)')
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            self.menu(msg)
        elif op == 99:
            self.splash()
            print('-' * 80)
            print('!' * 80)
            print('!!! Obrigado por usar !!!')
            print('!' * 80)
            print('!! bye ' * 2, '!!')
            print('-' * 80)
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


n = pyWinTools()