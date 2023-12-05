
import tkinter as tk
from funciones import agregar_producto, obtener_productos
from confing import *
class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Stock")
        self.label_nombre = tk.Label(root, text="Nombre del Producto:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()
        self.label_cantidad = tk.Label(root, text="Cantidad:")
        self.label_cantidad.pack()
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack()
        self.boton_agregar = tk.Button(root, text="Agregar Producto", command=self.agregar_producto)
        self.boton_agregar.pack()
        self.lista_productos = tk.Listbox(root)
        self.lista_productos.pack()

        self.actualizar_lista()

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        cantidad = int(self.entry_cantidad.get())
        agregar_producto(nombre, cantidad)
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_productos.delete(0, tk.END)
        productos = obtener_productos()
        for producto in productos:
            self.lista_productos.insert(tk.END, f"{producto[1]} - Cantidad: {producto[2]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
