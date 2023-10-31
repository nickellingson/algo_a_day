// Strategy Pattern

const map = (arr, fn) => {
        return arr.map(fn)
}

// or 

var map1 = function(arr, fn) {
    return arr.map(fn);
};

// or

var map2 = function(arr, fn) {
    const result = []
    for (const element of arr) {
        result.push(fn(element))
    }
    return result
}


arr = [1,2,3], fn = function plusone(n) { return n + 1; }

console.log(map1(arr, fn))
console.log(map1(arr, fn))
console.log(map2(arr, fn))