from propositional_logic import *
from dpll import *
import random


def randomVar(varNameList):
	return BoolVar(random.choice(varNameList))

def randomTruthValue():
	return random.choice([BoolConst(True), BoolConst(False)])

def randomExpression(varNameList, maxDepth):
	if(maxDepth < 1):
		return BoolVar(random.choice(varNameList))
	expChoice = random.choice(['binary', 'unary', 'variable'])#, 'constant'])
	if expChoice == 'constant':
		return randomTruthValue()
	elif expChoice == 'variable':
		return randomVar(varNameList)
	elif expChoice == 'unary':
		return Not(randomExpression(varNameList, maxDepth - 1))
	else:
		constructor = random.choice([And, Or, Implies, Iff])
		left_sub_exp = randomExpression(varNameList, maxDepth - 1)
		right_sub_exp = randomExpression(varNameList, maxDepth - 1)
		return constructor(left_sub_exp, right_sub_exp)

def random_sat_test(n):
	varNameList = 'uvwxyz'
	for i in range(n):
		rand_exp = randomExpression(varNameList, 4)
		# print(rand_exp.format())
		dpll_sat_result = dpll_sat(rand_exp)
		tt_sat_result = rand_exp.truthTable().isSAT()
		if(dpll_sat_result != tt_sat_result):
			print("ERROR")
			print(rand_exp)
			print(rand_exp.format())
			print(dpll_sat_result)
			print(tt_sat_result)

def random_count_test(n):
	varNameList = 'uvwxyz'
	for i in range(n):
		rand_exp = randomExpression(varNameList, 4)
		# print(rand_exp.format())
		dpll_count_result = dpll_model_count(rand_exp)
		tt_count_result = rand_exp.modelCount()
		# print(tt_count_result)
		if(dpll_count_result != tt_count_result):
			print("ERROR")
			print(rand_exp)
			print(rand_exp.format())
			print(dpll_sat_result)
			print(tt_sat_result)

