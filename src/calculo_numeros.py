from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    """Función para solicitar un número y validarlo."""
    try:
        numero = input("Ingrese un número: ")
        numero = float(numero)  
        if numero < 0:
            raise NumeroDebeSerPositivo()
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")

if __name__ == "__main__":
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        