"""
I Language AST.
Version: 0.1.2

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


#########
# TODOS #
#########

# TODO (ElBe): Extend this (#38)


###########
# IMPORTS #
###########

from __future__ import annotations

from dataclasses import dataclass, field
from typing import (
    Any,
    Dict,
    List,
    Optional,
)

import _types


#############
# BASE NODE #
#############


@dataclass
class Node:
    """Base class for all AST nodes."""

    name: str
    _type: str
    value: Any
    level: int
    below: List[Optional[Node]] = field(default_factory=list)
    arguments: Optional[Dict[str, str]] = None

    def __lt__(self: Node, compare_to: Node) -> bool:
        return (
            compare_to.level < self.level
        )  # This is supposed to be like this, the smaller the level, the higher it is in the tree


################
# BASE PROGRAM #
################


@dataclass(init=False)
class BaseProgram(Node):
    """Base program node."""

    def __init__(
        self,
        name: str,
        below: List[Optional[Node]],
        arguments: Optional[Dict[str, str]] = None,
    ) -> None:
        self.name = name
        self.below = below
        self.arguments = arguments

        super().__init__(name, "Program", None, 0, below, arguments)

    def __lt__(self: BaseProgram, compare_to: Node) -> bool:
        return False


##########
# IMPORT #
##########


@dataclass(init=False)
class Import(Node):
    """Import node."""

    def __init__(
        self,
        name: str,
        level: int,
        import_selectors: Optional[List[Optional[Node]]] = None,
        arguments: Optional[Dict[str, str]] = None,
    ) -> None:
        self.name = name
        self.level = level
        self.import_selectors: List[Optional[Node]] = (
            import_selectors if import_selectors is not None else []
        )
        self.arguments = arguments

        super().__init__(name, "Import", None, level, self.import_selectors, arguments)


############
# CONSTANT #
############


@dataclass(init=False)
class Constant(Node):
    """Constant node."""

    def __init__(
        self,
        name: str,
        value: Any,
        level: int,
        _type: _types.BaseType = _types.Dynamic,
        conditions: Optional[List[str]] = None,
        arguments: Optional[Dict[str, str]] = None,
    ) -> None:
        self.name = name
        self.value = value
        self.level = level
        self.type = _type
        self.conditions = conditions if conditions is not None else []
        self.arguments = arguments

        super().__init__(
            name,
            f"Constant type {_type.__class__.__name__}",
            value,
            level,
            self.conditions,
            arguments,
        )
