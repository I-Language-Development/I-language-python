
import ast
class ParserError(BaseException):
    def __init__(self,name,help,line,errcode=0):
        self.name = name
        self.help = help
        self.line = line
        self.errcode = errcode

    def __str__(self):
        return "Parser error: " + self.name.upper() + "(errno " + str(self.errcode) + ") - (line " + str(self.line) + "):\n" + self.help



class Parser:
    def __init__(self,tokens):
        self.tokens = tokens

    def tokenstolist(self,tokenlist):
        l = []
        for token in tokenlist:
            l.append(token.type)
        return l

    def parseoneof(self,tokens,line,local,*funcs):
        for f in funcs:
            retval = f(tokens,line,local)
            if type(retval) == ast.AST:
                return retval

    def parse(self,tokens = None,local=0,startline=0):
        line = startline
        if tokens is None:
            tokens = self.tokens
            print("parsing...")

    def parse_define_variable_definite(self,tokens,line,local):
        tl : list = self.tokenstolist(tokens)
        #valid = True
        indef = False
        listdimension = 0
        if tl[0] == "INDEFINITE":
            indef = True
            tl = tl[1:]
            tokens = tokens[1:]
        if tl[0] == "BASETYPE":
            if tl[1] == "INDEX_OPEN":
                i = 1
                while tl[i] == "INDEX_OPEN" and tl[i + 1] == "INDEX_CLOSE":
                    listdimension += 1
                    i += 2
                if tl[i-1] != "INDEX_CLOSE":
                    raise ParserError("unclosedindex", """In this line there is an unclosed '['. This is needed to have a working list""", line)
                tl = tl[1] + tl[i+1:]

            elif tl[1] == "NAME":
                if tl[2] == "END_CMD": # e.g. ?int my_int;
                    if not tokens[1].value in ast.known_vars:
                        ast.known_vars[tokens[1].value] = ast.Variable(tokens[1].value,tokens[0].value,local,listdimension,line,indef)
                        return ast.DefineVariable_novalue(tokens[1].value,tokens[0].value,listdimension,indef)
                    else:
                        raise ParserError("varoverlap",
                                          "This variable seems overlapping with an already existing one ('" + str(ast.known_vars[tokens[1].value]) + "', line " + str(ast.known_vars[tokens[1].value].line) + ")",
                                          line)
                else:
                    raise ParserError("noendcmd", """This Command seems to have no ';', which is required at the end of every Command""", line)
        elif indef:
            raise ParserError("unusedindef","""The '?' in this line could not be used, this could be because the rest of the declaration is wrong.""",line)

        return
