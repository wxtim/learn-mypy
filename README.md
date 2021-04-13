# Synopsis

A brief introduction to MyPy.

Contents:
- Why bother with MyPy.
- Two example scripts.
- Two excercise scripts.

# Why Bother With MyPy

- Prevents bugs sooner.
- Stops programme doing daft things.
  Classic example is:
  ```python
  def greet(name):
     print(f'Hello {name}')

   greet({42: 'Deep thought'})  # Python handles this, even if it's not sensible.
   >>> Hello {42: 'Deep thought'}
  ```
- Sets typing in the code rather than the docstring, where it can become out of date without being called out by continuous testing.

# How to get a copy of this repo:

Either:

1. [Download and unzip](https://github.com/wxtim/learn-mypy/archive/refs/heads/master.zip) in a location of your choice.
2. Command line `git clone https://github.com/wxtim/learn-mypy.git`. Then
   `cd learn-mypy`.

# Examples of MyPy

1. [Brief introduction to the syntax.](01.basic_syntax.py)
   - [Answers](.answers/01.basic_syntax.py.diff)
2. [An example where type annotation would have made my life better.](02.real_world_example.py)
   - [Answers](.answers/02.real_world_example.py.diff)
3. [Excercise 1: Make a broken function fail MyPy validation](03.broken_function.py)
   - [Answers](.answers/03.broken_function.py.diff)
4. [Excercise 2: Use MyPy on some example legacy code.](04.add_typing.py)
   - [Answers](.answers/04.add_typing.py.diff)
