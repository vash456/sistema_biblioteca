from libros import LibroFisico, Biblioteca

def main():
    mi_libro = LibroFisico("100 años de soledad", "Grabrial Garcias Marquez", "prueba", True)
    book2 = LibroFisico("libro2", "autor2", "prueba", True)
    book3 = LibroFisico("libro3", "autor3", "prueba", False)

    biblioteca = Biblioteca("Biblioteca virtual")
    biblioteca.libros = [
        mi_libro, book2, book3
    ]

    print(mi_libro.prestar())
    print(mi_libro.get_get_veces_prestado())
    print(mi_libro.prestar())
    print(mi_libro.devolver())

    books = [mi_libro, book2]

    for book in books:
        print(book)
        
    print("Libros disponibles: ")
    print(biblioteca.libros_disponibles())


if __name__ == "__main__":
    main()
