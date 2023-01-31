from propositional_logic import *
from dpll import *
from random_expression import *


T = BoolConst(True)
F = BoolConst(False)

A = BoolVar("A")
B = BoolVar("B")
C = BoolVar("C")

u = BoolVar('u')
v = BoolVar('v')
w = BoolVar('w')
x = BoolVar('x')
y = BoolVar('y')
z = BoolVar('z')

f1 = Or(x,y)
f2 = Or(Not(x), z)
f3 = Or(z, w)
f4 = x
f5 = Or(y,v)

f = And(f1, And(f2, And(f3, And(f4,f5))))



def test_dpll_sat():
	assert dpll_sat(T)
	assert dpll_sat(Not(F))
	assert dpll_sat(Not(Not(T)))
	assert dpll_sat(A)
	assert dpll_sat(And(A,T))
	assert dpll_sat(Or(A,A))
	assert dpll_sat(Or(A,B))
	assert dpll_sat(Or(A,Or(B,Or(C,A))))
	assert dpll_sat(Or(Not(A),B))
	assert dpll_sat(Or(Not(A),A))
	assert dpll_sat(And(Not(A),B))
	assert dpll_sat(And(Not(A),Not(B)))
	assert dpll_sat(And(Not(A),Not(A)))
	assert dpll_sat(Implies(F, A))
	assert dpll_sat(Implies(A, F))
	assert dpll_sat(f1)
	assert dpll_sat(f2)
	assert dpll_sat(f3)
	assert dpll_sat(f4)
	assert dpll_sat(f5)
	assert dpll_sat(Iff(f1,f1))
	assert dpll_sat(Iff(f2,f2))
	assert dpll_sat(Iff(f3,f3))
	assert dpll_sat(Iff(f4,f4))
	assert dpll_sat(Iff(f5,f5))
	
	assert not dpll_sat(F)
	assert not dpll_sat(Not(T))
	assert not dpll_sat(And(A,F))
	assert not dpll_sat(And(F,A))
	assert not dpll_sat(And(A,Not(A)))
	assert not dpll_sat(And(A,Not(A)))
	assert not dpll_sat(And(f1, Not(f1)))
	assert not dpll_sat(And(f2, Not(f2)))
	assert not dpll_sat(And(f3, Not(f3)))
	assert not dpll_sat(And(f4, Not(f4)))
	assert not dpll_sat(And(f5, Not(f5)))
	assert not dpll_sat(Not(Iff(f1,f1)))
	assert not dpll_sat(Not(Iff(f2,f2)))
	assert not dpll_sat(Not(Iff(f3,f3)))
	assert not dpll_sat(Not(Iff(f4,f4)))
	assert not dpll_sat(Not(Iff(f5,f5)))

