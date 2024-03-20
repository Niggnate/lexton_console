class UToken:
    def __init__(self, kind, row):
        self.kind = kind
        self.row = row
        self.locale, self.string = row.create_locale()

        self.string = self.string or "EOF"

    def __repr__(self):
        return f"{self.kind[0]}'{self.string}'"

    def tree_repr(self, _):
        return repr(self)

    def trace(self):
        self.row.trace(self)

    def has(self, *strings):
        return self.string in strings

    def of(self, *kinds):
        return self.kind in kinds
