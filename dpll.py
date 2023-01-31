from propositional_logic import *

# replace v by e in all disjuncts
# and return resulting list of clauses
def replaceInAllDisjuncts(disjuncts, v, e):
	# Implement me!!!
	pass

# replace v by e in all clauses 
# and return resulting list of clauses
def replaceInAllClauses(clauses, v, e):
	# Implement me!!!
	# You should call your replaceInAllDisjuncts function
	pass

# check if all disjuncts are unsat
# and return True or False
def allDisjunctsUNSAT(disjuncts):
	# Implement me!!!
	pass

# check if clauses contains an UNSAT clause
# and return True or False
def containsUNSATClause(clauses):
	# Implement me!!!
	# You should call your allDisjunctsUNSAT function
	pass

# check if disjuncts has some satisfied disjunct
# and return True or False
def someDisjunctSatisfied(disjuncts):
	# Implement me!!!
	pass

# check if all clauses are satisfied
# and return True or False
def allClausesSatisfied(clauses):
	# Implement me!!!
	pass

# the main dpll_sat funcion
# nothing to do here, it just calls the helper dpll
def dpll_sat(f):
	varlist = f.getVars()
	clauses = f.cnfListForm()
	return dpll(clauses, varlist)

def dpll(clauses, varlist):
	# Implement me!!!
	pass

# the main dpll_model_count funcion
# nothing to do here, it just calls the helper dpll_count
def dpll_model_count(f):
	varlist = f.getVars()
	clauses = f.cnfListForm()
	return dpll_count(clauses, varlist, len(varlist))

def dpll_count(clauses, varlist, t):
	# Implement me!!!
	pass

def equiv_dpll(f1, f2):
	# Implement me!!!
	pass

