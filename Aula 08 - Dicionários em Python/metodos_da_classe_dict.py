import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho 
print(" Métodos da Classe Dict \n".center(50, "=") + "\n")

# Criando um dicionário
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "altura": 1.68,
    "is_estudante": True
}
print(f"Pessoa: {pessoa}")
print(f"Tipo da variável: {type(pessoa)}\n")

# Obtendo as chaves do dicionário
print(f"Chaves do dicionário: {pessoa.keys()}")

# Obtendo os valores do dicionário
print(f"Valores do dicionário: {pessoa.values()}")

# Obtendo os itens (chave-valor) do dicionário
print(f"Itens do dicionário: {pessoa.items()}\n")

# Verificando se uma chave existe
print(f"A chave 'nome' existe? {'nome' in pessoa}")
print(f"A chave 'peso' existe? {'peso' in pessoa}\n")

# Obtendo o tamanho do dicionário
print(f"Quantidade de elementos no dicionário: {len(pessoa)}\n")

# Iterando sobre o dicionário
print("Iterando sobre o dicionário:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("\n" + " Outros Métodos ".center(50, "=") + "\n")

# .copy()
print("Método .copy()")
pessoa_copia = pessoa.copy()
print(f"Cópia do dicionário: {pessoa_copia}\n")

# .fromkeys()
print("Método .fromkeys()")
chaves = ["a", "b", "c"]
novo_dict = dict.fromkeys(chaves, "valor_padrao")
print(f"Dicionário criado com .fromkeys(): {novo_dict}\n")

# .get()
print("Método .get()")
print(f"Obtendo 'nome' com .get(): {pessoa.get('nome')}")
print(f"Obtendo 'peso' com .get() (chave inexistente): {pessoa.get('peso')}")
print(f"Obtendo 'peso' com .get() (com valor padrão): {pessoa.get('peso', 70.5)}\n")

# .setdefault()
print("Método .setdefault()")
pessoa.setdefault("peso", 65.0) # Se não existe, insere e retorna. Se existe, apenas retorna.
print(f"Após .setdefault('peso', 65.0): {pessoa}\n")

# .update()
print("Método .update()")
pessoa.update({"cidade": "São Paulo", "idade": 26})
print(f"Após .update() (atualizando 'idade' e adicionando 'cidade'): {pessoa}\n")

# .pop()
print("Método .pop()")
peso_removido = pessoa.pop("peso")
print(f"Valor removido com .pop('peso'): {peso_removido}")
print(f"Dicionário após .pop(): {pessoa}\n")

# .popitem()
print("Método .popitem()")
ultimo_item = pessoa.popitem()
print(f"Último item removido com .popitem(): {ultimo_item}")
print(f"Dicionário após .popitem(): {pessoa}\n")

# .clear()
print("Método .clear()")
pessoa.clear()
print(f"Dicionário após .clear(): {pessoa}\n")
