#! /usr/bin/python3
"""
Classe VPNCx

    Verifica disponibilidade dos servidores VPN CAIXA
    @autor: Thiago Serra <thiagonce@gmail.com>

"""
import requests
from Util import *
from operator import itemgetter

class VPNCx():

    def __init__(self):
        clear()
        print('*' * 80)
        print('* * * Verifica disponibilidade dos servidores VPN CAIXA * * *')
        print('*' * 80)

    def consulta(self):
        servers = []
        print("[i] Aguarde...")
        for i in range(0, 255):
            num = str(i).zfill(2)
            url = 'https://alcor'+num+'.caixa.gov.br'
            try:
                inicio = time()
                conn = requests.get(url)
                tempo_total = time() - inicio
                if(conn):
                    servers.append([url, tempo_total])
            except:
                pass

        print('*' * 80)
        if len(servers) == 0:
            print('[i] Nenhum servidor disponível!')
            return False
        else:
            servers = sorted(servers, key = itemgetter(1))
            for ss in servers:
                print('[i] Servidor: {} | Tempo de resposta: {:.3f} seg.'.format(ss[0], ss[1]))
        print('*' * 80)

        op = ''
        while op not in ('A', 'M'):
            op = str(input("[?] 'A' para tentar novamente, 'M' volta para o menu: ")).strip().upper()

        if op == 'A':
            clear()
            self.consulta()
        else:
            return True
