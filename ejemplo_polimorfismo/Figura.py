from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self):
        self.caracteristicas = ""
        self.area = 0.0

    def establecer_caracteristicas(self, c):
        self.caracteristicas = c

    @abstractmethod
    def calcular_area(self):
        pass

    def obtener_caracteristicas(self):
        return self.caracteristicas

    def obtener_area(self):
        return self.area


 