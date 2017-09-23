class Production:
    # Leftside and rightSide refer to the sides of the production rules as written
    def __init__(self, leftSide, rightSide):
        self.leftSide = leftSide
        self.rightSide = rightSide

def main():
    p = Production("a", "b")
    print(p.leftSide + " --> " + p.rightSide)

main()
