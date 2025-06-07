#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(description="Ejemplo de script con parámetros")
    parser.add_argument("-u", "--url", required=True, help="URL de entrada")
    parser.add_argument("-m", "--mensaje", required=True, help="Mensaje a procesar")

    args = parser.parse_args()

    print(f"URL recibida: {args.url}")
    print(f"Mensaje recibido: {args.mensaje}")


if __name__ == "__main__":
    main()
