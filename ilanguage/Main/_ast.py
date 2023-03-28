"""
I Language AST.
Version: 0.1.1

Copyright (c) 2023-present ElBe Development.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the 'Software'),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
#from _ast import AST # WE DO NOT NEED THIS DAMN

# TODO (ElBe): Add docstrings, tests and extend the modulesssss


known_vars = {}
known_funcs = {}


def delete_locals(local):
    for value in list(known_vars):
        if value.local >= local:
            known_vars.popitem(value)


class StaticValue:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "<" + self.type.upper() + ": " + str(self.value) + ">"

class StaticList:
    def __init__(self, type, values, dimension):
        self.type = type
        self.values = values
        self.dimension = dimension

    def __str__(self):
        return "<" + self.type.upper() + self.dimension*"[]" + ": " + str(self.values) + ">"
class AST:
    def __str__(self):
        self.nexttask: AST|None = None
        return "<Empty AST Node>"

    def __repr__(self):
        return self.__str__()

    def last(self):  # get last code in queue
        if self.nexttask is not None:
            return self.nexttask.last()
        return self


class Main(AST):
    def __init__(self, name="Main"):
        super().__init__()
        self.next_task = AST()
        self.name = name

    def __str__(self):
        return "<Main Program '" + self.name + "'>\n" + str(self.next_task)


class DefineVariableNovalue(AST):
    def __init__(self, name, _type, _list, indef):
        self.name = name
        self.type = _type
        self.list = _list
        self.indef = indef
        self.nexttask = AST()


class DefineVariable(AST):
    def __init__(self, name, _type, _list, indef, value):
        self.name = name
        self.type = _type
        self.list = _list
        self.indef = indef  # What is this used for?
        self.next_task = AST()
        self.value: AST = value


class Variable:
    def __init__(self, name, _type, local=0, _list=0, line=None, indef=False):
        self.name = name
        self.type = _type
        self.indef = indef  # What is this?
        self.list = _list
        self.local = local
        self.line = line


if __name__ == "__main__":
    print(Main())
