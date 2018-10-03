import time
import functools


def stopwatch(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print('`{}` started'.format(func.__name__))
        ret = func(*args, **kwargs)
        print('`{}` finished in {:.2f}s'.format(func.__name__, time.time() - start))
        return ret
    return wrapper
