from propositional_logic import *
from dpll import *
from random_expression import *

T = BoolConst(True)
F = BoolConst(False)

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')


v = BoolVar('v')
w = BoolVar('w')
x = BoolVar('x')
y = BoolVar('y')
z = BoolVar('z')


# dpll example from the slides
f1 = Or(x,y)
f2 = Or(Not(x), z)
f3 = Or(z, w)
f4 = x
f5 = Or(y,v)

f = And(f1, And(f2, And(f3, And(f4,f5))))

print(f.format())
print(f.cnfListForm())
print(f.truthTable())
print(f.truthTable().isSAT())
print(f.modelCount())
print()

# generate a random expression using 
# variables p,q,r with maxdepth = 5
f = randomExpression('pqr', 5)

print(f.format())
print(f.cnfListForm())
print(f.truthTable())
print(f.truthTable().isSAT())
print(f.modelCount())
