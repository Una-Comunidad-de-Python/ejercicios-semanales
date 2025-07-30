def agregar_tarea(lista_tareas, descripcion):
    # 1. Creamos un diccionario para representar la nueva tarea.
    #    Tendrá la descripción que nos pasan y el estado 'completada' en False por defecto.
    nueva_tarea = {
        'descripcion': descripcion,
        'completada': False
    }

    # 2. Usamos el método .append() para añadir el nuevo diccionario al final de la lista.
    lista_tareas.append(nueva_tarea)

    # 3. Devolvemos la lista, que ahora contiene la nueva tarea.
    return lista_tareas

# --- Pruebas ---
def probar_agregar_tarea():
    # Prueba 1: Agregar a una lista vacía
    tareas = []
    tareas_actualizadas = agregar_tarea(tareas, "Estudiar Python")
    print(f"Prueba 1: {tareas_actualizadas == [{'descripcion': 'Estudiar Python', 'completada': False}]}")

    # Prueba 2: Agregar a una lista existente
    tareas_existentes = [{'descripcion': 'Hacer ejercicio', 'completada': True}]
    tareas_actualizadas_2 = agregar_tarea(tareas_existentes, "Llamar al dentista")
    esperado = [
        {'descripcion': 'Hacer ejercicio', 'completada': True},
        {'descripcion': 'Llamar al dentista', 'completada': False}
    ]
    print(f"Prueba 2: {tareas_actualizadas_2 == esperado}")

probar_agregar_tarea()