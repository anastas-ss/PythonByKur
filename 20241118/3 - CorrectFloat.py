from functools import wraps

class Fix:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = [round(arg, self.n) if isinstance(arg, float) else arg for arg in args]
            new_kwargs = {k: round(v, self.n) if isinstance(v, float) else v for k, v in kwargs.items()}
            result = func(*new_args, **new_kwargs)
            return round(result, self.n) if isinstance(result, float) else result

        return wrapper
