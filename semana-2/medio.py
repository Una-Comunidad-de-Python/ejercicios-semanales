def generar_reporte_reabastecimiento(inventario, umbral_stock):

    productos_a_reabastecer = []

    for nombre, detalles in inventario.items():
        stock_actual = detalles['stock']

        if stock_actual <= umbral_stock:
            if stock_actual == 0:
                necesidad = "Urgente"
            else:
                necesidad = "Baja"

            productos_a_reabastecer.append({
                'nombre': nombre,
                'stock': stock_actual,
                'necesidad': necesidad
            })
    reporte_ordenado = sorted(productos_a_reabastecer, key=lambda producto: producto['stock'])
    return reporte_ordenado

# --- Pruebas ---
def probar_generar_reporte_reabastecimiento():
    inventario = {
        'Laptop': {'precio': 1200.00, 'stock': 5},
        'Mouse': {'precio': 25.50, 'stock': 20},
        'Teclado': {'precio': 75.00, 'stock': 10},
        'Monitor': {'precio': 300.00, 'stock': 0},
        'Webcam': {'precio': 50.00, 'stock': 8}
    }

    reporte1 = generar_reporte_reabastecimiento(inventario, 10)
    resultado_esperado1 = [
        {'nombre': 'Monitor', 'stock': 0, 'necesidad': 'Urgente'},
        {'nombre': 'Laptop', 'stock': 5, 'necesidad': 'Baja'},
        {'nombre': 'Webcam', 'stock': 8, 'necesidad': 'Baja'},
        {'nombre': 'Teclado', 'stock': 10, 'necesidad': 'Baja'}
    ]
    print(f"Prueba 1 (Umbral 10): {reporte1 == resultado_esperado1}")

    reporte2 = generar_reporte_reabastecimiento(inventario, 4)
    resultado_esperado2 = [
        {'nombre': 'Monitor', 'stock': 0, 'necesidad': 'Urgente'}
    ]
    print(f"Prueba 2 (Umbral 4): {reporte2 == resultado_esperado2}")

    reporte3 = generar_reporte_reabastecimiento(inventario, 30)
    resultado_esperado3 = [
        {'nombre': 'Monitor', 'stock': 0, 'necesidad': 'Urgente'},
        {'nombre': 'Laptop', 'stock': 5, 'necesidad': 'Baja'},
        {'nombre': 'Webcam', 'stock': 8, 'necesidad': 'Baja'},
        {'nombre': 'Teclado', 'stock': 10, 'necesidad': 'Baja'},
        {'nombre': 'Mouse', 'stock': 20, 'necesidad': 'Baja'}
    ]
    print(f"Prueba 3 (Umbral 30): {reporte3 == resultado_esperado3}")

probar_generar_reporte_reabastecimiento()