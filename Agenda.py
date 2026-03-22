# ==============================
# AGENDA PERSONAL CON TKINTER
# ==============================
# Autor: (Tu nombre)
# Descripción:
# Aplicación GUI que permite agregar, visualizar y eliminar eventos
# utilizando Tkinter.

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # pip install tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x400")

        # ==============================
        # FRAME LISTA DE EVENTOS
        # ==============================
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=100)
        self.tree.column("Descripción", width=300)

        self.tree.pack()

        # ==============================
        # FRAME ENTRADA DE DATOS
        # ==============================
        frame_inputs = tk.Frame(root)
        frame_inputs.pack(pady=10)

        # Fecha
        tk.Label(frame_inputs, text="Fecha:").grid(row=0, column=0, padx=5)
        self.fecha_entry = DateEntry(frame_inputs, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5)

        # Hora
        tk.Label(frame_inputs, text="Hora:").grid(row=0, column=2, padx=5)
        self.hora_entry = tk.Entry(frame_inputs)
        self.hora_entry.grid(row=0, column=3, padx=5)

        # Descripción
        tk.Label(frame_inputs, text="Descripción:").grid(row=0, column=4, padx=5)
        self.desc_entry = tk.Entry(frame_inputs, width=30)
        self.desc_entry.grid(row=0, column=5, padx=5)

        # ==============================
        # FRAME BOTONES
        # ==============================
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0, column=1, padx=10)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=10)

    # ==============================
    # FUNCIONES
    # ==============================

    def agregar_evento(self):
        """Agrega un evento a la tabla"""
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        # Insertar en TreeView
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Error", "Seleccione un evento")
            return

        # Confirmación
        confirm = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento?")
        if confirm:
            self.tree.delete(selected_item)

# ==============================
# EJECUCIÓN
# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
