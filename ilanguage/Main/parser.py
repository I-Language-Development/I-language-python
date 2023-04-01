import _ast as ast


class ParserError(BaseException):
    def __init__(self, name, _help, line, errcode=0):
        self.name = name
        self.help = _help
        self.line = line + 1
        self.errcode = errcode

    def __str__(self):
        return (
            "Parser error: "
            + self.name.upper()
            + "(errno "
            + str(self.errcode)
            + ") - (line "
            + str(self.line)
            + "):\n"
            + self.help
        )


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def tokens_to_list(self, tokens):
        l = []
        for token in tokens:
            l.append(token.type)
        return l

    def parse_one_of(self, tokens, line, local, funcs):
        for f in funcs:
            retval = f(tokens, line, local)
            if retval is not None:
                return retval

    def split_tokens(self, tokens, splitter):
        tl = [[]]
        i = 0
        for t in tokens:
            if t.type == splitter:
                i += 1
                tl.append([])
            else:
                tl[i].append(t)
        return tl

    def parse_function_definition(self, tokens, line, local):
        if tokens[0].type == "BASETYPE":
            if tokens[1].type == "NAME":
                split = self.split_tokens(tokens, "CLAMP_CLOSE")
                if len(split) == 2:
                    split[0] = split[0][1:]
                    if tokens[3].type == "CLAMP_OPEN":
                        pass

    def parse_value(self, tokens, line, local, list=0):
        if len(tokens) == 1:
            if tokens[0].type in ["BOOL", "STRING", "FLOAT", "INT", "HEX"]:
                return ast.StaticValue(tokens[0].type.lower(), tokens[0].value)
            elif tokens[0].value == "null":
                return ast.StaticValue("null", "null")
        print(tokens)
        if tokens[0].type == "INDEX_OPEN" and tokens[-1].type == "INDEX_CLOSE":
            typ = None
            lis = ast.StaticList(None, [], list + 1)
            if tokens[1:-1] == []:
                typ = "emptylist"
                lis.type = typ
                return lis
            for buf in self.split_tokens(tokens[1:-1], "SEPERATOR"):
                tree = self.parse_one_of(buf, line, local, [self.parse_value])
                if typ is None:
                    typ = tree.type
                if tree.type != typ:
                    typ = "dynamic"
                lis.values.append(tree)
            if tokens[1:-1] == []:
                typ = "emptylist"
            lis.type = typ
            return lis

    def parse(self, tokens=None, start: ast.AST = ast.Main(), local=0, start_line=0):
        line = start_line
        if tokens is None:
            tokens = self.tokens
            print("parsing...")
        index = 0
        buffer = []
        block = 0
        while index < len(tokens):
            # print(buffer)
            if tokens[index].type == "NEWLINE":
                line += 1
            else:
                buffer.append(tokens[index])
            if tokens[index].type == "BLOCK_OPEN":
                block += 1
            elif tokens[index].type == "BLOCK_CLOSE":
                block -= 1
                ast.delete_locals(block + 1)
            if block == 0 and tokens[index].type == "END_CMD":
                tree = self.parse_one_of(
                    buffer,
                    line,
                    local + block,
                    [self.parse_define_variable, self.parse_import],
                )
                # if tree is None: pass
                start.last().nexttask = tree
                buffer = []
            index += 1
        return start

    def parse_import(self, tokens, line, local):
        if tokens[0].type == "IMPORT":
            if tokens[1].type == "NAME":
                # if len(tokens) == 3 and tokens[2].type == "END_CMD":
                return ast.Import(tokens[1].value)

            else:
                raise ParserError(
                    "notaname", "Expected a module name after 'import'", line
                )

    def parse_define_variable(self, tokens, line, local):
        tl: list = self.tokens_to_list(tokens)
        # valid = True
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
                if tl[i - 1] != "INDEX_CLOSE":
                    raise ParserError(
                        "unclosedindex",
                        """In this line there is an unclosed '['. This is needed to have a working list""",
                        line,
                    )

                tl = [tl[0]] + tl[i:]
                # print(tl)
                tokens = [tokens[0]] + tokens[i:]

            if tl[1] == "NAME":
                if tl[2] == "END_CMD":  # e.g. ?int my_int;
                    if not tokens[1].value in ast.known_vars:
                        print("Variable found")
                        ast.known_vars[tokens[1].value] = ast.Variable(
                            tokens[1].value,
                            tokens[0].value,
                            local,
                            listdimension,
                            line,
                            indef,
                        )
                        return ast.DefineVariableNovalue(
                            tokens[1].value, tokens[0].value, listdimension, indef
                        )
                    else:
                        raise ParserError(
                            "varoverlap",
                            "This variable seems overlapping with an already existing one ('"
                            + str(ast.known_vars[tokens[1].value].name)
                            + "', line "
                            + str(ast.known_vars[tokens[1].value].line)
                            + ")",
                            line,
                        )
                elif tl[2] == "SET":
                    if tl[3] == "END_CMD":
                        raise ParserError(
                            "nosetvalue",
                            "It looks like you forgot to set a value here or you put in a '=' where you didn't want it.",
                            line,
                        )
                    elif tl[-1] == "END_CMD":
                        # print(tokens[3:-1])
                        tree = self.parse_one_of(
                            tokens[3:-1], line, local, [self.parse_value]
                        )
                        if tree is not None and (
                            tree.type == tokens[0].value
                            or tokens[0].value == "dynamic"
                            or (indef and tree.type == "null")
                            or tree.type == "emptylist"
                        ):
                            if not tokens[1].value in ast.known_vars:
                                ast.known_vars[tokens[1].value] = ast.Variable(
                                    tokens[1].value,
                                    tokens[0].value,
                                    local,
                                    listdimension,
                                    line,
                                    indef,
                                )
                                return ast.DefineVariable(
                                    tokens[1].value,
                                    tokens[0].value,
                                    listdimension,
                                    indef,
                                    tree,
                                )
                            else:
                                raise ParserError(
                                    "varoverlap",
                                    "This variable seems overlapping with an already existing one ('"
                                    + str(ast.known_vars[tokens[1].value].name)
                                    + "', line "
                                    + str(ast.known_vars[tokens[1].value].line)
                                    + ")",
                                    line,
                                )
                        raise ParserError(
                            "unmatchingtype",
                            "The return type of this variable ("
                            + str(tree)
                            + ") does not match the vars expected ("
                            + int(indef) * "?"
                            + str(tokens[0].value)
                            + listdimension * "[]"
                            + ")",
                            line,
                        )
                    else:
                        raise ParserError(
                            "noendcmd",
                            "This Command seems to have no ';', which is required at the end of every Command",
                            line,
                        )
                else:
                    raise ParserError(
                        "noendcmd",
                        """This Command seems to have no ';', which is required at the end of every Command""",
                        line,
                    )
        elif indef:
            raise ParserError(
                "unusedindef",
                """The '?' in this line could not be used, this could be because the rest of the declaration is wrong.""",
                line,
            )
