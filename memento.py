from prototype import Elemento

# Memento: Funciona como um "Save State". Guarda uma foto exata do mapa.
class MapaMemento:
    def __init__(self, lista_do_mapa):
        # Detalhe importante: precisamos usar o .clone() em cada item.
        # Se salvarmos a lista original direto, quando o mapa for alterado no futuro,
        # o historico tambem seria alterado (problema de referencia em Python).
        self.estado_salvo = []
        for item in lista_do_mapa:
            self.estado_salvo.append(item.clone())

# Originator: E o mapa propriamente dito, o objeto que sofre as edicoes.
class Mapa:
    def __init__(self):
        self.meus_elementos = [] # Lista de elementos ativos no mapa

    def botar_no_mapa(self, coisa):
        self.meus_elementos.append(coisa)

    def tirar_do_mapa(self, coisa):
        if coisa in self.meus_elementos:
            self.meus_elementos.remove(coisa)

    def salvar_agora(self):
        # Tira uma "foto" do estado atual e retorna o Memento
        return MapaMemento(self.meus_elementos)

    def voltar_no_tempo(self, memento_antigo):
        # Restaura o mapa usando o save state.
        # Clonamos de novo para garantir que podemos continuar editando sem corromper o save.
        self.meus_elementos = []
        for item in memento_antigo.estado_salvo:
            self.meus_elementos.append(item.clone())
    # Exibe a visao atual do mapa na tela (simulacao)
    def mostrar_tudo(self):
        print("\nVISAO ATUAL DO MAPA")
        if len(self.meus_elementos) == 0:
            print("  O mapa esta vazio.")
        else:
            for coisa in self.meus_elementos:
                coisa.mostrar()
        print("\n")

# Caretaker: O gerenciador da linha do tempo. Controla as listas de saves.
class Caretaker:
    def __init__(self, mapa_jogo):
        self.mapa = mapa_jogo
        self.lista_de_saves = []
        self.posicao_atual = -1
        
        # Cria um save inicial (mapa vazio) logo na largada
        self.salvar_passo()

    def salvar_passo(self):
        # Se o usuario voltou no tempo (Undo) e fez uma acao nova,
        # o historico "para frente" e descartado e reescrito.
        if self.posicao_atual < len(self.lista_de_saves) - 1:
            self.lista_de_saves = self.lista_de_saves[:self.posicao_atual + 1]
        
        novo_save = self.mapa.salvar_agora()
        self.lista_de_saves.append(novo_save)
        self.posicao_atual += 1

    def fazer_acao(self, funcao_fazer_algo):
        # Executa a acao pedida e automaticamente salva o novo estado
        funcao_fazer_algo()
        self.salvar_passo()

    def desfazer(self):
        if self.posicao_atual > 0:
            print("[ACAO] Desfazendo (Undo)...")
            self.posicao_atual -= 1
            save_velho = self.lista_de_saves[self.posicao_atual]
            self.mapa.voltar_no_tempo(save_velho)
        else:
            print("Ja estamos no comeco, nao ha mais o que desfazer.")

    def refazer(self):
        if self.posicao_atual < len(self.lista_de_saves) - 1:
            print("[ACAO] Refazendo (Redo)...")
            self.posicao_atual += 1
            save_da_frente = self.lista_de_saves[self.posicao_atual]
            self.mapa.voltar_no_tempo(save_da_frente)
        else:
            print("Nao ha acoes para refazer.")