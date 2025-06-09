#!./.venv/bin/python3

def main():
    print("Calcular hipoteca fija")
    dinero_pagar: float = float(input("Monto a pagar: "))
    cantidad_years: int = int(input("Cantidad de años: "))
    tasa_interes_anual: float = float(input("Tasa de interes anual: "))

    cantidad_meses = cantidad_years * 12
    tasa_interes_mensual = tasa_interes_anual / 12 / 100

    cuota = (dinero_pagar * tasa_interes_mensual * (1 + tasa_interes_mensual) ** cantidad_meses) / \
            ((1 + tasa_interes_mensual) ** cantidad_meses - 1)
    count = 1
    while 0 < dinero_pagar:
        dinero_restado = dinero_pagar * tasa_interes_mensual
        dinero_restado = dinero_restado + dinero_pagar
        dinero_pagar = dinero_restado - cuota
        dinero_pagar = round(dinero_pagar, 2)
        print(f"{count}: {dinero_pagar}")
        count += 1

    cuota = round(cuota, 2)
    print("Cuota mensual a pagar:", cuota, "(moneda local de tu pais)")
    print("Monto total despues de", cantidad_years, "años", "pagando es:", (cuota * cantidad_meses))


if __name__ == '__main__':
    main()
