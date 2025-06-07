#!./.venv/bin/python3
from datetime import datetime
import argparse
import qrcode


def main():

    parser = argparse.ArgumentParser(description="Es mensaje de qr")
    parser.add_argument("-m", "--mensaje", required=True, help="Mensaje a convertir en QR")

    texto = str(parser.parse_args())

    qr = qrcode.main.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(str(texto))
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
