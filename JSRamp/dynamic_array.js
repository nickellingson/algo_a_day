class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.arr = new Array(this.capacity).fill(0)
        this.size = 0
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.arr[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.arr[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if(this.size === this.capacity) {
            this.resize()
        }

        this.arr[this.size] = n
        this.size ++

    }

    /**
     * @returns {number}
     */
    popback() {
        if (this.size > 0) {
            this.size --
        }
        let temp = this.arr[this.size]
        this.arr[this.size] = 0
        return temp
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity *= 2
        const new_arr = new Array(this.capacity).fill(0)
        for (let i = 0; i < this.size; i ++) {
            new_arr[i] = this.arr[i]
        }
        this.arr = new_arr
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.size
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
