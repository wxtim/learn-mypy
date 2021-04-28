# A brief introduction to MyPy

Disclaimer: I wrote this to crystalize my own learning. I don't claim to be
an expert.

---

## Synopsis

A brief introduction to MyPy.

Contents:

- Why bother with MyPy.
- Two example scripts.
- Two exercise scripts.

---

## Why Bother With MyPy

Python is dynamically typed, but sometimes this can make life harder.

---

### Allows you to spot bugs sooner:

Debugging is easy in this trivial example, but in a bigger codebase
adding typechecking to this function would reduce risk of accidentally calling
it with args of the wrong type:

```python
def get_reachable_hosts(allhosts, badhosts):
    """Do something for every host that you can
    reach from a list of hosts.
    """
    goodhosts = allhosts - badhosts
    for goodhost in goodhosts:
        ...  # do stuff

get_reachable_hosts(['foo', 'bar', 'baz'], set('foo'))
```

---

### Programatically OK ≠ Intended Usage:

Classic example is:

```python
def greet(name):
    print(f'Hello {name}')

greet({42: 'Deep thought'})
# Python handles this
# even if it's not sensible.
>>> Hello {42: 'Deep thought'}
```

---

### Sets typing in the code rather than the docstring:
Docstring relies on human proofing for being up to date.

```python
def function_has_evolved(input_):
   """Do something to a string.

   Args (str): Do something to a string
   """
   return [func(i) for i in input_]
```

---

Ultimately though, MyPy is optional. You can have both static and dynamic
typing for different bits of the same script!

---
## How to get a copy of this repo:

Either:

1. [Use this link to download and unzip](https://github.com/wxtim/learn-mypy/archive/refs/heads/master.zip) in a location of your choice.
2. On the command line: `git clone https://github.com/wxtim/learn-mypy.git`. Then
   `cd learn-mypy`.

---

## Examples of MyPy

1. [Brief introduction to the syntax.](01.basic_syntax.py) ([Answers](.answers/01.basic_syntax.py.diff))
2. [An example where type annotation would have made my life better.](02.real_world_example.py) ([Answers](.answers/02.real_world_example.py.diff))
3. [Exercise 1: Make a broken function fail MyPy validation](03.broken_function.py) ([Answers](answers/03.broken_function.py.diff))
4. [Exercise 2: Use MyPy on some example legacy code.](04.add_typing.py) ([Answers](.answers/04.add_typing.py.diff))
