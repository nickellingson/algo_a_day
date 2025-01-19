
// Arrow
let arrow = (x, y) => {
    return x * y
}

console.log(arrow(4, 5))

// Object
const car = {
    type:"Fiat",
    model:"500",
    color:"white"
}


// displaying js

const person = {
    name: "john",
    age: 30,
    city: "New York"
};

document.getElementById("demo").innerHTML = person
// or
document.getElementById("demo").innerHTML = person.name + "," + person.age;


// Classes
class ExampleClass {
    constructor(val){
        this.val = val
    }

}

const exampleValue = new ExampleClass(10)