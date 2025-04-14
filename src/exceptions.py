class NumeroDebeSerPositivo(Exception):
    """Excepción personalizada para números negativos."""
    def __init__(self, message="El número debe ser positivo"):
        self.message = message
        super().__init__(self.message)
