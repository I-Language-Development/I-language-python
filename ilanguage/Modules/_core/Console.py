"""
I Language Console module.
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

###########
# IMPORTS #
###########

import io
import platform
from typing import (
    Dict,
    Iterable,
    List,
    Set,
    Tuple,
)


#########
# SETUP #
#########

# pylint: disable=R0801
if (
    platform.system() == "Windows" and platform.release() == "10"
):  # Fixes colored output on Windows
    import ctypes

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
# pylint: enable=R0801

#########
# TABLE #
#########


class Table:
    """
    Represents a printable table.
    """

    def __init__(self, data: Iterable) -> None:
        """Constructs a table with the given data.

        Args:
            data (Iterable): The data to construct the table with.
        """

        if isinstance(data, (Dict, List, Set, Tuple)):
            self.data = data
        elif isinstance(data, str):
            pass  # TODO (Ranastra): Add errors
        else:
            pass  # TODO (Ranastra): Add errors

    def __str__(self) -> str:
        """Returns the string representation of the table.

        Returns:
            The string representation of the table.
        """

        with io.StringIO() as result:
            if isinstance(self.data, Dict):
                length = 5, 7

                for key, value in self.data.items():
                    if len(str(key)) > length[0]:
                        length = len(str(key)), length[1]
                    if len(str(value)) > length[1]:
                        length = length[0], len(str(value))

                result.write(
                    f"┌{'─' * (length[0] + 2)}" + f"┬{'─' * (length[1] + 2)}" + "┐\n"
                )
                result.write(
                    f"│ {'Key'.center(length[0])} │ "
                    + f"{'Value'.center(length[1])} │\n"
                )
                result.write(
                    f"├{'─' * (length[0] + 2)}┼" + f"{'─' * (length[1] + 2)}┤\n"
                )

                for key, value in self.data.items():
                    result.write(
                        f"│ {str(key).center(length[0])} │ "
                        + f"{str(value).center(length[1])} │\n"
                    )

                result.write(
                    f"└{'─' * (length[0] + 2)}" + f"┴{'─' * (length[1] + 2)}" + "┘\n"
                )

            elif isinstance(self.data, (List, Set, Tuple)):
                length = 7, 7

                for index, value in enumerate(self.data):
                    if len(str(index)) > length[0]:
                        length = len(str(index)), length[1]
                    if len(str(value)) > length[1]:
                        length = length[0], len(str(value))

                result.write(
                    f"┌{'─' * (length[0] + 2)}" + f"┬{'─' * (length[1] + 2)}" + "┐\n"
                )
                result.write(
                    f"│ {'Index'.center(length[0])} │ "
                    + f"{'Value'.center(length[1])} │\n"
                )
                result.write(
                    f"├{'─' * (length[0] + 2)}┼" + f"{'─' * (length[1] + 2)}┤\n"
                )

                for index, value in enumerate(self.data):
                    result.write(
                        f"│ {str(index).center(length[0])} │ "
                        + f"{str(value).center(length[1])} │\n"
                    )

                result.write(
                    f"└{'─' * (length[0] + 2)}" + f"┴{'─' * (length[1] + 2)}" + "┘\n"
                )

            result = result.getvalue()

        return result

    def __repr__(self) -> str:
        """Returns the representation of the table.

        Returns:
            The representation of the table.
        """

        return str(self)


def table(data: Iterable) -> None:
    """Prints a table with the given data.

    Args:
        data (Iterable): The data to print.
    """

    print(Table(data))
