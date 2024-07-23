from Figura import Figura

class Triangulo(Figura):

    def __init__(self):
        super().__init__()
        self.base = 0.0
        self.altura = 0.0

    def establecer_base(self, b):
        self.base = b

    def establecer_altura(self, a):
        self.altura = a

    def obtener_base(self):
        return self.base

    def obtener_altura(self):
        return self.altura

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def __str__(self):
        return (f"Caracteristicas: {self.caracteristicas}\nBase: {self.base:.1f}\nAltura: {self.altura:.1f}\n"
                f"Area: {self.area:.1f}\n")
