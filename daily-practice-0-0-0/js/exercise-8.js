const objArray = [{name: "bob"}, {name: "TResp"},{name: "Aboba"}];

function returnName(objArray) {
    return objArray.map(obj => obj.name)
};

console.log(returnName(objArray));