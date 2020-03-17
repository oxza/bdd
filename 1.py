import sqlite3 as sq
import os, msvcrt, time

abc = sq.connect("bdd1.db")
abc.execute('''CREATE TABLE IF NOT EXISTS personas(
    id INT PRIMARY KEY,
    nombre CHAR(40))''')

def añadir():
    id3 = input("Introduce el id: ")
    nombre3 = input("Introduce el nombre: ")

    id = abc.execute('''INSERT INTO nombres(
        id,
        nombre)
        VALUES(
            %s,
            '%s')''' % (id3, nombre3))
    abc.commit()

    os.system("cls")
    print("Nombre añadido correctamente.")
    time.sleep(2)
    print("\n¿Qué quieres hacer?")
    print("\n1. Volver al menú.")
    print("2. Añadir otro nombre.")
    e2 = input("\nIntroduce tu respuesta: ")

    if e2 == "1":
        menu()
    elif e2 == "2":
        añadir()
    else:
        print("Respuesta inválida. Volviendo al menú...")
        time.sleep(3)
        menu()

def eliminar():
    id2 = int(input("Introduce el ID del nombre que quieres eliminar: "))

    abc.execute('''DELETE FROM nombres
        WHERE id = %s''' % (id2))

    os.system("cls")
    print("Eliminado correctamente.")

    time.sleep(2)
    print("\n¿Qué quieres hacer?")
    print("\n1. Volver al menú.")
    print("2. Eliminar otro nombre.")
    e2 = input("\nIntroduce tu respuesta: ")

    if e2 == "1":
        menu()
    elif e2 == "2":
        eliminar()
    else:
        print("Respuesta inválida. Volviendo al menú...")
        time.sleep(3)
        menu()

def actualizar():
    id1 = input("Introduce el id: ")
    nombre1 = input("Introduce el nuevo nombre: ")

    abc.execute('''UPDATE nombres SET nombre = '%s' WHERE id = %s)''' % (nombre1, id1))

    os.system("cls")
    print("Actualizado correctamente.")

    time.sleep(2)
    print("\n¿Qué quieres hacer?")
    print("\n1. Volver al menú.")
    print("2. Actualizar otro nombre.")
    e2 = input("\nIntroduce tu respuesta: ")

    if e2 == "1":
        menu()
    elif e2 == "2":
        actualizar()
    else:
        print("Respuesta inválida. Volviendo al menú...")
        time.sleep(3)
        menu()

def menu():
    os.system("cls")
    print("¿Qué quieres hacer?")
    print("\n1. Añadir un nombre.")
    print("2. Eliminar un nombre.")
    print("3. Actualizar un nombre.")
    eleccion = input("\nIntroduce una opción: ")

    os.system("cls")
    if eleccion == "1":
        añadir()
    elif eleccion == "2":
        eliminar()
    elif eleccion == "3":
        actualizar()
    else:
        print("Por favor, introduce una opción correcta.")
        menu()

menu()