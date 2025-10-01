function criarContadorDeChamadas() {
  // Esta variável 'contador' é declarada no escopo da função externa
  // e será "fechada" (closed over) pela função interna.
  let contador = 0;

  // A função interna, que é o closure.
  // Ela tem acesso e manipula a variável 'contador' de seu escopo pai.
  return function() {
    contador++; // Incrementa o contador cada vez que é chamada.
    console.log(`A função foi executada ${contador} vez(es).`);
    return contador;
  };
}

// Criamos uma instância do nosso closure.
// 'minhaFuncaoContadora' é agora a função interna retornada.
const minhaFuncaoContadora = criarContadorDeChamadas();

// Executando a função e vendo o contador aumentar:
minhaFuncaoContadora(); // Saída: A função foi executada 1 vez(es).
minhaFuncaoContadora(); // Saída: A função foi executada 2 vez(es).
minhaFuncaoContadora(); // Saída: A função foi executada 3 vez(es).

console.log('---');

// Se criarmos outra instância, ela terá seu PRÓPRIO contador:
const outroContador = criarContadorDeChamadas();
outroContador(); // Saída: A função foi executada 1 vez(es).
outroContador(); // Saída: A função foi executada 2 vez(es).

console.log('---');

const contador = () => {
    let contador = 0;
    return contadorFilho = () => {
        contador++
        console.log(`A função foi executada ${contador} vez(es).`);
        return contador
    }
}

const maisUmContador = contador();
maisUmContador();