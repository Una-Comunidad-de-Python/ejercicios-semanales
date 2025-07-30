def filtrar_posts_por_autor(lista_posts, nombre_autor):
    """
    Crea una nueva lista que contiene solo los posts de un autor específico.
    """
    # 1. Creamos una lista vacía para guardar los resultados.
    posts_filtrados = []

    # 2. Recorremos cada post en la lista original.
    for post in lista_posts:
        # 3. Verificamos si el valor de la clave 'autor' en el post actual
        #    es igual al nombre del autor que estamos buscando.
        if post['autor'] == nombre_autor:
            # 4. Si coincide, agregamos el post completo a nuestra lista de resultados.
            posts_filtrados.append(post)

    # 5. Devolvemos la nueva lista que solo contiene los posts del autor.
    return posts_filtrados

# --- Pruebas ---
def probar_filtrar_posts_por_autor():
    posts = [
        {'autor': 'ana_dev', 'contenido': '¡Aprendiendo Python!', 'likes': 50},
        {'autor': 'beto_data', 'contenido': 'Mi primer análisis de datos.', 'likes': 120},
        {'autor': 'ana_dev', 'contenido': 'Funciones Lambda son geniales.', 'likes': 95}
    ]

    posts_de_ana = filtrar_posts_por_autor(posts, 'ana_dev')
    esperado1 = [
        {'autor': 'ana_dev', 'contenido': '¡Aprendiendo Python!', 'likes': 50},
        {'autor': 'ana_dev', 'contenido': 'Funciones Lambda son geniales.', 'likes': 95}
    ]
    print(f"Prueba 1: {posts_de_ana == esperado1}")

    posts_de_carlos = filtrar_posts_por_autor(posts, 'carlos_design')
    print(f"Prueba 2: {posts_de_carlos == []}")

    posts_vacios = filtrar_posts_por_autor([], 'ana_dev')
    print(f"Prueba 3: {posts_vacios == []}")

probar_filtrar_posts_por_autor()