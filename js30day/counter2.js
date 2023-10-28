
function counterCreator(init) {
    let count = init
    // Arrow version
    const increment = () => {
        return ++ count;
    }
    // Inline
    const decrement = () => --count ;

    function reset () {
        count = init;
        return count;
    }
    return {
        // Short hand
        increment,
        decrement,
        // Longer version
        reset: reset
    }
}

const counter = counterCreator(5)
console.log(counter.increment())
console.log(counter.reset())
console.log(counter.decrement())


class Counter {
    constructor(init) {
        this.count = init;
        this.original = init
    }

    increment() {
        return ++ this.count
    }

    decrement() {
        return -- this.count
    }
    reset(){
        this.count = this.original
        return this.count
    }
}

counter_instance = new Counter(5)
console.log(counter_instance.increment())
console.log(counter_instance.reset())
console.log(counter_instance.decrement())