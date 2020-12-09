import requests
import time
import sys
import os
import datetime as dt

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

def consulta():
    clear()

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
        consulta()
    else:
        clear()
        print('*' * 80)
        print('* * * Verifica disponibilidade dos servidores VPN CAIXA * * *')
        print('*' * 80)
        print('! ! ! Finalizado ! ! !')
        print('*' * 80)

consulta()