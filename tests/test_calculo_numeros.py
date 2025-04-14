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


class TestIngresoNumerosNegativos(unittest.TestCase):
    @patch('builtins.input', return_value='-1')
    def test_numero_negativo_simple(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-999')
    def test_numero_negativo_grande(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()



if __name__ == '__main__':
    unittest.main() 