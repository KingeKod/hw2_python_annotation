def foo(x: dict[str, str]) -> dict[str, str]:
    return x


if __name__ == "__main__":
    foo({"foo": "bar"})
    # foo({"foo": 1}) expect-type-error
