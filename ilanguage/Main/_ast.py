"""
I Language AST.
Version: 0.1.2

Copyright (c) 2023-present I Language Development.

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

# TODO (MasterOktagon): Explain this and extend it.


known_vars = {}
known_funcs = {}


def delete_locals(local: int) -> None:
    """Deletes all local variables where local is bigger or equal to the variables local.

    Args:
        local (int): The variables local.
    """

    for value in list(known_vars):
        if value.local >= local:
            known_vars.popitem(value)


class AST:
    """
    Base AST node class.
    """

    def __str__(self):
        return "<Empty AST Node>"

    def __repr__(self):
        return self.__str__()


class Main(AST):
    """
    Main program node.
    """

    def __init__(self, name="Main"):
        self.next_task = AST()
        self.name = name

    def __str__(self):
        return "<Main Program '" + self.name + "'>\n" + str(self.next_task)


class DefineVariableEmpty(AST):
    """
    Empty variable node.
    """

    def __init__(self, name, _type, _list, in_def):
        self.name = name
        self.type = _type
        self.list = _list
        self.indef = in_def
        self.nexttask = AST()


class DefineVariable(AST):
    """
    Variable node.
    """

    def __init__(self, name, _type, _list, in_def, value):
        self.name = name
        self.type = _type
        self.list = _list
        self.in_def = in_def  # What is this used for?
        self.next_task = AST()
        self.value: AST = value


class Variable:
    """
    Variable access node.
    """

    def __init__(self, name, _type, local=0, _list=0, line=None, in_def=False):
        self.name = name
        self.type = _type
        self.in_def = in_def
        self.list = _list
        self.local = local
        self.line = line


if __name__ == "__main__":
    print(Main())
