from datetime import datetime

from lexing.lexer import Lexer
from lexing.worker import Worker

from parsing.parser import Parser
from util.exception.language_exception import LanguageException


class Application:
    def __init__(self):
        self.__style_config()
        self.running = True

    def __style_config(self):
        console_name = "Lexton Console\n"
        now = datetime.now()
        version = "v1.0.12"
        print("{} - {}\n\n{}".format(now, version, console_name))

    def derive_tree(self, row, parser, lexer):


        try:
            row = Worker(row)
            tokens = lexer.create_tokens(row) # show tokens
            tree = parser.create_tree(tokens) # show tree of expressions
            return tree
        except LanguageException as exception:
            return exception



    def launch(self):
        parser = Parser()
        lexer = Lexer()
        while self.running:
            row = input("→→ ")
            if row == "exit()" or row == "exit":
                break

            if row == "":
                continue

            try:
                tree = self.derive_tree(row, parser, lexer)
                print(tree)
                print(tree.interpret())
            except LanguageException as exception:
                print(exception)

if __name__ == "__main__":
    application = Application()
    application.launch()
