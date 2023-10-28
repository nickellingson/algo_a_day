// Closure inside function has access to variables defined outside of it

function createCounter(n) {
    return function() {
        return n ++;
    }
}

n = 10


const counter = createCounter(n)
console.log(counter()) // 10
console.log(counter()) // 11
console.log(counter()) // 12