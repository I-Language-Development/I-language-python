#!/usr/bin/python3
"""
I Language lexer.
Version: 0.1.5

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


#########
# SETUP #
#########

__author__ = "I-language Development"
__version__ = "0.1.5"


###########
# IMPORTS #
###########

import dataclasses
import io
import sys
from typing import (
    Dict,
    List,
    Optional,
)

from typing_extensions import (
    Final,
)


#############
# CONSTANTS #
#############

DIGITS_AS_STRINGS: Final[List[str]] = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# TODO (ElBe): Add grammar instead of this
SEPARATORS: Final[List[str]] = [" ", "\t", "\n"]
DOUBLE_MARKS: Final[Dict[str, str]] = {
    "==": "EQUAL",
    "!=": "NOT_EQUAL",
    "<=": "LESS_EQUAL",
    ">=": "GREATER_EQUAL",
    "++": "COUNT_UP",
    "--": "COUNT_DOWN",
    "&&": "AND",  # Maybe add and keyword?
    "||": "OR",  # Maybe add or keyword?
}
MARKS: Final[Dict[str, str]] = {
    ";": "SEMICOLON",
    "=": "SET",
    "{": "BLOCK_OPEN",  # Also dicts
    "}": "BLOCK_CLOSE",  # Also dicts
    "(": "CLAMP_OPEN",
    ")": "CLAMP_CLOSE",
    "[": "INDEX_OPEN",  # Also arrays
    "]": "INDEX_CLOSE",  # Also arrays
    "?": "INDEFINITE",
    ".": "DOT",
    ":": "COLON",
    ">": "GREATER",
    "<": "LESS",
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULTIPLY",
    "/": "DIVIDE",
    "%": "MODULO",
    ",": "COMMA",
    "!": "NOT",
}
COMMENTS: Final[Dict[str, str]] = {
    "//": "COMMENT",
    "/*": "COMMENT_OPEN",
    "*/": "COMMENT_CLOSE",
}
KEYWORDS: Final[Dict[str, str]] = {
    "class": "CLASS",
    "function": "FUNCTION",
    "use": "USE",
    "import": "IMPORT",
    "if": "IF",
    "elif": "ELIF",
    "else": "ELSE",
    "match": "MATCH",
    "case": "CASE",
    "default": "DEFAULT",
    "while": "WHILE",
    "for": "FOR",
    "return": "RETURN",
    "delete": "DELETE",
    "break": "BREAK",
    "continue": "CONTINUE",
    "try": "TRY",
    "catch": "CATCH",
    "throw": "THROW",
    "finally": "FINALLY",
}
BASE_TYPES: Final[List[str]] = [
    "any",
    "bool",
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
    "mdarray",
    "complex",  # Just for support thingy I guess idk lol
]


#################
# LEXER HELPERS #
#################


@dataclasses.dataclass
class LexerToken:
    """
    Represents a token for the lexer.
    """

    type: str
    value: str


class LexerError:  # pylint: disable=R0903
    """
    Represents an error while lexing.
    """

    def __init__(self, description: str, line: int, column: int, code: int = 1) -> None:
        """Initializes a lexing error.

        Args:
            description (str): Description of the error.
            line (int): Line the error occurred in.
            column (int): Column the error occurred in.
            code (int): The exit code of the error.
        """

        print(f"Error: {description} in line {line}, column {column}")
        sys.exit(code)


def validate_float(string: str) -> bool:
    """Validates if a string is a valid float.

    Args:
        string (str): Text to validate.

    Returns:
        True if the string is a valid float, False otherwise.
    """

    string = string.replace(" ", "")

    if string[0] == "-":
        string = string[1:]
    for character in string:
        if character in DIGITS_AS_STRINGS or character == ".":
            continue
        return False

    if "." not in string:
        return False

    return True


def validate_integer(string: str) -> bool:
    """Validates if a string is a valid integer.

    Args:
        string (str): Text to validate.

    Returns:
        True if the string is a valid integer, False otherwise.
    """

    string = string.replace(" ", "")

    if string[0] == "-":
        string = string[1:]
    for character in string:
        if character in DIGITS_AS_STRINGS:
            continue
        elif character == ".":
            return False
        return False

    return True


def gettoken(
    string: str, line: int, column: int
) -> Optional[LexerToken]:  # pylint: disable=R1710
    """Returns a token from the specified string.

    Args:
        string (str): String to get token from.
        line (int): Line number of the string.
        column (int): Column number of the token.

    Returns:
        Token from the specified string.
    """

    already_tokenized = False
    result = None

    if string in list(KEYWORDS) and not already_tokenized:
        already_tokenized = True
        result = LexerToken(KEYWORDS[string], string)

    elif (len(string) > 1 and string[0] == "_") and not already_tokenized:
        already_tokenized = True
        result = LexerToken("BUILTIN_CONST", string)

    elif string in ["true", "false"] and not already_tokenized:
        already_tokenized = True
        result = LexerToken("BOOL", string)

    elif string in BASE_TYPES and not already_tokenized:
        already_tokenized = True
        result = LexerToken("BASETYPE", string)

    elif len(string) == 0 and not already_tokenized:
        already_tokenized = True
        result = None

    elif validate_integer(string) and not already_tokenized:
        already_tokenized = True
        result = LexerToken("INT", string)

    elif (
        len(string) > 0 and string[0] not in DIGITS_AS_STRINGS
    ) and not already_tokenized:
        already_tokenized = True
        result = LexerToken("NAME", string)
    else:
        LexerError(f"Unrecognized Pattern: {string!r}", line, column)

    return result


##############
# MAIN LEXER #
##############


def lex(
    text: Optional[str] = None,
) -> Optional[List[LexerToken]]:  # pylint: disable=R0912
    """Lexes the specified string.

    Args:
         text (str): Text to lex.

    Returns:
        List of lexed tokens.
    """

    tokens = []
    line = 1
    comment = False
    multiline_comment = False
    append_newline = False
    helper = 0
    column = 1
    in_string = False

    buffer = io.StringIO()

    try:
        for index, character in enumerate(text):
            helper -= 1

            tokens = [token for token in tokens if token is not None]

            if character == "\n":
                append_newline = True and not multiline_comment

                line += 1
                column = 1
                comment = False

            else:
                column += 1

            if not comment:
                if len(text[index:]) > 1 and text[index: index + 2] == "//":
                    comment = 1

                if text[index: index + 2] == "/*":
                    multiline_comment = True

                if multiline_comment and text[index: index + 2] == "*/":
                    multiline_comment = False
                    helper = 2

                if not multiline_comment and not comment and helper <= 0:
                    try:
                        if character in ['"', "'"]:
                            in_string = not in_string
                            if not in_string:
                                tokens.append(LexerToken(
                                    "STRING", buffer.getvalue()))

                                buffer.close()
                                buffer = io.StringIO()

                        elif in_string:
                            buffer.write(character)

                        elif text[index] in SEPARATORS:
                            tokens.append(
                                gettoken(buffer.getvalue(), line, column))

                            buffer.close()
                            buffer = io.StringIO()

                        elif len(text[index:]) > 1 and text[index: index + 2] in list(
                            DOUBLE_MARKS
                        ):
                            tokens.append(
                                gettoken(buffer.getvalue(), line, column))
                            tokens.append(
                                LexerToken(
                                    DOUBLE_MARKS[text[index: index + 2]],
                                    text[index: index + 2],
                                )
                            )

                            buffer.close()
                            buffer = io.StringIO()

                            helper = 2

                        elif character in list(MARKS):
                            tokens.append(
                                gettoken(buffer.getvalue(), line, column))
                            tokens.append(LexerToken(
                                MARKS[character], character))
                            buffer.close()
                            buffer = io.StringIO()

                        else:
                            buffer.write(character)
                        if append_newline:
                            append_newline = False
                            tokens.append(LexerToken("NEWLINE", "\n"))

                    except IndexError:
                        pass
    finally:
        buffer.close()

    tokens = [token for token in tokens if token is not None]
    modified_tokens = {}

    for index, token in enumerate(tokens):
        try:
            if token.type == "NEWLINE" and index == 0:
                tokens.pop(index)
                index -= 1
            if token.type == "INT" and tokens[index - 1].type == "DOT":
                modified_tokens[index - 2] = LexerToken(
                    "FLOAT",
                    f"{tokens[index-2].value}.{tokens[index].value}",
                )

                tokens.pop(index)
                tokens.pop(index - 1)
                tokens.pop(index - 2)
        except IndexError:
            pass

    for index, token in modified_tokens.items():
        tokens.insert(index, token)

    return tokens


if __name__ == "__main__":
    options: Dict[str, bool] = {
        "types": False,
        "values": False,
        "no-split": False,
    }

    if len(sys.argv[1:]) > 0:
        for argument in sys.argv[2:]:
            if argument.lower() in ["-h", "--help"]:
                print(
                    "Usage: lexer.py [PATH] [-h] [-v] [--types] [--values] [--no-split]"
                )
                print("Lexer of the I-programming language.")
                print("Options:")
                print("    -h, --help             Shows this help and exits.")
                print(
                    "    -v, --version          Shows the version of the lexer and exits."
                )
                print("    --types                Only print the types of the tokens.")
                print("    --values               Only print the values of the tokens.")
                print("    --no-split             Prints the tokens in a list.")
                sys.exit(0)

            elif argument.lower() in ["-v", "--version"]:
                print(f"Version: {__version__}")
                sys.exit(0)

            elif argument.lower() == "--types":
                options["types"] = True

            elif argument.lower() == "--values":
                options["values"] = True

            elif argument.lower() == "--no-split":
                options["no-split"] = True

            else:
                print(
                    f"Error: Invalid argument: {argument!r}"
                )  # TODO (Ranastra): Add errors
                sys.exit(1)

    try:
        with open(sys.argv[1:][0], "r", encoding="utf-8") as file:
            DATA = file.read()
    except (IndexError, FileNotFoundError):
        DATA = """
        int i   = 1234
        float f = 12.34
        """

    if options["types"] and not options["values"]:
        result = [str(token.type) for token in lex(DATA)]
    elif options["values"] and not options["types"]:
        result = [str(token.value) for token in lex(DATA)]
    else:
        result = [str(token) for token in lex(DATA)]

    if not options["no-split"]:
        result = "\n".join(result)

    print(result)
