// Exercício 2: Soma de Números em um Array

// Objetivo: Criar uma função que calcula a soma de todos os números em um array.

// Instruções:
// 1. Defina uma função chamada `somarArray` que aceita um argumento: `numeros` (que será um array).
// 2. Dentro da função, itere sobre o array e some todos os seus elementos.
// 3. Retorne a soma total.
// 4. Crie um array de exemplo com alguns números (por exemplo: [10, 20, 30, 5]).
// 5. Chame a função `somarArray`, passando seu array como argumento.
// 6. Imprima o resultado no console para verificar se está correto.

// Exemplo de como chamar a função no terminal (depois de salvar o arquivo):
// node js/exercise-2.js


// --- Solução (Exemplo 1: Usando um loop for...of) ---
function somarArray(numeros) {
  let soma = 0;
  for (const numero of numeros) {
    console.log(`numero: ${numero}`)
    console.log(`numeros: ${numeros}`)
    soma += numero;
    }
    console.log(`soma: ${soma}`)
    return soma;
    }
    
const meusNumeros = [10, 20, 30, 5];
const resultado = somarArray(meusNumeros);

console.log(`A soma dos números na solução 1# é: ${resultado}\n`); // Deve imprimir 65



// --- Solução (Exemplo 2: Usando o método reduce) ---
function somarArrayComReduce(numeros) {
  return numeros.reduce((acumulador, valorAtual) => {
    console.log(`acumulador: ${acumulador}`)
    console.log(`valorAtual: ${valorAtual}`)
    return acumulador + valorAtual});
}

const meusNumeros2 = [10, 20, 30, 5];
const resultado2 = somarArrayComReduce(meusNumeros2);
console.log(`A soma (com reduce) solução #2 é: ${resultado2}\n`); // Deve imprimir 65

function somarArrayComReduce(numeros) {
  return numeros.reduce((acumulador, valorAtual) => acumulador + valorAtual, 0);
}

console.log(`A soma (com reduce reduzido) solução #3 é: ${resultado2}\n`); // Deve imprimir 65