from functools import update_wrapper
from inspect import getcallargs

__all__ = ['Predicate', 'P', 'sane', 'Len', 'Int', 'Float', 'Any', 'All', 'Contains']

decorator = (lambda f: f(f))(lambda d: lambda fn: update_wrapper(d(fn), fn))

class PredicateMeta(type):
    def __new__(cls, name, bases, attrs):
        return super(PredicateMeta, cls).__new__(cls, name, bases, attrs)
    def __getattr__(self, attr):
        return self(which_args=(attr,))

class Predicate(metaclass=PredicateMeta):
    def __init__(self, fun=lambda x: x[0], repr=None, which_args=(None,)):
        self.fun = fun
        self.repr = '{!r}' if repr is None else repr
        self.which_args = which_args
    def __repr__(self):
        return self.repr
    # fancy magic
    # it's all very simple once you've dissected one of them
    def __lt__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) < other.fun(x[n:]), '({}) < ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) < other, '({}) < {}'.format(self.repr, repr(other)), self.which_args)
    def __gt__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) > other.fun(x[n:]), '({}) > ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) > other, '({}) > {}'.format(self.repr, repr(other)), self.which_args)
    def __le__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) <= other.fun(x[n:]), '({}) <= ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) <= other, '({}) <= {}'.format(self.repr, repr(other)), self.which_args)
    def __ge__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) >= other.fun(x[n:]), '({}) >= ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) >= other, '({}) >= {}'.format(self.repr, repr(other)), self.which_args)
    def __eq__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) == other.fun(x[n:]), '({}) == ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) == other, '({}) == {}'.format(self.repr, repr(other)), self.which_args)
    def __ne__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) != other.fun(x[n:]), '({}) != ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) != other, '({}) != {}'.format(self.repr, repr(other)), self.which_args)
    def __getattr__(self, attr):
        return Predicate(lambda x: getattr(self.fun(x), attr), '({}).{}'.format(self.repr, attr), self.which_args)
    def __getitem__(self, item):
        if isinstance(item, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n])[item.fun(x[n:])], '({})[{}]'.format(self.repr, item.repr), self.which_args + item.which_args)
        return Predicate(lambda x: self.fun(x)[item], '({})[{}]'.format(self.repr, repr(item)), self.which_args)
    def __len__(self):
        return Predicate(lambda x: len(self.fun(x)), 'len({})'.format(self.repr,), self.which_args)
    def __add__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) + other.fun(x[n:]), '({}) + ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) + other, '({}) + {}'.format(self.repr, repr(other)), self.which_args)
    def __sub__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) - other.fun(x[n:]), '({}) - ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) - other, '({}) - {}'.format(self.repr, repr(other)), self.which_args)
    def __mul__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) * other.fun(x[n:]), '({}) * ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) * other, '({}) * {}'.format(self.repr, repr(other)), self.which_args)
    def __truediv__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) / other.fun(x[n:]), '({}) / ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) / other, '({}) / {}'.format(self.repr, repr(other)), self.which_args)
    def __floordiv__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) // other.fun(x[n:]), '({}) // ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) // other, '({}) // {}'.format(self.repr, repr(other)), self.which_args)
    def __mod__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) % other.fun(x[n:]), '({}) % ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) % other, '({}) % {}'.format(self.repr, repr(other)), self.which_args)
    def __divmod__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: divmod(self.fun(x[:n]), other.fun(x[n:])), 'divmod(({}), ({}))'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: divmod(self.fun(x), other), 'divmod(({}), {})'.format(self.repr, repr(other)), self.which_args)
    def __pow__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) ** other.fun(x[n:]), '({}) ** ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) ** other, '({}) ** {}'.format(self.repr, repr(other)), self.which_args)
    def __lshift__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) << other.fun(x[n:]), '({}) << ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) << other, '({}) << {}'.format(self.repr, repr(other)), self.which_args)
    def __rshift__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) >> other.fun(x[n:]), '({}) >> ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) >> other, '({}) >> {}'.format(self.repr, repr(other)), self.which_args)
    def __and__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) & other.fun(x[n:]), '({}) & ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) & other, '({}) & {}'.format(self.repr, repr(other)), self.which_args)
    def __xor__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) ^ other.fun(x[n:]), '({}) ^ ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) ^ other, '({}) ^ {}'.format(self.repr, repr(other)), self.which_args)
    def __or__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: self.fun(x[:n]) | other.fun(x[n:]), '({}) | ({})'.format(self.repr, other.repr), self.which_args + other.which_args)
        return Predicate(lambda x: self.fun(x) | other, '({}) | {}'.format(self.repr, repr(other)), self.which_args)
    def __radd__(self, other):
        return Predicate(lambda x: other + self.fun(x), '{} + ({})'.format(repr(other), self.repr), self.which_args)
    def __rsub__(self, other):
        return Predicate(lambda x: other - self.fun(x), '{} - ({})'.format(repr(other), self.repr), self.which_args)
    def __rmul__(self, other):
        return Predicate(lambda x: other * self.fun(x), '{} * ({})'.format(repr(other), self.repr), self.which_args)
    def __rtruediv__(self, other):
        return Predicate(lambda x: other / self.fun(x), '{} / ({})'.format(repr(other), self.repr), self.which_args)
    def __rfloordiv__(self, other):
        return Predicate(lambda x: other // self.fun(x), '{} // ({})'.format(repr(other), self.repr), self.which_args)
    def __rmod__(self, other):
        return Predicate(lambda x: other % self.fun(x), '{} % ({})'.format(repr(other), self.repr), self.which_args)
    def __rdivmod__(self, other):
        return Predicate(lambda x: divmod(other, self.fun(x)), 'divmod({}, ({}))'.format(repr(other), self.repr), self.which_args)
    def __rpow__(self, other):
        return Predicate(lambda x: other ** self.fun(x), '{} ** ({})'.format(repr(other), self.repr), self.which_args)
    def __rlshift__(self, other):
        return Predicate(lambda x: other << self.fun(x), '{} << ({})'.format(repr(other), self.repr), self.which_args)
    def __rrshift__(self, other):
        return Predicate(lambda x: other >> self.fun(x), '{} >> ({})'.format(repr(other), self.repr), self.which_args)
    def __rand__(self, other):
        return Predicate(lambda x: other & self.fun(x), '{} & ({})'.format(repr(other), self.repr), self.which_args)
    def __rxor__(self, other):
        return Predicate(lambda x: other ^ self.fun(x), '{} ^ ({})'.format(repr(other), self.repr), self.which_args)
    def __ror__(self, other):
        return Predicate(lambda x: other | self.fun(x), '{} | ({})'.format(repr(other), self.repr), self.which_args)
    def __neg__(self):
        return Predicate(lambda x: -self.fun(x), '-({})'.format(self.repr,), self.which_args)
    def __pos__(self):
        return Predicate(lambda x: +self.fun(x), '+({})'.format(self.repr,), self.which_args)
    def __abs__(self):
        return Predicate(lambda x: abs(self.fun(x)), 'abs({})'.format(self.repr,), self.which_args)
    def __invert__(self):
        return Predicate(lambda x: ~self.fun(x), '~({})'.format(self.repr,), self.which_args)
    def __complex__(self):
        return Predicate(lambda x: complex(self.fun(x)), 'complex({})'.format(self.repr,), self.which_args)
    def __int__(self):
        return Predicate(lambda x: int(self.fun(x)), 'int({})'.format(self.repr,), self.which_args)
    def __float__(self):
        return Predicate(lambda x: float(self.fun(x)), 'float({})'.format(self.repr,), self.which_args)
    def __round__(self, n=None):
        if n is None:
            return Predicate(lambda x: round(self.fun(x)), 'round({})'.format(self.repr,), self.which_args)
        else:
            return Predicate(lambda x: round(self.fun(x), n), 'round({}, n={})'.format(self.repr, repr(n)), self.which_args)
    def __contains__(self, other):
        if isinstance(other, Predicate):
            n = len(self.which_args)
            return Predicate(lambda x: other.fun(x[n:]) in self.fun(x[:n]), '({}) in ({})'.format(other.repr, self.repr), self.which_args + other.which_args)
        return Predicate(lambda x: other in self.fun(x), '{} in ({})'.format(repr(other), self.repr), self.which_args)
    def __call__(self, instead):
        return Predicate(lambda x: instead, repr(instead))

P = Predicate()

def Len(t):
    return t.__len__()

def Int(t):
    return t.__int__()

def Float(t):
    return t.__float__()

def Any(*t):
    def ifany(x):
        s = 0
        for i in t:
            if i.fun(x[s:s + len(i.which_args)]):
                return True
            s + len(i.which_args)
        return False
    return Predicate(ifany, 'any({})'.format(', '.join(i.repr for i in t)))

def All(*t):
    def ifall(x):
        s = 0
        for i in t:
            if not i.fun(x[s:s + len(i.which_args)]):
                return False
            s + len(i.which_args)
        return True
    return Predicate(ifall, 'all({})'.format(', '.join(i.repr for i in t)))

def Contains(container, item):
    return container.__contains__(item)

@decorator
def sane(f):
    ann = f.__annotations__
    def _s(*args, **kwargs):
        arguments = getcallargs(f, *args, **kwargs)
        for name, arg in arguments.items():
            if name in ann:
                pred = ann[name]
                passed = [arguments[name if alt is None else alt] for alt in pred.which_args]
                if not pred.fun(passed):
                    raise ValueError('precondition {} failed'.format(pred.repr.format(*passed)))
        ret = f(*args, **kwargs)
        if 'return' in ann:
            pred = ann['return']
            passed = [ret if alt is None else arguments[alt] for alt in pred.which_args]
            if not pred.fun(passed):
                raise ValueError('postcondition {} failed'.format(pred.repr.format(*passed)))
        return ret
    return _s
