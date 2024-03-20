from abc import ABC
from .addition_expression import AdditionExpression
from ..nodes.node import Node

class Expression(Node, ABC):
    @classmethod
    def construct(cls, parser):
        return AdditionExpression.construct(parser)
