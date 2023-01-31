TABWIDTH = 2

class BoolExpression(object):
    def __init__(self):
        super()
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return self.__class__.__name__ + "(" + ", ".join([str(v) for v in self.__dict__.values()]) + ")"
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return(hash(str(self)))
    def getVars(self):
        return []
    def eval(self, interp):
        return BoolConst(False)
    def truthTable(self):
        vars = self.getVars()
        interps = allInterpretations(vars)
        truthValues = []
        for i in interps:
            truthValues.append(self.eval(i))
        return TruthTable(vars, interps, truthValues)
    def isSAT(self):
        return self.truthTable().isSAT()
    def indented(self, d):
        return ''
    def treeView(self):
        print(self.indented(0))
    def equiv(self, other):
        return Iff(self, other).tautology()
    def tautology(self):
        return not Not(self).isSAT()
    def isLiteral(self):
        return False
    def isAtom(self):
        return False
    def removeImplications(self):
        return self
    def NNF(self):
        return self
    def isNNF(self):
        return False;
    def cnf(self):
        imp_free_NNF_exp = self.removeImplications().NNF()
        return self.cnf_helper(imp_free_NNF_exp) #.cnf_helper()
    @staticmethod
    def cnf_helper(exp):
        if exp.isLiteral():
            return exp
        elif isinstance(exp, And):
            return And(exp.cnf_helper(exp.exp1), exp.cnf_helper(exp.exp2))
        else:
            return distrOr(exp.cnf_helper(exp.exp1), exp.cnf_helper(exp.exp2))
    def disjunctsList(self):
        return [self]
    def conjunctsList(self):
        return [self]
    def cnfListForm(self):
        conjuncts = self.cnf().conjunctsList()
        return uniqueList([uniqueList(c.disjunctsList()) for c in conjuncts])
    def getModel(self):
        t = self.truthTable()
        i = t.truthValues.index(BoolConst(True))
        m = t.interps[i]
        return m
    def modelCount(self):
        tt = self.truthTable()
        return tt.truthValues.count(BoolConst(True))

class TruthTable(object):
    def __init__(self, vars, interps, truthValues):
        self.vars = vars
        self.interps = interps
        self.truthValues = truthValues
    def __repr__(self):
        return str(self)
    def __str__(self):
        tableString = '\n'
        for v in self.vars:
            tableString += v.name + '\t'
        tableString += '|\n'
        tableString += '----'*len(tableString) + '\n'
        for i in range(len(self.truthValues)):
            for v in self.vars:
                tableString += self.interps[i][v].format() + '\t'
            tableString += '|\t' + self.truthValues[i].format() + '\n'
        return tableString
    def isSAT(self):
        return BoolConst(True) in self.truthValues


class BoolConst(BoolExpression):
    def __init__(self, val):
        self.val = val
    def format(self):
        return "T" if self.val else "F"
    def tex(self):
        return self.format()
    def eval(self, interp):
        return self
    def NNF(self):
        return self
    def getVars(self):
        return []
    def replace1(self, var, exp):
        return self
    def simplify(self):
        return self
    def indented(self,d):
        return TABWIDTH*d*' ' + str(self.val)
    def removeImplications(self):
        return self
    def isLiteral(self):
        return True 
    def isAtom(self):
        return True
    def isNNF(self):
        return True
    def isPureDisjunctive(self):
        return True
    def isCNF(self):
        return True

class BoolVar(BoolExpression):
    def __init__(self, name):
        self.name = name
    def format(self):
        return str(self.name)
    def tex(self):
        return self.format()
    def eval(self, interp):
        return interp[self]
    def NNF(self):
        return self
    def getVars(self):
        return [self]
    def replace1(self, var, exp):
        return exp if var == self else self
    def simplify(self):
        return self
    def indented(self,d):
        return TABWIDTH*d*' ' + str(self.name)
    def removeImplications(self):
        return self
    def isAtom(self):
        return True
    def isLiteral(self):
        return True 
    def isNNF(self):
        return True
    def isPureDisjunctive(self):
        return True
    def isCNF(self):
        return True

