def consultar_horarios(cartelera, titulo_pelicula):
    """
    Busca una película en la cartelera y devuelve su lista de horarios.
    """
    # 1. Recorremos cada película (que es un diccionario) en la lista de la cartelera.
    for pelicula in cartelera:
        # 2. Comparamos el título de la película actual con el que estamos buscando.
        if pelicula['titulo'] == titulo_pelicula:
            # 3. Si encontramos la película, devolvemos su lista de horarios y la función termina.
            return pelicula['horarios']

    # 4. Si el bucle termina sin haber encontrado la película, devolvemos una lista vacía.
    return []

# --- Pruebas ---
def probar_consultar_horarios():
    cartelera = [
        {'titulo': 'Inception', 'horarios': ['18:00', '21:00']},
        {'titulo': 'The Matrix', 'horarios': ['17:30', '20:30']},
        {'titulo': 'Parasite', 'horarios': ['19:00', '22:00']}
    ]

    horarios_matrix = consultar_horarios(cartelera, 'The Matrix')
    print(f"Prueba 1: {horarios_matrix == ['17:30', '20:30']}")

    horarios_interstellar = consultar_horarios(cartelera, 'Interstellar')
    print(f"Prueba 2: {horarios_interstellar == []}")

    horarios_vacio = consultar_horarios([], 'Inception')
    print(f"Prueba 3: {horarios_vacio == []}")

probar_consultar_horarios()