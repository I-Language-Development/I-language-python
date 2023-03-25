"""
I Language lexer test.
Version: 0.1.0

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


###########
# IMPORTS #
###########


import pathlib
import sys
from typing import (
    List,
)

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from Main import lexer


####################
# LEXER TOKEN TEST #
####################

def test_lexer_token() -> None:
    """Tests lexer tokens."""

    assert lexer.LexerToken("TYPE", "VALUE").type == "TYPE"
    assert lexer.LexerToken("TYPE", "VALUE").value == "VALUE"


############
# LEX TEST #
############


@pytest.mark.parametrize(
    "data, expected",
    [
        ("\n", []),
        ("\t", []),
        ("  ", []),
        ("// Test", []),
        ("/* Test */", []),
        ("==", [lexer.LexerToken("EQUAL", "==")]),
        ("!=", [lexer.LexerToken("NOT_EQUAL", "!=")]),
        ("<=", [lexer.LexerToken("LESS_EQUAL", "<=")]),
        (">=", [lexer.LexerToken("GREATER_EQUAL", ">=")]),
        ("++", [lexer.LexerToken("COUNT_UP", "++")]),
        ("--", [lexer.LexerToken("COUNT_DOWN", "--")]),
        ("&&", [lexer.LexerToken("AND", "&&")]),
        ("||", [lexer.LexerToken("OR", "||")]),
        (";", [lexer.LexerToken("SEMICOLON", ";")]),
        ("=", [lexer.LexerToken("SET", "=")]),
        ("{", [lexer.LexerToken("BLOCK_OPEN", "{")]),
        ("}", [lexer.LexerToken("BLOCK_CLOSE", "}")]),
        ("(", [lexer.LexerToken("CLAMP_OPEN", "(")]),
        (")", [lexer.LexerToken("CLAMP_CLOSE", ")")]),
        ("[", [lexer.LexerToken("INDEX_OPEN", "[")]),
        ("]", [lexer.LexerToken("INDEX_CLOSE", "]")]),
        ("?", [lexer.LexerToken("INDEFINITE", "?")]),
        (".", [lexer.LexerToken("DOT", ".")]),
        (":", [lexer.LexerToken("COLON", ":")]),
        (">", [lexer.LexerToken("GREATER", ">")]),
        ("<", [lexer.LexerToken("LESS", "<")]),
        ("+", [lexer.LexerToken("PLUS", "+")]),
        ("-", [lexer.LexerToken("MINUS", "-")]),
        ("*", [lexer.LexerToken("MULTIPLY", "*")]),
        ("/", [lexer.LexerToken("DIVIDE", "/")]),
        ("%", [lexer.LexerToken("MODULO", "%")]),
        (",", [lexer.LexerToken("COMMA", ",")]),
        (
            "any;",
            [lexer.LexerToken("BASETYPE", "any"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "bool;",
            [lexer.LexerToken("BASETYPE", "bool"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "complex;",
            [
                lexer.LexerToken("BASETYPE", "complex"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "dict;",
            [lexer.LexerToken("BASETYPE", "dict"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "dictionary;",
            [
                lexer.LexerToken("BASETYPE", "dictionary"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "dynamic;",
            [
                lexer.LexerToken("BASETYPE", "dynamic"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "float;",
            [lexer.LexerToken("BASETYPE", "float"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "int;",
            [lexer.LexerToken("BASETYPE", "int"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "integer;",
            [
                lexer.LexerToken("BASETYPE", "integer"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "list;",
            [lexer.LexerToken("BASETYPE", "list"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "str;",
            [lexer.LexerToken("BASETYPE", "str"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "string;",
            [
                lexer.LexerToken("BASETYPE", "string"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "null;",
            [lexer.LexerToken("BASETYPE", "null"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "mdarray;",
            [
                lexer.LexerToken("BASETYPE", "mdarray"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "_NAME;",
            [
                lexer.LexerToken("BUILTIN_CONST", "_NAME"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "true;",
            [lexer.LexerToken("BOOL", "true"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "false;",
            [lexer.LexerToken("BOOL", "false"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        ("1;", [lexer.LexerToken("INT", "1"), lexer.LexerToken("SEMICOLON", ";")]),
        (
            "1.2;",
            [lexer.LexerToken("FLOAT", "1.2"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "name;",
            [lexer.LexerToken("NAME", "name"), lexer.LexerToken("SEMICOLON", ";")],
        ),
    ],
)
def test_lex(data: str, expected: List[lexer.LexerToken]) -> None:
    """Tests lexer function.

    Args:
        data (str): Data to test.
        expected (list[lexer.LexerToken]): Expected tokens.
    """

    assert [str(token) for token in lexer.Lexer(data).lex()] == [
        str(token) for token in expected
    ]


#################
# GETTOKEN TEST #
#################


@pytest.mark.parametrize(
    "data, expected",
    [
        ("class", lexer.LexerToken("CLASS", "class")),
        ("function", lexer.LexerToken("FUNCTION", "function")),
        ("use", lexer.LexerToken("USE", "use")),
        ("import", lexer.LexerToken("IMPORT", "import")),
        ("if", lexer.LexerToken("IF", "if")),
        ("elif", lexer.LexerToken("ELIF", "elif")),
        ("else", lexer.LexerToken("ELSE", "else")),
        ("match", lexer.LexerToken("MATCH", "match")),
        ("case", lexer.LexerToken("CASE", "case")),
        ("default", lexer.LexerToken("DEFAULT", "default")),
        ("while", lexer.LexerToken("WHILE", "while")),
        ("for", lexer.LexerToken("FOR", "for")),
        ("return", lexer.LexerToken("RETURN", "return")),
        ("delete", lexer.LexerToken("DELETE", "delete")),
        ("break", lexer.LexerToken("BREAK", "break")),
        ("continue", lexer.LexerToken("CONTINUE", "continue")),
    ],
)
def test_gettoken(data: str, expected: lexer.LexerToken) -> None:
    """Tests gettoken from the given data.

    Args:
        data (str): Data to test.
        expected (lexer.LexerToken): Expected token.
    """

    assert str(lexer.gettoken(data, 1, 1)) == str(expected)


####################
# VALIDATE INTEGER #
####################

@pytest.mark.parametrize(
    "data, expected",
    [
        ("0", True),
        ("1", True),
        ("0.1", False),
        ("1.1", False),
        ("0.0", False)
    ]
)
def test_validate_integer(data: str, expected: bool) -> None:
    """Tests validate integer function.

    Args:
        data (str): Data to test.
        expected (bool): Expected result.
    """

    assert lexer.validate_integer(data) == expected


##################
# VALIDATE FLOAT #
##################

@pytest.mark.parametrize(
    "data, expected",
    [
        ("0", False),
        ("1", False),
        ("0.1", True),
        ("1.2", True),
        ("0.0", True),
    ]
)
def test_validate_float(data: str, expected: bool) -> None:
    """Tests validate float function.

    Args:
        data (str): Data to test.
        expected (bool): Expected result.
    """

    assert lexer.validate_float(data) == expected
