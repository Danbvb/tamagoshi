class Tamagoshi:
    __nome = 'Sem nome'
    __fome = 100
    __higiene = 100
    __idade = 0

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def fome(self):
        return self.__fome 

    @property
    def idade(self):
        return self.__idade

    @property
    def higiene(self):
        return self.__higiene

    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            self.__idade = idade
    
    def comer(self):
        fome = self.__fome  + 10
        if fome > 0 and fome < 100:
            self.__fome = fome
    def banho(self):
        higiene = self.__higiene + 50
        if higiene > 0 and higiene < 100:
            self.__higiene = higiene    

name = input("Qual o nome do teu bichinho: ")
tamagoshi = Tamagoshi(name)
print("Olá, meu nome é " + tamagoshi.nome + ", eu sou o seu novo bichinho de estimação. ")

