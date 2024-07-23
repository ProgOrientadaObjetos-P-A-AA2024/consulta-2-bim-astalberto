from Figura import Figura

class Cuadrado(Figura):

    def __init__(self):
        super().__init__()
        self.lado = 0.0

    def establecer_lado(self, l):
        self.lado = l

    def obtener_lado(self):
        return self.lado

    def calcular_area(self):
        self.area = self.lado * self.lado

    def __str__(self):
        return f"Caracteristicas: {self.caracteristicas}\nLado: {self.lado:.1f}\nArea: {self.area:.1f}\n"
