def foo(x: tuple[()]) -> tuple[()]:
    return x


if __name__ == "__main__":
    foo(())
    # foo((1,)) expect-type-error
