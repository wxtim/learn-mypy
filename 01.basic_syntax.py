# Basic MyPy Syntax

# define a variable:
foo: str = 'Hello'
bar: int = 42

# Define something more complex (Python 3.6-3.8)
# The typing module provides some handy options for working with more complex
# variables which can't be expressed directly by the most basic built-in types
# (str, int, float, ...).
# A few examples of these "special typing primitives" below:
# (more in https://docs.python.org/3/library/typing.html#special-typing-primitives )
from typing import Dict, Optional, Union, Any, List, Iterable
mylist: List = []
my_nailed_down_list: List[str] = ["a", "b"]  # mypy will flag = [1, 2]
mydict: Dict = {}  # can nail down in similar fashion
myunsure: Optional[str] = "Hello, I could also be None"  # i.e. = None also OK
mychoice: Union[str, int] = 42  # Equally valid: = "meep"
baz: Any = "Anything really"  # Equally valid: = int; = None; ...
myiterable: Iterable = range(12)

# But MyPy can usually work types like this out.


# Adding typing: normally you'd start at function or class level:
def untyped_example(my_input):
    return len(my_input) ** 2

# For returned variables, the `->` arrow syntax shows what is expected:
def typed_example(my_input: str) -> int:
    return len(my_input) ** 2

print(untyped_example('Hello'))
print(untyped_example([1, 2]))  # Valid Python -> result. But did you mean this?
print(typed_example('Hello'))
print(typed_example([1, 2]))  # Gets flagged by mypy


# Typing added to a more complex example:
def two_possible_outputs(my_input: Union[str, int]) -> List[Any]:
    """Return a list containing elements with a broad range of types

    Input: Union to allow select options
    Output: Package up in List; Any for elements within, as type range is broad
    """
    from random import choice

    lotto = choice(['Foo', 12, 3.14])  # lotto chosen randomly from these options
    return [lotto, my_input]


print(two_possible_outputs('HI'))
print(two_possible_outputs(2))
print(two_possible_outputs(None))  # Gets flagged by mypy
