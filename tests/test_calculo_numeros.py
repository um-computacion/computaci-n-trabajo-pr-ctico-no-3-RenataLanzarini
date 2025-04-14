import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_numero_positivo(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='1')
    def test_ingreso_numero_positivo_minimo(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 1)
   

if __name__ == '__main__':
    unittest.main() 