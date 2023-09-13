from abc import ABC, abstractclassmethod

class DispositivoElectronico(ABC):
    def __init__(self, marca:str) -> None:
        super().__init__()
        self.marca = marca

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        if not isinstance(marca, str):
            raise TypeError("Valor deber ser tipo str")
        self.__marca = marca

    def on(self):
        pass

    def off(self):
        pass

class Celular(DispositivoElectronico):
    pass