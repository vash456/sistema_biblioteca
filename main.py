from libros import LibroFisico
from biblioteca import Biblioteca
from usuarios import Estudiante, Profesor, SolicitanteProtocol
from exceptions import BibliotecaError, UsuarioNoEncontradoError


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

    biblioteca.usuarios = [estudiante, estudiante_1, profesor]

    biblioteca.libros = [mi_libro, book2, book3]

    print("Bienvenido a la Biblioteca")
    
    print("Libros Disponibles:")
    for titulo in biblioteca.libros_disponibles():
        print(f"  - {titulo}")
    print()
        
    cedula = input("Digite el numero cedula: ")
    try:
        usuario = biblioteca.buscar_usuario(cedula)
        print(usuario.cedula, usuario.nombre)
    except UsuarioNoEncontradoError as e:
        print("El usuario que estas buscando no existe: {e}")
        
    
    
    
        



if __name__ == "__main__":
    main()
