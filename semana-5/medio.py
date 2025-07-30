from facil import buscar_libro_por_titulo

def gestionar_prestamo(catalogo, titulo, accion):
    """
    Gestiona el préstamo o devolución de un libro, actualizando su estado.
    """
    # 1. Recorremos el catálogo para encontrar el libro por su título.
    for libro in catalogo:
        if libro['titulo'] == titulo:
            # --- Libro encontrado. Ahora procesamos la acción ---

            # 2. Si la acción es "prestar"...
            if accion == "prestar":
                # ...verificamos si está disponible.
                if libro['disponible']:
                    # Si lo está, lo marcamos como no disponible y devolvemos True.
                    libro['disponible'] = False
                    return True
                else:
                    # Si no está disponible, no se puede prestar. Devolvemos False.
                    return False

            # 3. Si la acción es "devolver"...
            elif accion == "devolver":
                # ...verificamos si NO está disponible (es decir, está prestado).
                if not libro['disponible']:
                    # Si está prestado, lo marcamos como disponible y devolvemos True.
                    libro['disponible'] = True
                    return True
                else:
                    # Si ya está disponible, no se puede devolver. Devolvemos False.
                    return False

    # 4. Si el bucle termina, el libro no se encontró en el catálogo. Devolvemos False.
    return False

# --- Pruebas ---
# (Se necesita la función buscar_libro_por_titulo para las pruebas)
def probar_gestionar_prestamo():
    catalogo_base = [
        {'titulo': 'Cien Años de Soledad', 'autor': 'G.G. Márquez', 'disponible': True},
        {'titulo': 'El Señor de los Anillos', 'autor': 'J.R.R. Tolkien', 'disponible': False}
    ]

    catalogo_p1 = [libro.copy() for libro in catalogo_base]
    resultado1 = gestionar_prestamo(catalogo_p1, 'Cien Años de Soledad', 'prestar')
    libro_actualizado1 = buscar_libro_por_titulo(catalogo_p1, 'Cien Años de Soledad')
    print(f"Prueba 1 (Prestar éxito): {resultado1 is True and not libro_actualizado1['disponible']}")

    catalogo_p2 = [libro.copy() for libro in catalogo_base]
    resultado2 = gestionar_prestamo(catalogo_p2, 'El Señor de los Anillos', 'prestar')
    print(f"Prueba 2 (Prestar fallo): {resultado2 is False}")

    catalogo_p3 = [libro.copy() for libro in catalogo_base]
    resultado3 = gestionar_prestamo(catalogo_p3, 'El Señor de los Anillos', 'devolver')
    libro_actualizado3 = buscar_libro_por_titulo(catalogo_p3, 'El Señor de los Anillos')
    print(f"Prueba 3 (Devolver éxito): {resultado3 is True and libro_actualizado3['disponible']}")

probar_gestionar_prestamo()