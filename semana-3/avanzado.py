def reporte_prioritario(lista_tareas):
    """
    Devuelve una lista de tareas pendientes, ordenadas por prioridad: Alta, Media, Baja.
    """
    # 1. Primero, filtramos para quedarnos solo con las tareas pendientes.
    #    Usamos una "comprensión de lista" Ver: https://www.w3schools.com/python/python_lists_comprehension.asp
    tareas_pendientes = [
        tarea for tarea in lista_tareas if not tarea['completada']
    ]

    # 2. Definimos un mapa de prioridades. Asignamos números a cada prioridad
    #    para que Python sepa cómo ordenarlas (0 es más importante que 1, etc.).
    orden_prioridad = {
        "Alta": 0,
        "Media": 1,
        "Baja": 2
    }

    # 3. Usamos la función sorted() para ordenar la lista de tareas pendientes.
    #    La parte clave es el argumento 'key'. Le decimos a sorted() que para cada
    #    tarea, debe usar el valor numérico de su prioridad para decidir el orden.
    #    'tarea.get('prioridad', 'Baja')' obtiene la prioridad de la tarea,
    #    o usa 'Baja' si la tarea no tiene una clave de prioridad.
    reporte_ordenado = sorted(
        tareas_pendientes,
        key=lambda tarea: orden_prioridad.get(tarea.get('prioridad', 'Baja'))
    )

    # 4. Devolvemos la lista ya filtrada y ordenada.
    return reporte_ordenado

# --- Pruebas ---
def probar_reporte_prioritario():
    tareas = [
        {'descripcion': 'Revisar código', 'completada': False, 'prioridad': 'Media'},
        {'descripcion': 'Diseñar base de datos', 'completada': False, 'prioridad': 'Alta'},
        {'descripcion': 'Actualizar documentación', 'completada': True, 'prioridad': 'Baja'},
        {'descripcion': 'Corregir bug crítico', 'completada': False, 'prioridad': 'Alta'},
        {'descripcion': 'Enviar email de seguimiento', 'completada': False},
        {'descripcion': 'Reunión de equipo', 'completada': False, 'prioridad': 'Media'}
    ]

    reporte = reporte_prioritario(tareas)
    
    es_valido = (
        len(reporte) == 5 and
        # Usamos .get() en la prueba para evitar errores si la clave no estuviera
        reporte[0].get('prioridad') == 'Alta' and reporte[1].get('prioridad') == 'Alta' and
        reporte[2].get('prioridad') == 'Media' and reporte[3].get('prioridad') == 'Media' and
        # La última puede tener prioridad 'Baja' o no tener la clave
        reporte[4].get('prioridad', 'Baja') == 'Baja' 
    )
    print(f"Prueba 1: {es_valido}")

    tareas_completadas = [{'descripcion': 'Tarea 1', 'completada': True, 'prioridad': 'Alta'}]
    reporte2 = reporte_prioritario(tareas_completadas)
    print(f"Prueba 2 (solo completadas): {reporte2 == []}")

probar_reporte_prioritario()