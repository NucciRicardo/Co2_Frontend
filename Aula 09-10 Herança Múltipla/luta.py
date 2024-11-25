from abc import ABC

class Lutador(ABC):
    nome : str
    energia : float

    def __init__(self, n: str):
        self.nome = n
        self.energia = 100

    def soco(self, oponente):
        oponente.energia -= 5

    def __str__(self):
        return f"Nome: {self.nome}\nEnergia: {self.energia}"

class Boxeador(Lutador):
    def cruzado(self, oponente : Lutador):
        oponente.energia -= 10

    def gancho(self, oponente : Lutador):
        oponente.energia -= 20

    def cadeira(self, oponente : Lutador):
        oponente.energia -= 50
