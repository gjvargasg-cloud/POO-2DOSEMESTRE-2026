import os

class Semana:
    def __init__(self, nombre, ruta_base):
        self.nombre = nombre
        self.ruta = os.path.join(ruta_base, nombre)

    def crear(self):
        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)
            print(f"Semana {self.nombre} creada")
        else:
            print("La semana ya existe")

    def listar_tareas(self):
        if os.path.exists(self.ruta):
            archivos = os.listdir(self.ruta)
            if archivos:
                print(f"Tareas en {self.nombre}:")
                for a in archivos:
                    print(f"- {a}")
            else:
                print("No hay tareas aún")
        else:
            print("La semana no existe")

    def crear_tarea(self, nombre_tarea):
        if os.path.exists(self.ruta):
            ruta_tarea = os.path.join(self.ruta, nombre_tarea)
            with open(ruta_tarea, "w") as f:
                f.write("# Tarea de Programación Orientada a Objetos\n")
            print("Tarea creada correctamente")
        else:
            print("La semana no existe")


class Dashboard:
    def __init__(self):
        self.ruta_base = os.getcwd()

    def mostrar_semanas(self):
        print("\nSemanas del semestre:")
        for item in os.listdir(self.ruta_base):
            if item.startswith("Semana"):
                print(f"- {item}")

    def menu(self):
        while True:
            print("\n--- DASHBOARD POO  ---")
            print("1. Ver semanas")
            print("2. Crear semana")
            print("3. Ver tareas de una semana")
            print("4. Crear tarea en una semana")
            print("5. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                self.mostrar_semanas()

            elif opcion == "2":
                nombre = input("Nombre de la semana (Ej: Semana_03): ")
                semana = Semana(nombre, self.ruta_base)
                semana.crear()

            elif opcion == "3":
                nombre = input("Nombre de la semana: ")
                semana = Semana(nombre, self.ruta_base)
                semana.listar_tareas()

            elif opcion == "4":
                nombre = input("Nombre de la semana: ")
                tarea = input("Nombre del archivo (Ej: tarea1.py): ")
                semana = Semana(nombre, self.ruta_base)
                semana.crear_tarea(tarea)

            elif opcion == "5":
                print("Saliendo del sistema")
                break

            else:
                print("Opción inválida")


if __name__ == "__main__":
    app = Dashboard()
    app.menu()
