from flyweight import FabricaFlyweight
from prototype import Arvore, Pedra
from memento import Mapa, Caretaker

# Arquivo principal para rodar e simular o funcionamento do sistema
if __name__ == "__main__":
    print("INICIANDO EDITOR DE MAPAS")
    
    # Configuracao do Originator e Caretaker
    mapa = Mapa()
    editor = Caretaker(mapa)
    
    # 1. Testando o Flyweight (reaproveitamento de memoria)
    print("\n[Carregando texturas e modelos base]")
    tipo_arvore = FabricaFlyweight.pegar_tipo("Pinheiro", "pinheiro.png", "arvore_3d.obj")
    
    # A segunda chamada para "Pinheiro" deve reaproveitar a instancia existente
    tipo_arvore_repetida = FabricaFlyweight.pegar_tipo("Pinheiro", "pinheiro.png", "arvore_3d.obj")
    tipo_pedra = FabricaFlyweight.pegar_tipo("Pedra Grande", "pedra.png", "pedra_3d.obj")

    # 2. Instanciando os objetos reais (que suportam Prototype)
    arvore_um = Arvore(x=10, y=20, tipo=tipo_arvore, altura=5.0)
    arvore_dois = Arvore(x=30, y=40, tipo=tipo_arvore_repetida, altura=3.5)
    pedra_um = Pedra(x=100, y=200, tipo=tipo_pedra, peso=500)

    # 3. Simulando a edicao do mapa
    print("\n[Adicionando elementos no mapa]")
    editor.fazer_acao(lambda: mapa.botar_no_mapa(arvore_um))
    editor.fazer_acao(lambda: mapa.botar_no_mapa(pedra_um))
    mapa.mostrar_tudo()

    print("[Editando: Inserindo arvore 2 e removendo árvore 1]")
    editor.fazer_acao(lambda: mapa.botar_no_mapa(arvore_dois))
    editor.fazer_acao(lambda: mapa.tirar_do_mapa(arvore_um))
    mapa.mostrar_tudo()

    # 4. Testando a linha do tempo (Undo/Redo via Memento)
    print("\n[Testando recurso de Desfazer (Undo)]")
    
    editor.desfazer() # Deve desfazer a remocao da arvore 1
    mapa.mostrar_tudo()

    editor.desfazer() # Deve desfazer a insercao da arvore 2
    mapa.mostrar_tudo()

    print("\n[Testando recurso de Refazer (Redo)]")
    
    editor.refazer() # Deve recolocar a arvore 2
    mapa.mostrar_tudo()