# O objetivo do Flyweight e economizar memoria.
# Em vez de cada arvore carregar sua propria textura e modelo 3D,
# a gente guarda esses dados pesados em uma classe so e compartilha.
class TipoFlyweight:
    def __init__(self, nome, imagem_textura, modelo_3d):
        self.nome = nome
        self.textura = imagem_textura
        self.modelo_3d = modelo_3d

    def mostrar_na_tela(self, x, y, extra):
        # Apenas simulando a renderizacao na tela
        print(f"Desenhando [{self.nome}] no X:{x} e Y:{y} | Textura: {self.textura} | {extra}")

# A Fabrica controla a criacao desses tipos pesados.
class FabricaFlyweight:
    # Dicionario para guardar os tipos que ja foram carregados na memoria
    tipos_guardados = {}

    @classmethod
    def pegar_tipo(cls, nome, textura, modelo):
        chave = (nome, textura, modelo)
        
        # Se esse tipo ainda nao existe, cria um novo e guarda no dicionario
        if chave not in cls.tipos_guardados:
            print(f"[Fabrica] Memoria alocada para novo tipo: '{nome}'")
            cls.tipos_guardados[chave] = TipoFlyweight(nome, textura, modelo)
        else:
            # A grande sacada do Flyweight: se ja existe, apenas reaproveita a mesma referencia!
            print(f"[Fabrica] Tipo '{nome}' ja existe na memoria. Reaproveitando referencia!")
        
        return cls.tipos_guardados[chave]