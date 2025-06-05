#!/home/jhonatan/PyCharmMiscProject/venv/bin/python3

import qrcode


def main(texto: str):
    qr = qrcode.main.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.show()


if __name__ == '__main__':
    main(str(input("Ingrese el texto a convertir en QR: \n")))
