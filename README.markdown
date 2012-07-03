# Sanity

```python
from sanity import *
```

An experimental pre- and postcondition checking library for **Python 3**.

```python
@sane
def sqrt(x: P > 0):
    import math
    return math.sqrt(x)

print(sqrt(9))
# prints 3.0

print(sqrt(-9))
# ValueError: precondition (-9) > 0 failed
```

```python
@sane
def square(x) -> P > 0:
    return x * x

print(square(5))
# prints 25

class BadInt(int):
    def __mul__(self, other):
        return -int.__mul__(self, other)

print(square(BadInt(5)))
# ValueError: precondition (-25) > 0 failed
```


It uses operator overloading and other magic methods to be able to test some
pretty advanced conditions.

```python
@sane
def fork(lst: P.__len__() % 2 == 0):
    # we can't use len(P) because len() wants to return an int
    return lst[::2], lst[1::2]

print(fork([1, 2, 3, 4]))
# prints ([1, 3], [2, 4])

print(fork([1, 2, 3]))
# ValueError: precondition ((len([1, 2, 3])) % 2) == 0 failed
```

```python
class Person:
    def __init__(self, parent=None):
        self.parent = parent
    def __repr__(self):
        if self.parent is None:
            return 'someone'
        return 'child of ' + repr(self.parent)
    @sane
    def grandparent(self: P.parent != None):
        return self.parent.parent

print(Person(Person(Person(Person()))).grandparent())
# prints "child of someone"

print(Person().grandparent())
# ValueError: precondition ((someone).parent) != None failed
```

# Future work

## Varargs

Sanity can't currently handle `*args` or `**kwargs`, so that's scheduled.

## Multiple predicates

More importantly, I want to be able to do things like this:

```python
@sane
def pos_sub(a: P > P('b'), b):
    # or: P('a') > P('b')
    return a - b
```

@sane
def fork(lst: P.__len__() % 2 == 0) -> (P.__len__() == 2 and
        P[0].__len__() == P[1].__len__()):
    return lst[::2], lst[1::2]
```

This is currently not possible since the current design only allows one
argument for a predicate, which requires all predicates to be a single line,
so no multiple Ps per condition.
