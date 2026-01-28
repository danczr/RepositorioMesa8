class Cliente:
    def __init__(self, nome: str, idade: int, documento: str, saldo: float, diasEstadia: int):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.saldo = saldo
        self.diasEstadia = diasEstadia
        self.hospedado = False

    def custo_total(self, preco_diaria):
        return self.diasEstadia * self.preco_diaria

    def __str__(self):
        status = 'Hospedado' if self.hospedado else 'Não Hospedado'
        return f'{self.documento} - {self.nome} - {status}'

    class GerenciadorHotel:
        def __init__(self):
            self.listaClientes = [Cliente('Jhonatas', 23, '1112222', 2000, 10)
            ]
            self.precoDiaria = 130

        def buscarCliente(self, identificacao):
            identificacao = str(identificacao).strip().lower()
            resposta = [cliente for cliente in self.listaClientes if cliente.documento == identificacao]
            return resposta[0] if resposta else None

        @staticmethod
        def validarCpfCliente(self, documento):
            return len(documento) == 11 and documento.isdigit()

        def criarCliente(self):
            print(f'Cadastrando novo cliente...')
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            documento = input('Documento (CPF): ')

            if self.buscarCliente(documento):
                print('Já existe um cliente com esse documento!')
                return

            if not self.validarCpfCliente(documento):
                print('CPF Inválido!')
                return

            dias = int(input('Quantos dias você deseja ficar? '))
            saldo = float(input('Quanto pretende gastar? '))
            novoCliente = Cliente(nome, idade, documento, saldo, dias)
            self.listaClientes.append(novoCliente)
            print('Cliente criado com sucesso!')


        def listarCliente(self):
            if not self.listaCliente:
                print('LISTA VAZIA!')
            else:
                for cliente in self.listaClientes:
                    print(cliente)

        def removerCliente(self, documento):
            cliente = self.buscarCliente(documento)
            if cliente:
                self.listaClientes.remove(cliente)
                print(f'Cliente removido com sucesso: {cliente}')
            else:
                print('Cliente não encontrado!')

        def atualizarCliente(self, documento):
            cliente = self.buscarCliente(documento)
            if not cliente:
                print('Cliente não encontrado!')
            else:
                if cliente.idade < 18:
                    print('Menor de idade não pode fazer Check-In!')
                    return
                custo = cliente.custo_total(self.precoDiaria)
                if custo > cliente.saldo:
                    print('Saldo Insuficiente para realizar Check-In!')
                    return
                cliente.hospedado = not cliente.hospedado
                acao = 'CHECK-IN' if cliente.hospedado else 'CHECK-OUT'
                print(f'{acao} realizado com sucesso!')

    hotel = GerenciadorHotel()

    while True:
        print(f'\n{'='*20}\nSISTEMA GERENCIADOR HOTEL\n{'='*20}\n')
        try:
            escolha = int(input('1 - Criar\n2 - Buscar\n3 - Listar\n4 - Check-In/Check-Out\n5 - Deletar\n6 - Sair\n'))
            match escolha:
                case 1: hotel.criarCliente()
                case 2: hotel.buscarCliente(input('Digite o documento do cliente: '))
                case 3: hotel.listarCliente()
                case 4: hotel.atualizarCliente(input('Digite seu documento: '))
                case 5: hotel.removerCliente(input('Digite o documento do cliente: '))
                case 6: break
                case _: 'Opção Inválida!'
        except ValueError:
            print('Erro, digite apenas números inteiros!')