class Not(BoolExpression):
    def __init__(self, exp):
        self.exp = exp
    def format(self):
        return "~" + self.exp.format()
    def tex(self):
        return '\\not ' + self.exp.tex()
    def eval(self, interp):
        val = self.exp.eval(interp)
        return BoolConst(not val.val)
    def NNF(self):
        if isinstance(self.exp, Not):
            return self.exp.exp.NNF()
        elif isinstance(self.exp, And):
            return Or(Not(self.exp.exp1).NNF(), Not(self.exp.exp2).NNF())
        elif isinstance(self.exp, Or):
            return And(Not(self.exp.exp1).NNF(), Not(self.exp.exp2).NNF())
        elif isinstance(self.exp, Implies):
            return And(self.exp.exp1.NNF(), Not(self.exp.exp2).NNF())
        elif isinstance(self.exp, Iff):
            return Not(And(Implies(self.exp.exp1, self.exp.exp2),Implies(self.exp.exp2, self.exp.exp1))).NNF()
            # return And(self.exp.exp1.NNF(), Not(self.exp.exp2).NNF())
        else:
            return self
    def getVars(self):
        return uniqueList(self.exp.getVars())
    def replace1(self, var, exp):
        return Not(self.exp.replace1(var, exp))
    def simplify(self):
        expSimplified = self.exp.simplify()
        if isinstance(expSimplified, BoolConst):
            return BoolConst(not expSimplified.val) 
        elif isinstance(expSimplified, Not):
            return expSimplified.name
        else:
            return Not(expSimplified)
    def indented(self,d):
        return TABWIDTH*d*' ' + "Not\n" + self.exp.indented(d + 1) + "\n"
    def removeImplications(self):
        return Not(self.exp.removeImplications())
    def isLiteral(self):
        return isinstance(self.exp, BoolConst) or isinstance(self.exp, BoolVar)
    def isNNF(self):
        return self.isLiteral()
    def isPureDisjunctive(self):
        return self.isLiteral()
    def isCNF(self):
        return self.isPureDisjunctive()


