from typing import TypeVar

T = TypeVar("T", str, int)


def add(a: T, b: T) -> T:
    return a


if __name__ == "__main__":
    from typing import assert_type

    assert_type(add(1, 2), int)
    assert_type(add("1", "2"), str)

    # add(["1"], ["2"]) expect-type-error
    # add("1", 2) expect-type-error
