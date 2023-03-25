"""
I Language math test.
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
    Iterable,
)

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from Modules._core import Math


#################
# INFINITY TEST #
#################


def test_lexer_tokens() -> None:
    """Tests infinity constant."""

    assert Math.Infinite == float("inf")


##############
# ROUND TEST #
##############


@pytest.mark.parametrize(
    "data, expected",
    [
        (1.123456789, 1),
        (1.5, 2),
        (0.00000000000000000000000000003, 0),
    ],
)
def test_round(data: float, expected: int) -> None:
    """Tests round function.

    Args:
        data (float): Input data.
        expected (int): Expected result.
    """

    assert Math._round(data) == expected
