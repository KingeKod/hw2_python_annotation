class Foo:
    bar: int


if __name__ == "__main__":
    foo = Foo()
    foo.bar = 1
    # foo.bar = "1" expect-type-error
