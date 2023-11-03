var once = function(fn) {
    count = 0;
	return function(...args){
        count++
        if (count < 2) {
            return fn(...args)
        }
        return undefined
    }
};

var once1 = function(fn) {
    let called = false;

    return function(...args) {
        if (called){
            return undefined;
        }
        called = true;
        fn(...args);
    }
}


fn = (a,b,c) => (a*b*c);
const onceFn = once(fn);
console.log(onceFn(5,7,4));
console.log(onceFn(5,7,4));