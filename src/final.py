from typing import Final

my_list: Final[list[int]] = []


if __name__ == "__main__":
    my_list.append(1)
    # my_list = [] expect-type-error
    # my_list = "my_list" expect-type-error
