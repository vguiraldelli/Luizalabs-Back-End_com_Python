import textwrap
import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

from movimentacoes import Deposito, Saque
from cliente import Cliente, PessoaFisica
from conta import Conta, ContaCorrente

class Menu():
    def menu(self):
        menu = """
        ========== MENU ==========
        [ d ]   - Depositar
        [ s ]   - Sacar
        [ e ]   - Extrato
        [ nu ]  - Novo Usuário (Cliente)
        [ nc ]  - Nova Conta
        [ lu ]  - Listar Usuários (Clientes)
        [ lc ]  - Listar Contas
        [ q ]   - Sair
        ==========================
        """
        return input(textwrap.dedent(menu))
    
    def novo_cliente(self, clientes):
        cpf = int(input("Digite o CPF do cliente: "))
        cliente = self.filtrar_cliente(clientes, cpf)
        
        if cliente:
            print("\n### Cliente já cadastrado! ###\n")
            return

        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento: ")
        endereco = input("Digite o endereço: ")
        cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
        clientes.append(cliente)
        print("\n=== Usuário criado com sucesso! ===")

    def listar_clientes(self, clientes):
        if not clientes:
            print("\n### Nenhum cliente encontrado ###\n")
            return
        else:
            print("\n=== Listando Clientes ===")
            for cliente in clientes:
                print(f"CPF: {cliente.cpf} - Nome: {cliente.nome} - Endereço: {cliente.endereco}")  
    
    def nova_conta(self, numero_conta, clientes, contas):
        _cpf = int(input("Digite o CPF do cliente: "))
        _cliente = self.filtrar_cliente(clientes, _cpf)
        
        if not _cliente:
            print("\n### Cliente não encontrado!")
            return
        conta = ContaCorrente.nova_conta(_cliente, numero_conta)
        contas.append(conta)
        _cliente.adicionar_conta(conta)
        print("\n=== Conta criada com sucesso! ===")
    
    def listar_contas(self, contas):
        if not contas:
            print("\n### Nenhuma conta encontrada ###\n")
            return
        else:
            print("\n=== Listando Contas ===\n")
            for conta in contas:
                print(f"Agência: {conta.agencia} - Conta: {conta.numero} - CPF: {conta.cliente.cpf} - Cliente: {conta.cliente.nome} - Saldo: R$ {conta.saldo:.2f}")

    def recuperar_conta_cliente(self, cliente):
        if not cliente.contas:
            print("\n### Nenhuma conta encontrada para o cliente!")
            return
        
        # FIXME: Não permite o cliente escolher a conta
        return cliente.contas[0]    

    def filtrar_cliente(self, clientes, cpf):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    
    def filtrar_conta(self, cliente):
        if not cliente.contas:
            print("\n### Nenhuma conta encontrada para o cliente!")
            return None
        return cliente.contas[0]

    def depositar(self, clientes):
        cpf = int(input("Digite o CPF do cliente: "))
        cliente = self.filtrar_cliente(clientes, cpf)
        
        if not cliente:
            print("\n### Cliente não encontrado!")
            return

        valor = float(input("Digite o valor do depósito: "))
        transacao = Deposito(valor)
        conta = self.filtrar_conta(cliente)
        if conta:
            transacao.registrar(conta)

    def sacar(self, clientes):
        cpf = int(input("Digite o CPF do cliente: "))
        cliente = self.filtrar_cliente(clientes, cpf)
        
        if not cliente:
            print("\n### Cliente não encontrado!")
            return

        conta = self.filtrar_conta(cliente)

        if not conta:
            return

        valor = float(input("Digite o valor do saque: "))
        
        if valor > conta.saldo:
            print("\n### Você não tem saldo suficiente! ###")
            return
        
        transacao = Saque(valor)
        transacao.registrar(conta)

    def extrato(self, clientes):
        cpf = int(input("Digite o CPF do cliente: "))
        cliente = self.filtrar_cliente(clientes, cpf)
        
        if not cliente:
            print("\n### Cliente não encontrado!")
            return

        conta = self.filtrar_conta(cliente)
        if not conta:
            return

        print("\n=== Exibindo Extrato ===")
        transacoes = conta.historico.transacoes
        
        extrato = ""
        if not transacoes:
            extrato = "\n=== Nenhuma transação encontrada ===\n"
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}"

        print(extrato)
        print(f"\nSaldo Atual: R$ {conta.saldo:.2f}")
        

def main():
    clientes = []
    contas = []
    sistema_bancario = Menu()

    while True:
        opcao = sistema_bancario.menu()

        if opcao == "d":
            sistema_bancario.depositar(clientes)
        elif opcao == "s":
            sistema_bancario.sacar(clientes)
        elif opcao == "e":
            sistema_bancario.extrato(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            sistema_bancario.nova_conta(numero_conta, clientes, contas)
        elif opcao == "lu":
            sistema_bancario.listar_clientes(clientes)
        elif opcao == "lc":
            sistema_bancario.listar_contas(contas)
        elif opcao == "nu":
            sistema_bancario.novo_cliente(clientes)
        elif opcao == "q":
            break
        else:
            print("\n### Operação inválida! Tente novamente. ###\n")
    
if __name__ == "__main__":
    main()