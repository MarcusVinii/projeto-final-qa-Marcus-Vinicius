# ==================== IMPLEMENTAÇÃO ====================
class Calculadora:
    """Classe com operações matemáticas básicas"""
    
    @staticmethod
    def somar(a, b):
        """Retorna a soma de dois números"""
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        """Retorna a subtração de dois números"""
        return a - b
    
    @staticmethod
    def eh_par(numero):
        """Verifica se um número é par"""
        return numero % 2 == 0
    
    @staticmethod
    def dividir(a, b):
        """
        Retorna a divisão de dois números
        Levanta ValueError se divisor for zero
        """
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b


# ==================== TESTES UNITÁRIOS ====================
import unittest

class TestCalculadora(unittest.TestCase):
    """Classe de testes para a Calculadora"""
    
    def test_somar(self):
        """Testes para o método somar"""
        # Casos positivos
        self.assertEqual(Calculadora.somar(2, 3), 5)
        self.assertEqual(Calculadora.somar(-1, 1), 0)
        self.assertEqual(Calculadora.somar(0, 0), 0)
        
        # Casos com decimais
        self.assertAlmostEqual(Calculadora.somar(1.5, 2.5), 4.0)
    
    def test_subtrair(self):
        """Testes para o método subtrair"""
        self.assertEqual(Calculadora.subtrair(5, 3), 2)
        self.assertEqual(Calculadora.subtrair(10, 10), 0)
        self.assertEqual(Calculadora.subtrair(3, 5), -2)
    
    def test_eh_par(self):
        """Testes para o método eh_par"""
        # Números pares
        self.assertTrue(Calculadora.eh_par(2))
        self.assertTrue(Calculadora.eh_par(0))
        self.assertTrue(Calculadora.eh_par(-4))
        
        # Números ímpares
        self.assertFalse(Calculadora.eh_par(3))
        self.assertFalse(Calculadora.eh_par(-1))
    
    def test_dividir(self):
        """Testes para o método dividir"""
        # Casos normais
        self.assertEqual(Calculadora.dividir(10, 2), 5)
        self.assertEqual(Calculadora.dividir(1, 2), 0.5)
        
        # Divisão por zero
        with self.assertRaises(ValueError):
            Calculadora.dividir(5, 0)


# ==================== EXECUÇÃO ====================
if __name__ == '__main__':
    # Configuração para o Colab
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    
    # Demonstração das funções
    print("\n" + "="*50)
    print("Demonstração das Funções:")
    print(f"Soma: 2 + 3 = {Calculadora.somar(2, 3)}")
    print(f"Subtração: 5 - 3 = {Calculadora.subtrair(5, 3)}")
    print(f"É par? 10 → {Calculadora.eh_par(10)}")
    print(f"Divisão: 10 / 2 = {Calculadora.dividir(10, 2)}")
    print("="*50)
