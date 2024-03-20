from .multiplication_expression import MultiplicationExpression
from ..nodes.binary_node import BinaryNode

class AdditionExpression(BinaryNode):
    @classmethod
    def construct(cls, parser):
        return cls.construct_binary(parser, cls, MultiplicationExpression, ["+", "-"])

    def interpret(self):
        left = self.left.interpret()
        right = self.right.interpret()

        return left - right if self.op.has("-") else left + right
