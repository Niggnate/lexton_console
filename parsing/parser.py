from util.exception.parser_exception import ParserException
from .expressions.expression import Expression

class Parser:
    @property
    def expression(self):
        return Expression

    def __init__(self):
        self.tokens = None
        self.i = -1

    def upcoming(self):
        return self.tokens[self.i]

    def derive(self):
        token = self.upcoming()
        self.i += 1
        return token

    def expecting_has(self, *strings):
        if self.upcoming().has(*strings):
            return self.derive()

        raise ParserException(self.upcoming(), f"Expecting has {strings}")

    def expecting_of(self, *kinds):
        if self.upcoming().of(*kinds):
            return self.derive()

        raise ParserException(self.upcoming(), f"Expecting of {kinds}")

    def create_tree(self, tokens):
        self.tokens, self.i = tokens, 0
        node = Expression.construct(self)

        if self.upcoming().has("EOF"):
            return node

        raise ParserException(self.upcoming(), f"Unexpected token {self.upcoming()}")
