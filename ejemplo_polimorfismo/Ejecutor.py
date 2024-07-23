from Cuadrado import Cuadrado
from Rombo import Rombo
from Triangulo import Triangulo

def main():
    figuras = []

    cuadrado1 = Cuadrado()
    cuadrado1.establecer_caracteristicas("Cuadrado")
    cuadrado1.establecer_lado(12)
    cuadrado1.calcular_area()
    figuras.append(cuadrado1)

    cuadrado2 = Cuadrado()
    cuadrado2.establecer_caracteristicas("Cuadrado")
    cuadrado2.establecer_lado(7)
    cuadrado2.calcular_area()
    figuras.append(cuadrado2)

    cuadrado3 = Cuadrado()
    cuadrado3.establecer_caracteristicas("Cuadrado")
    cuadrado3.establecer_lado(25)
    cuadrado3.calcular_area()
    figuras.append(cuadrado3)

    cuadrado4 = Cuadrado()
    cuadrado4.establecer_caracteristicas("Cuadrado")
    cuadrado4.establecer_lado(37)
    cuadrado4.calcular_area()
    figuras.append(cuadrado4)

    rombo1 = Rombo()
    rombo1.establecer_caracteristicas("Rombo")
    rombo1.establecer_diagonal_mayor(23)
    rombo1.establecer_diagonal_menor(13)
    rombo1.calcular_area()
    figuras.append(rombo1)

    rombo2 = Rombo()
    rombo2.establecer_caracteristicas("Rombo")
    rombo2.establecer_diagonal_mayor(87)
    rombo2.establecer_diagonal_menor(56)
    rombo2.calcular_area()
    figuras.append(rombo2)

    rombo3 = Rombo()
    rombo3.establecer_caracteristicas("Rombo")
    rombo3.establecer_diagonal_mayor(48)
    rombo3.establecer_diagonal_menor(76)
    rombo3.calcular_area()
    figuras.append(rombo3)

    triangulo1 = Triangulo()
    triangulo1.establecer_caracteristicas("Triangulo")
    triangulo1.establecer_base(15)
    triangulo1.establecer_altura(20)
    triangulo1.calcular_area()
    figuras.append(triangulo1)

    triangulo2 = Triangulo()
    triangulo2.establecer_caracteristicas("Triangulo")
    triangulo2.establecer_base(6)
    triangulo2.establecer_altura(8)
    triangulo2.calcular_area()
    figuras.append(triangulo2)

    triangulo3 = Triangulo()
    triangulo3.establecer_caracteristicas("Triangulo")
    triangulo3.establecer_base(12)
    triangulo3.establecer_altura(6)
    triangulo3.calcular_area()
    figuras.append(triangulo3)

    triangulo4 = Triangulo()
    triangulo4.establecer_caracteristicas("Triangulo")
    triangulo4.establecer_base(18)
    triangulo4.establecer_altura(26)
    triangulo4.calcular_area()
    figuras.append(triangulo4)

    triangulo5 = Triangulo()
    triangulo5.establecer_caracteristicas("Triangulo")
    triangulo5.establecer_base(56)
    triangulo5.establecer_altura(48)
    triangulo5.calcular_area()
    figuras.append(triangulo5)

    # proceso para comprobar el polimorfismo
    for figura in figuras:
        figura.calcular_area()
        print(f"Datos de Figura\n{figura}")

if __name__ == "__main__":
    main()
