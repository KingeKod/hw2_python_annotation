from typing import TypedDict, Required


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


if __name__ == "__main__":
    a: Person = {
        "name": "Capy",
        "age": 1,
        "gender": "Male",
        "address": "earth",
        "email": "capy@bara.com",
    }
    a2: Person = {"name": "Capy"}
    # a: Person = {"age": 1, "gender": "Male", "address": "", "email": ""} expect-type-error
