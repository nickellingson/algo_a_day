
const nums = [1, 2, 3, 4]

function fn(acc_value, curr_value) {
    return acc_value + curr_value
}

var reduce = function(nums, fn, init) {
    result = init
    for (let i = 0; i < nums.length; i++) {
        result = fn(result, nums[i])
    }
    return result
};

// or 

var reduce1 = function(nums, fn, init) {
    return nums.reduce(fn, init, nums)
};

console.log(reduce(nums, fn, 0))
console.log(reduce1(nums, fn, 0))