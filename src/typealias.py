type Vector = list[float]


def foo(x: Vector) -> Vector:
    return x


if __name__ == "__main__":
    foo([1.1, 2])
    # foo(1) expect-type-error
    # foo(["1"]) expect-type-error
