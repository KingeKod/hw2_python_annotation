from src.any import foo as any_foo
from src.dict import foo as dict_foo
from src.final import my_list
from src.kwargs import foo as kwargs_foo
from src.list import foo as list_foo
from src.optional import foo as optional_foo
from src.parameter import foo as parameter_foo
from src.return_foo import foo as return_foo
from src.tuple import foo as tuple_foo
from src.typealias import foo as typealias_foo
from src.union import foo as union_foo
from src.await_foo import run_async
from src.callable import SingleStringInput
from src.class_var import Foo as FooClassVar
from src.decorator import decorator
from src.empty_tuple import foo as foo_empty_tuple
from src.generic import add
from src.generic2 import add as add2
from src.generic3 import add as add3
from src.instance_var import Foo as FooInstanceVar
from src.literal import foo as foo_literal
from src.literalstring import execute_query
from src.self import Foo as FooSelf
from src.typed_dict import Student
from src.typed_dict2 import Student as Student2
from src.typed_dict3 import Person
from src.unpack import Person as Person2, foo as foo_unpack


from typing import List, assert_type
from asyncio import Queue


def main() -> None:
    print("Hello from annotations!")
    any_foo(1)
    any_foo("10")
    dict_foo({"foo": "bar"})
    my_list.append(1)
    kwargs_foo(a=1, b="2")
    list_foo(["foo", "bar"])
    optional_foo(10)
    optional_foo(None)
    optional_foo()
    parameter_foo(10)
    assert_type(return_foo(), int)
    tuple_foo(("foo", 1))
    typealias_foo([1.1, 2])
    union_foo("foo")
    union_foo(1)
    queue: Queue[int] = Queue()
    queue2: Queue[str] = Queue()

    async def async_function() -> int:
        return await queue.get()

    async def async_function2() -> str:
        return await queue2.get()

    run_async(async_function())

    def accept_single_string_input(func: SingleStringInput) -> None: ...

    def string_name(name: str) -> None: ...

    def string_value(value: str) -> None: ...

    def int_value(value: int) -> None: ...

    def new_name(name: str) -> str:
        return name

    accept_single_string_input(string_name)
    accept_single_string_input(string_value)

    FooClassVar.bar = 1

    @decorator
    def foo(a: int, *, b: str) -> None: ...

    @decorator
    def bar(c: int, d: str) -> None: ...

    foo(1, b="2")
    bar(c=1, d="2")

    foo_empty_tuple(())
    assert_type(add(1, 2), int)
    assert_type(add("1", "2"), str)
    assert_type(add(["1"], ["2"]), List[str])

    assert_type(add2(1, 2), int)
    assert_type(add2("1", "2"), str)

    class MyInt(int):
        pass

    assert_type(add3(1), int)
    assert_type(add3(MyInt(1)), MyInt)

    foo_instance_var = FooInstanceVar()
    foo_instance_var.bar = 1

    foo_literal("left")
    foo_literal("right")

    def query_data(user_id: str, limit: bool) -> str:
        query: str = """
            SELECT
                user.name,
                user.age
            FROM data
            WHERE user_id = ?
        """

        if limit:
            query += " LIMIT 1"

        return execute_query(query, (user_id,))

    class SubclassOfFooSelf(FooSelf):
        pass

    f: FooSelf = FooSelf().return_self()
    sf: SubclassOfFooSelf = SubclassOfFooSelf().return_self()
    (f, sf)

    a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
    assert Student(name="Tom", age=15, school="Hogwarts") == dict(
        name="Tom", age=15, school="Hogwarts"
    )

    a2: Student2 = {"name": "Tom", "age": 15}
    a3: Student2 = {"name": "Tom", "age": 15, "school": "Hogwarts"}
    assert Student2(name="Tom", age=15) == dict(name="Tom", age=15)
    assert Student2(name="Tom", age=15, school="Hogwarts") == dict(
        name="Tom", age=15, school="Hogwarts"
    )

    a4: Person = {
        "name": "Capy",
        "age": 1,
        "gender": "Male",
        "address": "earth",
        "email": "capy@bara.com",
    }
    a5: Person = {"name": "Capy"}

    person: Person2 = {"name": "The Meaning of Life", "age": 1983}
    foo_unpack(**person)
    person2: dict[str, object] = {"name": "Brian", "age": 20}
    (a, a2, a3, a4, a5, person, person2)


if __name__ == "__main__":
    main()
