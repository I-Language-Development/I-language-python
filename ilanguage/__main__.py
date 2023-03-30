#!/usr/bin/python3
"""
I Language python package runner.
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

import platform
import sys

from . import Main  # pylint: disable=W0611


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


###########
# EXECUTE #
###########

if len(sys.argv[1:]) > 0:
    try:
        with open(sys.argv[1:][0], "r", encoding="utf-8") as file:
            pass
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except UnicodeEncodeError:
        print("Error: Can not read the specified file.")

else:
    print("Error: No file was specified.")
    sys.exit(1)
