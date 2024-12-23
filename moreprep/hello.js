
// hello function
var fun = function () {
    return () => {
       return "hello world"
    }
}

fu = fun()

console.log(fu())
console.log(fu())
console.log(fu())




// arrow function
const f = (i, j, s) => {
    sum = i + j
    console.log(sum)
    const res = s.split(",")
    res.push(sum)
    return res
}

console.log(f(4, 3, "1,2,3,4,5,4,3,5"))