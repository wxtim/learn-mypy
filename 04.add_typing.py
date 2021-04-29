"""
Aim
===

By the end of this exercise you should be able to add more complex
static typing to functions using the ``typing`` module.

Task
====

Here are a selection of functions - can you make them typed using MyPy?

Before Python 3.9 you will need to use special types imported from
``typing`` to annotate functions.
"""

import os

from typing import Dict, Optional, Any, Union


def linebreak_(text):
    """1. Add basic typing - this function should take a string and
    return a list.
    """
    return text.split('<br>')


# Quick check that function works.
assert (
    linebreak_('Hello Python Guild!<br>Is it a sunny day?') ==
    ['Hello Python Guild!', 'Is it a sunny day?']
)


def two_types_of_output():
    """2. Use ``Union`` from typing to allow multiple valid output types
    """
    if os.environ['USER'][0] in 'abcdefghijklm':
        return f'Hello {os.environ["USER"]}'
    else:
        return 42


two_types_of_output()


def get_host(platform):
    """3. Almost a real world example - based on some Cylc 8 work.

    You will need to tell mypy that the input can be of two possible types
    using Union[type1, type2].

    Try running mypy - note that you don't have to make everything
    work at once.

    Then add what the output should be.

    There are multiple possible right answers here!
    """
    PLATFORMS = [
        {'name': 'my_pc', 'host': 'localhost', 'job runner': 'background'},
        {'name': 'hpc', 'host': 'cray01', 'job runner': 'pbs'},
        {'name': 'sugar', 'host': 'localhost', 'job runner': 'slurm'},
    ]
    if isinstance(platform, str):
        for platform_ in PLATFORMS:
            if platform_['name'] == platform:
                return platform_['host']
        return f'can\'t find your platform {platform}'

    elif isinstance(platform, dict):
        if 'host' in platform:
            return platform['host']
        else:
            return f'no host in your platform {platform}'

    else:
        return None


assert get_host('my_pc') == 'localhost'
assert get_host('sugar') == 'localhost'
assert get_host('hpc') == 'cray01'
assert get_host(
    {'name': 'my_raspi', 'host': 'raspberry', 'job runner': 'slurm'}
) == 'raspberry'
