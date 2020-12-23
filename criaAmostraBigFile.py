"""
Classe BingWall

    copia as primeiras xLinhas do arquivo de origem para o arquivo de destino
    @autor: Thiago Serra <thiagonce@gmail.com>
"""
from Util import *

class criaAmostraBigFile():

    def __init__(self):
        clear()
        print("-" * 80)
        print("--- Cria amostra de arquivo (copia as primeiras linhas)")
        print("-" * 80)

    def copiar(self):
        err = 1
        self.arqorigem = ''
        while err == 1:
            self.arqorigem = str(input('[i] Informe o caminho do arquivo de origem: ')).strip()
            if self.arqorigem == 'q':
                return False
            if os.path.exists(self.arqorigem):
                print('[i] Arquivo de origem encontrado!')
                err = 0
            else:
                print('[i] Arquivo de origem não encontrado! Informado: ', self.arqorigem)

        err = 1
        self.xLinhas = 1
        while err == 1:
            linhas = str(input('[i] Quantas linhas deseja extrair do arquivo de origem? (máx. 10.000): ')).strip().replace('.', '').replace(',', '')
            try:
                self.xLinhas = int(linhas)
                if self.xLinhas > 10000:
                    self.xLinhas = 10000
                err = 0
            except ValueError:
                print('[x] Por favor, informe um número inteiro!')

        self.arqdestino  = 'amostra_' + str(dt.datetime.now().strftime("%d%m%Y-%H%M%S")) + '.txt'
        self.start = time()
        print("-" * 80)
        print("--- origem: " + self.arqorigem)
        print("--- destino: " + self.arqdestino)
        print("-" * 80)

        print('[i] Deletando, se houver, arquivo de destino com mesmo nome...')
        if os.path.exists(self.arqdestino):
            os.remove(self.arqdestino)

        destino = open(self.arqdestino, "w")
        origem = open(self.arqorigem, "r")

        print('[i] Criando amostra... Aguarde...')
        for i in range(self.xLinhas):
            destino.write(origem.readline())

        destino.close()
        origem.close()
        print('[i] Tempo total: ', formatarTimer(self.start, time()))
        sleep(5)

        return True