def test_dpll_sat_vs_tt_sat():
	assert dpll_sat(T)  == T.truthTable().isSAT()
	assert dpll_sat(Not(Not(T)))  == Not(Not(T)).truthTable().isSAT()
	assert dpll_sat(A)  == A.truthTable().isSAT()
	assert dpll_sat(And(A,T))  == And(A,T).truthTable().isSAT()
	assert dpll_sat(Or(A,A))  == Or(A,A).truthTable().isSAT()
	assert dpll_sat(Or(A,B))  == Or(A,B).truthTable().isSAT()
	assert dpll_sat(Or(A,Or(B,Or(C,A))))  == Or(A,Or(B,Or(C,A))).truthTable().isSAT()
	assert dpll_sat(Or(Not(A),B))  == Or(Not(A),B).truthTable().isSAT()
	assert dpll_sat(Or(Not(A),A))  == Or(Not(A),A).truthTable().isSAT()
	assert dpll_sat(And(Not(A),B))  == And(Not(A),B).truthTable().isSAT()
	assert dpll_sat(And(Not(A),Not(B)))  == And(Not(A),Not(B)).truthTable().isSAT()
	assert dpll_sat(And(Not(A),Not(A)))  == And(Not(A),Not(A)).truthTable().isSAT()
	assert dpll_sat(Implies(F, A))  == Implies(F, A).truthTable().isSAT()
	assert dpll_sat(Implies(A, F))  == Implies(A, F).truthTable().isSAT()
	assert dpll_sat(f1)  == f1.truthTable().isSAT()
	assert dpll_sat(f2)  == f2.truthTable().isSAT()
	assert dpll_sat(f3)  == f3.truthTable().isSAT()
	assert dpll_sat(f4)  == f4.truthTable().isSAT()
	assert dpll_sat(f5)  == f5.truthTable().isSAT()
	assert dpll_sat(Iff(f1,f1))  == Iff(f1,f1).truthTable().isSAT()
	assert dpll_sat(Iff(f2,f2))  == Iff(f2,f2).truthTable().isSAT()
	assert dpll_sat(Iff(f3,f3))  == Iff(f3,f3).truthTable().isSAT()
	assert dpll_sat(Iff(f4,f4))  == Iff(f4,f4).truthTable().isSAT()
	assert dpll_sat(Iff(f5,f5))  == Iff(f5,f5).truthTable().isSAT()
	assert dpll_sat(F)  == F.truthTable().isSAT()
	assert dpll_sat(Not(T))  == Not(T).truthTable().isSAT()
	assert dpll_sat(And(A,F))  == And(A,F).truthTable().isSAT()
	assert dpll_sat(And(F,A))  == And(F,A).truthTable().isSAT()
	assert dpll_sat(And(A,Not(A)))  == And(A,Not(A)).truthTable().isSAT()
	assert dpll_sat(And(A,Not(A)))  == And(A,Not(A)).truthTable().isSAT()
	assert dpll_sat(And(f1, Not(f1)))  == And(f1, Not(f1)).truthTable().isSAT()
	assert dpll_sat(And(f2, Not(f2)))  == And(f2, Not(f2)).truthTable().isSAT()
	assert dpll_sat(And(f3, Not(f3)))  == And(f3, Not(f3)).truthTable().isSAT()
	assert dpll_sat(And(f4, Not(f4)))  == And(f4, Not(f4)).truthTable().isSAT()
	assert dpll_sat(And(f5, Not(f5)))  == And(f5, Not(f5)).truthTable().isSAT()
	assert dpll_sat(Not(Iff(f1,f1)))  == Not(Iff(f1,f1)).truthTable().isSAT()
	assert dpll_sat(Not(Iff(f2,f2)))  == Not(Iff(f2,f2)).truthTable().isSAT()
	assert dpll_sat(Not(Iff(f3,f3)))  == Not(Iff(f3,f3)).truthTable().isSAT()
	assert dpll_sat(Not(Iff(f4,f4)))  == Not(Iff(f4,f4)).truthTable().isSAT()
	assert dpll_sat(Not(Iff(f5,f5)))  == Not(Iff(f5,f5)).truthTable().isSAT()

def test_dpll_model_count_vs_tt_count():
	assert dpll_model_count(T)  == T.modelCount()
	assert dpll_model_count(Not(Not(T)))  == Not(Not(T)).modelCount()
	assert dpll_model_count(A)  == A.modelCount()
	assert dpll_model_count(And(A,T))  == And(A,T).modelCount()
	assert dpll_model_count(Or(A,A))  == Or(A,A).modelCount()
	assert dpll_model_count(Or(A,B))  == Or(A,B).modelCount()
	assert dpll_model_count(Or(A,Or(B,Or(C,A))))  == Or(A,Or(B,Or(C,A))).modelCount()
	assert dpll_model_count(Or(Not(A),B))  == Or(Not(A),B).modelCount()
	assert dpll_model_count(Or(Not(A),A))  == Or(Not(A),A).modelCount()
	assert dpll_model_count(And(Not(A),B))  == And(Not(A),B).modelCount()
	assert dpll_model_count(And(Not(A),Not(B)))  == And(Not(A),Not(B)).modelCount()
	assert dpll_model_count(And(Not(A),Not(A)))  == And(Not(A),Not(A)).modelCount()
	assert dpll_model_count(Implies(F, A))  == Implies(F, A).modelCount()
	assert dpll_model_count(Implies(A, F))  == Implies(A, F).modelCount()
	assert dpll_model_count(f1)  == f1.modelCount()
	assert dpll_model_count(f2)  == f2.modelCount()
	assert dpll_model_count(f3)  == f3.modelCount()
	assert dpll_model_count(f4)  == f4.modelCount()
	assert dpll_model_count(f5)  == f5.modelCount()
	assert dpll_model_count(Iff(f1,f1))  == Iff(f1,f1).modelCount()
	assert dpll_model_count(Iff(f2,f2))  == Iff(f2,f2).modelCount()
	assert dpll_model_count(Iff(f3,f3))  == Iff(f3,f3).modelCount()
	assert dpll_model_count(Iff(f4,f4))  == Iff(f4,f4).modelCount()
	assert dpll_model_count(Iff(f5,f5))  == Iff(f5,f5).modelCount()
	assert dpll_model_count(F)  == F.modelCount()
	assert dpll_model_count(Not(T))  == Not(T).modelCount()
	assert dpll_model_count(And(A,F))  == And(A,F).modelCount()
	assert dpll_model_count(And(F,A))  == And(F,A).modelCount()
	assert dpll_model_count(And(A,Not(A)))  == And(A,Not(A)).modelCount()
	assert dpll_model_count(And(A,Not(A)))  == And(A,Not(A)).modelCount()
	assert dpll_model_count(And(f1, Not(f1)))  == And(f1, Not(f1)).modelCount()
	assert dpll_model_count(And(f2, Not(f2)))  == And(f2, Not(f2)).modelCount()
	assert dpll_model_count(And(f3, Not(f3)))  == And(f3, Not(f3)).modelCount()
	assert dpll_model_count(And(f4, Not(f4)))  == And(f4, Not(f4)).modelCount()
	assert dpll_model_count(And(f5, Not(f5)))  == And(f5, Not(f5)).modelCount()
	assert dpll_model_count(Not(Iff(f1,f1)))  == Not(Iff(f1,f1)).modelCount()
	assert dpll_model_count(Not(Iff(f2,f2)))  == Not(Iff(f2,f2)).modelCount()
	assert dpll_model_count(Not(Iff(f3,f3)))  == Not(Iff(f3,f3)).modelCount()
	assert dpll_model_count(Not(Iff(f4,f4)))  == Not(Iff(f4,f4)).modelCount()
	assert dpll_model_count(Not(Iff(f5,f5)))  == Not(Iff(f5,f5)).modelCount()

