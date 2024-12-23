function count (n) {
    let total = n
    function helper() {
        return total ++;
    }
    return helper
}

var createCounter = function(n) {
    return function() {
        return n ++;
    }
}

var ooCounter = function(n) {
    let count = n;
    return function() {
        return count++
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


const counter = new Counter(10)
console.log(counter.increment())
console.log(counter.increment())
console.log(counter.increment())

helper = count(10)
console.log(helper())
console.log(helper())
console.log(helper())

cou = createCounter(10)
console.log(cou())
console.log(cou())
console.log(cou())

