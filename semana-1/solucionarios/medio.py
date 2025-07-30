def analizar_sentimiento(texto, positivas, negativas):
    texto = texto.lower()
    palabras = texto.split()
    conteo_positivo = 0
    conteo_negativo = 0

    for palabra in palabras:
        if palabra in positivas:
            conteo_positivo += 1
        elif palabra in negativas:
            conteo_negativo += 1

    if conteo_positivo > conteo_negativo:
        return "positivo"
    elif conteo_negativo > conteo_positivo:
        return "negativo"
    else:
        return "neutral"


def probar_analizar_sentimiento():
    positivas = ["excelente", "fantástico", "bueno"]
    negativas = ["malo", "terrible", "pésimo"]

    texto1 = "Este producto es excelente y fantástico."
    resultado1 = analizar_sentimiento(texto1, positivas, negativas)
    print(f"Prueba 1: {resultado1 == 'positivo'}")

    texto2 = "El servicio es malo y pésimo."
    resultado2 = analizar_sentimiento(texto2, positivas, negativas)
    print(f"Prueba 2: {resultado2 == 'negativo'}")

    texto3 = "El producto es bueno, pero también malo."
    resultado3 = analizar_sentimiento(texto3, positivas, negativas)
    print(f"Prueba 3: {resultado3 == 'neutral'}")

probar_analizar_sentimiento()