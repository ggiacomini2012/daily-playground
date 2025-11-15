
## 1\. Em Python

### A Função Simples (`soma.py`)

```python
# soma.py

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b
```

### Esqueleto do Teste Unitário (`test_soma.py`)

Em Python, usamos geralmente o módulo embutido **`unittest`** ou bibliotecas externas como o `pytest`. Usaremos o `unittest` para este esqueleto.

```python
# test_soma.py

import unittest
from soma import soma  # Importa a função do arquivo 'soma.py'

class TestSoma(unittest.TestCase):
    """Classe de testes para a função soma."""

    def test_soma_positivos(self):
        """Verifica se a soma de 2 e 3 é 5."""
        
        # 1. Arrange (Preparação): Define os valores de entrada e a saída esperada
        a = 2
        b = 3
        esperado = 5
        
        # 2. Act (Ação): Executa a função a ser testada
        resultado = soma(a, b)
        
        # 3. Assert (Verificação): Compara o resultado com o valor esperado
        self.assertEqual(resultado, esperado, "A soma de 2 + 3 deveria ser 5")
        
    # Você adicionaria outros métodos de teste aqui, como test_soma_negativos, etc.
    
if __name__ == '__main__':
    unittest.main()
```

-----

## 2\. Em JavaScript

### A Função Simples (`soma.js`)

```javascript
// soma.js

/**
 * Retorna a soma de dois números.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
export const soma = (a, b) => {
    return a + b;
};
```

### Esqueleto do Teste Unitário (`soma.test.js`)

Em JavaScript, a maioria dos projetos usa *frameworks* como **Jest** ou **Mocha/Chai**. Usaremos a sintaxe limpa e popular do **Jest** para este esqueleto.

```javascript
// soma.test.js

import { soma } from './soma.js'; // Importa a função do arquivo 'soma.js'

describe('Teste da função soma', () => {
    
    test('deve retornar 5 ao somar 2 e 3', () => {
        
        // 1. Arrange (Preparação): Define os valores de entrada e a saída esperada
        const a = 2;
        const b = 3;
        const esperado = 5;
        
        // 2. Act (Ação): Executa a função a ser testada
        const resultado = soma(a, b);
        
        // 3. Assert (Verificação): Compara o resultado com o valor esperado
        expect(resultado).toBe(esperado); // Jest compara o valor real (resultado) com o esperado
    });
    
    // Você adicionaria outros testes aqui, como 'test('deve somar números negativos...', ...)'
});
```