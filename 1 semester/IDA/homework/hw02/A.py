def ackermann(m, n):
    ackermann.counter = 0
    
    def rec(m, n):
        ackermann.counter += 1
        if m == 0:
            return n + 1
        if n == 0:
            return rec(m - 1, 1)
        return rec(m - 1, rec(m, n - 1))
    
    return rec(m, n)
