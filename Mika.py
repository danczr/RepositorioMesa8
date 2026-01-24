diaria = 130.0
hospedes = []

def cadastrar_hospede():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    documento = input('Documento: ')
    saldo = float(input('Saldo (R$): '))
    dias = int(input('Quantos dias pretende ficar: '))

    hospede = {
        'nome': nome,
        'idade': idade,
        'documento': documento,
        'saldo': saldo,
        'dias': dias,
        'hospede': False
    }
    hospedes.append(hospede)
    print('Hóspede cadastrado com sucesso!\n')

def verificar_cadastro(indice):
    if indice < 0 or indice >= len(hospedes):
        print('Hóspede não encontrado')
        return

    pessoa = hospedes[indice]

    if pessoa['idade'] < 18:
        print('Você é menor de idade!')
    elif pessoa['saldo'] < diaria * pessoa['dias']:
        print('Saldo insuficiente')
    elif not pessoa['documento']:
        print('Sem documento')
    else:
        pessoa['hospede'] = True
        print('Hospedagem realizada!')

def deletar_cadastro(indice):
    if indice < 0 or indice >= len(hospedes):
        print('Hóspede não encontrado')
        return

    del hospedes[indice]
    print('Cadastro removido com sucesso!')
