"""
I Language Console module.
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

import os
from typing import (
    Dict,
    List,
    Set,
    Tuple,

    NewType,
)

# from ...Main import _errors


#########
# TABLE #
#########


class Table:
    """
    Represents a printable table.
    """

    def __init__(self, data: Dict | List | Set | Tuple) -> None:
        """Constructs a table with the given data.

        :param data: The data to construct the table with.
        """

        self.vertical_char = "│"
        self.horizontal_char = "─"
        self.junction_char = "┼"
        self.left_junction_char = "├"
        self.right_junction_char = "┤"
        self.top_left_junction_char = "┌"
        self.top_right_junction_char = "┐"
        self.top_junction_char = "┬"
        self.bottom_left_junction_char = "└"
        self.bottom_right_junction_char = "┘"
        self.bottom_junction_char = "┴"

        if (
            isinstance(data, Dict)
            or isinstance(data, List)
            or isinstance(data, Set)
            or isinstance(data, Tuple)
        ):
            self.data = data
        else:
            pass  # TODO (ElBe): Add errors

    def __str__(self) -> str:
        """Returns the string representation of the table.

        :return: The string representation of the table.
        """

        result = ""

        if isinstance(self.data, Dict):
            length = 5, 7

            for key, value in self.data.items():
                if len(str(key)) > length[0]:
                    length = len(str(key)), length[1]
                if len(str(value)) > length[1]:
                    length = length[0], len(str(value))

            result += f"{self.top_left_junction_char}{self.horizontal_char * (length[0] + 2)}" + \
                      f"{self.top_junction_char}{self.horizontal_char * (length[1] + 2)}" + \
                      f"{self.top_right_junction_char}\n"
            result += f"{self.vertical_char} {'Key'.center(length[0])} {self.vertical_char} " + \
                      f"{'Value'.center(length[1])} {self.vertical_char}\n"
            result += f"{self.left_junction_char}{self.horizontal_char * (length[0] + 2)}{self.junction_char}" + \
                      f"{self.horizontal_char * (length[1] + 2)}{self.right_junction_char}\n"

            for key, value in self.data.items():
                result += f"{self.vertical_char} {str(key).center(length[0])} {self.vertical_char}" + \
                          f"{str(value).center(length[1])} {self.vertical_char}\n"

            result += f"{self.bottom_left_junction_char}{self.horizontal_char * (length[0] + 2)}" + \
                      f"{self.bottom_junction_char}{self.horizontal_char * (length[1] + 2)}" + \
                      f"{self.bottom_right_junction_char}\n"

        elif (
            isinstance(self.data, List)
            or isinstance(self.data, Set)
            or isinstance(self.data, Tuple)
        ):
            length = 7, 7

            for index, value in enumerate(self.data):
                if len(str(index)) > length[0]:
                    length = len(str(index)), length[1]
                if len(str(value)) > length[1]:
                    length = length[0], len(str(value))

            result += f"{self.top_left_junction_char}{self.horizontal_char * (length[0] + 2)}" + \
                      f"{self.top_junction_char}{self.horizontal_char * (length[1] + 2)}" + \
                      f"{self.top_right_junction_char}\n"
            result += f"{self.vertical_char} {'Index'.center(length[0])} {self.vertical_char} " + \
                      f"{'Value'.center(length[1])} {self.vertical_char}\n"
            result += f"{self.left_junction_char}{self.horizontal_char * (length[0] + 2)}{self.junction_char}" + \
                      f"{self.horizontal_char * (length[1] + 2)}{self.right_junction_char}\n"

            for index, value in enumerate(self.data):
                result += f"{self.vertical_char} {str(index).center(length[0])} {self.vertical_char} " + \
                          f"{str(value).center(length[1])} {self.vertical_char}\n"

            result += f"{self.bottom_left_junction_char}{self.horizontal_char * (length[0] + 2)}" + \
                      f"{self.bottom_junction_char}{self.horizontal_char * (length[1] + 2)}" + \
                      f"{self.bottom_right_junction_char}\n"

        return result

    def __repr__(self) -> str:
        """Returns the representation of the table.

        :return: The representation of the table.
        """

        return str(self)


def table(data: Dict | List | Set | Tuple) -> None:
    """Prints a table with the given data.

    :param data: The data to print.
    """

    print(Table(data))
