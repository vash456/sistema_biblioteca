from libros import LibroFisico
from biblioteca import Biblioteca
from usuarios import Estudiante, Profesor, SolicitanteProtocol
from exceptions import BibliotecaError, UsuarioNoEncontradoError, LibroNoDisponibleError
from data import data_estudiantes, data_libros

def main():
    biblioteca = Biblioteca("Biblioteca virtual")
    profesor = Profesor("Felipe", "12345612")

    biblioteca.usuarios = [profesor] + data_estudiantes

    biblioteca.libros = data_libros

    print("Bienvenido a la Biblioteca")
    
    print("Libros Disponibles:")
    for libro in biblioteca.libros_disponibles():
        print(libro.descripcion_completa)
    print()
        
    cedula = input("Digite el numero cedula: ")
    try:
        usuario = biblioteca.buscar_usuario(cedula)
        print(usuario.nombre_completo)
    except UsuarioNoEncontradoError as e:
        print(e)
        
    titulo = input("Digite el titulo del libro: ")
    try:
        libro = biblioteca.buscar_libro(titulo)
        print(f"El libro que seleccionaste es: {libro}")
    except LibroNoDisponibleError as e:
        print(e)
    
    resultado = usuario.solicitar_libro(libro.titulo)
    print(f"\n{resultado}")
    
    try:
        resultado_prestar = libro.prestar()
        print(f"\n{resultado_prestar}")
    except LibroNoDisponibleError as e:
        print(e)
    
        



if __name__ == "__main__":
    main()
