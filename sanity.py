from functools import update_wrapper
from inspect import getcallargs

__all__ = ['Predicate', 'P', 'sane', 'Len', 'Int', 'Float']

decorator = (lambda f: f(f))(lambda d: lambda fn: update_wrapper(d(fn), fn))

class Predicate(object):
    def __init__(self, fun=lambda x: x, repr=None):
        self.fun = fun
        self.repr = '{}' if repr is None else repr
    def __repr__(self):
        return self.repr
    # fancy magic
    # it's all very simple once you've dissected one of them
    def __lt__(self, other):
        return Predicate(lambda x: self.fun(x) < other, '({}) < {}'.format(self.repr, repr(other)))
    def __gt__(self, other):
        return Predicate(lambda x: self.fun(x) > other, '({}) > {}'.format(self.repr, repr(other)))
    def __le__(self, other):
        return Predicate(lambda x: self.fun(x) <= other, '({}) <= {}'.format(self.repr, repr(other)))
    def __ge__(self, other):
        return Predicate(lambda x: self.fun(x) >= other, '({}) >= {}'.format(self.repr, repr(other)))
    def __eq__(self, other):
        return Predicate(lambda x: self.fun(x) == other, '({}) == {}'.format(self.repr, repr(other)))
    def __ne__(self, other):
        return Predicate(lambda x: self.fun(x) != other, '({}) != {}'.format(self.repr, repr(other)))
    def __getattr__(self, attr):
        return Predicate(lambda x: getattr(self.fun(x), attr), '({}).{}'.format(self.repr, attr))
    def __getitem__(self, item):
        return Predicate(lambda x: self.fun(x)[item], '({})[{}]'.format(self.repr, repr(item)))
    def __len__(self):
        return Predicate(lambda x: len(self.fun(x)), 'len({})'.format(self.repr,))
    def __add__(self, other):
        return Predicate(lambda x: self.fun(x) + other, '({}) + {}'.format(self.repr, repr(other)))
    def __sub__(self, other):
        return Predicate(lambda x: self.fun(x) - other, '({}) - {}'.format(self.repr, repr(other)))
    def __mul__(self, other):
        return Predicate(lambda x: self.fun(x) * other, '({}) * {}'.format(self.repr, repr(other)))
    def __truediv__(self, other):
        return Predicate(lambda x: self.fun(x) / other, '({}) / {}'.format(self.repr, repr(other)))
    def __floordiv__(self, other):
        return Predicate(lambda x: self.fun(x) // other, '({}) // {}'.format(self.repr, repr(other)))
    def __mod__(self, other):
        return Predicate(lambda x: self.fun(x) % other, '({}) % {}'.format(self.repr, repr(other)))
    def __divmod__(self, other):
        return Predicate(lambda x: divmod(self.fun(x), other), 'divmod(({}), {})'.format(self.repr, repr(other)))
    def __pow__(self, other):
        return Predicate(lambda x: self.fun(x) ** other, '({}) ** {}'.format(self.repr, repr(other)))
    def __lshift__(self, other):
        return Predicate(lambda x: self.fun(x) << other, '({}) << {}'.format(self.repr, repr(other)))
    def __rshift__(self, other):
        return Predicate(lambda x: self.fun(x) >> other, '({}) >> {}'.format(self.repr, repr(other)))
    def __and__(self, other):
        return Predicate(lambda x: self.fun(x) & other, '({}) & {}'.format(self.repr, repr(other)))
    def __xor__(self, other):
        return Predicate(lambda x: self.fun(x) ^ other, '({}) ^ {}'.format(self.repr, repr(other)))
    def __or__(self, other):
        return Predicate(lambda x: self.fun(x) | other, '({}) | {}'.format(self.repr, repr(other)))
    def __radd__(self, other):
        return Predicate(lambda x: other + self.fun(x), '{} + ({})'.format(repr(other), self.repr))
    def __rsub__(self, other):
        return Predicate(lambda x: other - self.fun(x), '{} - ({})'.format(repr(other), self.repr))
    def __rmul__(self, other):
        return Predicate(lambda x: other * self.fun(x), '{} * ({})'.format(repr(other), self.repr))
    def __rtruediv__(self, other):
        return Predicate(lambda x: other / self.fun(x), '{} / ({})'.format(repr(other), self.repr))
    def __rfloordiv__(self, other):
        return Predicate(lambda x: other // self.fun(x), '{} // ({})'.format(repr(other), self.repr))
    def __rmod__(self, other):
        return Predicate(lambda x: other % self.fun(x), '{} % ({})'.format(repr(other), self.repr))
    def __rdivmod__(self, other):
        return Predicate(lambda x: divmod(other, self.fun(x)), 'divmod({}, ({}))'.format(repr(other), self.repr))
    def __rpow__(self, other):
        return Predicate(lambda x: other ** self.fun(x), '{} ** ({})'.format(repr(other), self.repr))
    def __rlshift__(self, other):
        return Predicate(lambda x: other << self.fun(x), '{} << ({})'.format(repr(other), self.repr))
    def __rrshift__(self, other):
        return Predicate(lambda x: other >> self.fun(x), '{} >> ({})'.format(repr(other), self.repr))
    def __rand__(self, other):
        return Predicate(lambda x: other & self.fun(x), '{} & ({})'.format(repr(other), self.repr))
    def __rxor__(self, other):
        return Predicate(lambda x: other ^ self.fun(x), '{} ^ ({})'.format(repr(other), self.repr))
    def __ror__(self, other):
        return Predicate(lambda x: other | self.fun(x), '{} | ({})'.format(repr(other), self.repr))
    def __neg__(self):
        return Predicate(lambda x: -self.fun(x), '-({})'.format(self.repr,))
    def __pos__(self):
        return Predicate(lambda x: +self.fun(x), '+({})'.format(self.repr,))
    def __abs__(self):
        return Predicate(lambda x: abs(self.fun(x)), 'abs({})'.format(self.repr,))
    def __invert__(self):
        return Predicate(lambda x: ~self.fun(x), '~({})'.format(self.repr,))
    def __complex__(self):
        return Predicate(lambda x: complex(self.fun(x)), 'complex({})'.format(self.repr,))
    def __int__(self):
        return Predicate(lambda x: int(self.fun(x)), 'int({})'.format(self.repr,))
    def __float__(self):
        return Predicate(lambda x: float(self.fun(x)), 'float({})'.format(self.repr,))
    def __round__(self, n=None):
        if n is None:
            return Predicate(lambda x: round(self.fun(x)), 'round({})'.format(self.repr,))
        else:
            return Predicate(lambda x: round(self.fun(x), n), 'round({}, n={})'.format(self.repr, repr(n)))

P = Predicate()

def Len(t):
    return t.__len__()

def Int(t):
    return t.__int__()

def Float(t):
    return t.__float__()

@decorator
def sane(f):
    ann = f.__annotations__
    def _s(*args, **kwargs):
        arguments = getcallargs(f, *args, **kwargs)
        for name, arg in arguments.items():
            if name in ann and not ann[name].fun(arg):
                raise ValueError('precondition {} failed'.format(ann[name].repr.format(repr(arg))))
        ret = f(*args, **kwargs)
        if 'return' in ann:
            if not ann['return'].fun(ret):
                raise ValueError('postcondition {} failed'.format(ann['return'].repr.format(repr(ret))))
        return ret
    return _s
