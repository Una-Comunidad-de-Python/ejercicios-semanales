def contar_palabras(texto):
    
    conteo = {}
        
    # con split() separamos el texto en palabras
    for palabra in texto.split():
        # con strip() eliminamos caracteres no deseados para solo contar palabras
        palabra = palabra.lower().strip('.,!?;:"()[]{}')
        # contamos las palabras
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo


# --- Pruebas para verificar que la función funciona correctamente ---

def probar_contar_palabras():
    texto1 = "Hola mundo, hola. Mundo!"
    resultado1 = contar_palabras(texto1)
    print(f"Prueba 1: {resultado1 == {'hola': 2, 'mundo': 2}}")

    texto2 = "Python es genial. Genial es Python."
    resultado2 = contar_palabras(texto2)
    print(f"Prueba 2: {resultado2 == {'python': 2, 'es': 2, 'genial': 2}}")

    texto3 = ""
    resultado3 = contar_palabras(texto3)
    print(f"Prueba 3: {resultado3 == {}}")

probar_contar_palabras()