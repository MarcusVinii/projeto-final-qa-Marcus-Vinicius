# ==================== IMPLEMENTAÇÃO ====================
class GerenciadorUsuarios:
    """Classe para gerenciamento de usuários"""
    
    def __init__(self):
        self.usuarios = []
    
    def cadastrar_usuario(self, nome, email, idade):
        """
        Cadastra um novo usuário
        Levanta ValueError se email já existir ou idade for inválida
        """
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade deve ser um número positivo")
            
        if any(u['email'] == email for u in self.usuarios):
            raise ValueError("Email já cadastrado")
            
        usuario = {
            'nome': nome,
            'email': email,
            'idade': idade
        }
        self.usuarios.append(usuario)
        return usuario
    
    def buscar_usuario(self, email):
        """Busca usuário por email, retorna None se não encontrado"""
        for usuario in self.usuarios:
            if usuario['email'] == email:
                return usuario
        return None
    
    def usuarios_maiores_de(self, idade_minima):
        """Retorna lista de usuários com idade maior ou igual à especificada"""
        return [u for u in self.usuarios if u['idade'] >= idade_minima]
    
    def total_usuarios(self):
        """Retorna o total de usuários cadastrados"""
        return len(self.usuarios)


# ==================== TESTES UNITÁRIOS ====================
import unittest

class TestGerenciadorUsuarios(unittest.TestCase):
    """Classe de testes para o Gerenciador de Usuários"""
    
    def setUp(self):
        """Prepara ambiente de teste antes de cada método"""
        self.gerenciador = GerenciadorUsuarios()
        self.usuario_teste = self.gerenciador.cadastrar_usuario(
            "João Silva", "joao@email.com", 25
        )
    
    def test_cadastrar_usuario(self):
        """Testes para cadastro de usuário"""
        # Cadastro válido
        usuario = self.gerenciador.cadastrar_usuario(
            "Maria Souza", "maria@email.com", 30
        )
        self.assertEqual(usuario['nome'], "Maria Souza")
        
        # Email duplicado
        with self.assertRaises(ValueError):
            self.gerenciador.cadastrar_usuario(
                "Outro João", "joao@email.com", 40
            )
        
        # Idade inválida
        with self.assertRaises(ValueError):
            self.gerenciador.cadastrar_usuario(
                "Erro Idade", "erro@email.com", -5
            )
    
    def test_buscar_usuario(self):
        """Testes para busca de usuário"""
        # Usuário existente
        encontrado = self.gerenciador.buscar_usuario("joao@email.com")
        self.assertEqual(encontrado['nome'], "João Silva")
        
        # Usuário não existente
        self.assertIsNone(self.gerenciador.buscar_usuario("inexistente@email.com"))
    
    def test_usuarios_maiores_de(self):
        """Testes para filtro por idade"""
        self.gerenciador.cadastrar_usuario("Jovem", "jovem@email.com", 17)
        self.gerenciador.cadastrar_usuario("Adulto", "adulto@email.com", 30)
        
        maiores = self.gerenciador.usuarios_maiores_de(18)
        self.assertEqual(len(maiores), 2)  # João (25) + Adulto (30)
        
        maiores_30 = self.gerenciador.usuarios_maiores_de(30)
        self.assertEqual(len(maiores_30), 1)
    
    def test_total_usuarios(self):
        """Testes para contagem de usuários"""
        self.assertEqual(self.gerenciador.total_usuarios(), 1)
        
        self.gerenciador.cadastrar_usuario("Novo", "novo@email.com", 40)
        self.assertEqual(self.gerenciador.total_usuarios(), 2)


# ==================== EXECUÇÃO ====================
if __name__ == '__main__':
    # Configuração para o Colab
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGerenciadorUsuarios)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)
    
    # Demonstração das funcionalidades
    print("\n" + "="*50)
    print("Demonstração do Sistema:")
    demo = GerenciadorUsuarios()
    
    # Cadastro
    u1 = demo.cadastrar_usuario("Ana Costa", "ana@email.com", 28)
    u2 = demo.cadastrar_usuario("Pedro Alves", "pedro@email.com", 35)
    
    print(f"Total de usuários: {demo.total_usuarios()}")
    print(f"Usuário encontrado: {demo.buscar_usuario('ana@email.com')['nome']}")
    print(f"Maiores de 30: {len(demo.usuarios_maiores_de(30))} usuário(s)")
    print("="*50)
