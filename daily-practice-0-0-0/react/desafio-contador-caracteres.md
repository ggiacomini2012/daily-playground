# Desafio Rápido de React: Contador de Caracteres

**Objetivo:** Criar um componente que exibe a contagem de caracteres em tempo real de uma área de texto (`<textarea>`).

**Tempo Estimado:** 5-7 minutos

**Conceitos Praticados:**
*   Componentes Funcionais
*   State (`useState`)
*   Event Handlers (`onChange`)

---

### Passo a Passo

#### 1. Estrutura Inicial

Comece com este código base em seu arquivo de componente (por exemplo, `App.js` ou `CharacterCounter.js`). Ele já possui a estrutura visual.

```jsx
import React from 'react';

function CharacterCounter() {
  return (
    <div>
      <h2>Contador de Caracteres</h2>
      <textarea
        placeholder="Digite algo..."
        rows="5"
        style={{ width: '300px', padding: '10px' }}
      />
      <p>Contagem: 0</p>
    </div>
  );
}

export default CharacterCounter;
```

#### 2. Crie o Estado para o Texto

Precisamos de um lugar para guardar o texto que o usuário digita. Use o hook `useState` para isso.

*   Importe `useState` de `'react'`.
*   Crie um estado chamado `text` com o valor inicial `''` (uma string vazia).

```jsx
import React, { useState } from 'react'; // Importe o useState

function CharacterCounter() {
  const [text, setText] = useState(''); // Crie o estado

  return (
    // ... resto do JSX
  );
}
```

#### 3. Conecte o Estado ao `<textarea>`

Agora, vamos fazer duas coisas:
1.  O valor do `<textarea>` deve ser o do nosso estado `text`.
2.  Quando o usuário digitar, devemos atualizar o estado.

*   Adicione a prop `value` ao `<textarea>`.
*   Crie uma função `handleChange` que recebe o evento (`e`) e chama `setText(e.target.value)`.
*   Passe essa função para a prop `onChange` do `<textarea>`.

```jsx
// ...
const [text, setText] = useState('');

const handleChange = (e) => {
  setText(e.target.value);
};

return (
  <div>
    <h2>Contador de Caracteres</h2>
    <textarea
      placeholder="Digite algo..."
      rows="5"
      style={{ width: '300px', padding: '10px' }}
      value={text} // Conecte o valor
      onChange={handleChange} // Conecte o evento
    />
    <p>Contagem: 0</p>
  </div>
);
// ...
```

#### 4. Exiba a Contagem Dinamicamente

Por último, substitua o `0` fixo pela contagem real de caracteres. A contagem é simplesmente o comprimento (`length`) da nossa string de estado `text`.

```jsx
// ...
return (
  <div>
    {/* ... textarea ... */}
    <p>Contagem: {text.length}</p> {/* Use o comprimento do estado */}
  </div>
);
// ...
```

---

### Código Final

Seu componente completo deve se parecer com isto:

```jsx
import React, { useState } from 'react';

function CharacterCounter() {
  const [text, setText] = useState('');

  const handleChange = (e) => {
    setText(e.target.value);
  };

  return (
    <div>
      <h2>Contador de Caracteres</h2>
      <textarea
        placeholder="Digite algo..."
        rows="5"
        style={{ width: '300px', padding: '10px' }}
        value={text}
        onChange={handleChange}
      />
      <p>Contagem: {text.length}</p>
    </div>
  );
}

export default CharacterCounter;
```

**Parabéns!** Você completou o desafio.