def test_allClausesSatisfied():
	clauses = [[T]]
	assert allClausesSatisfied(clauses)
	clauses = [[F, T]]
	assert allClausesSatisfied(clauses)
	clauses = [[T, F]]
	assert allClausesSatisfied(clauses)
	clauses = [[T, y]]
	assert allClausesSatisfied(clauses)
	clauses = [[T, z]]
	assert allClausesSatisfied(clauses)
	clauses = [[F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [T]]
	assert allClausesSatisfied(clauses)
	clauses = [[F, F, T]]
	assert allClausesSatisfied(clauses)
	clauses = [[F, F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, v]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, w]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x, y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[y, v]]
	assert not allClausesSatisfied(clauses)
	clauses = [[z, w]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(F), x]]
	assert allClausesSatisfied(clauses)
	clauses = [[F], [T]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F], [x]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(T)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x], [F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x], [T]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, F, F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, F, z]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, y, z]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x, y, z]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x), F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x), x]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x), y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x), z]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x, Not(x)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x)], [x]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x)], [y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [Not(y)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x], [Not(x)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, F, T], [F, F, T]]
	assert allClausesSatisfied(clauses)
	clauses = [[F, F], [T], [T]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, T], [T], [F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x)], [Not(y)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, v], [T], [Not(v)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, w], [T], [Not(w)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, y], [T], [Not(y)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, z], [T], [Not(z)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T, v], [F], [Not(v)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T, w], [F], [Not(w)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T, y], [F], [Not(y)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T, z], [F], [Not(z)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T, z, F], [T, z, Not(z)]]
	assert allClausesSatisfied(clauses)
	clauses = [[F, v, T], [F, v, Not(v)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, w, T], [F, w, Not(w)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F, y, T], [F, y, Not(y)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x), z], [x], [Not(z)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x, y], [Not(x)], [Not(y)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[y, v], [Not(y)], [Not(v)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[z, w], [Not(z)], [Not(w)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x, y, Not(x)], [x, y, Not(y)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[y, v, Not(y)], [y, v, Not(v)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[z, w, Not(z)], [z, w, Not(w)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [T, F], [F, T], [F], [F, T]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [T, T], [T, T], [T], [F, F]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x), z, x], [Not(x), z, Not(z)]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F], [F, Not(v)], [Not(v), F], [Not(v)], [T, v]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F], [F, Not(w)], [Not(w), F], [Not(w)], [T, w]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F], [F, Not(y)], [Not(y), F], [Not(y)], [T, y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[F], [F, Not(z)], [Not(z), F], [Not(z)], [T, z]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [T, Not(v)], [Not(v), T], [Not(v)], [F, v]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [T, Not(w)], [Not(w), T], [Not(w)], [F, w]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [T, Not(y)], [Not(y), T], [Not(y)], [F, y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[T], [T, Not(z)], [Not(z), T], [Not(z)], [F, z]]
	assert not allClausesSatisfied(clauses)
	clauses = [[x], [x, Not(z)], [Not(z), x], [Not(z)], [Not(x), z]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(x)], [Not(x), Not(y)], [Not(y), Not(x)], [Not(y)], [x, y]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(y)], [Not(y), Not(v)], [Not(v), Not(y)], [Not(v)], [y, v]]
	assert not allClausesSatisfied(clauses)
	clauses = [[Not(z)], [Not(z), Not(w)], [Not(w), Not(z)], [Not(w)], [z, w]]
	assert not allClausesSatisfied(clauses)

