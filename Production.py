class Production:
    # Leftside and rightSide refer to the sides of the production rules as written
    def __init__(self, leftSide, rightSide):
        self.leftSide = leftSide
        self.rightSide = rightSide

    def output(self):
        return self.leftSide + " ==> " + self.rightSide

    def generate(self, inputSymbol):
        if inputSymbol == self.leftSide:
            return self.rightSide
        else:
            return ""
