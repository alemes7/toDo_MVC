from Model import *
from Dao import *

class ControllerAdicionarTarefa():
    
    def __init__(self, tarefa):
        self.tarefa = tarefa
        try:
            if dao.adicionarTarefa(self.tarefa) == True:
                  print("Tarefa Adicionada!")
            else:
                 print("Tarefa não foi adicionada.")

        except Exception:
            print("Digite uma tarefa válida.")

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
        try:
            tarefas = dao.listarTarefa()
            if tarefas:
                cont = 1
                for tarefa in tarefas:
                    print(f"{cont} -- {tarefa}")
                    cont += 1

        except Exception as erro:
            print(f"Erro: {erro}")
