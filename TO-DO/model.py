from dao import *

class ToDo():
    def __init__(self, tarefa=str):
        self.tarefa = tarefa

    def AdicionarTarefa(self, tarefa, idtarefa, status):
        daoAdicionar = DaoAdicionarTarefa()
        return daoAdicionar.adicionar_tarefa(tarefa, idtarefa, status)
        
    def ListarTarefas(self):
        daoListar = DaoListarTarefa()
        return daoListar.listar()
    
    def RemoverTarefa(self, idexcluir):
        daoExcluir = DaoExcluirTarefa()
        return daoExcluir.excluir(idexcluir)
    
    def AtualizarTarefas(self, tarefas_lista):
        daoAtualizar = DaoAlterarTarefa()
        return daoAtualizar.AtualizarTarefas(tarefas_lista)
    
    def StatusTarefaC(self, status):
        daoStatusC = DaoStatusTarefa()
        return daoStatusC.concluir(status)
    
    def StatusTarefaI(self, status):
        daoStatusI = DaoStatusTarefa()
        return daoStatusI.inativar(status)
    
TODO = ToDo()