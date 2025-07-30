# Modelo del diccionario utilizado en el inventario:
# inventario = [
#     {'nombre': '', 'precio': 0, 'stock': 0},
# ]

def calcular_valor_total(inventario):
    # 1. Empezamos con un contador de valor total en cero.
    valor_total = 0.0|

    for producto in inventario:
        precio_producto = producto['precio']
        stock_producto = producto['stock']

        valor_total += precio_producto * stock_producto

    return valor_total

# --- Pruebas ---
def probar_calcular_valor_total():
    inventario1 = [
        {'nombre': 'Laptop', 'precio': 1200.00, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25.50, 'stock': 20}
    ]
    resultado1 = calcular_valor_total(inventario1)
    print(f"Prueba 1: {resultado1 == 6510.0}")

    inventario2 = []
    resultado2 = calcular_valor_total(inventario2)
    print(f"Prueba 2 (inventario vacío): {resultado2 == 0.0}")

    inventario3 = [
        {'nombre': 'Teclado', 'precio': 75.00, 'stock': 0}
    ]
    resultado3 = calcular_valor_total(inventario3)
    print(f"Prueba 3 (sin stock): {resultado3 == 0.0}")


probar_calcular_valor_total()