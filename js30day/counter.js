// Closure inside function has access to variables defined outside of it

function createCounter(n) {
    return function() {
        return n ++;
    }
}


function createCounter2(n){
    let count = n
    return function() {
        return count ++
    }
}


class Counter {
    constructor(n) {
        this.n = n;
    }

    increment() {
        return this.n ++;
    }
}

const counter_instance = new Counter(10);
console.log(counter_instance.increment())
console.log(counter_instance.increment())
console.log(counter_instance.increment())


n = 10

const counter = createCounter(n)
console.log(counter()) // 10
console.log(counter()) // 11
console.log(counter()) // 12