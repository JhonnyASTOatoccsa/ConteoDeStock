import sqlite3

def crear_tabla():
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            cantidad INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def agregar_producto(nombre, cantidad):
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos (nombre, cantidad) VALUES (?, ?)', (nombre, cantidad))
    conn.commit()
    conn.close()

def obtener_productos():
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conn.close()
    return productos