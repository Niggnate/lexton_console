from abc import ABC
from .node import Node

class PrimaryNode(Node, ABC):
    def __init__(self, token):
        self.token = token

    def nodes(self):
        return [self.token]

    def tree_repr(self, prefix = " " * 4):
        return f"{type(self).__name__} ── {self.token}"
