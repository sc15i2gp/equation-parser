class ParseTree:
    def __init__(self, symbol, parent):
        self.children = []
        self.parent = parent
        self.nodeSymbol = symbol

    def hasChildren(self):
        return len(self.children) > 0

    def hasParent(self):
        if self.parent:
            return True
        else:
            return False

    def nodeValue(self):
        return self.nodeSymbol
