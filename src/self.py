from typing import Self


class Foo:
    def return_self(self: Self) -> Self:
        return self


if __name__ == "__main__":

    class SubclassOfFoo(Foo):
        pass

    f: Foo = Foo().return_self()
    sf: SubclassOfFoo = SubclassOfFoo().return_self()

    # sf2: SubclassOfFoo = Foo().return_self() expect-type-error
