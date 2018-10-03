import functools


def once(func):
    called = False
    res = None

    @functools.wraps(func)
    def wrapper(*args, **kwards):
        nonlocal called, res
        if not called:
            res = func(*args, **kwards)
            called = True
        return res
    return wrapper
