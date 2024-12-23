const counter = function (i) {
    let temp = i
    function increment () {
        return i + 1
    }
    function decrement () {
        return i - 1
    }
    function reset () {
        i = temp
        return i
    }
    const write = () => {
        return i
    }

    return {
    increment:increment,
    //or
    decrement,
    reset,
    write
    }
}

c = counter(5)
console.log(c.increment())
console.log(c.decrement())
console.log(c.decrement())
console.log(c.decrement())
console.log(c.reset())
console.log(c.write())
console.log(c.increment())




// equivalent to above

class Count {

    constructor(i) {
        this.i = i;
        this.currentCount = i;
    }

    increment() {
        return this.currentCount ++;
    }

    decrement() {
        return this.currentCount --
    }

    reset(){
        this.currentCount = this.i
    }
}