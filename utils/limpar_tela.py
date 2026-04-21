import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    limpar_tela()