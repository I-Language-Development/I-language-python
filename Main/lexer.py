#!/usr/bin/python3
"""
I Language lexer.
Version: 0.1.3

Copyright (c) 2023-present ElBe Devleopment.

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


###########
# IMPORTS #
###########

import ast
from typing import Any, List


#############
# CONSTANTS #
#############

DIGITS: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
DIGITS_AS_STRINGS: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


##############
# MAIN LEXER #
##############


class LexerToken:
    def __init__(self, token_type: Any, value: Any) -> None:
        self.type = token_type
        self.value = value

    def __str__(self) -> str:
        return "{" + self.type + ":'" + self.value + "'}"

    def __repr__(self) -> str:
        return "{" + self.type + ":'" + self.value + "'}"


class LexerError(BaseException):
    def __init__(self, description: str, line: int, column: int) -> None:
        self.desc = description
        self.line = line
        self.column = column

    def __str__(self) -> str:
        return (
            str(self.desc)
            + " in line "
            + str(self.line)
            + ", column "
            + str(self.column)
        )


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.separators = [" ", "\t", "\n"]
        self.double_marks = {
            "==": "EQUAL",
            "++": "COUNT_UP",
            "--": "COUNT_DOWN"
        }
        self.marks = {
            ";": "END_CMD",
            "=": "SET",
            "{": "BLOCK_OPEN",  # Also dicts
            "}": "BLOCK_CLOSE",  # Also dicts
            "(": "CLAMP_OPEN",
            ")": "CLAMP_CLOSE",
            "[": "INDEX_OPEN",  # Also arrays
            "]": "INDEX_CLOSE",  # Also arrays
            "?": "INDEFINITE",
            ".": "SEPERATOR",
            ":": "SLICE",
            ">": "GREATER",
            "<": "LESS",
            "+": "ADD",
            "-": "SUBTRACT",
            "*": "MULTIPLY",
            "/": "DIVIDE",
            "%": "MODULO",
            ".": "CHILD",
            ",": "SEPERATOR"
        }
        self.keywords = {
            "class": "CLASS",
            "use": "USE",
            "import": "IMPORT",
            "if": "IF",
            "else": "ELSE",
            "while": "WHILE",
            "for": "FOR",
            "return": "RETURN",
            "delete": "DELETE",
            "break": "BREAK",
            "continue": "CONTINUE",
        }
        self.base_types = [
            "string",  # and str
            "int",  # and integer
            "float",
            "complex",
            "list",  # and array
            "dict",  # and dictionary
            "bool",
            "dynamic",
            "null",  # CONST, can't be changed
        ]

        self.tokens = []

    def lex(self):
        def validate_float(string: str) -> bool:
            dot = False
            valid = True

            if string[0] == "-":
                string = string[1:]
            for char in string:
                valid = valid and (
                    char in DIGITS_AS_STRINGS or (char == "." and not dot)
                )
                if char == ".":
                    dot = True
            return valid

        def validate_integer(string: str) -> bool:
            valid = True
            if string[0] == "-":
                string = string[1:]
            for char in string:
                valid = valid and char in DIGITS_AS_STRINGS

            return valid

        def gettoken(
            string: str, line: int, column: int
        ) -> LexerToken | None:
            if string in list(self.keywords.keys()):
                return LexerToken(self.keywords[string], string)
            elif len(string) > 0 and string[0] == "_":
                return LexerToken("BUILTIN_CONST", string)
            elif string in ["true", "false", "True", "False"]:
                return LexerToken("BOOL", string)
            elif string in self.base_types:
                return LexerToken("BASETYPE", string)
            elif len(string) == 0:
                return None
            elif validate_float(string):
                if validate_integer(string):
                    return LexerToken("INT", string)
                return LexerToken("FLOAT", string)

            elif len(string) > 0 and string[0] not in DIGITS_AS_STRINGS:
                return LexerToken("NAME", string)

            else:
                raise LexerError("Unrecognized Pattern: '" + string + "'", line, column)

        def replace_none(ar): # What's that?
            n = []
            for el in ar:
                if el is not None:
                    n.append(el)
            return n

        line = 1
        comment = 0
        column = 1
        index = 0
        buffer = ""
        in_string = False
        while index < len(self.text):
            if self.text[index] == "\n":
                self.tokens.append(gettoken(buffer, line, column))
                line += 1
                column = 1
                buffer = ""
                if comment == 1:
                    comment = 0
            else:
                column += 1
            if comment < 1:
                if len(self.text[index:]) > 1 and self.text[index : index + 2] == "//":
                    comment = 1
                elif self.text[index] == "'" or self.text[index] == '"':
                    in_string = not in_string
                    if not in_string:
                        self.tokens.append(LexerToken("STRING", buffer))

                        buffer = ""

                elif in_string:
                    buffer += self.text[index]
                elif self.text[index] in self.separators:
                    self.tokens.append(gettoken(buffer, line, column))
                    buffer = ""
                elif len(self.text[index:]) > 1 and self.text[
                    index : index + 2
                ] in list(self.double_marks.keys()):
                    self.tokens.append(gettoken(buffer, line, column))
                    self.tokens.append(
                        LexerToken(
                            self.double_marks[self.text[index : index + 2]],
                            self.text[index: index + 2],
                        )
                    )
                    buffer = ""
                    index += 1

                elif self.text[index] in list(self.marks.keys()):
                    self.tokens.append(gettoken(buffer, line, column))
                    self.tokens.append(
                        LexerToken(self.marks[self.text[index]], self.text[index])
                    )
                    buffer = ""

                else:
                    buffer += self.text[index]

            index += 1
        self.tokens = replace_none(self.tokens)
        return self.tokens


if __name__ == "__main__":
    with open("../test.ilang") as test:
        data = test.read()

    lexer = Lexer(data)
    print(lexer.lex())
