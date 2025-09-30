#Miguel Ángel Ramos
#Biblioteca universitaria

class Libro:
    def __init__(self, titulo, autor, categoria, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = True
        self.cantidad = cantidad

    def prestar(self):
        if self.disponible:
            self.disponible = False

    def devolver(self):
        self.disponible = True

    def tomar_titulo(self):
        return self.titulo
    
    def tomar_autor(self):
        return self.autor
    
    def tomar_categoría(self):
        return self.categoria

    def confirmar_disponibilidad(self):
        return self.disponible
    
    def confirmar_cantidad(self):
        return self.cantidad

class Usuario:
    def __init__(self,nombre,libros_prestados):
        self.nombre = nombre
        self.libros_prestados = []

    def pedir_libro(self):
        x=input("Ingrese el nombre del libro que quiere pedir")


        
class Administrador(Libro, Usuario):
    categorias_libros=["Ciencia Ficción", "Drama", "Infantil"]
    def generar_variables(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self):
         self.libros.append(Libro(titulo=input("Ingrese el título del libro"), autor=input("Ingrese el autor del libro"), categoria=input("Ingrese la categoría del libro") ))

    def desplegar_menu(self):
        print("Vienvenido a la biblioteca virtual MARS\nMarque 1 o 2 según su el perfil con el que va a ingresar\n\n" \
        "1)Usuario\n2)administrador" )
        input("Ingrese su nombre")
