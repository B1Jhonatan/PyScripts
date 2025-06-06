#!./venv/bin/python3

from faker import *
import random
import csv

fake = Faker('es_CO')


def writte_csv(name_file, cantidad_persons):
    ruta = f"/home/jhonatan/Documents/Proyectos csv/{name_file}"
    Faker.seed(0)
    random.seed(0)

    header = ["nombre", "apellido", "num_telefono", "email", "pais", "ciudad"]

    with open(ruta, mode='w', newline='', encoding='utf-8') as file:
        writter = csv.writer(file)
        writter.writerow(header)

        for _ in range(cantidad_persons):
            fila = [
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email(),
                fake.country(),
                fake.city()
            ]
            writter.writerow(fila)


def run():
    name_file = input("Nombre del archivo: ")
    cantidad = int(input("Cantidad de registros: "))
    writte_csv(name_file, cantidad)


if __name__ == '__main__':
    run()
