
## Teste de Unidade para a Função de Soma

### 1. Código da Função (A ser testada)

Primeiro, definimos a função que queremos testar. Salve-a como `matematica.py`:

**Python**

```
# matematica.py

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b
```

---

### 2. Código do Teste de Unidade

Em seguida, criamos o teste de unidade para verificar se essa função se comporta conforme o esperado. Salve o código abaixo como `test_matematica.py`:

**Python**

```
# test_matematica.py
import unittest
from matematica import somar # Importa a função do arquivo anterior

class TestSoma(unittest.TestCase):
    """Classe que contém todos os testes para a função somar."""

    def test_soma_positivos(self):
        """Testa a soma de dois números positivos."""
        resultado_esperado = 5
        resultado_obtido = somar(2, 3)
        # O Assert: Verifica se o resultado obtido é IGUAL ao esperado
        self.assertEqual(resultado_obtido, resultado_esperado)

    def test_soma_negativos(self):
        """Testa a soma de dois números negativos."""
        resultado_esperado = -10
        resultado_obtido = somar(-3, -7)
        # O Assert: Verifica se o resultado obtido é IGUAL ao esperado
        self.assertEqual(resultado_obtido, resultado_esperado)

    def test_soma_zero(self):
        """Testa a soma com zero."""
        self.assertEqual(somar(5, 0), 5) # Assert direto

# Se o arquivo for executado diretamente, roda os testes
if __name__ == '__main__':
    unittest.main()
```

---

## Estrutura do `assert` e Por Que o Teste é Importante

### O Comando `assert`

O coração de qualquer teste de unidade é a chamada  **`assert`** .

* No exemplo, usamos self.assertEqual(a, b). Este é um método de asserção (afirmação) que verifica:
  ![](data:,)

Outros comandos `assert` comuns incluem:

| Método `assert`          | Descrição                                         |
| --------------------------- | --------------------------------------------------- |
| `assertEqual(a, b)`       | Verifica se `a == b`                              |
| `assertTrue(x)`           | Verifica se a condição `x`é Verdadeira         |
| `assertFalse(x)`          | Verifica se a condição `x`é Falsa              |
| `assertIsNone(x)`         | Verifica se `x`é `None`                        |
| `assertRaises(Exception)` | Verifica se uma exceção específica foi levantada |

### Por Que Isso é um "Teste de Unidade"

Um **Teste de Unidade** tem como objetivo testar a **menor parte isolável** do seu código—neste caso, a função `somar()`.

1. **Isolamento:** Ele testa a função `somar` **sem** depender de banco de dados, arquivos ou da internet.
2. **Verificação:** Ele **afirma** (com `assertEqual`) que, para uma entrada conhecida (2 e 3), a saída deve ser uma saída específica e conhecida (5).

Se, no futuro, alguém alterar a função `somar` acidentalmente para subtrair, o teste  **falhará instantaneamente** , alertando o desenvolvedor sobre a regressão (erro).
