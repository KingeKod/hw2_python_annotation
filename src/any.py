from typing import Any


def foo(x: Any) -> Any:
    return x


if __name__ == "__main__":
    foo(1)
    foo("10")
    # foo(1, 2) expect-type-error
