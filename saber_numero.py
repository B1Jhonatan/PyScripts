

def saber_numero():
    numeros = list(range(10, 86))
    print(len(numeros))
    for n in numeros:
        resultado = n * 103
        nstr = str(resultado)
        coincidencia2 = nstr[:2]
        coincidencia1 = nstr[-2:]
        if coincidencia1 == '85':
            print("aqui: ", resultado)
        elif coincidencia2 == '85':
            print("aqui: ", resultado)
        else:
            print(resultado)


if __name__ == '__main__':
    saber_numero()
