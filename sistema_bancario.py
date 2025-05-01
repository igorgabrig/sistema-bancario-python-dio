# OBJETIVO GERAL:
## Criar um sistema bancário com as operações: SACAR, DEPOSITAR e VISUALIZAR EXTRATO.

# REQUISITOS:
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
## Usuários deve ser uma lista com: Nome, Data de nasc, cpf e endereço
## Endereço string com formato: Logradouro, nr, bariro, cidade, sigla estado
## deve ser armazenado somente os números do cpf, não podendo cadastrar usuários com o mesmo cpf


def menu():
    print(
        """
        ========== MENU ==========
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar Usuário
        [5] Criar Conta
        [6] Listar Contas
        [7] Listar Usuários
        [8] Sair
        =========================
        """
    )
    opcao = int(input("Escolha uma opção: "))
    return opcao


def depositar(saldo, extrato, /):

    valor_deposito = float(input("Informe o valor do depósito: R$ "))

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(("Depósito", valor_deposito))
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! O depósito deve ser maior que zero.")

    return saldo, extrato


def sacar(*, saldo, limite, numero_saques, extrato, LIMITE_SAQUES):

    valor_saque = float(input("Informe o valor do saque: R$ "))
    if numero_saques <= LIMITE_SAQUES and valor_saque <= limite:
        if valor_saque <= saldo:
            print("Saque Realizado com sucesso")
            extrato.append(("Saque", valor_saque))
            saldo -= valor_saque
            numero_saques += 1
        else:
            print("Saque não realizado, saldo insuficiente")
    else:
        print("Limite de saques diários atingido ou valor maior que R$ 500,00.")

    return saldo, extrato, numero_saques, LIMITE_SAQUES


def extrato_funcao(saldo, /, *, extrato):

    if extrato:
        print(
            """
        ========== EXTRATO ==========
        """
        )

        numeracao = len(extrato)
        for i, (tipo, valor) in enumerate(reversed(extrato), start=1):
            print(f"{numeracao} - {tipo}: R$ {valor:.2f}")
            numeracao -= 1
        print(f"Saldo Atual: R$ {saldo:.2f}")

    else:
        print("Não foram realizadas movimentações.")
        print(f"Saldo Atual: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    if cpf in usuarios:
        print("Usuário já cadastrado!")
        return usuarios

    nome = input("Informe o nome do usuário: ")

    data_nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
    rua = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe a sigla do estado: ")

    usuarios.update(
        {
            cpf: {
                "nome": nome,
                "data_nasc": data_nasc,
                "endereco": {
                    "rua": rua,
                    "numero": numero,
                    "bairro": bairro,
                    "cidade": cidade,
                    "estado": estado,
                },
            }
        }
    )

    print(f"Usuário {nome} cadastrado com sucesso!")

    return usuarios


def listar_usuarios(usuarios):

    for chave, valor in usuarios.items():
        print(f"CPF: {chave}")
        print(f"Nome: {valor['nome']}")
        print(f"Data de Nascimento: {valor['data_nasc']}")
        print(f"Endereço: {valor['endereco']}")
        print("------------------------------")


def criar_conta(contas, AGENCIA, usuarios):
    user = input("Informe o CPF do usuário: ")
    if user not in usuarios:
        print("Usuário não encontrado!")
        return contas
    else:
        num_conta = len(contas) + 1
        contas.update({num_conta: {"agencia": AGENCIA, "usuario": user}})
        print(f"Conta {num_conta} criada com sucesso!")
        return contas


def listar_contas(contas, usuarios):

    for num_conta, dados_conta in contas.items():
        print(f"Conta: {num_conta}")
        print(f"Agência: {dados_conta['agencia']}")
        print(
            f"Essa conta pertence a {usuarios[dados_conta['usuario']]['nome']}, cadastrado no CPF {dados_conta['usuario']}, mora na cidade {usuarios[dados_conta['usuario']]['endereco']['cidade']} - {usuarios[dados_conta['usuario']]['endereco']['estado']}."
        )
        #print(f"Usuário: {usuarios[dados_conta['usuario']]}")
        print("------------------------------")


def main():
    saldo = 0
    limite = 500
    extrato = []  # Inicia lista vazia para armazenar os depósitos e saques
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = {}
    contas = {}

    while True:

        opcao = menu()

        if opcao == 1:
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 2:
            saldo, extrato, numero_saques, LIMITE_SAQUES = sacar(
                saldo=saldo,
                limite=limite,
                numero_saques=numero_saques,
                extrato=extrato,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
        elif opcao == 3:
            extrato_funcao(saldo, extrato=extrato)

        elif opcao == 4:
            usuarios = criar_usuario(usuarios)

        elif opcao == 5:
            contas = criar_conta(contas, AGENCIA, usuarios)

        elif opcao == 6:
            listar_contas(contas, usuarios)

        elif opcao == 7:
            listar_usuarios(usuarios)

        elif opcao == 8:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


main()
