def buscar_libro_por_titulo(catalogo, titulo_buscado):
    """
    Busca un libro en el catálogo por su título y devuelve el diccionario del libro.
    """
    # 1. Recorremos cada libro (que es un diccionario) en la lista del catálogo.
    for libro in catalogo:
        # 2. Comparamos el título del libro actual con el título que buscamos.
        if libro['titulo'] == titulo_buscado:
            # 3. Si coinciden, hemos encontrado el libro. Lo devolvemos y la función termina.
            return libro

    # 4. Si el bucle termina y no hemos encontrado el libro, significa que no está.
    #    Devolvemos None.
    return None

# --- Pruebas ---
def probar_buscar_libro_por_titulo():
    catalogo = [
        {'titulo': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez', 'disponible': True},
        {'titulo': 'El Señor de los Anillos', 'autor': 'J.R.R. Tolkien', 'disponible': False},
        {'titulo': '1984', 'autor': 'George Orwell', 'disponible': True}
    ]

    libro_encontrado = buscar_libro_por_titulo(catalogo, '1984')
    esperado1 = {'titulo': '1984', 'autor': 'George Orwell', 'disponible': True}
    print(f"Prueba 1: {libro_encontrado == esperado1}")

    libro_no_encontrado = buscar_libro_por_titulo(catalogo, 'Fahrenheit 451')
    print(f"Prueba 2: {libro_no_encontrado is None}")

    libro_en_catalogo_vacio = buscar_libro_por_titulo([], 'Cien Años de Soledad')
    print(f"Prueba 3: {libro_en_catalogo_vacio is None}")

probar_buscar_libro_por_titulo()