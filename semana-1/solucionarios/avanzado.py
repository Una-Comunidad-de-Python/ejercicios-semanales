import re

def extraer_emails(texto):
    patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(patron_email, texto)
    return emails


def probar_extraer_emails():
    texto1 = "Mi correo es usuario@dominio.com y otro es prueba@subdominio.dominio.net"
    resultado1 = extraer_emails(texto1)
    print(f"Prueba 1: {resultado1 == ['usuario@dominio.com', 'prueba@subdominio.dominio.net']}")

    texto2 = "No hay correos aquí."
    resultado2 = extraer_emails(texto2)
    print(f"Prueba 2: {resultado2 == []}")

    texto3 = "Correo inválido: @dominio.com, otro: usuario@dominio."
    resultado3 = extraer_emails(texto3)
    print(f"Prueba 3: {resultado3 == []}") # Ninguno válido

probar_extraer_emails()