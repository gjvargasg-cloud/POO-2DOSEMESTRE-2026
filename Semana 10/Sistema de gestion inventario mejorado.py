import os


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Formato para guardar en archivo
        return f"{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo de texto."""
        if not os.path.exists(self.ARCHIVO):
            try:
                open(self.ARCHIVO, "w").close()
                print("Archivo de inventario creado correctamente.")
            except PermissionError:
                print("Error: No tienes permisos para crear el archivo.")
            return

        try:
            with open(self.ARCHIVO, "r") as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    try:
                        nombre, cantidad, precio = linea.strip().split(",")
                        self.productos.append(
                            Producto(nombre, int(cantidad), float(precio))
                        )
                    except ValueError:
                        print(f"Advertencia: Línea {num_linea} con formato incorrecto.")
            print("Inventario cargado correctamente.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo."""
        try:
            with open(self.ARCHIVO, "w") as archivo:
                for producto in self.productos:
                    archivo.write(str(producto) + "\n")
            print("Archivo actualizado correctamente.")
        except PermissionError:
            print("Error: No se pudo escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un producto nuevo al inventario."""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print("Error: El producto ya existe.")
                return

        self.productos.append(Producto(nombre, cantidad, precio))
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, nueva_cantidad, nuevo_precio):
        """Actualiza un producto existente."""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                self.guardar_en_archivo()
                print(f"Producto '{nombre}' actualizado correctamente.")
                return

        print("Error: Producto no encontrado.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print(f"Producto '{nombre}' eliminado correctamente.")
                return

        print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos."""
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\nInventario Actual:")
        for producto in self.productos:
            print(
                f"{producto.nombre} - Cantidad: {producto.cantidad}, "
                f"Precio: ${producto.precio:.2f}"
            )


# Programa principal
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Mostrar Inventario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")

            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: Debes ingresar valores numéricos válidos.")
                continue

            inventario.agregar_producto(nombre, cantidad, precio)

        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")

            try:
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
            except ValueError:
                print("Error: Debes ingresar valores numéricos válidos.")
                continue

            inventario.actualizar_producto(nombre, cantidad, precio)

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")