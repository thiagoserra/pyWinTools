#! /usr/bin/python3
# -------------------------------------------------------------------------------------------------
#   Author: Thiago Serra <thiagonce@gmail.com>
#   https://github.com/thiagoserra/wintools
#   License: MIT
#   Description: pesquisa servidores disponiveis para conexao pelo VPN da CAIXA
# -------------------------------------------------------------------------------------------------

import requests
import time
from Util import *

class VPNCx():

    def __init__(self) -> None:
        super().__init__()
        self.consulta()

    def consulta(self):
        servers = []
        print('*' * 80)
        print('* * * Verifica disponibilidade dos servidores VPN CAIXA * * *')
        print('* * * v.2 * * * * * * * * * * * * * * * * * C073835 * * * * *')
        print('*' * 80)
        check()
        print("[i] Aguarde...")
        for i in range(0, 255):
            num = str(i).zfill(2)
            url = 'https://alcor'+num+'.caixa.gov.br'
            try:
                inicio = time.time()
                conn = requests.get(url)
                tempo_total = time.time() - inicio
                if(conn):
                    servers.append([url, tempo_total])
            except:
                pass

        print('*' * 80)
        if len(servers) == 0:
            print('[i] Nenhum servidor disponível!')
        else:
            for ss in servers:
                print('[i] Servidor: {} | Tempo de resposta: {:.3f} seg.'.format(ss[0], ss[1]))
        print('*' * 80)

        op = ''
        while op not in ('A', 'X'):
            op = str(input("[?] 'A' para tentar novamente, 'X' para sair: ")).strip().upper()

        if op == 'A':
            clear()
            self.consulta()
        else:
            print('*' * 80)
            print('* * * Verifica disponibilidade dos servidores VPN CAIXA * * *')
            print('*' * 80)
            print('! ! ! Finalizado ! ! !')
            print('*' * 80)

