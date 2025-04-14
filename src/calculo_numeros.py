from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    """Función para solicitar un número y validarlo."""
    try:
        numero = input("Ingrese un número: ")
        numero = float(numero)  
        if numero < 0:
            raise NumeroDebeSerPositivo 
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")
