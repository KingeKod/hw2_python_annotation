def foo(**kwargs: int | str) -> dict[str, int | str]:
    return kwargs


if __name__ == "__main__":
    foo(a=1, b="2")
    # foo(a=[1]) expect-type-error
