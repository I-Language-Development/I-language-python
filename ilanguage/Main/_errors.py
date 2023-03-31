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

    def __init__(self, description: str, line: int = 0, column: int = 0) -> None:
        """Initialize a new unspecified error.

        :param description: Description of the error.
        :param line: Line the error occurred on.
        :param column: Column the error occurred on.
        """

        super().__init__(description, line, column)


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
