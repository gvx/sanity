'''
Several test cases

Uncomment the commented-out function calls to get precondition exceptions
'''

from sanity import *

print (P)

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

