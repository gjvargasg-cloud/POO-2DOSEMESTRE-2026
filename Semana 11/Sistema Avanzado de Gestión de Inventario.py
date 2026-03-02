import pickle
import os

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto '{producto.nombre}' agregado al inventario.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado.")
        else:
            print("Error: No se encontró un producto con este ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print(f"Producto con ID {id} actualizado.")
        else:
            print("Error: No se encontró un producto con este ID.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)
        print(f"Inventario guardado en '{archivo}'.")

    def cargar_inventario(self, archivo):
        if os.path.exists(archivo):
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print(f"Inventario cargado desde '{archivo}'.")
        else:
            print("No se encontró el archivo de inventario. Se creará uno nuevo al guardar.")


# Interfaz de Usuario
def menu():
    inventario = Inventario()
    archivo_inventario = "inventario.dat"
    inventario.cargar_inventario(archivo_inventario)

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            inventario.guardar_inventario(archivo_inventario)
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()