"""Fundamentos de Programación 213022, Fase 5, Problema 3."""


def cantidad_a_pedir(stock_actual, stock_minimo):
    """Devuelve las unidades necesarias para alcanzar el mínimo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def mostrar_pedidos(inventario):
    """Imprime el nombre y la cantidad a pedir de cada artículo."""
    print("Lista de pedidos")
    for codigo, nombre, actual, minimo in inventario:
        cantidad = cantidad_a_pedir(actual, minimo)
        print(f"{nombre}: {cantidad}")


def main():
    # Columnas: código, nombre, stock actual y stock mínimo.
    inventario = [
        ["A01", "Cuaderno", 4, 10],
        ["A02", "Lápiz", 15, 10],
        ["A03", "Borrador", 8, 8],
        ["A04", "Regla", 0, 5],
        ["A05", "Marcador", 7, 8],
    ]
    mostrar_pedidos(inventario)


if __name__ == "__main__":
    main()
