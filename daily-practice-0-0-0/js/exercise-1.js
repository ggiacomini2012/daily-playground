// Exercício de JavaScript Simples

// Objetivo: Criar uma função que gera uma saudação.

// Instruções:
// 1. Defina uma função chamada `criarSaudacao` que aceita um argumento: `nome`.
// 2. Dentro da função, retorne uma string que diga "Olá, [nome]! Bem-vindo ao mundo do JavaScript.".
// 3. Chame a função, passando seu próprio nome como argumento, e armazene o resultado em uma variável chamada `minhaSaudacao`.
// 4. Imprima o valor da variável `minhaSaudacao` no console.

// Exemplo de como chamar a função no terminal (depois de salvar o arquivo):
// node js/exercise.js

// --- Escreva seu código abaixo ---

function criarSaudacao(nome) {
  return `Olá, ${nome}! Tudo bem?`  
};

console.log(criarSaudacao(`Gui`));


// --- Solução ---
/*
function criarSaudacao(nome) {
  return `Olá, ${nome}! Bem-vindo ao mundo do JavaScript.`;
}

const minhaSaudacao = criarSaudacao("Seu Nome");
console.log(minhaSaudacao);
*/

