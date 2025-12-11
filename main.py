from libros import LibroFisico
from biblioteca import Biblioteca
from usuarios import Estudiante, Profesor, SolicitanteProtocol
from exceptions import BibliotecaError, UsuarioNoEncontradoError
from data import data_estudiantes, data_libros

def main():
    biblioteca = Biblioteca("Biblioteca virtual")
    profesor = Profesor("Felipe", "12345612")

    biblioteca.usuarios = [profesor] + data_estudiantes

    biblioteca.libros = data_libros

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
