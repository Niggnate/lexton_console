from abc import ABC
from .node import Node

class BinaryNode(Node, ABC):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def nodes(self):
        return [self.left, self.op, self.right]

    @classmethod
    def construct_binary(cls, parser, make, part, ops):
        node = part.construct(parser)

        while parser.upcoming().has(*ops):
            op = parser.derive()
            right = part.construct(parser)
            node = make(node, op, right)

        return node
