from typing import TypeVar

T = TypeVar("T", bound=int)


def add(a: T) -> T:
    return a


if __name__ == "__main__":
    from typing import assert_type

    class MyInt(int):
        pass

    assert_type(add(1), int)
    assert_type(add(MyInt(1)), MyInt)
    # assert_type(add("1"), str) expect-type-error
    # add(["1"], ["2"]) expect-type-error
    # add("1", 2) expect-type-error
