import tarefas  # importa o módula tarefas criado previamente (tarefas.py)

def menu():
    while True:
        print("\n*** GERENCIADOR DE TAREFAS ***")
        print("1- Listar tarefas")
        print("2- Adicionar tarefa")
        print("3- Concluir tarefa")
        print("4- Remover tarefa")
        print("5- SAIR")


        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefas.listar_tarefas()
        elif opcao == '2':
            titulo = input("Digite a nova tarefa: ")
            tarefas.adicionar_tarefa(titulo)
        elif opcao == '3':
            try:
                indice = int(input("Digite o numero da tarefa a concluir: ")) - 1
                tarefas.concluir_tarefa(indice)
            except ValueError:
                print("Você deve digitar um número válido")
        elif opcao == '4':
            try:
                indice = int(input("Digite o numero da tarefa a remover: ")) - 1
                tarefas.remover_tarefa(indice)
            except ValueError:
                print("Você deve digitar um numero valido")
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção invalida. Tente novamente.")

menu ()            