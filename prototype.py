from flyweight import TipoFlyweight

# Superclasse base para qualquer coisa que for colocada no mapa
class Elemento:
    def __init__(self, x, y, tipo: TipoFlyweight):
        self.x = x
        self.y = y
        self.tipo = tipo # Atributo compartilhado (Flyweight)

    def clone(self):
        # O padrao Prototype exige um metodo para o objeto copiar a si mesmo
        pass

    def mostrar(self):
        pass

class Arvore(Elemento):
    def __init__(self, x, y, tipo, altura):
        super().__init__(x, y, tipo) # Repassa x, y e o tipo para a classe pai
        self.altura = altura

    def clone(self):
        # Cria uma nova arvore identica a atual.
        # As coordenadas e a altura sao copiadas, mas a referencia ao 'tipo' (pesado)
        # continua apontando para o mesmo lugar na memoria.
        nova_arvore = Arvore(self.x, self.y, self.tipo, self.altura)
        return nova_arvore

    def mostrar(self):
        self.tipo.mostrar_na_tela(self.x, self.y, f"Altura: {self.altura}m")

class Pedra(Elemento):
    def __init__(self, x, y, tipo, peso):
        super().__init__(x, y, tipo)
        self.peso = peso

    def clone(self):
        nova_pedra = Pedra(self.x, self.y, self.tipo, self.peso)
        return nova_pedra

    def mostrar(self):
        self.tipo.mostrar_na_tela(self.x, self.y, f"Peso: {self.peso}kg")