def foo(x: int) -> int:
    return x


if __name__ == "__main__":
    foo(10)
    # foo("10") expect-type-error
