#!./venv/bin/python3

biblioteca_texto = {
    # Letras minúsculas
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
    'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21,
    'm': 22, 'n': 23, 'ñ': 24, 'o': 25, 'p': 26, 'q': 27,
    'r': 28, 's': 29, 't': 30, 'u': 31, 'v': 32, 'w': 33,
    'x': 34, 'y': 35, 'z': 36,

    # Letras mayúsculas
    'A': 37, 'B': 38, 'C': 39, 'D': 40, 'E': 41, 'F': 42,
    'G': 43, 'H': 44, 'I': 45, 'J': 46, 'K': 47, 'L': 48,
    'M': 49, 'N': 50, 'Ñ': 51, 'O': 52, 'P': 53, 'Q': 54,
    'R': 55, 'S': 56, 'T': 57, 'U': 58, 'V': 59, 'W': 60,
    'X': 61, 'Y': 62, 'Z': 63,

    # Caracteres especiales
    '!': 64, '#': 65, '$': 66, '%': 67, '&': 68,
    '*': 69, '+': 70, '-': 71, '=': 72, '?': 73,
    '@': 74, '^': 75, '_': 76, ' ': 85
}


biblioteca_numeros = {
    '10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f',
    '16': 'g', '17': 'h', '18': 'i', '19': 'j', '20': 'k', '21': 'l',
    '22': 'm', '23': 'n', '24': 'ñ', '25': 'o', '26': 'p', '27': 'q',
    '28': 'r', '29': 's', '30': 't', '31': 'u', '32': 'v', '33': 'w',
    '34': 'x', '35': 'y', '36': 'z',

    '37': 'A', '38': 'B', '39': 'C', '40': 'D', '41': 'E', '42': 'F',
    '43': 'G', '44': 'H', '45': 'I', '46': 'J', '47': 'K', '48': 'L',
    '49': 'M', '50': 'N', '51': 'Ñ', '52': 'O', '53': 'P', '54': 'Q',
    '55': 'R', '56': 'S', '57': 'T', '58': 'U', '59': 'V', '60': 'W',
    '61': 'X', '62': 'Y', '63': 'Z',

    '64': '!', '65': '#', '66': '$', '67': '%', '68': '&',
    '69': '*', '70': '+', '71': '-', '72': '=', '73': '?',
    '74': '@', '75': '^', '76': '_', '85': ' '
}

biblioteca_no_usados = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
}


def encriptar(text):
    texto_encriptado = ""
    for char in text:
        if char in biblioteca_texto:
            numero = biblioteca_texto[char] * 103  # Multiplicamos

            numero_str = str(numero)  # Aseguramos al menos 4 dígitos
            primera_mitad = numero_str[:2]
            segunda_mitad = numero_str[-2:]

            letra1 = biblioteca_numeros.get(primera_mitad, str(primera_mitad))
            letra2 = biblioteca_numeros.get(segunda_mitad, str(segunda_mitad))

            texto_encriptado += str(letra1) + str(letra2)
        else:
            texto_encriptado += char  # Dejamos los caracteres no encriptables

    print("  |------------------Encriptado------------------")
    print("  |", texto_encriptado)
    print("  |", len(texto_encriptado), "letras")


def desencriptar(texto_encriptado):
    texto_desencriptado = ""
    numero = ""
    for char in texto_encriptado:
        if char in biblioteca_texto:
            n = biblioteca_texto[char]
            numero += str(n)
        elif char in biblioteca_no_usados:
            numero += str(char)
    numero_n = int(numero)
    for i in range(0, len(numero), 4):
        par = numero[i:i + 4]
        par = int(par) // 103
        par = str(par)
        if par in biblioteca_numeros:
            par = biblioteca_numeros[par]

        texto_desencriptado += par

    print("  |-----------------Desncriptado-----------------")
    print("  |", texto_desencriptado)


def main():
    seguir = True
    while seguir:
        print("")
        print("   ----------------------------------------------")
        opcion = input("  | Que desea realizar encriptar o desencriptar: Opciones [ e / d ] ")
        if opcion.lower() == 'e':
            encriptar(input("  | Ingrese palabras: "))
            print("   ----------------------------------------------")
        elif opcion.lower() == 'd':
            desencriptar(input("  | Ingrese lo encriptado: \n  | "))
            print("   ----------------------------------------------")
        else:
            print("   ----------------------------------------------")
            print("")
            seguir = False


if __name__ == '__main__':
    main()
