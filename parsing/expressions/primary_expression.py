import math

from ..nodes.node import Node
from ..nodes.primary_node import PrimaryNode

class PrimaryExpression(Node):
    def __init__(self, left, expression, right):
        self.left = left
        self.expression = expression
        self.right = right

    def nodes(self):
        return [self.left, self.expression, self.right]

    def interpret(self):
        value = self.expression.interpret()

        match self.left.string:
            case "(":
                return value
            case "|":
                return math.fabs(value)
            case "_":
                return math.floor(value)
            case "^":
                return math.ceil(value)

    @classmethod
    def construct(cls, parser):
        if not parser.upcoming().has("(", "|", "_", "^"):
            return Number.construct(parser)

        left = parser.derive()
        expression = parser.expression.construct(parser)
        right = parser.expecting_has(")" if left.has("(") else left.string)

        return PrimaryExpression(left, expression, right)



class Number(PrimaryNode):
    @classmethod
    def construct(cls, parser):
        return Number(parser.expecting_of("Number"))

    def interpret(self):
        return (float if "." in self.token.string else int)(self.token.string)
