# Curso DIO - Luizalabs: Back-End com Python

Este repositório contém os exercícios, exemplos e atividades práticas do bootcamp "Back-End com Python" da DIO, em parceria com o Luizalabs.

## Conteúdo das Aulas

Abaixo estão listadas as pastas e os respectivos temas abordados em cada etapa do curso:

- **Aula 01 - Primeiro Programa:** Introdução ao Python e execução do primeiro script.
- **Aula 02 - Conhecendo a Linguagem:** Sintaxe básica, variáveis, entrada/saída de dados e tipos de dados built-in.
- **Aula 03 - Tipos de Operadores:** Operadores aritméticos, lógicos, de comparação, de identidade, de associação e atribuição.
- **Aula 04 - Estruturas Condicionais e de Repetição:** Controle de fluxo utilizando `if`, `elif`, `else`, `for` e `while`. Identação e blocos.
- **Aula 05 - Dominando Strings e Fatiamento:** Manipulação de texto, interpolação, métodos úteis de strings e slicing (fatiamento).
- **Aula 06 - Trabalhando com Listas em Python:** Criação de listas, manipulação de itens e métodos da classe list.
- **Aula 07 - Conhecendo Tuplas em Python:** Trabalhando com estruturas de dados imutáveis.
- **Aula 08 - Dicionários em Python:** Estruturas de chave-valor e seus principais métodos.
- **Aula 09 - Programação Orientada a Objetos (POO) com Python:** Introdução ao paradigma OO, criando classes, objetos, construtores, métodos e atributos.
- **Aula 10 - Conceito de Herança com Python:** Reutilização de código através da herança simples e múltipla.
- **Aula 11 - Encapsulamento em Python:** Modificadores de acesso, proteção de dados e properties.
- **Aula 12 - Polimorfismo em Python:** Métodos com o mesmo nome e comportamentos diferentes.
- **Aula 13 - Ampliando o conhecimento em POO:** Aprofundamento em conceitos de Orientação a Objetos, variáveis de classe e de instância, métodos de classe e métodos estáticos.
- **Aula 14 - Atividade - Modelando o Sistema Bancário:** Projeto prático integrando os conceitos de POO em um sistema bancário interativo.

---

## Como rodar o Sistema Bancário (Aula 14)

O sistema bancário interativo, desenvolvido como atividade prática aplicando os conceitos de Orientação a Objetos, está localizado na pasta da Aula 14.

Para executá-lo, siga os passos abaixo em seu terminal:

1. Certifique-se de estar na raiz do projeto.
2. Navegue até a pasta da atividade:
   ```bash
   cd "Aula 14 - Atividade - Modelando o Sistema Bancário"
   ```
3. Execute o arquivo principal, que contém o menu interativo:
   ```bash
   python menu.py
   ```

### Funcionalidades do Sistema Bancário

Ao rodar o programa, você terá acesso a um menu no próprio terminal com as seguintes opções:

- **`[ nu ]` Novo Usuário (Cliente):** Cadastra um novo cliente no sistema informando CPF, Nome, Data de Nascimento e Endereço.
- **`[ nc ]` Nova Conta:** Cria e vincula uma nova conta corrente a um cliente existente (buscando pelo CPF).
- **`[ d ]` Depositar:** Adiciona um valor ao saldo de uma conta existente.
- **`[ s ]` Sacar:** Retira um valor do saldo.
- **`[ e ]` Extrato:** Exibe o histórico de todas as transações (saques e depósitos) e o saldo atual da conta.
- **`[ lu ]` Listar Usuários:** Mostra todos os clientes cadastrados.
- **`[ lc ]` Listar Contas:** Exibe todas as contas criadas com seus respectivos dados e saldos.
- **`[ q ]` Sair:** Encerra a execução da aplicação.

> **Aviso Importante:**
> Para realizar operações bancárias (como depósito, saque e extrato) ou abrir uma conta, é obrigatório primeiro cadastrar um novo usuário através da opção `[ nu ]`.
