from typing import Protocol
from exceptions import LibroNoDisponibleError

class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Método de prestar un libro"""
        ...

    def devolver(self) -> str:
        """Método de devolver un libro"""
        ...

    def calcular_duracion(self) -> str:
        """Calcula el tiempo de prestamo"""
        ...


class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0
    
    def __str__(self):
        return f"mi_libro: {self.titulo} - {self.autor} - disponible: {self.disponible}"
        
    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponibleError(f"'{self.titulo}' no esta disponible")
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1 
            return f"'{self.titulo}' prestado exitosamente. Total prestamos {self.__veces_prestado}"
            
    def devolver(self):
        self.disponible = True
        return f"'{self.titulo}' devuelto y disponible nuevamente"
    
    def es_popular(self):
        if self.veces_prestado >= 5:
            return True
        return False
    
    def get_get_veces_prestado(self):
        return self.__veces_prestado
    
    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado
        

class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 días"


class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"
    

        
        
