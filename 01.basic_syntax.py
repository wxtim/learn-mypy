# Basic MyPy Syntax

# define a variable:
foo: str = 'Hello'
bar: int = 42

# define something more complex (Python 3.6-3.8)
from typing import Dict, Optional, Union, Any, List, Iterable
baz: Any = 'Anything really'
mylist: List = []
mydict: Dict = {}
myiterable: Iterable = range(12)
myunsure: Optional[str] = 'Hello'
mychoice: Union[str, int] = 42


# But MyPy can usually work types like this out.
# Normally you'd start typing at function or Class level:

# `->` Arrow syntax shows what is expected:
def pointless_example(input_):
    return len(input_) ** 2


print(pointless_example('Hello'))


def two_possible_outputs(input_):
    from random import choice
    lotto = choice(['Foo', 12, 'Zaphod'])
    return [lotto, input_]


print(two_possible_outputs('Hi'))
