
class Tarefa:
    def __init__(self, categoria, descricao, urgencia, diasrestantes):
        self.categoria = categoria
        self.descricao = descricao
        self.urgencia = urgencia
        self.diasrestantes = diasrestantes
        self.status = 'Pendente'

    def __str__(self):
        return f'{self.descricao} - {self.categoria} - {self.status} - {self.diasrestantes}'


class Gerenciador:

    def __init__(self):
        self.listaTarefas = [
            Tarefa('casa', 'varrer', 'alta', 1)
        ]


    def criarTarefa(self):
        print(f'{'-'*10}Criando Tarefa{'-'*10}')
        categoria = input('Categoria: ')
        descricao = input('Descricao: ')
        try:
            urgencia = input('Urgência: ')
            diasrestantes = int(input('Dias Restantes: '))

            novaTarefa = Tarefa(categoria, descricao, urgencia, diasrestantes)
            self.listaTarefas.append(novaTarefa)
            print('Tarefa criada com sucesso!')
        except ValueError:
            print('Erro do tipo de dado de cadastro')


    def listarTarefas(self):
        if not self.listaTarefas:
            print('Lista Vazia')

        else:
            for i, tarefa in enumerate(self.listaTarefas, 1):
                print(f'Tarefa {i}: {tarefa}')


    def atualizarTarefa(self):
        self.listarTarefas()
        if self.listaTarefas:
            try:
                indice = int(input('Indice da tarefa: '))
                indice -= 1
                novostatus = input('Novo Status: ')
                if 0 <= indice < len(self.listaTarefas):
                    self.listaTarefas[indice].status = novostatus
                else:
                    print('Indice Inválido!')
            except ValueError:
                print('Digite um valor inteiro!')

    def deletarTarefa(self):
        self.listarTarefas()
        if self.listaTarefas:
            try:
                indice = int(input('Indice da tarefa: '))
                indice -= 1
                if 0 <= indice < len(self.listaTarefas):
                    removido = self.listaTarefas.pop(indice)
                    print(f'Tarefas removida: {removido.descricao}')
                else:
                    print('Indice inválido')
            except ValueError:
                print('Digite um número inteiro!')


sistema = Gerenciador()
while True:
    print(f'\n{'='*20}\nSISTEMA GERENCIADOR DE TAREFAS\n{'='*20}\n')
    print('1 - Criar Tarefa\n2 - Listar Tarefas\n 3 - Atualizar Tarefa\n4 - Deletar Tarefa\n5 - Sair')
    opcao = input('\nEscolha uma opção: ')
    match opcao:
        case '1':
            sistema.criarTarefa()
        case '2':
            sistema.listarTarefas()
        case '3':
            sistema.atualizarTarefa()
        case '4':
            sistema.deletarTarefa()
        case '5':
            print('SAINDO DO SISTEMA...')
            break
        case _:
            print('Opção Inválida!')





