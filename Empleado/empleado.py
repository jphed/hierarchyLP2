from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre:str) -> None:
        super().__init__()
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("Value must be str")
        self.__nombre = nombre

    def getSueldo(self):
        pass

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}"
    

class EmpleadoHoras(Empleado):
    def __init__(self, nombre: str, horas:int, horas_sueldo: float) -> None:
        super().__init__(nombre)
        self.horas = horas
        self.horas_sueldo = horas_sueldo

    @property
    def horas(self):
        return self.__horas
    
    @horas.setter
    def horas(self, horas):
        if not isinstance(horas, int):
            raise TypeError("Value must be int")
        self.__horas = horas

    @property
    def horas_sueldo(self):
        return self.__horas_sueldo
    
    @horas_sueldo.setter
    def horas_sueldo(self, horas_sueldo):
        if not isinstance(horas_sueldo, float):
            raise TypeError("Value must be float")
        self.__horas_sueldo = horas_sueldo

    def getSueldo(self):
        total = float(self.horas) * self.horas_sueldo
        return total
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nHoras: {self.horas}\nSueldo por hora: {self.horas_sueldo}"
    
class EmpleadoBase(Empleado):
    def __init__(self, nombre: str, sueldo:float) -> None:
        super().__init__(nombre)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self.__sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        if not isinstance(sueldo, float):
            raise TypeError("Value must be float")
        self.__sueldo = sueldo

    def getSueldo(self):
        return self.sueldo
    
    def  __str__(self) -> str:
        return f"{super().__str__()},\nSueldo: {self.sueldo}"
    

class EmpleadoComision(EmpleadoBase):
    def __init__(self, nombre: str, sueldo: float, comision_porc:int, ventas:float) -> None:
        super().__init__(nombre, sueldo)
        self.comision_porc = comision_porc
        self.ventas = ventas

    @property
    def comision_porc(self):
        return self.__comision_porc
    
    @comision_porc.setter
    def comision_porc(self, comision_porc):
        if not isinstance(comision_porc, int):
            raise TypeError("Value must be int")
        self.__comision_porc = comision_porc

    @property
    def ventas(self):
        return self.__ventas
    
    @ventas.setter
    def ventas(self, ventas):
        if not isinstance(ventas, float):
            raise TypeError("Value must be float")
        self.__ventas = ventas

    def getSueldo(self):
        return self.sueldo
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nComision porcentual: {self.comision_porc}\nVentas: {self.ventas}"
    
# -------------------------------------------------------------------------------------------------------------- #

obj = EmpleadoComision(nombre="Jorge", sueldo=10.0, comision_porc=5, ventas=5.0)
print(obj.__str__())