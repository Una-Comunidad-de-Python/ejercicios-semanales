def vender_entrada(sesiones, titulo_pelicula, horario, cantidad_entradas):
    """
    Vende una cantidad de entradas para una sesión específica si hay asientos disponibles.
    """
    # 1. Verificamos si la película existe en nuestro diccionario de sesiones.
    if titulo_pelicula in sesiones:
        sesiones_de_la_pelicula = sesiones[titulo_pelicula]
        
        # 2. Si la película existe, verificamos si el horario específico está disponible.
        if horario in sesiones_de_la_pelicula:
            asientos_disponibles = sesiones_de_la_pelicula[horario]
            
            # 3. Si el horario existe, verificamos si hay suficientes asientos.
            if asientos_disponibles >= cantidad_entradas:
                # 4. Si todas las comprobaciones son exitosas, restamos las entradas vendidas.
                sesiones_de_la_pelicula[horario] -= cantidad_entradas
                return True  # La venta fue un éxito.

    # 5. Si cualquiera de las comprobaciones anteriores falla, la función llega a este punto.
    #    No se modifica nada y se devuelve False para indicar que la venta no se pudo realizar.
    return False

# --- Pruebas ---
def probar_vender_entrada():
    sesiones_base = {
        'Inception': {'18:00': 10, '21:00': 5},
        'The Matrix': {'17:30': 25, '20:30': 1}
    }

    sesiones_p1 = {k: v.copy() for k, v in sesiones_base.items()}
    resultado1 = vender_entrada(sesiones_p1, 'Inception', '18:00', 3)
    print(f"Prueba 1 (Venta exitosa): {resultado1 is True and sesiones_p1['Inception']['18:00'] == 7}")

    sesiones_p2 = {k: v.copy() for k, v in sesiones_base.items()}
    resultado2 = vender_entrada(sesiones_p2, 'The Matrix', '20:30', 2)
    print(f"Prueba 2 (Falta de asientos): {resultado2 is False and sesiones_p2['The Matrix']['20:30'] == 1}")

    sesiones_p3 = {k: v.copy() for k, v in sesiones_base.items()}
    resultado3 = vender_entrada(sesiones_p3, 'Inception', '19:00', 1)
    print(f"Prueba 3 (Horario no existe): {resultado3 is False}")

probar_vender_entrada()