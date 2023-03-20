"""
I Language Random module.
Version: 0.1.0

Copyright (c) 2023-present ElBe Development.

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

import random
from typing import (
    Any,
    List,
)


###########
# RANDINT #
###########

def randint(minimum: int, maximum: int) -> int:
    """Generates a random number.

    :param minimum: Lowest possible value.
    :param maximum: Highest possible value.
    :return: Random number between minimum and maximum.
    """

    return random.randint(minimum, maximum)


###########
# CHOICES #
###########

def choices(iterable: List, choices: int = 1) -> Any:
    """Returns a random value from a given list.

    :param iterable: List to return a random value from.
    :param choices: Number of choices to return form the iterable. If choices is bigger than the iterable, the remaining
                    values will be skipped.
    :return: Random value(s) from iterable.
    """

    if choices == 1:
        return random.choice(iterable)
    else:
        return random.choices(iterable)

###########
# SHUFFLE #
###########
