class Desconto:
    
    # 1. Construtor: Armazena nome e preço no objeto
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    # 2. Método: Calcula 10% do preço do objeto
    def calcular_desconto(self):
        return self.preco * 0.1
        
    # 3. Método: Retorna o preço final após o desconto (Bônus!)
    def preco_final(self):
        return self.preco - self.calcular_desconto()

# ----------------------------------------------------
# Exemplo de uso:

# 1. Instanciar (criar) um objeto
produto = Desconto("Livro de Python", 100.00)

# 2. Acessar os atributos
print(f"Produto: {produto.nome}")
print(f"Preço original: R$ {produto.preco:.2f}")

# 3. Chamar o método para calcular o desconto
valor_desconto = produto.calcular_desconto()
print(f"Valor do Desconto: R$ {valor_desconto:.2f}") # Deve ser R$ 10.00

# 4. Chamar o método para obter o preço final
print(f"Preço Final: R$ {produto.preco_final():.2f}") # Deve ser R$ 90.00