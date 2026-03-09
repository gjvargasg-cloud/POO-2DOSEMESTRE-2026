# Sistema de Gestión de Biblioteca Digital

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para almacenar título y autor (no cambian)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para libros prestados
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros usando ISBN como clave
        self.libros = {}
        # Diccionario para usuarios
        self.usuarios = {}
        # Set para asegurar IDs únicos
        self.ids_usuarios = set()

    # Añadir libro
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("Este libro ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente.")

    # Quitar libro
    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("El ID de usuario ya existe.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")

    # Dar de baja usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if not libro.prestado:
                libro.prestado = True
                usuario.libros_prestados.append(libro)
                print("Libro prestado correctamente.")
            else:
                print("El libro ya está prestado.")
        else:
            print("Libro o usuario no encontrado.")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro in usuario.libros_prestados:
                libro.prestado = False
                usuario.libros_prestados.remove(libro)
                print("Libro devuelto correctamente.")
            else:
                print("Ese usuario no tiene este libro.")
        else:
            print("Libro o usuario no encontrado.")

    # Buscar libros
    def buscar_libro(self, criterio):
        encontrados = []

        for libro in self.libros.values():
            if (criterio.lower() in libro.info[0].lower() or
                criterio.lower() in libro.info[1].lower() or
                criterio.lower() in libro.categoria.lower()):
                encontrados.append(libro)

        if encontrados:
            print("\nResultados de búsqueda:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros.")

    # Listar libros prestados de un usuario
    def libros_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"\nLibros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("Este usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Menú de prueba del sistema
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Biblioteca Digital ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Ver libros de un usuario")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")

            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ")
            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            criterio = input("Buscar por título, autor o categoría: ")
            biblioteca.buscar_libro(criterio)

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.libros_usuario(id_usuario)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()