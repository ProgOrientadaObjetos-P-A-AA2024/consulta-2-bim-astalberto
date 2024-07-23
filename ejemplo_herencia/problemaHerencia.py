class Estudiante:
    def __init__(self, nombres, apellidos, identificacion, edad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.identificacion = identificacion
        self.edad = edad

    def establecer_nombres_estudiante(self, nombres):
        self.nombres = nombres

    def establecer_apellidos_estudiante(self, apellidos):
        self.apellidos = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self.identificacion = identificacion

    def establecer_edad_estudiante(self, edad):
        self.edad = edad

    def obtener_nombres_estudiante(self):
        return self.nombres

    def obtener_apellidos_estudiante(self):
        return self.apellidos

    def obtener_identificacion_estudiante(self):
        return self.identificacion

    def obtener_edad_estudiante(self):
        return self.edad


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_asignaturas = 0
        self.costo_asignatura = 0.0
        self.matricula_distancia = 0.0

    def establecer_numero_asignaturas(self, numero):
        self.numero_asignaturas = numero

    def establecer_costo_asignatura(self, costo):
        self.costo_asignatura = costo

    def calcular_matricula_distancia(self):
        self.matricula_distancia = self.numero_asignaturas * self.costo_asignatura

    def obtener_numero_asignaturas(self):
        return self.numero_asignaturas

    def obtener_costo_asignatura(self):
        return self.costo_asignatura

    def obtener_matricula_distancia(self):
        return self.matricula_distancia


class EstudiantePresencial(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_creditos = 0
        self.costo_credito = 0.0
        self.matricula_presencial = 0.0

    def establecer_numero_creditos(self, numero):
        self.numero_creditos = numero

    def establecer_costo_credito(self, costo):
        self.costo_credito = costo

    def calcular_matricula_presencial(self):
        self.matricula_presencial = self.numero_creditos * self.costo_credito

    def obtener_numero_creditos(self):
        return self.numero_creditos

    def obtener_costo_credito(self):
        return self.costo_credito

    def obtener_matricula_presencial(self):
        return self.matricula_presencial


def main():
    continuar = "S"

    while continuar == "S":
        print("Tipo de Estudiante a ingresar.\n1) Estudiante Presencial.\n2) Estudiante Distancia")
        tipo_estudiante = int(input("Ingrese el tipo de estudiante: "))

        if tipo_estudiante in [1, 2]:
            nombres_est = input("Ingrese el nombre del estudiante: ")
            apellidos_est = input("Ingrese el apellido del estudiante: ")
            identificacion_est = input("Ingrese la identificación del estudiante: ")
            edad_est = int(input("Ingrese la edad del estudiante: "))

            if tipo_estudiante == 1:
                numero_creds = int(input("Ingrese el número de créditos del estudiante: "))
                costo_cred = float(input("Ingrese el costo de cada crédito del estudiante: "))
                estudiante_p = EstudiantePresencial(nombres_est, apellidos_est, identificacion_est, edad_est)
                estudiante_p.establecer_numero_creditos(numero_creds)
                estudiante_p.establecer_costo_credito(costo_cred)
                estudiante_p.calcular_matricula_presencial()

                print("Datos del estudiante Presencial")
                print(f"Nombre: {estudiante_p.obtener_nombres_estudiante()}")
                print(f"Apellido: {estudiante_p.obtener_apellidos_estudiante()}")
                print(f"Identificación: {estudiante_p.obtener_identificacion_estudiante()}")
                print(f"Edad: {estudiante_p.obtener_edad_estudiante()}")
                print(f"Matricula final $: {estudiante_p.obtener_matricula_presencial():.2f}")

            else:
                numero_asigs = int(input("Ingrese el número de asignaturas del estudiante: "))
                costo_asig = float(input("Ingrese el costo de cada asignatura del estudiante: "))
                estudiante_d = EstudianteDistancia(nombres_est, apellidos_est, identificacion_est, edad_est)
                estudiante_d.establecer_numero_asignaturas(numero_asigs)
                estudiante_d.establecer_costo_asignatura(costo_asig)
                estudiante_d.calcular_matricula_distancia()

                print("Datos del estudiante a Distancia")
                print(f"Nombre: {estudiante_d.obtener_nombres_estudiante()}")
                print(f"Apellido: {estudiante_d.obtener_apellidos_estudiante()}")
                print(f"Identificación: {estudiante_d.obtener_identificacion_estudiante()}")
                print(f"Edad: {estudiante_d.obtener_edad_estudiante()}")
                print(f"Matricula: {estudiante_d.obtener_matricula_distancia():.2f}")

        else:
            print("Error en la opción")

        continuar = input("Desea ingresar más estudiantes. Digite la letra S para continuar o digite la letra N para salir: ").upper()


if __name__ == "__main__":
    main()