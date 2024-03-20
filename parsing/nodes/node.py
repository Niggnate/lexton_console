from abc import ABC, abstractmethod

class Node(ABC):
    @property
    def row(self):
        return self.nodes()[0].row

    @abstractmethod
    def nodes(self):
        pass

    def __repr__(self):
        return self.tree_repr()

    def tree_repr(self, prefix = " " * 4):
        string = type(self).__name__
        nodes = self.nodes()

        for i, node in enumerate(nodes):
            at_last = (i == len(nodes) - 1)
            symbol = "└──" if at_last else "├──"
            prefix_symbol = "" if at_last else "│"

            node_string = node.tree_repr(f"{prefix}{prefix_symbol}{' ' * 4}")
            string += f"\n{prefix}{symbol} {node_string}"

        return string

    def trace(self):
        for node in self.nodes():
            node.trace()

    @classmethod
    @abstractmethod
    def construct(cls, parser):
        pass

    @abstractmethod
    def interpret(self):
        pass
