#oi # Daniel Cézar - Mesa 8

DIARIA = 130.0
hosts = []

def cadastroHost():
    nome = input("Nome: ")
    idade = input("Idade: ")
    doc = input("Documento: ")
    saldo = input("Quanto pode gastar: ")
    dias = input("Quantos dias pretende ficar: ")

    host = {
        "nome": nome,
        "idade": idade,
        "doc": doc,
        "saldo": saldo,
        "dias": dias
    }
    hosts.append(host)
    print('Hóspede cadastrado com sucesso!')


def listarHost():
    if not hosts:
        print("Nenhum hospéde cadastrado foi encontrado.")
        return

    for i, h in enumerate(hosts):
        print(f"{i}: {h['nome']} | Documento: {h['doc']}")


def verificarElegibilidade():
    listarHost()
    if not hosts:
        return

    indice = int(input("Selecione o índice do hóspede: "))
    hospede = hosts[indice]

    custo_total = hospede["dias"] * DIARIA
    elegivel = hospede["saldo"] >= custo_total

    print(f"\nHóspede: {hospede['nome']}")
    print(f"Custo total: R$ {custo_total:.2f}")
    print(f"Saldo disponível: R$ {hospede['saldo']:.2f}")

    if elegivel:
        print("Check-in autorizado!")
    else:
        print("Check-in negado!")

def deletarHost():
    listarHost()
    if not hosts:
        return

    indice = int(input('Selecione um hóspede para remover:'))
    removido = hosts.pop(indice)
    print(f'Hóspede {removido["nome"]} removido com sucesso!')

def menu():
    while True:
        print("===== MENU HOTEL =====")
        print("1. Cadastrar hóspede")
        print("2. Listar hóspedes")
        print("3. Verificar elegibilidade")
        print("4. Deletar hóspede")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastroHost()
        elif opcao == "2":
            listarHost()
        elif opcao == "3":
            verificarElegibilidade()
        elif opcao == "4":
            deletarHost()
        elif opcao == "5":
            print("Encerrando sistema...Até!")
            break
        else:
            print("Opção inválida!\n")


menu()