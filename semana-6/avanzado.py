def generar_reporte_taquilla(cartelera_completa):
    """
    Calcula los ingresos totales por película y devuelve un ranking ordenado.
    """
    # 1. Creamos una lista para almacenar los resultados (título e ingresos).
    lista_ingresos = []

    # 2. Recorremos cada película en la cartelera.
    for pelicula in cartelera_completa:
        titulo = pelicula['titulo']
        precio_entrada = pelicula['precio_entrada']
        ingresos_pelicula = 0.0

        # 3. Por cada película, recorremos sus diferentes sesiones.
        #    Usamos .values() porque solo nos interesan los datos de la sesión (asientos), no la hora (clave).
        for sesion in pelicula['sesiones'].values():
            entradas_vendidas = sesion['vendidas']
            # 4. Calculamos los ingresos de esta sesión y los sumamos al total de la película.
            ingresos_pelicula += entradas_vendidas * precio_entrada

        # 5. Añadimos una tupla con el título y el total de ingresos a nuestra lista.
        lista_ingresos.append((titulo, ingresos_pelicula))
        
    # 6. Ordenamos la lista de ingresos.
    #    - key=lambda item: item[1] le dice que ordene usando el segundo elemento de la tupla (los ingresos).
    #    - reverse=True ordena de mayor a menor.
    reporte_ordenado = sorted(lista_ingresos, key=lambda item: item[1], reverse=True)

    # 7. Devolvemos el reporte final ordenado.
    return reporte_ordenado

# --- Pruebas ---
def probar_generar_reporte_taquilla():
    cartelera = [
        {'titulo': 'Oppenheimer', 'precio_entrada': 12.50, 'sesiones': {'19:00': {'vendidas': 80}, '22:00': {'vendidas': 90}}},
        {'titulo': 'Barbie', 'precio_entrada': 10.00, 'sesiones': {'18:30': {'vendidas': 110}, '21:30': {'vendidas': 115}}},
        {'titulo': 'Gran Turismo', 'precio_entrada': 11.00, 'sesiones': {'20:00': {'vendidas': 40}}}
    ]

    reporte = generar_reporte_taquilla(cartelera)
    esperado1 = [
        ('Barbie', 2250.0),
        ('Oppenheimer', 2125.0),
        ('Gran Turismo', 440.0)
    ]
    print(f"Prueba 1: {reporte == esperado1}")

    reporte2 = generar_reporte_taquilla([])
    print(f"Prueba 2: {reporte2 == []}")

probar_generar_reporte_taquilla()