class ExceptionTree:
    def __init__(self):
        self._cache = {}

    def __call__(self, n):
        if n in self._cache:
            return self._cache[n]
        
        parent_class = self.__call__(n // 2) if n > 1 else Exception
        new_exception = type(f"{n}", (parent_class,), {'n': n})

        self._cache[n] = new_exception
        return new_exception






