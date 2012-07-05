'''
Several test cases

Uncomment the commented-out function calls to get precondition exceptions
'''

from sanity import *

print (P)

_ = Predicate

a = {'dict': 'Yo'}
b = {'dict': 'Ya'}

@sane
def sqrt(a: P > 0) -> P > 0:
    import math
    return a - 2

print(sqrt(3))
#print(sqrt(1))
#print(sqrt(-3))

@sane
def insane(in_: P['dict'] == 'Yo'):
    return in_['dict']

print(insane(a))
#print(insane(b))

@sane
def addition(arg: 1 + P + 2 == 3) -> P + 3 == 3:
    return arg

print(addition(0))
#print(addition(1))

@sane
def a1(arg: 2 + P >> 1 > 5, arg2):
    return arg - arg2

print(a1(10, 5))
#print(a1(5, 10))

@sane
def a2(a: Len(P[0][0]) > 2):
    return a[0][0][2]

print(a2([[[1, 2, 4]]]))
#print(a2([[[1, 2]]]))

@sane
def a3(*k: Len(P) == 3):
	return k

print(a3(1, 2, 3))
#print(a3(1, 2))
#print(a3(1, 2, 3, 4))
#print(a3(1, 2, 3, 4, 5)) # right out

@sane
def a4(*q, **kw: P['foo'] != 0):
	return kw['foo']

print(a4(foo=2, hi=9001))
#print(a4(foo=0, hi=9001))

@sane
def a5(a: _.a < 0, b: _.a > -100 =None):
	return -a

print(a5(-10))
#print(a5(10))
#print(a5(-100))


@sane
def a6(x: P != "Hi"):
	return x

print(a6("Yay"))
#print(a6("Hi"))

@sane
def a7(x: _.x > _.y, y):
	return x - y

print(a7(10, 5))
#print(a7(5, 10))

@sane
def a8(x) -> P > _.x:
	return x * 10

print(a8(2))
#print(a8(0))
