from .unary_expression import UnaryExpression
from ..nodes.binary_node import BinaryNode

class ExponentialExpression(BinaryNode):
    @classmethod
    def construct(cls, parser):
        node = UnaryExpression.construct(parser)

        if not parser.upcoming().has("**"):
            return node

        op = parser.derive()
        right = ExponentialExpression.construct(parser)
        return ExponentialExpression(node, op, right)


    def interpret(self):
        left = self.left.interpret()
        right = self.right.interpret()
        return left ** right
