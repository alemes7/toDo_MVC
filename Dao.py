from Controller import *

class Dao():
    def __init__(self):
        self.arquivo = "tarefas.txt"

    def adicionarTarefa(self, tarefa):
        with open(self.arquivo, "a") as f:
            f.write(f"{tarefa}\n")
        return True

    def listarTarefa(self):
        with open(self.arquivo, "r") as f:
            tarefas = f.readlines()
            for tarefa in tarefas:
                print(tarefa.strip())

dao = Dao()