"""
I Language errors.
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


##########
# LINTER #
##########

# pylint: disable=R0903, W0622


###########
# IMPORTS #
###########

import sys


#########
# ERROR #
#########


class Error:
    """
    Represents a base error object.
    """

    def __init__(
        self,
        description: str,
        *,
        long_description: str = "",
        line: int = 0,
        column: int = 0,
        exit_code: int = 1,
    ) -> None:
        """Initializes a new error.

        Args:
            description (str): Error text.
            long_description (str, keyword only): Long, more detailed error text.
            line (int, keyword only): Line the error occurred on.
            column (int, keyword only): Column the error occurred on.
            exit_code (int, keyword only): Code to use when exiting. If code is 0, there won't be an exit.
        """

        print(
            f"Error: {description}, in line {line} column {column}.{long_description}"
        )
        if exit_code != 0:
            sys.exit(exit_code)


##########
# ERRORS #
##########


class Unspecified(Error):
    """
    Represents an unspecified error.
    """

    def __init__(
        self,
        description: str,
        line: int = 0,
        column: int = 0,
    ) -> None:
        super().__init__(
            description,
            line=line,
            column=column,
            exit_code=2,
        )


class UnknownError(Error):
    """
    Represents an unknown error.
    """

    def __init__(self, long_description: str, line: int = 0, column: int = 0) -> None:
        super().__init__(
            "Unknown error",
            long_description=long_description,
            line=line,
            column=column,
            exit_code=2,
        )


class EncodingError(Error):
    """
    Represents an encoding error.
    """

    def __init__(
        self, filename: str, encoding: str = "UTF-8", line: int = 0, column: int = 0
    ) -> None:
        super().__init__(
            "Encoding error",
            long_description=f"Tried to open file {filename} with the {encoding} encoding",
            line=line,
            column=column,
            exit_code=3,
        )


class KeyboardInterrupt(Error):
    """
    Represents a keyboard interrupt.
    """

    def __init__(self, line: int, column: int) -> None:
        super().__init__("Keyboard Interrupt", line=line, column=column, exit_code=4)


class OSError(Error):
    """
    Represents an operating system error.
    """

    def __init__(self, line: int, column: int) -> None:
        super().__init__(
            "OS Error",
            long_description="This error can be caused by anything." + \
                             "\nPlease report this errors to the bug tracker, if you need more help.",
            line=line,
            column=column,
            exit_code=5,
        )


class SyntaxError(Error):
    """
    Represents a syntax error.
    """

    def __init__(
        self,
        description: str = "Syntax error",
        *,
        long_description: str = "",
        line: int = 0,
        column: int = 0,
        exit_code: int = 3,
    ) -> None:
        super().__init__(
            description,
            long_description=long_description,
            line=line,
            column=column,
            exit_code=exit_code,
        )


class TypeError(SyntaxError):
    """
    Represents a type error.
    """

    def __init__(
        self,
        description: str = "Type error",
        *,
        line: int = 0,
        column: int = 0,
        expected: str = "",
        got: str = "",
        exit_code=4,
    ) -> None:
        expected = "type " + expected if "assignment" not in expected else expected
        got = "type " + got if "nothing" not in got else got

        super().__init__(
            description,
            long_description=f"Expected {expected} got {got}",
            line=line,
            column=column,
            exit_code=exit_code,
        )


class InvalidAssignmentError(TypeError):
    """
    Represents an invalid assignment error.
    """

    def __init__(self, *, got: str, line: int = 0, column: int = 0) -> None:
        super().__init__(
            "Invalid assignment error",
            line=line,
            column=column,
            expected="no assignment",
            got=got,
            exit_code=5,
        )


class EmptyAssignmentError(TypeError):
    """
    Represents an empty assignment error.
    """

    def __init__(self, *, expected: str, line: int = 0, column: int = 0) -> None:
        super().__init__(
            "Empty assignment error",
            line=line,
            column=column,
            expected=expected,
            got="nothing",
            exit_code=6,
        )


class UnclosedError(SyntaxError):
    """
    Represents an unclosed error.
    """

    def __init__(self, delimiter: str, line: int = 0, column: int = 0) -> None:
        super().__init__(
            "Unclosed error",
            long_description=f"Expected: {delimiter}",
            line=line,
            column=column,
            exit_code=7,
        )


class RuntimeError(Error):
    """
    Represents a runtime error.
    """

    def __init__(
        self,
        description: str = "Runtime error",
        *,
        long_description: str = "",
        line: int = 0,
        column: int = 0,
        exit_code: int = 8,
    ) -> None:
        super().__init__(
            description,
            long_description=long_description,
            line=line,
            column=column,
            exit_code=exit_code,
        )


class PythonError(RuntimeError):
    """
    Represents a python error.
    """

    def __init__(self, error: BaseException, line: int = 0, column: int = 0):
        super().__init__(
            description="Python Error",
            long_description=str(error),
            line=line,
            column=column,
            exit_code=9,
        )


class ValueError(Error):
    def __init__(self, line: int, column: int, obj, function_name: str):
        print(f"invalid argument {obj} for function {function_name}")
        super().__init__(
            description="Value Error", line=line, column=column, exit_code=11
        )


class MemoryError(RuntimeError):
    def __init__(
        self,
        line: int,
        column: int,
        exit_code=12,
        hint: str = "",
        description="Memory Error",
    ):
        if hint:
            print(hint)
        super().__init__(
            description=text, line=line, column=column, exit_code=exit_code
        )


class NameError(MemoryError):
    def __init__(self, line: int, column: int, name: str):
        hint = f"name {name} is not defined"
        super().__init__(
            description="Name Error", line=line, column=column, exit_code=13, hint=hint
        )


class KeyError(MemoryError):
    def __init__(self, line: int, column: int, key: str):
        hint = f"key {key} is not valid"
        super().__init__(
            description="Key Error", line=line, column=column, exit_code=14, hint=hint
        )


class IndexError(MemoryError):
    def __init__(self, line: int, column: int, index: int):
        hint = f"Index {index} out of range"
        super().__init__(
            description="Index Error", line=line, column=column, exit_code=15, hint=hint
        )


class ArithmeticError(RuntimeError):
    def __init__(self, line: int, column: int, exit_code=16, hint=""):
        if hint:
            print(hint)
        super().__init__(
            description="Arithmetic Error",
            line=line,
            column=column,
            exit_code=exit_code,
        )


class DivisionByZeroError(ArithmeticError):
    def __init__(self, line: int, column: int):
        super().__init__(
            line=line, column=column, exit_code=17, hint="Division by Zero"
        )


class FloatingPointError(ArithmeticError):
    def __init__(self, line: int, column: int):
        super().__init__(
            line=line, column=column, exit_code=18, hint="Floating Point Error"
        )


class TestError(RuntimeError):
    def __init__(self, line: int, column: int, test_number: int):
        super().__init__(
            description=f"Test {test_number} failed",
            line=line,
            column=column,
            exit_code=19,
        )


class OverflowError(Error):
    def __init__(
        self,
        line: int,
        column: int,
        exit_code=22,
        description="Overflow Error",
        hint="",
    ):
        if hint:
            print(hint)
        super().__init__(
            description=text, line=line, column=column, exit_code=exit_code
        )


class RecursionError(OverflowError):
    def __init__(self, line: int, column: int, depth: int):
        super().__init__(
            line=line,
            column=column,
            exit_code=23,
            description="Recursion Error",
            hint=f"Max recursion depth {depth} reached",
        )


class NumberOverflow(OverflowError):
    def __init__(self, line: int, column: int, _type: str):
        hint = f"Number Overflow for type {_type}"
        super().__init__(
            line=line,
            column=column,
            exit_code=24,
            description="Number Overflow",
            hint=hint,
        )


class BufferError(RuntimeError):
    def __init__(self, line: int, column: int):
        super().__init__(
            description="Buffer Error", line=line, column=column, exit_code=25
        )


####################
# HELPER FUNCTIONS #
####################


def description_from_message(message: str) -> str:
    """Returns the error description from a message.

    Args:
        message (str): The error message.

    Returns:
        (str): The error description.
    """

    return " ".join(message.split(",")[0].split(" ")[1:])


def line_from_message(message: str) -> int:
    """Returns the line number from a message.

    Args:
        message (str): The error message.

    Returns:
        (int): The line number.
    """

    return int(message.split(",")[1].split(" ")[3])


def column_from_message(message: str) -> int:
    """Returns the column number from a message.

    Args:
        message (str): The error message.

    Returns:
        (int): The column number.
    """

    return int(message.split(",")[1].split(" ")[5])