def test_allDisjunctsUNSAT():
	disjuncts = [F]
	assert allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, F]
	assert allDisjunctsUNSAT(disjuncts)
	disjuncts = [T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [x]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [y]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(T)]
	assert allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, F, F]
	assert allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, v]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, w]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, y]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, z]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, F]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, v]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, w]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, y]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, z]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [x, y]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [y, v]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [z, w]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(v)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(w)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(z)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, F, z]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, v, T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, w, T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, y, T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, y, z]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [x, y, z]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, Not(v)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, Not(w)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, Not(z)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(v), F]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(v), T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(w), F]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(w), T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x), F]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x), x]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x), y]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x), z]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(y), F]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(y), T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(z), F]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(z), T]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(z), x]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, Not(v)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, Not(w)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [T, Not(z)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [x, Not(x)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [x, Not(z)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, v, Not(v)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, w, Not(w)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [F, y, Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x), z, x]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [x, y, Not(x)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [x, y, Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [y, v, Not(v)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [y, v, Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [z, w, Not(w)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [z, w, Not(z)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(v), Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(w), Not(z)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x), Not(y)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(y), Not(v)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(y), Not(x)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(z), Not(w)]
	assert not allDisjunctsUNSAT(disjuncts)
	disjuncts = [Not(x), z, Not(z)]
	assert not allDisjunctsUNSAT(disjuncts)



def test_containsUNSATClause():
	clauses = [[F]]
	assert containsUNSATClause(clauses)
	clauses = [[F, F]]
	assert containsUNSATClause(clauses)
	clauses = [[x]]
	assert not containsUNSATClause(clauses)
	clauses = [[F], [T]]
	assert containsUNSATClause(clauses)
	clauses = [[F], [x]]
	assert containsUNSATClause(clauses)
	clauses = [[Not(T)]]
	assert containsUNSATClause(clauses)
	clauses = [[T], [F]]
	assert containsUNSATClause(clauses)
	clauses = [[x], [F]]
	assert containsUNSATClause(clauses)
	clauses = [[F, F, F]]
	assert containsUNSATClause(clauses)
	clauses = [[F, v]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, w]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, y]]
	assert not containsUNSATClause(clauses)
	clauses = [[x, y]]
	assert not containsUNSATClause(clauses)
	clauses = [[y, v]]
	assert not containsUNSATClause(clauses)
	clauses = [[z, w]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x)]]
	assert not containsUNSATClause(clauses)
	clauses = [[T], [y]]
	assert not containsUNSATClause(clauses)
	clauses = [[x], [T]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, F, z]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, y, z]]
	assert not containsUNSATClause(clauses)
	clauses = [[x, y, z]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x), F]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x), x]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x), y]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x), z]]
	assert not containsUNSATClause(clauses)
	clauses = [[x, Not(x)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, F], [T], [T]]
	assert containsUNSATClause(clauses)
	clauses = [[F, T], [T], [F]]
	assert containsUNSATClause(clauses)
	clauses = [[Not(x)], [x]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x)], [y]]
	assert not containsUNSATClause(clauses)
	clauses = [[T], [Not(y)]]
	assert not containsUNSATClause(clauses)
	clauses = [[x], [Not(x)]]
	assert not containsUNSATClause(clauses)
	clauses = [[T, v], [F], [Not(v)]]
	assert containsUNSATClause(clauses)
	clauses = [[T, w], [F], [Not(w)]]
	assert containsUNSATClause(clauses)
	clauses = [[T, y], [F], [Not(y)]]
	assert containsUNSATClause(clauses)
	clauses = [[T, z], [F], [Not(z)]]
	assert containsUNSATClause(clauses)
	clauses = [[Not(x)], [Not(y)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, v], [T], [Not(v)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, w], [T], [Not(w)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, y], [T], [Not(y)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, z], [T], [Not(z)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, v, T], [F, v, Not(v)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, w, T], [F, w, Not(w)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F, y, T], [F, y, Not(y)]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x), z], [x], [Not(z)]]
	assert not containsUNSATClause(clauses)
	clauses = [[x, y], [Not(x)], [Not(y)]]
	assert not containsUNSATClause(clauses)
	clauses = [[y, v], [Not(y)], [Not(v)]]
	assert not containsUNSATClause(clauses)
	clauses = [[z, w], [Not(z)], [Not(w)]]
	assert not containsUNSATClause(clauses)
	clauses = [[T], [T, F], [F, T], [F], [F, T]]
	assert containsUNSATClause(clauses)
	clauses = [[T], [T, T], [T, T], [T], [F, F]]
	assert containsUNSATClause(clauses)
	clauses = [[x, y, Not(x)], [x, y, Not(y)]]
	assert not containsUNSATClause(clauses)
	clauses = [[y, v, Not(y)], [y, v, Not(v)]]
	assert not containsUNSATClause(clauses)
	clauses = [[z, w, Not(z)], [z, w, Not(w)]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x), z, x], [Not(x), z, Not(z)]]
	assert not containsUNSATClause(clauses)
	clauses = [[F], [F, Not(v)], [Not(v), F], [Not(v)], [T, v]]
	assert containsUNSATClause(clauses)
	clauses = [[F], [F, Not(w)], [Not(w), F], [Not(w)], [T, w]]
	assert containsUNSATClause(clauses)
	clauses = [[F], [F, Not(y)], [Not(y), F], [Not(y)], [T, y]]
	assert containsUNSATClause(clauses)
	clauses = [[F], [F, Not(z)], [Not(z), F], [Not(z)], [T, z]]
	assert containsUNSATClause(clauses)
	clauses = [[T], [T, Not(v)], [Not(v), T], [Not(v)], [F, v]]
	assert not containsUNSATClause(clauses)
	clauses = [[T], [T, Not(w)], [Not(w), T], [Not(w)], [F, w]]
	assert not containsUNSATClause(clauses)
	clauses = [[T], [T, Not(y)], [Not(y), T], [Not(y)], [F, y]]
	assert not containsUNSATClause(clauses)
	clauses = [[T], [T, Not(z)], [Not(z), T], [Not(z)], [F, z]]
	assert not containsUNSATClause(clauses)
	clauses = [[x], [x, Not(z)], [Not(z), x], [Not(z)], [Not(x), z]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(x)], [Not(x), Not(y)], [Not(y), Not(x)], [Not(y)], [x, y]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(y)], [Not(y), Not(v)], [Not(v), Not(y)], [Not(v)], [y, v]]
	assert not containsUNSATClause(clauses)
	clauses = [[Not(z)], [Not(z), Not(w)], [Not(w), Not(z)], [Not(w)], [z, w]]
	assert not containsUNSATClause(clauses)




