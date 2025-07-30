def encontrar_post_con_mas_likes(lista_posts):
    """
    Encuentra y devuelve el post con el mayor número de likes.
    """
    # 1. Primero, manejamos el caso de que la lista esté vacía.
    if not lista_posts:
        return None

    # 2. Asumimos que el primer post de la lista es el que tiene más likes.
    #    Guardamos el post completo y también su número de likes.
    post_mas_popular = lista_posts[0]
    max_likes = lista_posts[0]['likes']

    # 3. Recorremos el resto de la lista (empezando desde el segundo elemento).
    for post in lista_posts[1:]:
        # 4. Si los likes del post actual son mayores que nuestro máximo guardado...
        if post['likes'] > max_likes:
            # ...actualizamos nuestro máximo y guardamos este nuevo post como el más popular.
            max_likes = post['likes']
            post_mas_popular = post

    # 5. Después de revisar todos los posts, devolvemos el que resultó ser el más popular.
    return post_mas_popular

# --- Pruebas ---
def probar_encontrar_post_con_mas_likes():
    posts = [
        {'autor': 'ana_dev', 'contenido': '¡Python es divertido!', 'likes': 50},
        {'autor': 'beto_data', 'contenido': 'Análisis con Pandas.', 'likes': 150},
        {'autor': 'ana_dev', 'contenido': 'Creando una API.', 'likes': 200}
    ]

    top_post = encontrar_post_con_mas_likes(posts)
    esperado1 = {'autor': 'ana_dev', 'contenido': 'Creando una API.', 'likes': 200}
    print(f"Prueba 1: {top_post == esperado1}")

    top_post_vacio = encontrar_post_con_mas_likes([])
    print(f"Prueba 2: {top_post_vacio is None}")

    posts_empate = [
        {'autor': 'ana_dev', 'contenido': 'Post 1', 'likes': 300},
        {'autor': 'beto_data', 'contenido': 'Post 2', 'likes': 100},
        {'autor': 'ana_dev', 'contenido': 'Post 3', 'likes': 300}
    ]
    top_post_empate = encontrar_post_con_mas_likes(posts_empate)
    es_valido = top_post_empate in [posts_empate[0], posts_empate[2]]
    print(f"Prueba 3 (empate): {es_valido}")

probar_encontrar_post_con_mas_likes()