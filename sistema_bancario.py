#OBJETIVO GERAL:
## Criar um sistema bancário com as operações: SACAR, DEPOSITAR e VISUALIZAR EXTRATO.

#REQUISITOS:
## Deve ser possível depositar valores positivos para a minha conta bancária.
## Não é necessário identificar agência e conta bancária, pois a v1 é somente com um usuário.
## Todos os depositos devem ser armazenados em uma variável na operação de extrato.
## O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
## Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinehrio por falta de saldo.
## Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
## O extrato deve ser uma operação para listar todos os depósitos e saques realizados na conta.
## No fim da listagem deve ser exibido o saldo atual da conta
## Se o extrato estiver em branco, deve ser exibida a mensagem "Não foram realizadas movimentações."
## Os valores devem ser exibidos utilizando o formato R$ 0,00 com duas casas decimais.

saldo = 0
limite = 500
extrato = [] # Inicia lista vazia para armazenar os depósitos e saques
numero_saques = 0
LIMITE_SAQUES = 3


def menu():
    print('''
        ========== MENU ==========
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
        =========================
        ''')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def condicionais(opcao):
    if opcao == 1:
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        extrato_funcao()
    elif opcao == 4:
        print('Saindo...')
        return False
    else:
        print('Opção inválida! Tente novamente.')
    return True

def depositar():
    global saldo, extrato
    valor_deposito = float(input('Informe o valor do depósito: R$ '))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(('Depósito', valor_deposito))
        print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
    else:
        print('Valor inválido! O depósito deve ser maior que zero.')    

def sacar():
    global saldo, limite, numero_saques, extrato, LIMITE_SAQUES

    valor_saque = float(input('Informe o valor do saque: R$ '))
    if numero_saques <= LIMITE_SAQUES and valor_saque <= limite:
        if valor_saque <= saldo:
            print("Saque Realizado com sucesso")
            extrato.append(('Saque', valor_saque))
            saldo -= valor_saque
            numero_saques += 1
        else:
            print("Saque não realizado, saldo insuficiente")
    else:
        print("Limite de saques diários atingido ou valor maior que R$ 500,00.")

        
def extrato_funcao():
    global extrato, saldo

    if extrato:
        print('''
        ========== EXTRATO ==========
        ''')
        
        numeracao = len(extrato)
        for i, (tipo, valor) in enumerate(reversed(list(extrato)), start=1):
            print(f'{numeracao} - {tipo}: R$ {valor:.2f}')
            numeracao -= 1
        print(f'Saldo Atual: R$ {saldo:.2f}')

    else:
        print('Não foram realizadas movimentações.')
        print(f'Saldo Atual: R$ {saldo:.2f}')



# Programa Principal
# Inicia o loop do programa
while True:
   
   printar = menu()
   opcao = condicionais(printar)
   
   if not opcao:
    break

