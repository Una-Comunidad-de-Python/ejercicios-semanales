def marcar_y_filtrar(lista_tareas, descripcion, estado_filtro):
    """
    Marca una tarea como completada y luego filtra la lista según un estado.
    """
    # --- PASO 1: MARCAR LA TAREA COMO COMPLETADA ---
    for tarea in lista_tareas:
        # Si la descripción de la tarea actual coincide con la que buscamos
        if tarea['descripcion'] == descripcion:
            # Cambiamos el estado de 'completada'.
            tarea['completada'] = True
            # Usamos 'break' para detener la búsqueda una vez que la encontramos.
            break

    # --- PASO 2: FILTRAR LA LISTA SEGÚN EL ESTADO ---
    # Creamos una lista vacía para guardar los resultados del filtro.
    tareas_filtradas = []
    for tarea in lista_tareas:
        if estado_filtro == 'todas':
            tareas_filtradas.append(tarea)
        elif estado_filtro == 'pendientes' and not tarea['completada']:
            tareas_filtradas.append(tarea)
        elif estado_filtro == 'completadas' and tarea['completada']:
            tareas_filtradas.append(tarea)

    # Devolvemos la nueva lista que solo contiene las tareas filtradas.
    return tareas_filtradas

# --- Pruebas ---
def probar_marcar_y_filtrar():
    lista_base = [
        {'descripcion': 'Comprar leche', 'completada': False},
        {'descripcion': 'Pagar facturas', 'completada': False},
        {'descripcion': 'Sacar al perro', 'completada': False}
    ]

    tareas_p1 = [t.copy() for t in lista_base]
    resultado1 = marcar_y_filtrar(tareas_p1, 'Pagar facturas', 'completadas')
    print(f"Prueba 1: {resultado1 == [{'descripcion': 'Pagar facturas', 'completada': True}]}")

    tareas_p2 = [t.copy() for t in lista_base]
    resultado2 = marcar_y_filtrar(tareas_p2, 'Comprar leche', 'pendientes')
    esperado2 = [
        {'descripcion': 'Pagar facturas', 'completada': False},
        {'descripcion': 'Sacar al perro', 'completada': False}
    ]
    print(f"Prueba 2: {resultado2 == esperado2}")

    tareas_p3 = [t.copy() for t in lista_base]
    resultado3 = marcar_y_filtrar(tareas_p3, 'Leer un libro', 'todas')
    print(f"Prueba 3: {resultado3 == lista_base}")

probar_marcar_y_filtrar()