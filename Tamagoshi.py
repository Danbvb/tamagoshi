import os
import time
import platform
from tamagotchi.pet import Pet
from tamagotchi.attributes import Attributes

escolha = input("Escolha uma opção N para novo jogo ou S para sair do jogo: n")


if escolha == "N" or "n":
    tamagotchi_name = input('Coloque o nome do teu novo amigo: ')
    
    #instância de propriedade
    tamagotchi = Pet(tamagotchi_name)
    tamagotchi_attributes = Attributes(tamagotchi)

    # O tempo é formado por segundos * minutos * horas * dias
    TIME_EAT = 4*4*5
    TIME_SLEEP = 4*4*6
    TIME_RELOAD = 6*1
    TIME_AGE = 4*4*5

    #Contador de tempo percorido
    time_count_eat = 0
    time_count_age = 0 
    time_count_sleep = 0

    while tamagotchi.get_age() != 70:
        
        #Mostar status
        tamagotchi_attributes.status()

        #Tempo para atualizar informções
        time.sleep(TIME_RELOAD)

        # Mudar valores dos status do tamagotchi
        tamagotchi.set_hungry(tamagotchi.get_hungry() - 1)
        tamagotchi.set_power(tamagotchi.get_power() - 0.5)

        # Verificar tempo gasto sem comer para se alimentar
        if time_count_eat >= TIME_EAT:
            tamagotchi_attributes.eat()
            time_count_eat = -TIME_RELOAD

        # Verificar tempo acordado para poder dormir
        if time_count_sleep >= TIME_SLEEP:
            tamagotchi_attributes.sleep()
            time_count_sleep = -TIME_RELOAD

        # Verificar tempo percorido para envelhecer
        if time_count_age >= TIME_AGE:
            age = tamagotchi_attributes.older(10)
            time_count_age = -TIME_RELOAD    
        
        if tamagotchi.get_hungry() == 0:
            break

        if tamagotchi.get_power() == 0:
            break

        #adição de tempo percorido
        time_count_eat = time_count_eat + TIME_RELOAD
        time_count_sleep = time_count_sleep + TIME_RELOAD
        time_count_age = time_count_age + TIME_RELOAD 
    
    print('e morreu')
    
    if escolha == "S" or "s":
        exit()

class Attributes:
    def __init__(self, pet: Pet):
        self.pet = pet

    def eat(self):
        '''
        Esse componente  vai fazer com que seja 
        possivel modifcar o valor da fome. 
        '''

        print("Estou com fome")
        ask_user = input('alimentar?')

        if ask_user == 'sim':
            self.pet.set_hungry(100)

    def sleep(self):
        '''
        Esse componente  vai fazer com que seja 
        possivel recaregar o valor da energia.
        '''
        print("Estou com sono")
        ask_user = input("dormir? ")

        if ask_user == 'sim':
            while self.pet.get_power() != 100:
                self.pet.set_power(100)


    def older(self, age):
        '''
        Esse componente  vai fazer com que seja 
        somado a idade colocada com a idade atual. 
        '''
        return self.pet.set_age(self.pet.get_age() + age)

    def status(self):
        '''
        vai printar na tela as informações do
        tamagotchi.
        '''
        print(
            f'''
    Nome: {self.pet.get_name()}
    Fome: {self.pet.get_hungry()}
    Idade: {self.pet.get_age()}
    Energia: {self.pet.get_power()}
    ''')
class Pet:
    __name = ''
    __age = 0
    __power = 100
    __life = 100
    __hungry = 100

    def __init__(self, name):
        self.__name = name
    def get_power(self):
        return self.__power

    def get_name(self):
        '''
        Retornar o nome do Tamagotchi
        '''
        return self.__name

    def get_age(self):
        '''
        Retornar a idade do Tamagotchi
        '''
        return self.__age
    
    def get_life(self):
        '''
        Retornar o valor da vida do Tamagotchi
        '''
        return self.__life

    def get_hungry(self):
        '''
        Retornar o valor da fome do Tamagotchi
        '''
        return self.__hungry

    def set_life(self, life_value):
        '''
        Modificar o valor da vida do Tamagotchi
        '''
        self.__life = life_value
        return self.__life
        
    def set_hungry(self, hungry_value):
        '''
        Modificar o valor da fome do Tamagotchi
        '''
        self.__hungry = hungry_value
        return self.__hungry

    def set_power(self, power_value):
        '''
        Modificar o valor da energia do Tamagotchi
        '''
        self.__power = power_value
        return self.__power
    
    def set_age(self, age_value):
        '''
        Modificar a idade do Tamagotchi
        '''
        self.__age = age_value
        return self.__age
    