from functools import wraps
from time import time
from typing import Any, Callable


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Выполняется {func} c аргументами: {args}, {kwargs}.')
            start = time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time()
                total = end - start
                print(f'Завершилась {func} за {total:.4f} секунд.')
        return wrapped
    return wrapper