def test_someDisjunctSatisfied():
	disjuncts = [T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [F, T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, F]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, v]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, w]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, y]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, z]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [x]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [y]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, F, T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [F, v, T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [F, w, T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [F, y, T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, z, F]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [F, F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, v]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, w]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, y]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, z]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [x, y]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [y, v]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [z, w]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(F), x]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(v), T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(w), T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(y), T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(z), T]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, Not(v)]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, Not(w)]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, Not(y)]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [T, Not(z)]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(T)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(v)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(w)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(y)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(z)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, F, F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, F, z]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, y, z]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [x, y, z]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [T, z, Not(z)]
	assert someDisjunctSatisfied(disjuncts)
	disjuncts = [F, Not(v)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, Not(w)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, Not(y)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, Not(z)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(v), F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(w), F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x), F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x), x]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x), y]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x), z]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(y), F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(z), F]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(z), x]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [x, Not(x)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [x, Not(z)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, v, Not(v)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, w, Not(w)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [F, y, Not(y)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x), z, x]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [x, y, Not(x)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [x, y, Not(y)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [y, v, Not(v)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [y, v, Not(y)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [z, w, Not(w)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [z, w, Not(z)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(v), Not(y)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(w), Not(z)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x), Not(y)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(y), Not(v)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(y), Not(x)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(z), Not(w)]
	assert not someDisjunctSatisfied(disjuncts)
	disjuncts = [Not(x), z, Not(z)]
	assert not someDisjunctSatisfied(disjuncts)





def test_replaceInAllDisjuncts():
	disjuncts = [T]
	var = v
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = v
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = w
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = w
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [T]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [x]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F]
	disjuncts = [x]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [y]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [y]
	disjuncts = [y]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [y]
	disjuncts = [y]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F]
	disjuncts = [y]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [Not(v)]
	var = v
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [Not(v)]
	var = v
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F]
	disjuncts = [Not(w)]
	var = w
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [Not(w)]
	var = w
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F]
	disjuncts = [Not(x)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [Not(x)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F]
	disjuncts = [Not(y)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [Not(y)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F]
	disjuncts = [Not(z)]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T]
	disjuncts = [Not(z)]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F]
	disjuncts = [F, v]
	var = v
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F]
	disjuncts = [F, v]
	var = v
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [F, w]
	var = w
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F]
	disjuncts = [F, w]
	var = w
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [F, y]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F]
	disjuncts = [F, y]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [F, z]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F]
	disjuncts = [F, z]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [x, y]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, y]
	disjuncts = [x, y]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, y]
	disjuncts = [y, v]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, v]
	disjuncts = [y, v]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, v]
	disjuncts = [z, w]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, w]
	disjuncts = [z, w]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, w]
	disjuncts = [Not(v)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(v)]
	disjuncts = [Not(v)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(v)]
	disjuncts = [Not(w)]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(w)]
	disjuncts = [Not(w)]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(w)]
	disjuncts = [Not(y)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(y)]
	disjuncts = [Not(y)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(y)]
	disjuncts = [Not(z)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(z)]
	disjuncts = [Not(z)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(z)]
	disjuncts = [Not(v), T]
	var = v
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [Not(v), T]
	var = v
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [Not(w), T]
	var = w
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [Not(w), T]
	var = w
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [Not(x), F]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, F]
	disjuncts = [Not(x), F]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F]
	disjuncts = [Not(x), x]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, F]
	disjuncts = [Not(x), x]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [Not(x), y]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, y]
	disjuncts = [Not(x), y]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, y]
	disjuncts = [Not(x), z]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, z]
	disjuncts = [Not(x), z]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, z]
	disjuncts = [Not(y), T]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [Not(y), T]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [Not(z), T]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [Not(z), T]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [T, Not(v)]
	var = v
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [T, Not(v)]
	var = v
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, F]
	disjuncts = [T, Not(w)]
	var = w
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [T, Not(w)]
	var = w
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, F]
	disjuncts = [T, Not(y)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [T, Not(y)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, F]
	disjuncts = [T, Not(z)]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, T]
	disjuncts = [T, Not(z)]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, F]
	disjuncts = [x, Not(x)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T]
	disjuncts = [x, Not(x)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, F]
	disjuncts = [F, F, z]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, F]
	disjuncts = [F, F, z]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, T]
	disjuncts = [F, v, T]
	var = v
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, T]
	disjuncts = [F, v, T]
	var = v
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T, T]
	disjuncts = [F, w, T]
	var = w
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, T]
	disjuncts = [F, w, T]
	var = w
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T, T]
	disjuncts = [F, y, T]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, T]
	disjuncts = [F, y, T]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T, T]
	disjuncts = [F, y, z]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, z]
	disjuncts = [F, y, z]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T, z]
	disjuncts = [x, y, z]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, y, z]
	disjuncts = [x, y, z]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, y, z]
	disjuncts = [Not(z), x]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(z), F]
	disjuncts = [Not(z), x]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(z), T]
	disjuncts = [x, Not(z)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, Not(z)]
	disjuncts = [x, Not(z)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, Not(z)]
	disjuncts = [F, v, Not(v)]
	var = v
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, T]
	disjuncts = [F, v, Not(v)]
	var = v
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T, F]
	disjuncts = [F, w, Not(w)]
	var = w
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, T]
	disjuncts = [F, w, Not(w)]
	var = w
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T, F]
	disjuncts = [F, y, Not(y)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, F, T]
	disjuncts = [F, y, Not(y)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, T, F]
	disjuncts = [Not(x), z, x]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, z, F]
	disjuncts = [Not(x), z, x]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, z, T]
	disjuncts = [x, y, Not(x)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, y, T]
	disjuncts = [x, y, Not(x)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, y, F]
	disjuncts = [y, v, Not(y)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, v, T]
	disjuncts = [y, v, Not(y)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, v, F]
	disjuncts = [z, w, Not(z)]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, w, T]
	disjuncts = [z, w, Not(z)]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, w, F]
	disjuncts = [Not(v), Not(y)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(v), T]
	disjuncts = [Not(v), Not(y)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(v), F]
	disjuncts = [Not(w), Not(z)]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(w), T]
	disjuncts = [Not(w), Not(z)]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(w), F]
	disjuncts = [Not(x), Not(y)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, Not(y)]
	disjuncts = [Not(x), Not(y)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, Not(y)]
	disjuncts = [Not(y), Not(v)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, Not(v)]
	disjuncts = [Not(y), Not(v)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, Not(v)]
	disjuncts = [Not(y), Not(x)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(y), T]
	disjuncts = [Not(y), Not(x)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [Not(y), F]
	disjuncts = [Not(z), Not(w)]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, Not(w)]
	disjuncts = [Not(z), Not(w)]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, Not(w)]
	disjuncts = [x, y, Not(y)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, y, Not(y)]
	disjuncts = [x, y, Not(y)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, y, Not(y)]
	disjuncts = [y, v, Not(v)]
	var = y
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, v, Not(v)]
	disjuncts = [y, v, Not(v)]
	var = y
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, v, Not(v)]
	disjuncts = [z, w, Not(w)]
	var = z
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, w, Not(w)]
	disjuncts = [z, w, Not(w)]
	var = z
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, w, Not(w)]
	disjuncts = [Not(x), z, Not(z)]
	var = x
	e = F
	assert replaceInAllDisjuncts(disjuncts, var, e) == [T, z, Not(z)]
	disjuncts = [Not(x), z, Not(z)]
	var = x
	e = T
	assert replaceInAllDisjuncts(disjuncts, var, e) == [F, z, Not(z)]


