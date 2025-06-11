#!./.venv/bin/python3

import matplotlib.pyplot as plt


def calcular_hipoteca(capital_inicial: float, cantidad_years: int, interes_anual: float):
    # Convertir parámetros
    cantidad_meses = cantidad_years * 12
    interes_mensual = (interes_anual / 100) / 12  # Convertir porcentaje a decimal y dividir por 12

    # Calcular cuota mensual fija
    cuota_mensual = (capital_inicial * interes_mensual * (1 + interes_mensual) ** cantidad_meses) / \
                    ((1 + interes_mensual) ** cantidad_meses - 1)

    # Simular amortización mes a mes
    capital_restante = capital_inicial
    cuotas = []

    for mes in range(cantidad_meses):
        interes_mes = capital_restante * interes_mensual
        amortizacion = cuota_mensual - interes_mes
        capital_restante -= amortizacion

        # Evitar valores negativos por redondeo
        if capital_restante < 0:
            capital_restante = 0

        cuotas.append(capital_restante)

        # Si ya hemos pagado todos, salir del bucle
        if capital_restante == 0:
            break

    return cuotas


def plot_grafico(array_cuotas: list[float]):
    meses = list(range(len(array_cuotas)))

    plt.figure(figsize=(12, 6))

    plt.bar(meses, array_cuotas, width=1.0)

    plt.xticks(meses[::12])

    plt.xlabel("Meses")
    plt.ylabel("monto")
    plt.title("Grafico hipoteca")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()  # Ajustar layout
    plt.show()


def run():
    print("Calcular hipoteca fija")
    dinero_pagar: float = float(input("Monto a pagar: "))
    cantidad_years: int = int(input("Cantidad de años: "))
    tasa_interes_anual: float = float(input("Tasa de interes anual: "))
    cuotas = calcular_hipoteca(dinero_pagar, cantidad_years, tasa_interes_anual)
    plot_grafico(cuotas)


if __name__ == '__main__':
    run()