class And(BoolExpression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " & " + self.exp2.format() + ")"
    def tex(self):
        return "(" + self.exp1.tex() + " \\land " + self.exp2.tex() + ")"
    def eval(self, interp):
        val1 = self.exp1.eval(interp)
        val2 = self.exp2.eval(interp)
        return BoolConst(val1.val and val2.val)
    def NNF(self):
        return And(self.exp1.NNF(), self.exp2.NNF())
    def getVars(self):
        return uniqueList(self.exp1.getVars() + self.exp2.getVars())
    def replace1(self, var, exp):
        return And(self.exp1.replace1(var, exp), self.exp2.replace1(var, exp))
    def simplify(self):
        expSimplified1 = self.exp1.simplify()
        expSimplified2 = self.exp2.simplify()
        if expSimplified1 == BoolConst(False):
            return BoolConst(False)
        elif expSimplified1 == BoolConst(True):
            return expSimplified2
        elif expSimplified2 == BoolConst(True):
            return expSimplified1
        elif expSimplified2 == BoolConst(False):
            return BoolConst(False)
        elif expSimplified1 == expSimplified2:
            return expSimplified1
        else:
            return And(expSimplified1, expSimplified2)
    def indented(self,d):
        result = TABWIDTH*d*' '
        result += "And\n"
        result += self.exp1.indented(d + 1) + "\n"
        result += self.exp2.indented(d + 1)
        return result
    def removeImplications(self):
        return And(self.exp1.removeImplications(), self.exp2.removeImplications())
    def isLiteral(self):
        return False
    def conjunctsList(self):
        return self.exp1.conjunctsList() + self.exp2.conjunctsList()
    def isNNF(self):
        return self.exp1.isNNF() and self.exp2.isNNF()
    def isPureDisjunctive(self):
        return False
    def isCNF(self):
        return self.exp1.isCNF() and self.exp2.isCNF()


class Or(BoolExpression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " | " + self.exp2.format() + ")"
    def tex(self):
        return "(" + self.exp1.tex() + " \\lor " + self.exp2.tex() + ")"
    def eval(self, interp):
        val1 = self.exp1.eval(interp)
        val2 = self.exp2.eval(interp)
        return BoolConst(val1.val or val2.val)
    def NNF(self):
        return Or(self.exp1.NNF(), self.exp2.NNF())
    def getVars(self):
        return uniqueList(self.exp1.getVars() + self.exp2.getVars())
    def replace1(self, var, exp):
        return Or(self.exp1.replace1(var, exp), self.exp2.replace1(var, exp))
    def simplify(self):
        expSimplified1 = self.exp1.simplify()
        expSimplified2 = self.exp2.simplify()
        if expSimplified1 == BoolConst(True):
            return BoolConst(True)
        elif expSimplified1 == BoolConst(False):
            return expSimplified2
        elif expSimplified2 == BoolConst(False):
            return expSimplified1
        elif expSimplified2 == BoolConst(True):
            return BoolConst(True)
        elif expSimplified1 == expSimplified2:
            return expSimplified1
        else:
            return Or(expSimplified1, expSimplified2)
    def indented(self,d):
        result = TABWIDTH*d*' '
        result += "Or\n"
        result += self.exp1.indented(d + 1) + "\n"
        result += self.exp2.indented(d + 1)
        return result
    def removeImplications(self):
        return Or(self.exp1.removeImplications(), self.exp2.removeImplications())
    def isLiteral(self):
        return False
    def disjunctsList(self):
        return self.exp1.disjunctsList() + self.exp2.disjunctsList()
    def isNNF(self):
        return self.exp1.isNNF() and self.exp2.isNNF()
    def isPureDisjunctive(self):
        return self.exp1.isPureDisjunctive() and self.exp2.isPureDisjunctive()
    def isCNF(self):
        return self.isPureDisjunctive()


class Implies(BoolExpression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " => " + self.exp2.format() + ")"
    def tex(self):
        return "(" + self.exp1.tex() + " \\Rightarrow " + self.exp2.tex() + ")"
    def eval(self, interp):
        val1 = self.exp1.eval(interp)
        val2 = self.exp2.eval(interp)
        return BoolConst(not val1.val or val2.val)
    def NNF(self):
        return Or(Not(self.exp1), self.exp2).NNF()
    def getVars(self):
        return uniqueList(self.exp1.getVars() + self.exp2.getVars())
    def replace1(self, var, exp):
        return Implies(self.exp1.replace1(var, exp), self.exp2.replace1(var, exp))
    def simplify(self):
        expSimplified1 = self.exp1.simplify()
        expSimplified2 = self.exp2.simplify()
        if expSimplified1 == BoolConst(True):
            return expSimplified2
        elif expSimplified1 == BoolConst(False):
            return BoolConst(True)
        elif expSimplified1 == expSimplified2:
            return BoolConst(True)
        elif expSimplified2 == BoolConst(True):
            return expSimplified1
        elif expSimplified2 == BoolConst(False):
            return Not(expSimplified1).simplify()
        else:
            return Implies(expSimplified1, expSimplified2)
    def indented(self,d):
        result = TABWIDTH*d*' '
        result += "Implies\n"
        result += self.exp1.indented(d + 1) + "\n"
        result += self.exp2.indented(d + 1) + "\n"
        return result
    def removeImplications(self):
        return Or(Not(self.exp1.removeImplications()), self.exp2.removeImplications())
    def isLiteral(self):
        return False
    def isNNF(self):
        return self.exp1.isNNF() and self.exp2.isNNF()
    def isPureDisjunctive(self):
        return False
    def isCNF(self):
        return False

class Iff(BoolExpression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " <=> " + self.exp2.format() + ")"
    def tex(self):
        return "(" + self.exp1.tex() + " \\Leftrightarrow " + self.exp2.tex() + ")"
    def eval(self, interp):
        val1 = self.exp1.eval(interp)
        val2 = self.exp2.eval(interp)
        return BoolConst(val1.val == val2.val)
    def NNF(self):
        # return Iff(self.exp1.NNF(), self.exp2.NNF())
        return self.removeImplications().NNF()
    def getVars(self):
        return uniqueList(self.exp1.getVars() + self.exp2.getVars())
    def replace1(self, var, exp):
        return Iff(self.exp1.replace1(var, exp), self.exp2.replace1(var, exp))
    def simplify(self):
        expSimplified1 = self.exp1.simplify()
        expSimplified2 = self.exp2.simplify()
        if expSimplified1 == BoolConst(True):
            return expSimplified2
        elif expSimplified1 == BoolConst(False):
            return Not(expSimplified2).simplify()
        elif expSimplified2 == BoolConst(False):
            return Not(expSimplified1).simplify()
        elif expSimplified1 == expSimplified2:
            return expSimplified1
        elif expSimplified2 == BoolConst(True):
            return expSimplified1
        else:
            return Iff(expSimplified1, expSimplified2)
    def indented(self,d):
        result = TABWIDTH*d*' '
        result += "Iff\n"
        result += self.exp1.indented(d + 1) + "\n"
        result += self.exp2.indented(d + 1)
        return result
    def removeImplications(self):
        arg1 = self.exp1.removeImplications()
        arg2 = self.exp2.removeImplications()
        return Or(And(arg1, arg2), And(Not(arg1), Not(arg2)))
    def isLiteral(self):
        return False
    def isNNF(self):
        return self.exp1.isNNF() and self.exp2.isNNF()
    def isPureDisjunctive(self):
        return False
    def isCNF(self):
        return False

    
def uniqueList(expList): 
   # order preserving
   seen = []
   for e in expList:
       if e not in seen:
           seen.append(e)
   return seen

def distrOr(exp1, exp2):
    if isinstance(exp1, And):
        return And(distrOr(exp1.exp1, exp2), distrOr(exp1.exp2, exp2))
    elif isinstance(exp2, And):
        return And(distrOr(exp1, exp2.exp1), distrOr(exp1, exp2.exp2))
    else:
        return Or(exp1, exp2)

def dictUnite(d1, d2):
    return dict(list(d1.items()) + list(d2.items()))

def dictListProduct(dl1, dl2):
    return [dictUnite(d1,d2) for d1 in dl1 for d2 in dl2]

def allInterpretations(varList):
    if varList == []:
        return [{}]
    else:
        v = varList[0]
        v_interps = [{v : BoolConst(False)}, {v : BoolConst(True)}]
        return dictListProduct(v_interps, allInterpretations(varList[1:]))
