class Point2D():
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("Value must be int")
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("Value must be int")
        self.__y = y

    def __str__(self) -> str:
        return f"x value: {self.x}\ny value: {self.y}"

class Point3D(Point2D):
    def __init__(self, x: int, y: int, z:int) -> None:
        super().__init__(x, y)
        self.__z = z

    @property
    def z(self):
        return self.__z
    
    @z.setter
    def x(self, z):
        if not isinstance(z, int):
            raise TypeError("Value must be int")
        self.__z = z

    def __str__(self) -> str:
        return f"{super().__str__()}\nz value: {self.z}"

# -------------------------------------------------------------------------------------------------------------------- #

c = Point3D(x=1,y=2,z=3)
print(c.__str__())