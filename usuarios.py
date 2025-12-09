from typing import Protocol

class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo}' realizada."


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Prestamos del libro: {titulo} autorizado."
        else:
            return (
                f"No puedes prestar mas libros, limite alcanzado {self.limite_libros}"
            )


class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro: {titulo} autorizado."


estudiante = Estudiante("luis", "55454", "sistemas")
estudiante_1 = Estudiante("jose", "35658", "salud")
profesor = Profesor("oscar", "32164")

from libros import Libro

libro = Libro("libro x", "Fulano", "3425", True)

usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_1, profesor]

for usuario in usuarios:
    print(usuario.solicitar_libro("titulo de ejemplo"))