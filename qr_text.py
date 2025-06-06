#!./venv/bin/python3
from datetime import datetime

import qrcode


def main():
    print("")
    print("   ----------------------------------------------")
    texto = str(input("  | Ingrese el texto a convertir en QR: \n  | "))
    print("   ----------------------------------------------")
    print("")

    qr = qrcode.main.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(texto)
    qr.make(fit=True)

    ahora = datetime.now()
    fecha = ahora.strftime("%y-%m-%d")

    name_file: str = str(len(texto))
    name_file += texto[:2]
    name_file += texto[-2:]

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"/home/jhonatan/Pictures/QR/QR_{fecha}_{name_file}.png")
    img.show()


if __name__ == '__main__':
    main()
