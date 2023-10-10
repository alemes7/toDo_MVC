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
                        print("Algum problema foi encontrado, tente novamente.")

                except Exception as erro:
                    print("Erro ao adicionar a tarefa: {erro}")

        except Exception as erro:
                print("Erro ao adicionar a tarefa: {erro}")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        try:
            self.excluir_convert = excluir
            excluir_convert = int(self.excluir)
            excluir_convert-=1
            
            TODO.RemoverTarefa(self.excluir) == True
            print("Tarefa removida.")
            
        except Exception as erro:
                print("Digite um número válido. Esta tarefa não existe.")
                

class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        cont = 0

        for tarefas in ControllerLista:
            cont += 1
            print(f"{cont}. {tarefas}")