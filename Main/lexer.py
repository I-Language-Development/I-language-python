#!/usr/bin/python3
"""
I Language lexer.
Version: 0.1.3

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


###########
# IMPORTS #
###########

import sys
from typing import (
    Any,
    Dict,
    List,
    Final,
)

import Main._types

#############
# CONSTANTS #
#############

DIGITS_AS_STRINGS: Final[List[str]] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

SEPARATORS: Final[List[str]] = [" ", "\t", "\n"]
DOUBLE_MARKS: Final[Dict[str, str]] = {
    "==": "EQUAL",
    "<=": "LESS_EQUALS",
    ">=": "GREATER_EQUALS",
    "++": "COUNT_UP",
    "--": "COUNT_DOWN",
}
MARKS: Final[Dict[str, str]] = {
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
    " .".replace(" ", ""): "CHILD",  # Duplicate, needs escaping
    ",": "SEPERATOR",
}
KEYWORDS: Final[Dict[str, str]] = {
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
BASE_TYPES: Final[List[str]] = [
    "any",
    "bool",
    "complex",
    "dict",
    "dictionary",
    "dynamic",
    "float",
    "int",
    "integer",
    "list",
    "str",
    "string",
    "null",
]


#################
# LEXER HELPERS #
#################

class LexerToken:
    """
    Represents a token for the lexer.
    """

    def __init__(self, token_type: Any, value: Any) -> None:
        """Initializes a new token.

        :param token_type: Type of the token.
        :param value: Value of the token
        """

        self.type = token_type
        self.value = value

    def __repr__(self) -> str:
        """Returns the representation of the token.

        :return: String representation of the token.
        """

        return f"{self.type}: {self.value!r}"


class LexerError:
    """
    Represents an error while lexing.
    """

    def __init__(self, description: str, line: int, column: int, code: int = 1) -> None:
        """Initializes a lexing error.

        :param description: Description of the error.
        :param line: Line the error occurred in.
        :param column: Column the error occurred in.
        :param code: The exit code of the error.
        """

        print(
            f"{description} in line {line}, column {column}"
        )
        sys.exit(code)


####################
# MAIN LEXER CLASS #
####################


class Lexer:
    """
    Represents a lexer object.
    """

    def __init__(self, text: str):
        self.text = text
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

        def gettoken(string: str, line: int, column: int) -> LexerToken | None:
            if string in list(KEYWORDS):
                return LexerToken(KEYWORDS[string], string)
            elif len(string) > 0 and string[0] == "_":
                return LexerToken("BUILTIN_CONST", string)
            elif string in ["true", "false", "True", "False"]:
                return LexerToken("BOOL", string)
            elif string in BASE_TYPES:
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
                LexerError("Unrecognized Pattern: '" + string + "'", line, column)

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
                elif self.text[index] in SEPARATORS:
                    self.tokens.append(gettoken(buffer, line, column))
                    buffer = ""
                elif len(self.text[index:]) > 1 and self.text[
                    index : index + 2
                ] in list(DOUBLE_MARKS):
                    self.tokens.append(gettoken(buffer, line, column))
                    self.tokens.append(
                        LexerToken(
                            DOUBLE_MARKS[self.text[index : index + 2]],
                            self.text[index : index + 2],
                        )
                    )
                    buffer = ""
                    index += 1

                elif self.text[index] in list(MARKS):
                    self.tokens.append(gettoken(buffer, line, column))
                    self.tokens.append(
                        LexerToken(MARKS[self.text[index]], self.text[index])
                    )
                    buffer = ""

                else:
                    buffer += self.text[index]

            index += 1

        return [str(token) for token in self.tokens if token is not None]  # TODO (ElBe): Change it back


if __name__ == "__main__":
    """Only for testing purposes."""

    with open("../test.ilang") as test:
        data = test.read()

    lexer = Lexer(data)
    print("\n".join(lexer.lex()))
