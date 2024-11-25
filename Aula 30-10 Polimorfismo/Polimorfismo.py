from abc import ABC, abstractmethod, ABCMeta

class Jogador:
    def __init__(self):
        self.energia = 150
    
    def atirar(self, d, j):
        if isinstance(d, Disparavel):
            d.disparar(j)

    def bater(self, g, a, j):
        if isinstance(a, Arma):
            a.agredir(j)
        elif isinstance(g, Golpe):
            g.golpear(j)

    def __str__(self):
        return f"Jogador com {self.energia} de energia"

# Classes abstratas
class Disparavel(ABC):
    @abstractmethod
    def disparar(self, jogador):
        pass
    
    @abstractmethod
    def recarregar(self):
        pass

class Golpe(ABC):
    @abstractmethod
    def golpear(self, jogador):
        pass

# Classes concretas para Armas
class Arma(ABC):
    def __init__(self, destruicao):
        self.destruicao = destruicao
    
    def agredir(self, jogador):
        pass
    
    def __str__(self):
        return f"Arma com dano {self.destruicao}"

class Revolver(Arma, Disparavel):
    def __init__(self):
        super().__init__(destruicao = 20)
        self.cartuchos = 6

    def disparar(self, jogador):
        if self.cartuchos > 0:
            self.cartuchos -= 1
            jogador.energia -= self.destruicao
        else:
            print("arma sem municao")
    
    def recarregar(self):
        self.cartuchos = 6
    
class LancaChamas(Arma, Disparavel):
    def __init__(self):
        super().__init__(destruicao = 30)
        self.gas = 100
    
    def disparar(self, jogador):
        if self.gas >= 5:
            self.gas -= 5
            jogador.energia -= self.destruicao
        else:
            print("lanca chamas sem gas")
        
    def recarregar(self):
        self.gas = 100

class Faca(Arma):
    def __init__(self):
        super().__init__(destruicao = 15)
        self.lamina = 10
    
    def agredir(self, jogador):
        if self.lamina > 0:
            jogador.energia -= self.destruicao
            self.lamina -= 1
        else:
            print("a faca esta sem lamina")

# Classes concretas para Golpes
class Soco(Golpe):
    def golpear(self, jogador):
        jogador.energia -= 1 
    
    def __str__(self):
        return f"Soco que tira 1 de energia"

class Chute(Golpe):
    def golpear(self, jogador):
        jogador.energia -= 2
    
    def __str__(self):
        return f"Chute que tira 2 de energia"

class SocoIngles(Faca):
    def agredir(self, jogador):
        super().agredir(jogador)
        print ("soco ingles")

# Exemplo de uso
if __name__ == "__main__":
    # Criando jogadores
    jogador1 = Jogador()
    jogador2 = Jogador()

    # Criando armas
    revolver = Revolver()
    lanca_chamas = LancaChamas()
    faca = Faca()

    # Criando golpes
    soco = Soco()
    chute = Chute()
    soco_ingles = SocoIngles()

    # Exemplo de combate
    print(jogador1)
    print(jogador2)

    jogador1.bater(soco, None, jogador2)
    jogador1.bater(None, faca, jogador2)

    print(jogador1)
    print(jogador2)

    jogador1.atirar(revolver, jogador2)
    print(revolver)
    print(jogador2)