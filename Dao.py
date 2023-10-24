class DaoAdicionarTarefa():
    def __init__(self, tarefa, idtarefa):
        self.idtarefa = idtarefa
        idtarefa = None
        with open("tarefas.txt", "a") as arquivo:
            arquivo.write(' - ')
            arquivo.write(tarefa)
            arquivo.write("\n")
            print("Tarefa adicionada ao DAO.")

class DaoExcluirTarefa():
    def __init__(self, excluir):
         with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            linhas.pop(int(excluir) - 1)
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(linhas)
                print("Tarefa removida do DAO.")

class DaoListarTarefa():
    def __init__(self):
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            cont = -1
            for tarefas in linhas:
                cont += 1
                print(f"{cont}. {tarefas}")