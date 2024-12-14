
class Fib:

    # 0 1 1 2 3 5 8 13 21
    def get_fib_rec(self, n):
        # base case
        if n <= 1:
            return n
        # recursion
        return self.get_fib_rec(n-1) + self.get_fib_rec(n-2)

    # 0 1 2 3 4 5 6 7  8
    # 0 1 1 2 3 5 8 13 21
    def get_fib_iter(self, n):
        i = 2
        total = 1
        lp = 0
        rp = 0

        if n <= 1:
            return n

        while i <= n:
            rp = total
            total = lp + rp
            lp = rp
            i += 1
        return total
            



# instantiate class
f = Fib()
n = 8
# call functions, print result
print(f.get_fib_rec(n))
print(f.get_fib_iter(n))

