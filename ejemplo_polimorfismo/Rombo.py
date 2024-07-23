from Figura import Figura

class Rombo(Figura):

    def __init__(self):
        super().__init__()
        self.diagonal_menor = 0.0
        self.diagonal_mayor = 0.0

    def establecer_diagonal_menor(self, m):
        self.diagonal_menor = m

    def establecer_diagonal_mayor(self, m):
        self.diagonal_mayor = m

    def obtener_diagonal_menor(self):
        return self.diagonal_menor

    def obtener_diagonal_mayor(self):
        return self.diagonal_mayor

    def calcular_area(self):
        self.area = (self.diagonal_mayor * self.diagonal_menor) / 2

    def __str__(self):
        return (f"Caracteristicas: {self.caracteristicas}\nDiagonal Mayor: {self.diagonal_mayor:.1f}\n"
                f"Diagonal Menor: {self.diagonal_menor:.1f}\nArea: {self.area:.1f}\n")
