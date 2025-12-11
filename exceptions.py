class BibliotecaError(Exception):
    """Excepcion base para errores de la biblioteca"""
    pass

class LibroNoDisponibleError(BibliotecaError):
    """El libro no esta disponible para prestamos"""
    pass

class LimitePrestamosError(BibliotecaError):
    """Se excedio el limite de prestamos permitidos"""
    pass

class TituloInvalidoError(BibliotecaError):
    """El titulo del libro no esvalido"""
    pass

class UsuarioNoEncontradoError(BibliotecaError):
    """El usuario no fue encontrado en el sistema"""
    pass