const somaTodosElementosDoArray = (array) => array.reduce((acc, num) => acc + num, 0);

console.log(somaTodosElementosDoArray([1,2,3,4,5])); // 15