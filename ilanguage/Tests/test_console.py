"""
I Language console test.
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


import pathlib
import sys
from typing import (
    Iterable,
)

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from Modules._core import Console  # pylint: disable=E0401, C0413


################
# CONSOLE TEST #
################


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [1, 2, 3, 4],
            """┌─────────┬─────────┐
│  Index  │  Value  │
├─────────┼─────────┤
│    0    │    1    │
│    1    │    2    │
│    2    │    3    │
│    3    │    4    │
└─────────┴─────────┘
""",
        ),
        (
            {1: "1", 2: "2", 3: "3", 4: "4"},
            """┌───────┬─────────┐
│  Key  │  Value  │
├───────┼─────────┤
│   1   │    1    │
│   2   │    2    │
│   3   │    3    │
│   4   │    4    │
└───────┴─────────┘
""",
        ),
        (
            (1, 2, 3, 4),
            """┌─────────┬─────────┐
│  Index  │  Value  │
├─────────┼─────────┤
│    0    │    1    │
│    1    │    2    │
│    2    │    3    │
│    3    │    4    │
└─────────┴─────────┘
""",
        ),
        (
            {1, 2, 3, 4},
            """┌─────────┬─────────┐
│  Index  │  Value  │
├─────────┼─────────┤
│    0    │    1    │
│    1    │    2    │
│    2    │    3    │
│    3    │    4    │
└─────────┴─────────┘
""",
        ),
    ],
)
def test_lexer_tokens(data: Iterable, expected: str) -> None:
    """Tests table creation.

    Args:
        data (Iterable): Data to test.
        expected (str): Expected result.
    """

    assert str(Console.Table(data)) == expected
