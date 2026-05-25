from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable)


def decorator(func: F) -> F:
    return func


if __name__ == "__main__":

    @decorator
    def foo(a: int, *, b: str) -> None: ...

    @decorator
    def bar(c: int, d: str) -> None: ...

    foo(1, b="2")
    bar(c=1, d="2")

    # foo(1, "2") expect-type-error
    # foo(a=1, e="2") expect-type-error
