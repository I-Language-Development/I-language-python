import termcolor
import sys
import iast as ast
class ParserError(BaseException):
    def __init__(self,name,help,line,errcode=0):
        self.name = name
        self.help = help
        self.line = line+1
        self.errcode = errcode

        print(termcolor.colored(
            "\nParser error: " + self.name.upper() + "(errno " + str(self.errcode) + ") - (line " + str(
                self.line) + "):\n" + self.help, "red"))
        sys.exit(self.errcode)






class Parser:
    def __init__(self,tokens):
        self.tokens = tokens

    def tokenstolist(self,tokenlist):
        l = []
        for token in tokenlist:
            l.append(token.type)
        return l

    def parseoneof(self,tokens,line,local,funcs):
        for f in funcs:
            retval = f(tokens,line,local)
            if retval is not None:
                return retval
    def splittokens(self,tokens,splitter):
        tl = [[]]
        i = 0
        for t in tokens:
            if t.type == splitter:
                i += 1
                tl.append([])
            else: tl[i].append(t)
        return tl

    def parse_var_call(self, tokens, line, local):
        #print("vars:", ast.known_vars)
        if tokens[0].type == "NAME" and len(tokens) == 1:
            #print(ast.known_vars[tokens[0].value])
            if tokens[0].value in list(ast.known_vars.keys()):
                v: ast.Variable = ast.known_vars[tokens[0].value]
                return ast.CallVariable(tokens[0].value, v.type)


    def parse_function_definition(self,tokens,line,local):
        if tokens[0].type == "BASETYPE":
            if tokens[1].type == "NAME":
                if tokens[3].type == "CLAMP_OPEN":
                    tok = self.splittokens(tokens,"BLOCK_OPEN")
                    if len(tok) == 2:
                        if tok[0][-1].type == "CLAMP_CLOSE":
                            if tok[1][-1].type == "BLOCK_CLOSE":
                                pass
                                ##############
                                # Add: Arguments and parse of do
                                ##############
                            else:
                                raise ParserError("unclosedblock",
                                                  "The block opened here were not closed",
                                                  line)
                        else:
                            raise ParserError("unclosedclamp","The clamp of this function definition was not closed in the right position (after all arguments)",line)


    def parse_value(self,tokens,line,local,list=0):
        if len(tokens) == 1:
            if tokens[0].type in ["BOOL","STRING","FLOAT","INT","HEX"]:
                return ast.StaticValue(tokens[0].type.lower(),tokens[0].value)
            elif tokens[0].value == "null":
                return ast.StaticValue("null","null")
        print(tokens)
        if tokens[0].type == "INDEX_OPEN" and tokens[-1].type == "INDEX_CLOSE":
            typ = None
            lis = ast.StaticList(None,[],list+1)
            if tokens[1:-1] == []:
                typ = "emptylist"
                lis.type = typ
                return lis
            for buf in self.splittokens(tokens[1:-1],"SEPERATOR"):
                tree = self.parseoneof(buf,line,local,[self.parse_value, self.parse_var_call])
                if typ is None: typ = tree.type
                if tree.type != typ: typ = "dynamic"
                lis.values.append(tree)
            if tokens[1:-1] == []:
                typ = "emptylist"
            lis.type = typ
            return lis



    def parse(self,tokens = None,start:ast.AST=ast.Main(),local=0,startline=0):
        line = startline
        if tokens is None:
            tokens = self.tokens
            print("parsing...")
        index = 0
        buffer = []
        block = 0
        while index < len(tokens):
            #print(buffer)
            if tokens[index].type == "NEWLINE":
                line += 1
            else: buffer.append(tokens[index])
            if tokens[index].type == "BLOCK_OPEN":
                block += 1
            elif tokens[index].type == "BLOCK_CLOSE":
                block -= 1
                ast.delete_locals(block+1)
            if block == 0 and tokens[index].type == "END_CMD":
                tree = self.parseoneof(buffer,line,local + block,[
                    self.parse_define_variable,
                    self.parse_import,

                ])
                #if tree is None: pass
                start.last().nexttask = tree
                buffer = []
            index += 1
        return start

    def parse_import(self,tokens,line,local):
        if tokens[0].type == "IMPORT":
            if tokens[1].type == "NAME":
                #if len(tokens) == 3 and tokens[2].type == "END_CMD":
                return ast.Import(tokens[1].value)

            else: raise ParserError("notaname",
                                    "Expected a module name after 'import'",
                                    line)


    def parse_define_variable(self,tokens,line,local):
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

                tl = [tl[0]] + tl[i:]
                #print(tl)
                tokens = [tokens[0]] + tokens[i:]

            if tl[1] == "NAME":
                if tl[2] == "END_CMD": # e.g. ?int my_int;
                    if not tokens[1].value in ast.known_vars:
                        print("Variable found")
                        ast.known_vars[tokens[1].value] = ast.Variable(tokens[1].value,tokens[0].value,local,listdimension,line,indef)
                        return ast.DefineVariableNovalue(tokens[1].value,tokens[0].value,listdimension,indef)
                    else:
                        raise ParserError("varoverlap",
                                          "This variable seems overlapping with an already existing one ('" + str(ast.known_vars[tokens[1].value].name) + "', line " + str(ast.known_vars[tokens[1].value].line) + ")",
                                          line)
                elif tl[2] == "SET":
                    if tl[3] == "END_CMD": raise ParserError("nosetvalue",
                                          "It looks like you forgot to set a value here or you put in a '=' where you didn't want it.",
                                          line)
                    elif tl[-1] == "END_CMD":
                        #print(tokens[3:-1])
                        tree = self.parseoneof(tokens[3:-1],line,local,[self.parse_var_call, self.parse_value, ])
                        if tree is not None and (tree.type == tokens[0].value or tokens[0].value == "dynamic" or (indef and tree.type == "null") or tree.type == "emptylist"):
                            if not tokens[1].value in ast.known_vars:
                                ast.known_vars[tokens[1].value] = ast.Variable(tokens[1].value, tokens[0].value, local,
                                                                               listdimension, line, indef)
                                return ast.DefineVariable(tokens[1].value, tokens[0].value, listdimension, indef,tree)
                            else:
                                raise ParserError("varoverlap",
                                                  "This variable seems overlapping with an already existing one ('" + str(
                                                      ast.known_vars[tokens[1].value].name) + "', line " + str(
                                                      ast.known_vars[tokens[1].value].line) + ")",
                                                  line)
                        raise ParserError("unmatchingtype",
                                          "The return type of this variable (" + str(tree) + ") does not match the vars expected (" + int(indef)*"?" + str(tokens[0].value) + listdimension*"[]" + ")",
                                          line)
                    else:
                        raise ParserError("noendcmd",
                                          "This Command seems to have no ';', which is required at the end of every Command",
                                          line)
                else:
                    raise ParserError("noendcmd", """This Command seems to have no ';', which is required at the end of every Command""", line)
        elif indef:
            raise ParserError("unusedindef","""The '?' in this line could not be used, this could be because the rest of the declaration is wrong.""",line)


