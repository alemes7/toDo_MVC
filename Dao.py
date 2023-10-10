from Controller import *

class Dao():
    def __init__(self):
        self.arquivo = "tarefas.txt"
        self.tarefas = []

    def adicionarTarefa(self, tarefa):
        with open(self.arquivo, "a") as f:
            f.write(tarefa + "\n")
        return True

    def listarTarefa(self):
        with open(self.arquivo, "r") as f:
            linhas = f.readlines()
        return linhas

    def excluirTarefa(self, tarefa):
        with open(self.arquivo, "r") as f:
            linhas = f.readlines()
        with open(self.arquivo, "w") as f:
            for linha in linhas:
                if linha.strip() != tarefa:
                    f.write(linha)
        return True