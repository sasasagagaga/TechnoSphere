def brackets(n):
    def rec(n, s, delta):
        if n == 0 and delta == 0:
            yield s
        if n == 0 or delta < 0:
            return
        yield from rec(n - 1, s + '(', delta + 1)
        yield from rec(n - 1, s + ')', delta - 1)
    yield from rec(2 * n, '', 0)

if __name__ == '__main__':
    print('\n'.join([str(x) for x in brackets(int(input()))]))
