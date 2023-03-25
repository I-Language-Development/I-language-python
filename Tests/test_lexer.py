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
            "class;",
            [lexer.LexerToken("CLASS", "class"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "function;",
            [
                lexer.LexerToken("FUNCTION", "function"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        ("use;", [lexer.LexerToken("USE", "use"), lexer.LexerToken("SEMICOLON", ";")]),
        (
            "import;",
            [lexer.LexerToken("IMPORT", "import"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        ("if;", [lexer.LexerToken("IF", "if"), lexer.LexerToken("SEMICOLON", ";")]),
        (
            "elif;",
            [lexer.LexerToken("ELIF", "elif"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "else;",
            [lexer.LexerToken("ELSE", "else"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "match;",
            [lexer.LexerToken("MATCH", "match"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "case;",
            [lexer.LexerToken("CASE", "case"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "default;",
            [
                lexer.LexerToken("DEFAULT", "default"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
        (
            "while;",
            [lexer.LexerToken("WHILE", "while"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        ("for;", [lexer.LexerToken("FOR", "for"), lexer.LexerToken("SEMICOLON", ";")]),
        (
            "return;",
            [lexer.LexerToken("RETURN", "return"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "delete;",
            [lexer.LexerToken("DELETE", "delete"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "break;",
            [lexer.LexerToken("BREAK", "break"), lexer.LexerToken("SEMICOLON", ";")],
        ),
        (
            "continue;",
            [
                lexer.LexerToken("CONTINUE", "continue"),
                lexer.LexerToken("SEMICOLON", ";"),
            ],
        ),
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
def test_lexer_tokens(data: str, expected: List[lexer.LexerToken]) -> None:
    """Tests lexer tokens from the given data.

    Args:
        data (str): Data to test.
        expected (list[lexer.LexerToken]): Expected tokens.
    """

    assert [str(token) for token in lexer.Lexer(data).lex()] == [
        str(token) for token in expected
    ]
