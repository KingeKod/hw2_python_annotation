def foo(x: list[str]) -> list[str]:
    return x


if __name__ == "__main__":
    foo(["foo", "bar"])
    # foo(["foo", 1]) expect-type-error
