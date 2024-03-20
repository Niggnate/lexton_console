from .primary_expression import PrimaryExpression
from ..nodes.node import Node

class UnaryExpression(Node):
    def __init__(self, op, expression):
        self.op = op
        self.expression = expression

    def nodes(self):
        return [self.op, self.expression]

    @classmethod
    def construct(cls, parser):
        if parser.upcoming().has("+", "-", "~"):
            op = parser.derive()
            expression = UnaryExpression.construct(parser)
            return UnaryExpression(op, expression)

        return PrimaryExpression.construct(parser)

    def interpret(self):
        value = self.expression.interpret()

        match self.op.string:
            case "+":
                return value
            case "-":
                return -value
            case "~":
                return round(value)
