const arrayObj = [{name: 'bob'}, {name: 'max'}, {name: 'Liberte'}];

function returnName(array) {
    return array.map(obj => obj.name)
}

console.log(returnName(arrayObj));