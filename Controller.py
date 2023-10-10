from Model import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):

        try:
            if tarefa == "":
                print("Digite uma tarefa válida.")

            else:

                try:
                    self.tarefa = tarefa
                    if TODO.AdicionarTarefa(self.tarefa) == True:
                        print("Tarefa adicionada.")
                    else:
                        print("Algum problema foi encontrado.")

                except Exception as erro:
                    print("Erro ao adicionar a tarefa: {erro}")

        except Exception as erro:
                print("Erro ao adicionar a tarefa: {erro}")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir - 1

        try:
            if TODO.RemoverTarefa(self.excluir) == True:
                print("Tarefa removida.")
   
            else:
                print("Algum problema foi encontrado.")                

        except Exception as erro:
                print("Erro ao excluir a tarefa: {erro}")


class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        cont = 0

        for tarefas in ControllerLista:
            cont += 1
            print(f"{cont}. {tarefas}")