def binomial(n):
    for k in range(-1, n):
        Cnk = Cnk * (n - k) // (k + 1) if k >= 0 else 1
        yield Cnk

if __name__ == '__main__':
    for n in map(int, input().split(' ')):
        print(' '.join([str(x) for x in binomial(n)]))
