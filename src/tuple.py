def foo(x: tuple[str, int]) -> tuple[str, int]:
    return x


if __name__ == "__main__":
    foo(("foo", 1))
    # foo((1, 2))
    # foo(("foo", "bar"))
    # foo((1, "bar"))
