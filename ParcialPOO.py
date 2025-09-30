class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._isbn = isbn
        self._disponible = True

    def prestar(self): self._disponible = False
    def devolver(self): self._disponible = True
    def disponible(self): return self._disponible
    def isbn(self): return self._isbn
    def info(self): return f"{self._titulo} ({self._categoria})"


class Usuario:
    def __init__(self, nombre, id_u):
        self._nombre = nombre
        self._id = id_u
        self._libros = []

    def prestar(self, libro): self._libros.append(libro)
    def id(self): return self._id
    def libros(self): return self._libros


class Biblioteca:
    def __init__(self):
        self._libros = []
        self._usuarios = []
        self._categorias = ["Ciencia", "Literatura", "Ingeniería"]

    def registrar_libro(self):
        t = input("Título: ")
        a = input("Autor: ")
        c = input("Categoría: ")
        i = input("ISBN: ")
        if c not in self._categorias:
            print("Categoría inválida.")
            return
        self._libros.append(Libro(t, a, c, i))
        print("Libro registrado.")

    def registrar_usuario(self):
        n = input("Nombre: ")
        i = input("ID: ")
        self._usuarios.append(Usuario(n, i))
        print("Usuario registrado.")

    def prestar_libro(self):
        id_u = input("ID usuario: ")
        isbn = input("ISBN libro: ")
        usuario = next((u for u in self._usuarios if u.id() == id_u), None)
        libro = next((l for l in self._libros if l.isbn() == isbn), None)
        if usuario and libro and libro.disponible():
            libro.prestar()
            usuario.prestar(libro)
            print("¡Libro prestado!")
        else:
            print("Error: usuario, libro o no disponible.")

    def menu(self):
        while True:
            print("\n1. Registrar libro\n2. Registrar usuario\n3. Prestar libro\n4. Salir")
            op = input("Opción: ")
            if op == "1": self.registrar_libro()
            elif op == "2": self.registrar_usuario()
            elif op == "3": self.prestar_libro()
            elif op == "4": break
            else: print("Opción inválida.")


# Ejecución
Biblioteca().menu()
