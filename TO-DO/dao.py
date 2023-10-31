with open("tarefas.txt", "a") as arquivo:
    arquivo.write("ST   ID  TAREFA\n")

class Dao:
    def __init__(self):
        self.arquivo= "tarefas.txt"

class DaoAdicionarTarefa():

    def adicionar_tarefa(self, tarefa, idtarefa, status):
        with open("tarefas.txt", "a") as arquivo:
            arquivo.write(status)
            arquivo.write("\t")
            arquivo.write(idtarefa)
            arquivo.write("\t")
            arquivo.write(tarefa)
            arquivo.write("\n")
        return True
    
class DaoExcluirTarefa():
    def excluir(self, idexcluir):
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            linhas.pop(int(idexcluir) - 1)
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(linhas)
            return True
                    
class DaoListarTarefa():
    def listar(self):
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas

class DaoStatusTarefa():
    def concluir(self):
        with open("tarefas.txt", "") as arquivo:
            pass
    
    def inativar(self):
        with open("tarefas.txt", "") as arquivo:
            pass

class DaoAlterarTarefa():
    def AtualizarTarefas(self, tarefas_lista):
        with open("tarefas.txt", "w") as arquivo:
            arquivo.writelines(tarefas_lista)

dao = Dao()