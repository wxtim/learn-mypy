"""
Aim
===

By the end of this exercise you should be able to use MyPy
annotation syntax for a basic function:

```python
def function(input:type) -> outputtype:
    ...
```

Task
====

This function works, but it probably shouldn't - can you make it fail
validation with MyPy?


To run MyPy on this file

.. code:: python

   mypy 03.broken_function.py


(It's taken pretty directly from the MyPy docs)
"""


def hello(name):
    return f'Hello {name}'


# Decide which of these you think are acceptable inputs...
TEST_CASES = [
    'World',
    ['Python', 'Guild'],
    99,
]

for case in TEST_CASES:
    print(hello(case))


# def extension_exercise(name):
#     """If you fancy a challenge try doing the same here...

#     (
#         You will need to use ``from typing import Union`` and add
#         ``Union[str, list]``...
#     )
#     """
#     if isinstance(name, str):
#         return hello(name)
#     elif isinstance(list, name) and all([isinstance(str, i) for i in name]):
#         return ' '.join(name)


# for case in TEST_CASES:
#     print(extension_exercise(case))
