## Definição da Classe Base (Superclasse)

class Animal:
    """
    Classe base que representa um animal genérico.
    """
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitirSom(self):
        """
        Método padrão para o som do animal.
        Será sobrescrito nas classes filhas.
        """
        # Note que este método não é implementado completamente aqui (poderia ser uma exceção)
        # mas definimos o comportamento padrão esperado de um animal.
        return f"{self.nome} da espécie {self.especie} faz um som genérico."

    def descrever(self):
        """
        Método para descrever o animal.
        """
        return f"Nome: {self.nome}, Espécie: {self.especie}"


## Definição da Classe Filha (Subclasse)

class Cachorro(Animal):
    """
    Classe que herda de Animal e representa um cachorro.
    """
    def __init__(self, nome, raca):
        # Chama o construtor da classe pai (Animal)
        # Usamos 'Cachorro' como a espécie padrão
        super().__init__(nome, especie="Cachorro") 
        self.raca = raca

    def emitirSom(self):
        """
        SOBRESCRITA do método emitirSom da classe Animal.
        Define um som específico para o cachorro.
        """
        return f"O cachorro {self.nome} (raça {self.raca}) diz: AU! AU!"

    def brincar(self):
        """
        Método exclusivo da classe Cachorro.
        """
        return f"{self.nome} está abanando o rabo e querendo brincar."


# 1. Objeto da Classe Base
animal_generico = Animal("Bicho", "Desconhecida")
print("--- Animal Genérico ---")
print(animal_generico.descrever())
print(animal_generico.emitirSom())
# Saída: O Bicho da espécie Desconhecida faz um som genérico.

print("\n--- Cachorro ---")
# 2. Objeto da Classe Filha
meu_cachorro = Cachorro("Max", "Golden Retriever")
print(meu_cachorro.descrever()) 
# Note que herdou o método descrever() e a espécie "Cachorro"

# Chama o método SOBRESCRITO da classe Cachorro
print(meu_cachorro.emitirSom()) 
# Saída: O cachorro Max (raça Golden Retriever) diz: AU! AU!

# Chama um método exclusivo
print(meu_cachorro.brincar())