def test_replaceInAllClauses():
	clauses = [[x]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F]]
	clauses = [[x]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T]]
	clauses = [[Not(x)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T]]
	clauses = [[Not(x)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F]]
	clauses = [[F, v]]
	var = v
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F]]
	clauses = [[F, v]]
	var = v
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T]]
	clauses = [[F, w]]
	var = w
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F]]
	clauses = [[F, w]]
	var = w
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T]]
	clauses = [[F, y]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F]]
	clauses = [[F, y]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T]]
	clauses = [[x, y]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, y]]
	clauses = [[x, y]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, y]]
	clauses = [[y, v]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, v]]
	clauses = [[y, v]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, v]]
	clauses = [[z, w]]
	var = z
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, w]]
	clauses = [[z, w]]
	var = z
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, w]]
	clauses = [[T], [y]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [F]]
	clauses = [[T], [y]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [T]]
	clauses = [[x], [T]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F], [T]]
	clauses = [[x], [T]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [T]]
	clauses = [[Not(x), F]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T, F]]
	clauses = [[Not(x), F]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, F]]
	clauses = [[Not(x), x]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T, F]]
	clauses = [[Not(x), x]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T]]
	clauses = [[Not(x), y]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T, y]]
	clauses = [[Not(x), y]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, y]]
	clauses = [[Not(x), z]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T, z]]
	clauses = [[Not(x), z]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, z]]
	clauses = [[x, Not(x)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, T]]
	clauses = [[x, Not(x)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, F]]
	clauses = [[F, F, z]]
	var = z
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F, F]]
	clauses = [[F, F, z]]
	var = z
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, F, T]]
	clauses = [[F, y, z]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F, z]]
	clauses = [[F, y, z]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T, z]]
	clauses = [[x, y, z]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, y, z]]
	clauses = [[x, y, z]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, y, z]]
	clauses = [[Not(x)], [x]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [F]]
	clauses = [[Not(x)], [x]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F], [T]]
	clauses = [[Not(x)], [y]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [y]]
	clauses = [[Not(x)], [y]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F], [y]]
	clauses = [[T], [Not(y)]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T]]
	clauses = [[T], [Not(y)]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [F]]
	clauses = [[x], [Not(x)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F], [T]]
	clauses = [[x], [Not(x)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [F]]
	clauses = [[Not(x)], [Not(y)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [Not(y)]]
	clauses = [[Not(x)], [Not(y)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F], [Not(y)]]
	clauses = [[F, v], [T], [Not(v)]]
	var = v
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F], [T], [T]]
	clauses = [[F, v], [T], [Not(v)]]
	var = v
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T], [T], [F]]
	clauses = [[F, w], [T], [Not(w)]]
	var = w
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F], [T], [T]]
	clauses = [[F, w], [T], [Not(w)]]
	var = w
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T], [T], [F]]
	clauses = [[F, y], [T], [Not(y)]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F], [T], [T]]
	clauses = [[F, y], [T], [Not(y)]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T], [T], [F]]
	clauses = [[F, z], [T], [Not(z)]]
	var = z
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F], [T], [T]]
	clauses = [[F, z], [T], [Not(z)]]
	var = z
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T], [T], [F]]
	clauses = [[F, v, T], [F, v, Not(v)]]
	var = v
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F, T], [F, F, T]]
	clauses = [[F, v, T], [F, v, Not(v)]]
	var = v
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T, T], [F, T, F]]
	clauses = [[F, w, T], [F, w, Not(w)]]
	var = w
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F, T], [F, F, T]]
	clauses = [[F, w, T], [F, w, Not(w)]]
	var = w
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T, T], [F, T, F]]
	clauses = [[F, y, T], [F, y, Not(y)]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, F, T], [F, F, T]]
	clauses = [[F, y, T], [F, y, Not(y)]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, T, T], [F, T, F]]
	clauses = [[Not(x), z], [x], [Not(z)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T, z], [F], [Not(z)]]
	clauses = [[Not(x), z], [x], [Not(z)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, z], [T], [Not(z)]]
	clauses = [[x, y], [Not(x)], [Not(y)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, y], [T], [Not(y)]]
	clauses = [[x, y], [Not(x)], [Not(y)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, y], [F], [Not(y)]]
	clauses = [[y, v], [Not(y)], [Not(v)]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, v], [T], [Not(v)]]
	clauses = [[y, v], [Not(y)], [Not(v)]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, v], [F], [Not(v)]]
	clauses = [[z, w], [Not(z)], [Not(w)]]
	var = z
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, w], [T], [Not(w)]]
	clauses = [[z, w], [Not(z)], [Not(w)]]
	var = z
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, w], [F], [Not(w)]]
	clauses = [[x, y, Not(x)], [x, y, Not(y)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, y, T], [F, y, Not(y)]]
	clauses = [[x, y, Not(x)], [x, y, Not(y)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, y, F], [T, y, Not(y)]]
	clauses = [[y, v, Not(y)], [y, v, Not(v)]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, v, T], [F, v, Not(v)]]
	clauses = [[y, v, Not(y)], [y, v, Not(v)]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, v, F], [T, v, Not(v)]]
	clauses = [[z, w, Not(z)], [z, w, Not(w)]]
	var = z
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F, w, T], [F, w, Not(w)]]
	clauses = [[z, w, Not(z)], [z, w, Not(w)]]
	var = z
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T, w, F], [T, w, Not(w)]]
	clauses = [[Not(x), z, x], [Not(x), z, Not(z)]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T, z, F], [T, z, Not(z)]]
	clauses = [[Not(x), z, x], [Not(x), z, Not(z)]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F, z, T], [F, z, Not(z)]]
	clauses = [[T], [T, Not(v)], [Not(v), T], [Not(v)], [F, v]]
	var = v
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, T], [T, T], [T], [F, F]]
	clauses = [[T], [T, Not(v)], [Not(v), T], [Not(v)], [F, v]]
	var = v
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, F], [F, T], [F], [F, T]]
	clauses = [[T], [T, Not(w)], [Not(w), T], [Not(w)], [F, w]]
	var = w
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, T], [T, T], [T], [F, F]]
	clauses = [[T], [T, Not(w)], [Not(w), T], [Not(w)], [F, w]]
	var = w
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, F], [F, T], [F], [F, T]]
	clauses = [[T], [T, Not(y)], [Not(y), T], [Not(y)], [F, y]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, T], [T, T], [T], [F, F]]
	clauses = [[T], [T, Not(y)], [Not(y), T], [Not(y)], [F, y]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, F], [F, T], [F], [F, T]]
	clauses = [[T], [T, Not(z)], [Not(z), T], [Not(z)], [F, z]]
	var = z
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, T], [T, T], [T], [F, F]]
	clauses = [[T], [T, Not(z)], [Not(z), T], [Not(z)], [F, z]]
	var = z
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, F], [F, T], [F], [F, T]]
	clauses = [[x], [x, Not(z)], [Not(z), x], [Not(z)], [Not(x), z]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[F], [F, Not(z)], [Not(z), F], [Not(z)], [T, z]]
	clauses = [[x], [x, Not(z)], [Not(z), x], [Not(z)], [Not(x), z]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, Not(z)], [Not(z), T], [Not(z)], [F, z]]
	clauses = [[Not(x)], [Not(x), Not(y)], [Not(y), Not(x)], [Not(y)], [x, y]]
	var = x
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, Not(y)], [Not(y), T], [Not(y)], [F, y]]
	clauses = [[Not(x)], [Not(x), Not(y)], [Not(y), Not(x)], [Not(y)], [x, y]]
	var = x
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F], [F, Not(y)], [Not(y), F], [Not(y)], [T, y]]
	clauses = [[Not(y)], [Not(y), Not(v)], [Not(v), Not(y)], [Not(v)], [y, v]]
	var = y
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, Not(v)], [Not(v), T], [Not(v)], [F, v]]
	clauses = [[Not(y)], [Not(y), Not(v)], [Not(v), Not(y)], [Not(v)], [y, v]]
	var = y
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F], [F, Not(v)], [Not(v), F], [Not(v)], [T, v]]
	clauses = [[Not(z)], [Not(z), Not(w)], [Not(w), Not(z)], [Not(w)], [z, w]]
	var = z
	e = F
	assert replaceInAllClauses(clauses, var, e) == [[T], [T, Not(w)], [Not(w), T], [Not(w)], [F, w]]
	clauses = [[Not(z)], [Not(z), Not(w)], [Not(w), Not(z)], [Not(w)], [z, w]]
	var = z
	e = T
	assert replaceInAllClauses(clauses, var, e) == [[F], [F, Not(w)], [Not(w), F], [Not(w)], [T, w]]


