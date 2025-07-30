from datetime import date, timedelta

def reporte_libros_vencidos(catalogo, fecha_actual):
    """
    Genera un reporte de libros con fecha de devolución vencida,
    ordenados por días de retraso.
    """
    # 1. Creamos una lista vacía para guardar los libros vencidos.
    libros_con_retraso = []

    # 2. Recorremos el catálogo para revisar cada libro.
    for libro in catalogo:
        # 3. Verificamos tres cosas:
        #    a) que el libro NO esté disponible (está prestado).
        #    b) que el libro TENGA una fecha de devolución.
        #    c) que esa fecha de devolución SEA ANTERIOR a la fecha actual.
        if (not libro['disponible'] and
                'fecha_devolucion' in libro and
                libro['fecha_devolucion'] < fecha_actual):
            
            # 4. Si se cumplen las condiciones, calculamos los días de retraso.
            dias_retraso = (fecha_actual - libro['fecha_devolucion']).days
            
            # 5. Creamos un diccionario para el reporte y lo añadimos a nuestra lista.
            libros_con_retraso.append({
                'titulo': libro['titulo'],
                'dias_retraso': dias_retraso
            })

    # 6. Ordenamos la lista de libros con retraso.
    #    key=lambda item: item['dias_retraso'] le dice a sorted que ordene usando el número de días.
    #    reverse=True ordena de mayor a menor.
    reporte_ordenado = sorted(libros_con_retraso, key=lambda item: item['dias_retraso'], reverse=True)

    # 7. Devolvemos la lista ordenada.
    return reporte_ordenado

# --- Pruebas ---
def probar_reporte_libros_vencidos():
    hoy = date(2023, 10, 27)
    catalogo = [
        {'titulo': '1984', 'autor': 'George Orwell', 'disponible': False, 'fecha_devolucion': date(2023, 10, 20)},
        {'titulo': 'Dune', 'autor': 'Frank Herbert', 'disponible': False, 'fecha_devolucion': date(2023, 10, 30)},
        {'titulo': 'El Hobbit', 'autor': 'J.R.R. Tolkien', 'disponible': True},
        {'titulo': 'Fahrenheit 451', 'autor': 'Ray Bradbury', 'disponible': False, 'fecha_devolucion': date(2023, 9, 27)}
    ]

    reporte = reporte_libros_vencidos(catalogo, hoy)
    esperado1 = [
        {'titulo': 'Fahrenheit 451', 'dias_retraso': 30},
        {'titulo': '1984', 'dias_retraso': 7}
    ]
    print(f"Prueba 1: {reporte == esperado1}")

    catalogo_sin_vencidos = [
        {'titulo': 'Dune', 'autor': 'Frank Herbert', 'disponible': False, 'fecha_devolucion': date(2023, 11, 1)}
    ]
    reporte2 = reporte_libros_vencidos(catalogo_sin_vencidos, hoy)
    print(f"Prueba 2: {reporte2 == []}")

probar_reporte_libros_vencidos()