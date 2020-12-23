"""
Classe pyWinTools

    Classe responsavel pelo fluxo de telas do app.
    @autor: Thiago Serra <thiagonce@gmail.com>

"""
from Util import *
import BingWall

class pyWinTools():

    __versao = '2.0'

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
        print('-' * 45)
        print('-- [99]  Sair')
        if msg != '':
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

            if not msg :
                print('[x] Erro executando rotina!')
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            sleep(5)
            self.menu(msg)
        elif op == 2:
            msg = ''
            obj = BingWall()
            msg = obj.download_old_wallpapers()

            if not msg :
                print('[x] Erro executando rotina!')
            else:
                msg = '[i] Rotina finalizada com sucesso!'
            sleep(5)
            self.menu(msg)
        elif op == 99:
            self.splash()
            print('!' * 80)
            print('!!! Programa Finalizado !!!')
            print('!' * 80)
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