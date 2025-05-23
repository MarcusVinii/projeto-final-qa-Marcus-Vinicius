# ==================== IMPLEMENTAÇÃO ====================
class Biblioteca:
    """Classe para gerenciamento de acervo bibliotecário"""
    
    def __init__(self):
        self.acervo = []
        self.emprestimos = []
    
    def adicionar_livro(self, titulo, autor, isbn):
        """
        Adiciona um novo livro ao acervo
        Levanta ValueError se ISBN já existir
        """
        if any(livro['isbn'] == isbn for livro in self.acervo):
            raise ValueError("ISBN já cadastrado")
            
        livro = {
            'titulo': titulo,
            'autor': autor,
            'isbn': isbn,
            'disponivel': True
        }
        self.acervo.append(livro)
        return livro
    
    def buscar_livro(self, termo):
        """
        Busca livros por título, autor ou ISBN
        Retorna lista vazia se não encontrar
        """
        termo = termo.lower()
        return [livro for livro in self.acervo 
                if termo in livro['titulo'].lower() 
                or termo in livro['autor'].lower()
                or termo == livro['isbn'].lower()]
    
    def emprestar_livro(self, isbn):
        """
        Realiza empréstimo de livro se disponível
        Retorna o livro emprestado ou None se indisponível
        """
        for livro in self.acervo:
            if livro['isbn'] == isbn:
                if livro['disponivel']:
                    livro['disponivel'] = False
                    self.emprestimos.append(livro)
                    return livro
                return None
        raise ValueError("Livro não encontrado")
    
    def devolver_livro(self, isbn):
        """
        Registra devolução de livro
        Retorna o livro devolvido
        """
        for livro in self.acervo:
            if livro['isbn'] == isbn:
                if not livro['disponivel']:
                    livro['disponivel'] = True
                    self.emprestimos.remove(livro)
                    return livro
                raise ValueError("Livro já está disponível")
        raise ValueError("Livro não encontrado")
    
    def livros_disponiveis(self):
        """Retorna lista de livros disponíveis para empréstimo"""
        return [livro for livro in self.acervo if livro['disponivel']]


# ==================== TESTES UNITÁRIOS ====================
import unittest

class TestBiblioteca(unittest.TestCase):
    """Classe de testes para o Sistema de Biblioteca"""
    
    def setUp(self):
        """Prepara ambiente de teste antes de cada método"""
        self.bib = Biblioteca()
        self.livro1 = self.bib.adicionar_livro(
            "Python Fluente", "Luciano Ramalho", "978-85-7522-563-8"
        )
        self.livro2 = self.bib.adicionar_livro(
            "Clean Code", "Robert Martin", "978-85-7452-258-1"
        )
    
    def test_adicionar_livro(self):
        """Testes para adição de livros"""
        # Adição válida
        novo_livro = self.bib.adicionar_livro(
            "Domain-Driven Design", "Eric Evans", "978-85-5519-021-7"
        )
        self.assertEqual(novo_livro['titulo'], "Domain-Driven Design")
        
        # ISBN duplicado
        with self.assertRaises(ValueError):
            self.bib.adicionar_livro(
                "Outro Livro", "Autor", "978-85-7522-563-8"
            )
    
    def test_buscar_livro(self):
        """Testes para busca de livros"""
        # Busca por título
        resultados = self.bib.buscar_livro("Python")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]['isbn'], "978-85-7522-563-8")
        
        # Busca por autor
        resultados = self.bib.buscar_livro("Martin")
        self.assertEqual(len(resultados), 1)
        
        # Busca por ISBN
        resultados = self.bib.buscar_livro("978-85-7452-258-1")
        self.assertEqual(len(resultados), 1)
        
        # Busca sem resultados
        self.assertEqual(len(self.bib.buscar_livro("inexistente")), 0)
    
    def test_emprestar_devolver_livro(self):
        """Testes para empréstimo e devolução"""
        # Empréstimo válido
        livro_emprestado = self.bib.emprestar_livro("978-85-7522-563-8")
        self.assertIsNotNone(livro_emprestado)
        self.assertFalse(livro_emprestado['disponivel'])
        
        # Tentar emprestar livro indisponível
        self.assertIsNone(self.bib.emprestar_livro("978-85-7522-563-8"))
        
        # Devolução válida
        livro_devolvido = self.bib.devolver_livro("978-85-7522-563-8")
        self.assertTrue(livro_devolvido['disponivel'])
        
        # Tentar devolver livro disponível
        with self.assertRaises(ValueError):
            self.bib.devolver_livro("978-85-7522-563-8")
        
        # Tentar emprestar/devolver livro inexistente
        with self.assertRaises(ValueError):
            self.bib.emprestar_livro("000-00-0000-000-0")
        with self.assertRaises(ValueError):
            self.bib.devolver_livro("000-00-0000-000-0")
    
    def test_livros_disponiveis(self):
        """Testes para listagem de livros disponíveis"""
        # Todos disponíveis inicialmente
        self.assertEqual(len(self.bib.livros_disponiveis()), 2)
        
        # Após empréstimo
        self.bib.emprestar_livro("978-85-7522-563-8")
        self.assertEqual(len(self.bib.livros_disponiveis()), 1)
        
        # Após devolução
        self.bib.devolver_livro("978-85-7522-563-8")
        self.assertEqual(len(self.bib.livros_disponiveis()), 2)


# ==================== EXECUÇÃO ====================
if __name__ == '__main__':
    # Configuração para o Colab
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestBiblioteca)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)
    
    # Demonstração das funcionalidades
    print("\n" + "="*50)
    print("Demonstração do Sistema de Biblioteca:")
    demo = Biblioteca()
    
    # Adicionar livros
    l1 = demo.adicionar_livro("Arquitetura Limpa", "Robert Martin", "978-85-508-0460-6")
    l2 = demo.adicionar_livro("Código Sustentável", "David Thomas", "978-85-5519-019-4")
    
    print(f"Total de livros: {len(demo.acervo)}")
    print(f"Busca por 'Robert': {len(demo.buscar_livro('Robert'))} resultado(s)")
    
    # Empréstimo
    demo.emprestar_livro("978-85-508-0460-6")
    print(f"Livros disponíveis: {len(demo.livros_disponiveis())}")
    
    # Devolução
    demo.devolver_livro("978-85-508-0460-6")
    print(f"Livros disponíveis após devolução: {len(demo.livros_disponiveis())}")
    print("="*50)
