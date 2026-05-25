from typing import ClassVar


class Foo:
    bar: ClassVar[int]


if __name__ == "__main__":
    Foo.bar = 1
    # Foo.bar = "1" expect-type-error
    # Foo().bar = 1 expect-type-error
