from typing import Optional


def foo(x: Optional[int] = None) -> Optional[int]:
    return x


if __name__ == "__main__":
    foo(10)
    foo(None)
    foo()
    # foo("10") expect-type-error
