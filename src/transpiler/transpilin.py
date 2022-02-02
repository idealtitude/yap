#-*- coding: utf-8 -*-

"""Lexing and Parsing the input file."""

from typing import Any
from dataclasses import dataclass

@dataclass
class Node:
    """This class defines each node of the document."""
    name: str
    attributes: dict[str, str]
    autoclose: bool
    text: str | list[str | Node]
    parent: Node | None
    children: list[Node] | None
    sibling: Node | None
    state: bool # True → open, False -> closed
