from typing import Literal


def foo(direction: Literal["left", "right"]) -> Literal["left", "right"]:
    return direction


if __name__ == "__main__":
    foo("left")
    foo("right")

    a = "".join(["l", "e", "f", "t"])
    # foo(a) expect-type-error
