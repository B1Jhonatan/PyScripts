#!./.venv/bin/python3

import sqlite3 as sql

rutas = {
    'encriptado': "./data_base/encriptado.db"
}


# def create_db():
#     conn = sql.connect(rutas.get('encriptado'))
#     conn.commit()
#     conn.close()


# def create_table():
#     name_table = ""
#     columns_table = ""
#     conn = sql.connect(rutas.get('encriptado'))
#     cursor = conn.cursor()
#     instruccion = f"CREATE TABLE '{name_table}' ({columns_table})"
#     cursor.execute(instruccion)
#     conn.commit()
#     conn.close()


def save_text_db():
    text = str(input("Texto a guardar en la base de datos: "))
    conn = sql.connect(rutas.get('encriptado'))
    cursor = conn.cursor()
    instruccion = f"INSERT INTO encriptado (text) VALUES ('{text}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def read_text_db():
    conn = sql.connect(rutas.get('encriptado'))
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM encriptado"
    cursor.execute(instruccion)
    muestra = cursor.fetchall()

    for m in muestra:
        print(f"ID: {m[0]}, {m[1]}")

    conn.commit()
    conn.close()


def update_text_db():
    id_update = str(input("ID a actualizar: "))
    text_update = str(input("Texto a actualizar: "))
    conn = sql.connect(rutas.get('encriptado'))
    cursor = conn.cursor()
    instruccion = f"UPDATE encriptado SET text = '{text_update}' WHERE id = '{id_update}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def delete_text_db():
    id_borrar = str(input("ID del elemento que quiere eliminar: "))
    conn = sql.connect(rutas.get('encriptado'))
    cursor = conn.cursor()
    instruccion = f"DELETE FROM encriptado WHERE id= {id_borrar}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def main():
    loop = True
    while loop:
        choise = str(input("Que desea hacer, Crear, Leer, Actualizar, Borrar: [ c / l / a / b] "))
        if choise.lower() == 'c':
            save_text_db()
        elif choise.lower() == 'l':
            read_text_db()
        elif choise.lower() == 'a':
            update_text_db()
        elif choise.lower() == 'b':
            delete_text_db()
        else:
            loop = False


if __name__ == '__main__':
    main()
