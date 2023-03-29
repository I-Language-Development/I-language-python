"""
I Language shell.
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

import sys
from typing import (
    Callable,
    Dict,
    List,
    Optional,
    Union,
)


####################
# HELPER FUNCTIONS #
####################


def register_command(
    name: str,
    function: Callable,
    commands: Dict[str, Dict[str, Union[str, List[str], Callable]]],
) -> Dict[str, Dict[str, Union[str, List[str], Callable]]]:
    """Registers a command.

    Args:
        name (str): The name of the command.
        function (Callable): The function to execute when the command is called.
        commands (Dict[str, Dict[str, Union[str, List[str], Callable]]]): Dictionary of commands.
    """

    commands[name] = {
        "description": function.__doc__.splitlines()[0],
        "long_description": [
            line.replace("    ", "", 1) for line in function.__doc__.splitlines()[2:]
        ],
        "function": function,
    }

    return commands


############
# COMMANDS #
############


def exit_command(*_) -> None:
    """Exits the shell.

    Exits the shell.
    """

    sys.exit(0)


def help_command(  # pylint: disable=W1113
    commands: Dict[str, Dict[str, Union[str, List[str], Callable]]],
    command: Optional[str] = "",
    *_,
) -> None:
    """Shows this message or help for a specific command.

    Shows the help message or help for a specified command.

    Usage: help [command]
    Arguments:
        command (Optional): The name of the command to show the help for.
    """

    if command is None or command == "" or command.isspace():
        print("Usage: help [command]\n")
        print("Available commands:")
        for key, value in commands.items():
            print(f"{key:20} {value['description']}")
    else:
        for key, value in commands.items():
            if command.lower() == key:
                print("\n".join(commands[key]["long_description"]))


##############
# MAIN SHELL #
##############


def main() -> None:
    """
    Main shell function.
    """

    commands = {}

    commands = register_command("exit", exit_command, commands)
    commands = register_command("help", help_command, commands)

    print(
        r"""
 _____   _                                              
|_   _| | |                                             
  | |   | |     __ _ _ __   __ _ _   _  __ _  __ _  ___      I language shell   
  | |   | |    / _` | '_ \ / _` | | | |/ _` |/ _` |/ _ \     Copyright (c) 2023-present I Language Development.
 _| |_  | |___| (_| | | | | (_| | |_| | (_| | (_| |  __/
|_____| |______\__,_|_| |_|\__, |\__,_|\__,_|\__, |\___|
                            __/ |             __/ |     
                           |___/             |___/  
                                
You can use the help command, to get a list of commands.
"""
    )

    while True:
        try:
            command = input(">>> ").lower().split(" ")

            for key, values in commands.items():
                if key == command[0]:
                    values["function"](commands, *command[1:])

        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    main()
