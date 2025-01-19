var filter = (arr, fn) => {
    let res = new Array();
    for (let i = 0; i < arr.length; i ++) {
        if (fn(arr[i], i)){
            res.push(arr[i])
        }
    }
    return res
}


// or

var filter = (arr, fn) => {
    return arr.filter(fn)
}