from copy import deepcopy


class FragileDict:
    def __init__(self, d=None):
        if d is not None:
            self._data = deepcopy(d)
        self._lock = False

    def __getitem__(self, item):
        return self._data[item]

    def __enter__(self):
        self._backup = deepcopy(self._data)
        self._lock = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock = False
        if exc_type is not None:
            print('Exception has been suppressed.')
            self._data = deepcopy(self._backup)
        del self._backup
        self._data = deepcopy(self._data)
        return True

    def __setitem__(self, item, value):
        if not self._lock:
            raise RuntimeError("Protected state")
        self._data[item] = value

    def __contains__(self, item):
        return item in self._data
