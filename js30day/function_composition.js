// var compose = function(functions) {
// 	return function(x) {
//         result = x;
//         for (let i = functions.length - 1; i >= 0; i --) {
//             result = (functions[i])(result);
//         }
//         return result;
//     }
// };

// var compose = function(functions) {
// 	return function(x) {
//         for (const fn of functions.reverse()) {
//             x = fn(x)
//         }
//         return x;
//     }
// };

var compose = function(functions) {
    const fn = (acc, f) => f(acc);

	return function(x) {
        return functions.reduceRight(fn, x)

    }
};

// Another example of reduce
// const numbers = [175, 50, 25];
// document.getElementById("demo").innerHTML = numbers.reduce(myFunc);

// function myFunc(total, num) {
//   return total - num;
// }