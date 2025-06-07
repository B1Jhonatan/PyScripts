#!./.venv/bin/python3

import argparse


def run():
    parser = argparse.ArgumentParser(description="Ejemplo de script con parámetros")
    parser.add_argument("-u", "--url", required=False, help="URL de entrada")
    parser.add_argument("-m", "--mensaje", required=False, help="Mensaje a procesar")
    parser.add_argument("-e", "--encode", required=False, help="Encriptar")
    parser.add_argument("-d", "--decode", required=False, help="Desencriptar")

    args = parser.parse_args()

    print(f"URL recibida: {args.url}")
    print(f"Mensaje recibido: {args.mensaje}")


if __name__ == "__main__":
    run()
