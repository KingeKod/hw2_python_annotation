from typing import Union


def foo(x: Union[str, int]) -> Union[str, int]:
    return x


if __name__ == "__main__":
    foo("foo")
    foo(1)
    # foo([]) expect-type-error
