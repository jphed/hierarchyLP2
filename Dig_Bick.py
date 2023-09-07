class Figura():
    def __init__(self, color:str = "Verde") -> None:
        self.color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("Valor deber ser tipo str")
        self.__color = color

    def __str__(self) -> str:
        return f"color: {self.color}"
    

class Circulo(Figura):
    def __init__(self, color: str = "rojo", radio:float = 1.0) -> None:
        super().__init__(color)
        self.radio = radio

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        if not isinstance(radio, float):
            raise TypeError("Valor deber ser tipo float")
        self.__radio = radio

    def __str__(self) -> str:
        return f"{super().__str__()}, radio: {self.radio}"
    
class Rectangulo(Figura):
    def __init__(self, color: str = "Rojo", base:float = 1.0, altura:float = 1.0) -> None:
        super().__init__(color)
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        if not isinstance(base, float):
            raise TypeError("Valor deber ser tipo float")
        self.__base = base

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float):
            raise TypeError("Valor deber ser tipo float")
        self.__altura = altura

    def __str__(self) -> str:
        return f"{super().__str__()}, base:{self.base}, altura:{self.altura}"
    
#Atributos definidos
obj = Rectangulo(color="Verde", base=2.0, altura=3.0)
print(obj.__str__())

#Atributos no definidos        
obj2 = Rectangulo()
print(obj2.__str__())