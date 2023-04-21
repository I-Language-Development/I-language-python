"""
I Language grammar.
Version: 0.1.1

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


#
#
#

# Todo (ElBe): Fix names able to be integer

###########
# IMPORTS #
###########

from typing import List

from typing_extensions import Final

###########
# GRAMMAR #
###########

# Base types

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
]

# Useable options
USE_OPTIONS: Final[List[str]] = ["Python", "GarbageCollection"]

# Comments
COMMENT: Final[str] = r"// .* \n$"
LONG_COMMENT: Final[str] = r"\/\*(.|\n)*\*\/"

# Imports
IMPORT: Final[
    str
] = r"^import ([a-zA-Z0-9_]+,?)+( from [a-zA-Z0-9_]+)?( as [a-zA-Z0-9_]+)?;$"

# Constant
CONSTANT: Final[str] = rf"^const( ({'|'.join(BASE_TYPES)}))? [a-zA-Z0-9-_]+( )?=.*;$"

# Variable
VARIABLE: Final[str] = rf"^(var|({'|'.join(BASE_TYPES)}))( [a-zA-Z0-9-_]?)( )?=.*;$"

# Class
CLASS: Final[str] = r"^class [a-zA-Z1-9-_]+( )?\(([a-zA-Z1-9-_]*)\)( )?{(.|\n)*};$"

# Function
FUNCTION: Final[
    str
] = r"^(private )?(func(tion)?|(str|boolean)) [a-zA-Z0-9-_]+( )?\((((str|boolean) )?[a-zA-Z0-9-_]+( )?=( )?.*)*\)( )?{(.|\n)*};$"

# Use
USE: Final[str] = rf"^use ({'|'.join(USE_OPTIONS)});$"

# If clauses
IF: Final[str] = r"^if (\()?(.*)(\))?( )?{((.|\n)+)}(;)?$"
ELSE: Final[str] = r"^} else {((.|\n)+)};$"
ELIF: Final[str] = r"^} elif {((.|\n)+)}(;)?"

# Match statements
MATCH: Final[str] = r"^match (\))?(.*)(\))?( )?{((.|\n)+)};$"
CASE: Final[str] = r"^case (\()?(.*)(\))?( )?{((.|\n)+)}(;)?$"
DEFAULT: Final[str] = r"^default( )?{((.|\n)+)};$"

# Loops
WHILE: Final[str] = r"^while (\()?(.*)(\))?( )?{((.|\n)+)};$"
FOR: Final[str] = r"^for (\()?(.*)(\))?( )?{((.|\n)+)};$"

# Return
RETURN: Final[str] = r"^return (.*);$"

# Delete
DELETE: Final[str] = r"^delete (.*);$"

# Break
BREAK: Final[str] = r"^break;$"

# Continue
CONTINIUE: Final[str] = r"^continue;$"

# Try statements
TRY: Final[
    str
] = r"^try {((.|\n)+)} catch (\()?(.*)(\))?( )?{((.|\n)+)}(;)?"  # Try statements have to have at least one catch statement
CATCH: Final[str] = r"^} catch (\()?(.*)(\))?( )?{((.|\n)+)}(;)?"
THROW: Final[str] = r"^throw ([a-zA-Z0-9-_])+( from ([a-zA-Z0-9-_])+)?;$"
FINALLY: Final[str] = r"^} finally {((.|\n)+)};"
