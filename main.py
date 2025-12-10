from libros import LibroFisico
from biblioteca import Biblioteca
from usuarios import Estudiante, Profesor, SolicitanteProtocol
from exceptions import BibliotecaError


def main():
    biblioteca = Biblioteca("Biblioteca virtual")
    mi_libro = LibroFisico(
        "100 años de soledad", "Gabrial Garcias Marquez", "prueba", True
    )
    book2 = LibroFisico("libro2", "autor2", "prueba", True)
    book3 = LibroFisico("libro3", "autor3", "prueba", False)
    estudiante = Estudiante("luis", "55454", "sistemas")
    estudiante_1 = Estudiante("jose", "35658", "salud")
    profesor = Profesor("oscar", "32164")

    usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_1, profesor]

    biblioteca.libros = [mi_libro, book2, book3]

    print(biblioteca.libros)
    
    try:
        print(estudiante.solicitar_libro(None))
    except BibliotecaError as e:
        print(f"{e}, {type(e)}")
        print("Error: No se pudo solicitar el libro")
        



if __name__ == "__main__":
    main()
