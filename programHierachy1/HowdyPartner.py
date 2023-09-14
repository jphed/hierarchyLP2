from abc import ABC, abstractclassmethod

#Abstract class 
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

    @abstractclassmethod
    def on(self):
        pass

    @abstractclassmethod
    def off(self):
        pass
    
    def __str__(self) -> str:
        return f"Marca: {self.marca}"

# --------------------------------------------------------------------------------------------------------------------- #

class Celular(DispositivoElectronico):
    def __init__(self, marca: str, precio: float) -> None:
        super().__init__(marca)
        self.precio = precio

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        if not isinstance(precio, float):
            raise TypeError("Valor deber ser tipo float")
        if precio < 0:
            raise ValueError("Precio no puede ser menor a 0")
        self.__precio = precio

    def on(self):
        return f"Prendiendo..."

    def off(self):
        return "apagando..."

    def llamar(self):
        return "Llamando..."

    def __str__(self) -> str:
        return f"{super().__str__()}\nPrecio: {self.precio}"
    

class Television(DispositivoElectronico):
    def __init__(self, marca: str, canales: int) -> None:
        super().__init__(marca)
        self.canales = canales

    @property
    def canales(self):
        return self.__canales
    
    @canales.setter
    def canales(self, canales):
        if not isinstance(canales, int):
            raise TypeError("Valor deber ser tipo int")
        if canales < 0:
            raise ValueError("Los canales no pueden ser menor a 0")
        self.__canales = canales

    def on(self):
        return f"Prendiendo..."

    def off(self):
        return "apagando..."

    def verNetflix(self):
        print("Viendo netflix")

    def __str__(self) -> str:
        return f"{super().__str__()}\Canales: {self.canales}"
    

# -----------------------------------------------------------------------------------------------------------------------#

sus = Celular(marca="Iphone", precio=float(20000))
print(sus.llamar())