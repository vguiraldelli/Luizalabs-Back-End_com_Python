# Função para formatar o retorno do tipo de dado, mantendo apenas o que vem entre as ''
def formatar_tipo(tipo):
    return str(tipo).split("'")[1]