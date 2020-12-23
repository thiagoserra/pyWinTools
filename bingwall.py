"""
Classe BingWall

    Classe responsavel pela verificação e Download de WallPapers diários do BING
"""
#! /usr/bin/python3
# -------------------------------------------------------------------------------------------------
# Based on version of:
#   Author: Maximilian Muth <mail@maxi-muth.de>
#   https://github.com/mammuth/bing-wallpaper
#   License: GPL-2.0
#   Description: Downloads the Bing picture of the Day and sets it as wallpaper (Linux / Windows).
# -------------------------------------------------------------------------------------------------
# !! Modified !! Thiago Serra <thiagonce@gmail.com> :
#   POO aplicada a ideia original
#   alteracao do path de salvamento
#   adicionado ao pacote wintools (https://github.com/thiagoserra/wintools)
# -------------------------------------------------------------------------------------------------
import datetime
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
from Util import *

class BingWall():

    def __init__(self):
        clear()
        print('*' * 80)
        print('* * * Baixar WallPaper Diário do Bing * * *')
        print('*' * 80)
        self.pic_path = ''
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.save_dir = 'C:\\Users\\thiag\\OneDrive\\Imagens'
        if not os.path.exists(self.save_dir):
            self.save_dir = self.join_path(self.dir_path, 'images')

    def join_path(self, *args):
        if isinstance(args[0], list):
            path_list = args[0]
        else:
            path_list = args
        val = [str(v).strip(' ') for v in path_list]
        return os.path.normpath('/'.join(val))


    def set_windows_wallpaper(self):
        #TODO: verificar... não teve efeito no teste: Windows 10 v. 20H2 comp. 19042.685
        # incio ----
        print("[i] Removendo TranscodedImageCache do registro do Windows...")
        os.system('REG DELETE \"HKCU\Control Panel\Desktop\" /v TranscodedImageCache /f')

        print("[i] Definindo imagem baixada no registro do Windows...")
        cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' % self.pic_path
        os.system(cmd)

        print("[i] Limpando diretórios de cache de imagens do tema do windows...")
        os.system("del /F /Q %AppData%\Microsoft\Windows\Themes\CachedFiles")
        os.system("del /F /Q %AppData%\Microsoft\Windows\Themes\TranscodedWallpaper")

        os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
        print('[i] Wallpaper definido!')
        # fim ----

    def set_linux_wallpaper(self):
        os.system(''.join(['gsettings set org.gnome.desktop.background picture-uri file://', self.pic_path]))
        print('[i] Wallpaper definido!')


    def set_wallpaper(self):
        if sys.platform.startswith('win32'):
            self.set_windows_wallpaper()
        elif sys.platform.startswith('linux'):
            self.set_linux_wallpaper()
        else:
            print('[x] Sistema operacional não suportado.')


    def download_old_wallpapers(self, minus_days=False):
        """
        Uses download_wallpaper(set_wallpaper=False) to download the last 20 wallpapers.
        If minus_days is given an integer a specific day in the past will be downloaded.
        """
        if minus_days:
            self.download_wallpaper(idx=minus_days, use_wallpaper=False)
            return
        for i in range(0, 20):
            self.download_wallpaper(idx=i, use_wallpaper=False)


    def download_wallpaper(self, idx=0, use_wallpaper=True):
        try:
            usock = urlopen(''.join(['http://www.bing.com/HPImageArchive.aspx?format=xml&idx=',
                                    str(idx), '&n=1&mkt=pt-BR']))
        except Exception as e:
            print('[x] Erro fazendo o download #', idx, e)
            return False
        try:
            xmldoc = minidom.parse(usock)
        except Exception as e:
            print('[x] Erro processando XML #', idx, e)
            return False

        for element in xmldoc.getElementsByTagName('url'):
            url = 'http://www.bing.com' + element.firstChild.nodeValue
            now = datetime.datetime.now()
            date = now - datetime.timedelta(days=int(idx))

            self.pic_path = self.join_path(self.save_dir, ''.join([date.strftime('bing_wp_%d-%m-%Y'), '.jpg']))
            print(f'[i] Imagem salva em: {self.pic_path}')

            if os.path.isfile(self.pic_path):
                print('[i] Imagem de ', date.strftime('%d-%m-%Y'), ' já foi baixada!')
                if use_wallpaper:
                    self.set_wallpaper()
                return True
            print('[i] Baixando: ', date.strftime('%d-%m-%Y'), 'index #', idx)

            urlretrieve(url.replace('_1366x768', '_1920x1200'), self.pic_path)
            if use_wallpaper:
                self.set_wallpaper()
                return True
