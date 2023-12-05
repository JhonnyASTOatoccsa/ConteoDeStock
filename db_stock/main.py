
from funciones import crear_tabla
from interfaz import Interfaz
import tkinter as tk

crear_tabla()

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
