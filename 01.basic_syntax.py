# Basic MyPy Syntax

# define a variable:
foo: str = 'Hello'
bar: int = 42

# define something more complex (Python 3.6-3.8)
from typing import Dict, Optional, Union, Any, List, Iterable
mylist: List = []
my_nailed_down_list: List[str] = ["a", "b"]  # mypy will flag = [1, 2]
mydict: Dict = {}  # can nail down in similar fashion
myunsure: Optional[str] = "Hello, I could also be None"  # i.e. = None also OK
mychoice: Union[str, int] = 42  # Equally valid: = "meep"
baz: Any = "Anything really"  # Equally valid: = int; = None; ...
myiterable: Iterable = range(12)

# But MyPy can usually work types like this out.

# Normally you'd start typing at function or Class level:

# `->` Arrow syntax shows what is expected:
def pointless_example(input_):
    return len(input_) ** 2


print(pointless_example('Hello'))
print(pointless_example([1, 2]))


def two_possible_outputs(input_) -> List[Any]:
    from random import choice
    lotto = choice(['Foo', 12, 'Zaphod'])
    return [lotto, input_]


print(two_possible_outputs('HI'))
