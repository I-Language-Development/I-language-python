
known_vars = {}
known_funcs = {}

def delete_locals(local):
    for var in list(known_vars):
        if var.local >= local:
            known_vars.popitem(var)
class AST:
    def __str__(self):
        return "<Empty AST Node>"
    def __repr__(self):
        return  self.__str__()

class Main(AST):
    def __init__(self,threadname="Main"):
        self.nexttask = AST()
        self.name = threadname
    def __str__(self):
        return "<Main Program '" + self.name + "'>\n" + str(self.nexttask)
class DefineVariable_novalue(AST):
    def __init__(self,name,type,list,indef):
        self.name = name
        self.type = type
        self.list = list
        self.indef = indef
        self.nexttask = AST()

class DefineVariable(AST):
    def __init__(self,name,type,list,indef,value):
        self.name = name
        self.type = type
        self.list = list
        self.indef = indef
        self.nexttask = AST()
        self.value : AST = value

if __name__ == "__main__":
    print(Main())

class Variable:
    def __init__(self,name,type,local=0,list=0,line=None,indef=False):
        self.name = name
        self.type = type
        self.indef = indef
        self.list = list
        self.local=local
        self.line=line


