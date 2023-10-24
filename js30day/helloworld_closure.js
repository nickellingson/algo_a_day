const createFunction = function() {
    return function() {
        console.log("hello world")
    }
}

const fun = createFunction()
fun() // Print hello world