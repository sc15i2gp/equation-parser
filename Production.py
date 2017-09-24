class Production:
    # Leftside and rightSide refer to the sides of the production rules as written
    def __init__(self, leftSide, rightSide):
        self.leftSide = leftSide
        self.rightSide = rightSide

    def output(self):
        output = self.leftSide + " ==> " + self.rightSide[0]
        if len(self.rightSide) > 1:
            output += self.rightSide[1]
        return output

    def generate(self, inputSymbol):
        if inputSymbol == self.leftSide:
            return self.rightSide
        else:
            return ""

    def generates(self, outputSymbol):
        if len(self.rightSide) > 1:
            return outputSymbol == self.rightSide[0] + self.rightSide[1]
        return outputSymbol == self.rightSide[0]

    def inputSymbol(self):
        return self.leftSide
