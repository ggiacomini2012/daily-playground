const array = ['bob', 'alice', 'john'];

const captalizarPalavras = (array) => {
    return array.map(palavra => palavra.charAt(0).toUpperCase() + palavra.slice(1));
}
console.log(captalizarPalavras(array));