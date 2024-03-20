from util.exception.lexer_exception import LexerException
from .u_token import UToken

class Lexer:
    def __init__(self):
        self.row = None

    def generate_token(self, kind):
        return UToken(kind, self.row)

    def create_tokens(self, row):
        self.row = row
        tokens = []

        while not self.row.done():
            self.ignore_spaces()
            if self.row.done():
                break

            tokens += [self.create_token()]
        tokens += [self.generate_token("Punctuator")]
        return tokens

    def ignore_spaces(self):
        while self.row.upcoming().isspace():
            self.row.derive()
            self.row.ignore()

    def create_token(self):
        if self.row.upcoming() in "()|_^":
            return self.generate_punctuator()

        if self.row.upcoming() in "~+-*/%":
            return self.generate_operator()

        if self.row.upcoming() in "0123456789.":
            return self.generate_number()

        self.row.derive()
        raise LexerException(self.generate_token("?"), "Unrecognized symbol")

    def generate_punctuator(self):
        self.row.derive()
        return self.generate_token("Punctuator")

    def generate_operator(self):
        op = self.row.derive()

        if op == "*" and self.row.upcoming() == "*":
            self.row.derive()

        return self.generate_token("Operator")

    def generate_number(self):
        while self.row.upcoming() in "0123456789.":
            self.row.derive()

        if self.row.derived().count(".") < 2:
            return self.generate_token("Number")

        raise LexerException(self.generate_token("Number"), "Numbers can have at least one decimal point!")
