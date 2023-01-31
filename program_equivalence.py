from propositional_logic import *
from dpll import *
from if_then_else_programs import *

A = BoolVar('A')
B = BoolVar('B')

program1 = IfThenElse(And(Not(A), Not(B)), 
		FunctionCall('h'),
		IfThenElse(Not(A),
			FunctionCall('g'),
			FunctionCall('f')
		)
	)
	
program2 = IfThenElse(A,
				FunctionCall('f'),
				IfThenElse(Not(B),
					FunctionCall('g'),
					FunctionCall('h')
					)
				)

program3 = IfThenElse(A,
				FunctionCall('f'),
				IfThenElse(B,
					FunctionCall('g'),
					FunctionCall('h')
					)
				)

def equiv_programs(P1, P2):
	# Implement me!
	pass
	
print("Program 1")
print(program1.format())
print()

print("Program 2")
print(program2.format())
print()

print("Program 3")
print(program3.format())
print()


print("Is program1 equivalent to itself?")
print(equiv_programs(program1, program1))
print()

print("Is program1 equivalent to program2?")
print(equiv_programs(program1, program2))
print()

print("Is program2 equivalent to itself?")
print(equiv_programs(program2, program2))
print()

print("Is program2 equivalent to program3?")
print(equiv_programs(program2, program3))
print()

print("Is program3 equivalent to itself?")
print(equiv_programs(program3, program3))
print()

print("Is program1 equivalent to program3?")
print(equiv_programs(program1, program3))
print()