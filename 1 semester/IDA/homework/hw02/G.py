def check(s):
    delta = 0
    for c in s:
        delta += 1 if c == '(' else -1
        if delta < 0:
            return False
    return delta == 0
    
def brackets(n):
    def rec(n, s):
        if n == 0:
            if check(s):
                yield s
            return
        yield from rec(n - 1, s + '(')
        yield from rec(n - 1, s + ')')
    yield from rec(2 * n, '')

if __name__ == '__main__':
    print('\n'.join([str(x) for x in brackets(int(input()))]))
