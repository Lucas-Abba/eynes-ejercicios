from math import pi


class Circle:
    def __init__(self, radius):
            self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('El radio no puede ser negativo')
        self._radius = value

    def getArea(self):
        return (pi * self.radius * self.radius)
    
    def getPerimeter(self):
        return (2 * pi * self.radius)

    def multiplyCircle(self, n):
        if n < 0:
            print('Operacion denegada')
            return
        else:
            return (Circle(self.radius * n))
    
    def __str__(self):
        return("{Tipo: Circulo, Radio: %d}" % self.radius)


