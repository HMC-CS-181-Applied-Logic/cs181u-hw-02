from propositional_logic import *

class IfThenElse(BoolExpression):
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def indented(self,d):
        result = TABWIDTH*d*' '
        result += "If(" + str(self.condition.format()) + ")\n"
        result += self.then_branch.indented(d + 1) + "\n"
        result += TABWIDTH*d*' ' + "else\n"
        result += self.else_branch.indented(d + 1)
        return result
    def format(self):
        return self.indented(0)
    def toBool(self):
        # Implement me!!!
        pass

class FunctionCall(BoolExpression):
    def __init__(self, fun_name):
        self.fun_name = fun_name
    def indented(self,d):
        result = TABWIDTH*d*' '
        result += "Call " + self.fun_name
        return result
    def toBool(self):
        # Implement me!!!
        pass
