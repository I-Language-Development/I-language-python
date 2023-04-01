"""
I Language errors.
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


##########
# LINTER #
##########

# pylint: disable=R0903


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
        self, text: str, line: int = 0, column: int = 0, exit_code: int = 1
    ) -> None:
        """Initializes a new type.

        :param text: Error text
        :param line: Line the error occurred on.
        :param column: Column the error occurred on.
        :param exit_code: Code to use when exiting. If code is 0, there won't be an exit.
        """

        print(f"Error: {text}, in line {line} column {column}.")
        sys.exit(exit_code)


##########
# ERRORS #
##########


class Unspecified(Error):
    """
    Represents a unspecified error.
    """

    def __init__(self, description: str, line: int = 0, column: int = 0, exit_code=2) -> None:
        """Initialize a new unspecified error.
        :param description: Description of the error.
        :param line: Line the error occurred on.
        :param column: Column the error occurred on.
        """

        super().__init__(text=description, line=line, column=column, exit_code=exit_code)

class UnknownError(Error):
    def __init__(self, line: int, column: int):
        super().__init__(description="Don't you dare trying to break this stuff", line=line, column=column)


class SyntaxError(Error):
    def __init__(self, line: int, column: int, text="Syntax Error", hint: str = "", exit_code=3):
        if hint: print(hint)
        super().__init__(text=text, line=line, column=column, exit_code=exit_code)


class TypeError(SyntaxError):
    def __init__(self, line: int, column: int, type_expected, type_got, text="Type Error", exit_code=4):
        hint = f"expected {type_expected} got {type_got}"
        super().__init__(text=text, line=line, column=column, exit_code=exit_code, hint=hint)


class InvalidAssignmentError(TypeError):
    def __init__(self, line: int, column: int, type_expected, type_got):
        super().__init__(line=line, column=column, text="Invalid Assignment", exit_code=5, type_expected=type_expected, type_got=type_got)


class EmptyAssignmentError(TypeError):
    def __init__(self, line: int, column: int, type_expected):
        super().__init__(line=line, column=column, text="Empty Assignment", exit_code=6, type_expected=type_expected, type_got=None)


class UnclosedError(SyntaxError):
    def __init__(self, line: int, column: int, delimiter: str):
        super().__init__(line=line, column=column, exit_code=7, hint=f"Expected: {delimiter}")


class RuntimeError(Error):
    def __init__(self, line: int, column: int, exit_code=8, text="Runtime Error"):
        super().__init__(text=text, line=line, column=column, exit_code=exit_code)


class PythonError(RuntimeError):
    def __init__(self, line: int, column: int, python_error: BaseException):
        print(python_error)
        super().__init__(text="Python Error", line=line, column=column, exit_code=9)


class EncodingError(Error):
    def __init__(self, line: int, column: int, text="Encoding Error"):
        super().__init__(text=text, line=line, column=column, exit_code=10)


class ValueError(Error):
    def __init__(self, line: int, column: int, obj, function_name: str):
        print(f"invalid argument {obj} for function {function_name}")
        super().__init__(text="Value Error", line=line, column=column, exit_code=11)


class MemoryError(RuntimeError):
    def __init__(self, line: int, column: int, exit_code=12, hint: str = "", text="Memory Error"):
        if hint: print(hint)
        super().__init__(text=text, line=line, column=column, exit_code=exit_code)


class NameError(MemoryError):
    def __init__(self, line: int, column: int, name: str):
        hint = f"name {name} is not defined"
        super().__init__(text="Name Error", line=line, column=column, exit_code=13, hint=hint)


class KeyError(MemoryError):
    def __init__(self, line: int, column: int, key: str):
        hint = f"key {key} is not valid"
        super().__init__(text="Key Error", line=line, column=column, exit_code=14, hint=hint)

class IndexError(MemoryError):
    def __init__(self, line: int, column: int, index: int):
        hint = f"Index {index} out of range"
        super().__init__(text="Index Error", line=line, column=column, exit_code=15, hint=hint)


class ArithmeticError(RuntimeError):
    def __init__(self, line: int, column: int, exit_code=16, hint=""):
        if hint: print(hint)
        super().__init__(text="Arithmetic Error", line=line, column=column, exit_code=exit_code)


class DivisionByZeroError(ArithmeticError):
    def __init__(self, line: int, column: int):
        super().__init__(line=line, column=column, exit_code=17, hint="Division by Zero")


class FloatingPointError(ArithmeticError):
    def __init__(self, line: int, column: int):
        super().__init__(line=line, column=column, exit_code=18, hint="Floating Point Error")


class TestError(RuntimeError):
    def __init__(self, line: int, column: int, test_number: int):
        super().__init__(text=f"Test {test_number} failed", line=line, column=column, exit_code=19)


class OSError(Error):
    def __init__(self, line: int, column: int, function_name: str):
        print(f"there was an Error in function {function_name}")
        super().__init__(text="OS Error", line=line, column=column, exit_code=20)


class KeyboardInterrupt(Error):
    def __init__(self, line: int, column: int):
        super().__init__(text="Keyboard Interrupt", line=line, column=column, exit_code=21)


class OverflowError(Error):
    def __init__(self, line: int, column: int, exit_code=22, text="Overflow Error", hint=""):
        if hint: print(hint)
        super().__init__(text=text, line=line, column=column, exit_code=exit_code)


class RecursionError(OverflowError):
    def __init__(self, line: int, column: int, depth: int):
        super().__init__(line=line, column=column, exit_code=23, text="Recursion Error", hint=f"Max recursion depth {depth} reached")


class NumberOverflow(OverflowError):
    def __init__(self, line: int, column: int, type):
        hint = f"Number Overflow for Type {type}"
        super().__init__(line=line, column=column, exit_code=24, text="Number Overflow", hint=hint)


class BufferError(RuntimeError):
    def __init__(self, line: int, column: int):
        super().__init__(text="Buffer Error", line=line, column=column, exit_code=25)


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
