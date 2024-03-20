class Worker:
    def __init__(self, row):
        self.row = row
        self.locale = [0, 0]
        self.traced = [len(row), -1]

    def done(self):
        return self.locale[1] >= len(self.row)

    def upcoming(self):
        return "EOF" if self.done() else self.row[self.locale[1]]

    def derive(self):
        symbol = self.upcoming()
        self.locale[1] += 0 if self.done() else 1
        return symbol

    def ignore(self):
        self.locale[0] = self.locale[1]

    def derived(self):
        return self.row[self.locale[0]:self.locale[1]]

    def create_locale(self):
        locale, derived = self.locale.copy(), self.derived()
        self.locale[0] = self.locale[1]
        return locale, derived

    def trace(self, token):
        self.traced[0] = min(token.locale[0], self.traced[0])
        self.traced[1] = max(token.locale[1], self.traced[1])

    def obtain_traces(self):
        traces = "   "

        for i in range(len(self.row) + 1):
            between = self.traced[0] <= i < self.traced[1]
            traces += "^" if between or self.traced[0] == i else " "

        return traces
