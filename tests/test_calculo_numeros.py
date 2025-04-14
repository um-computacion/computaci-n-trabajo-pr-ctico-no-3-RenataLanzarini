import unittest

from unittest.mock import patch
from src.exceptions import NumeroDebeSerPositivo
from src.calculo_numeros import ingrese_numero

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
class TestIngresoTextoNoNumerico(unittest.TestCase):
    @patch('builtins.input', return_value='abc')
    def test_ingreso_letras(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='10abc')
    def test_ingreso_numero_con_letras(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='@#$')
    def test_ingreso_simbolos(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()


if __name__ == '__main__':
    unittest.main() 