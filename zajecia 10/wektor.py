import math


class Vector:
    @classmethod
    def create_from_Cartesian_coordinates(cls, name="No name", x=0, y=0, z=0):
        return cls(name, x, y, z)

    '''@classmethod
    def create_from_polar_coordinates(cls, name="No name", r=0, theta=0):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return cls(name, x, y) '''

    def __init__(self, name="No name", x=0, y=0):
        self._x = x
        self._y = y
        self._z = z
        self._name = name
        print(
            f"Wektor {self._name} o współrzędnych ({self._x}, {self._y}) został utworzony")

    def __del__(self):
        print(
            f"Wektor {self._name} o współrzędnych ({self._x}, {self._y}) został usunięty")

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y
    @property
    def z(self) -> float:
        return self._z
