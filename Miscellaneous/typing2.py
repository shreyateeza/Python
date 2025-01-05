# from typing import list, Any, Dict, Optional, Union, tuple
from typing import Generic, TypeVar, Callable, Union

class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        return self.stack.pop()


class Stack:
    def __init__(self) -> None:
        self.stack: list[str] = []

    def push(self, val: str) -> None:
        self.stack.append(val)

    def pop(self) -> str:
        return self.stack.pop()



R = TypeVar("R")

class Stack(Generic[R]):
    def __init__(self, val: list[R]) -> None:
        self.stack: list[R] = val

    def push(self, val: R) -> None:
        self.stack.append(val)

    def pop(self) -> R:
        return self.stack.pop()


T = TypeVar("T", int, float)

def add(a: T, b: T) -> T:
    return a + b

def add2(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

add2(1, 2.0)

def test(*args: tuple[int, float]) -> None:
    print(args)

test((1, 2.0))


T1 = TypeVar("T1")
R1 = TypeVar("R1")

def log_dec(func: Callable[[T1], R1]) -> Callable[[T1], R1]:
    def wrapper(*args: T1, **kwargs: T1) -> R1:
        print("hello")
        return func(*args, **kwargs)
    return wrapper


@log_dec
def double(x: int) -> int:
    return x * 2


result = double(10)