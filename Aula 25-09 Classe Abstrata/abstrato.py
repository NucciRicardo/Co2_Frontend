from abc import ABC, abstractmethod

class Funcionario(ABC):
    nome : str
    cpf : str
    __senha : int

    def __init__(self, nome : str, cpf : str, senha : int):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    @abstractmethod
    def autenticar(user : str, senha : int):
        pass

    def __str__(self):
        return f'Nome: {self.nome} | CPF: {self.cpf} | Senha: {self.get_senha()}'

class Gerente(Funcionario):
    def autenticar(self, user : str, senha : int):
        if user == self.cpf and senha == self.get_senha():
            return True
        else:
            return False
    
    def cancelar_operação(self):
        return f'Operação cancelada.'

class Operador_Caixa(Funcionario):
    numero_caixa : int

    def __init__(self, nome, cpf, senha, numero : int):
        super().__init__(nome, cpf, senha)
        self.numero_caixa = numero

    def autenticar(self, user, senha):
        if user == self.numero_caixa and senha == self.get_senha():
            return True
        else:
            return False
    
    def registrar_produto(self):
        return f'Produto registrado.'

    def __str__(self):
        return f'Nome: {self.nome} | CPF: {self.cpf} | Senha: {self.get_senha()} | Numero: {self.numero_caixa}'

class Seguranca(Funcionario):
    posto : int

    def __init__(self, nome, cpf, senha, posto: int):
        super().__init__(nome, cpf, senha)
        self.posto = posto
    
    def autenticar(self, user, senha):
        if user == self.posto and senha == self.get_senha():
            return True
        else:
            return False
        
    def acionar_alarme(self):
        return f'Uooooooooouuuuooooouuuoouuuu!'
