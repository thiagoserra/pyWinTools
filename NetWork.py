#! /usr/bin/python3
"""
Classe NetWork

    Funções para obter dados da máquina em relação a conectividade
    @autor: Thiago Serra <thiagonce@gmail.com>

"""
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from ipaddress import IPv4Interface, IPv6Interface
import urllib.request
import socket
from Util import *


class NetWork():
    def __init__(self):
        clear()
        self.cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,MACAddress,IPSubnet,DNSHostName,Caption,DefaultIPGateway /format:rawxml'
        self.nics = []
        print('*' * 80)
        print('* * * Consulta Dados de Rede * * *')
        print('*' * 80)

    def externalIp(self):
        ex_ip = ''
        try:
            ex_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            return str(ex_ip).strip()
        except:
            return False

    def localIP(self):
        hostname = ''
        local_ip = ''
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return str(f'host: {hostname} | ip: {local_ip}')
        except:
            return False

    def getNics(self):
        xml_text = check_output(self.cmd, creationflags=8)
        xml_root = fromstring(xml_text)
        keyslookup = {
            'DNSHostName' : 'hostname',
            'IPAddress' : 'ip',
            'IPSubnet' : '_mask',
            'Caption' : 'hardware',
            'MACAddress' : 'mac',
            'DefaultIPGateway' : 'gateway',
        }

        for nic in xml_root.findall("./RESULTS/CIM/INSTANCE") :
            n = {
                'hostname':'',
                'ip':[],
                '_mask':[],
                'hardware':'',
                'mac':'',
                'gateway':[],
            }
            for prop in nic :
                name = keyslookup[prop.attrib['NAME']]
                if prop.tag == 'PROPERTY':
                    if len(prop):
                        for v in prop:
                            n[name] = v.text
                elif prop.tag == 'PROPERTY.ARRAY':
                    for v in prop.findall("./VALUE.ARRAY/VALUE") :
                        n[name].append(v.text)
            self.nics.append(n)

            for i in range(len(n['ip'])) :
                arg = '%s/%s'%(n['ip'][i],n['_mask'][i])
                if ':' in n['ip'][i] : n['ip'][i] = IPv6Interface(arg)
                else : n['ip'][i] = IPv4Interface(arg)
            del n['_mask']
        return self.nics


    def show_networks(self):
        self.nics = self.getNics()
        ext_ip = self.externalIp()
        if ext_ip:
            print(f'ip externo: [{ext_ip}]')
        for nic in self.nics :
            for k,v in nic.items() :
                print('%s : %s'%(k,v))
            print()
        return True
