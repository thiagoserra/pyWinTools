# pyWinTools
Pequenos utilitários em Python 3 para automação de tarefas no Windows.

## Notas da versão
**v.1.0**
* Ainda cru, somente commit incial, sem integração.

**v.2.0**
* Interface criada para shell/prompt (pyWinTools.py)
* Utilitário de Download do WallPaper Diário do Bing adicionado
* Verificador de disponibilidade de Servidor VPN da CAIXA

## Como rodar
```
python pyWinTools.py
```

Existe um pacote executável disponível (exe) para Windows 10.
É possível gerar pelo PyInstaller este mesmo executável na sua máquina fazendo o seguinte:

1. Clone este repositõrio na sua máquina
2. No cmd ou powershell ou windos terminal entre no diretório de digite:

```
pip install -r requirements.txt
```
(Lembre-se que é necessário ter o Python 3 instalado e funcionando!)

3. Digite o comando 'geraExe.bat':
```
geraExe.bat
```

O arquivo **pyWinTools.exe** será criado na mesma pasta do projeto.
