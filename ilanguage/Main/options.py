"""
I Language options.
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

from typing import (
    Any,
    Dict,
    List,
    Union,
)

###########
# OPTIONS #
###########

options: Dict[str, Union[bool, str, List[Any]]] = {
    # Keep ordered
    "enable_all_experimental_features": False,  # Enables all experimental features.
    "enabled_experimental_features": [          # Enables listed experimental features.
        # Possible values: "semicolon_not_required"
    ],
    "exit_zero": False,                         # Exits with exit code zero, even if errors occur.
                                                # When an exit using the PyAPI is called, the exit can have non-zero exit codes tho.
}
