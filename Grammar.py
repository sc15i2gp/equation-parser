from Production import *
class Grammar:
    def __init__(self, variables, terminals, startSymbol, productions):
        self.terminals = terminals
        self.variables = variables
        self.startSymbol = startSymbol
        self.productions = productions

    def output(self):
        outputString = "Grammar <V, T, S, P>: \n"
        outputString += "V = " + str(self.variables) + "\n"
        outputString += "T = " + str(self.terminals) + "\n"
        outputString += "S = " + self.startSymbol + "\n"
        outputString += "P = "
        productionSet = []
        for production in self.productions:
            productionSet.append(production.output())
        outputString += str(productionSet)
        return outputString

    def isTerminal(self, symbol):
        return symbol in self.terminals

    def isVariable(self, symbol):
        return symbol in self.variables

    def isProductionRule(self, inputSymbol, outputSymbol):
        for production in self.productions:
            if production.generate(inputSymbol) == outputSymbol:
                return True
        return False

    def generates(self, string, returnTable = True):
        #Implements CYK
        n = len(string)
        if n < 1:
            return False
        else:
            V = [[[] for x in range(n)] for y in range(n)]
            N = [[[] for x in range(n)] for y in range(n)]

            for i in range(n):
                #V[i][i] = {A in V where A ==> string[i] is a production rule}
                currentChar = string[i]
                for production in self.productions:
                    if production.generates(currentChar):
                        V[i][i].append(production.inputSymbol())
                N[i][i].append(-1)

            for b in range(1, n):
                for i in range(1, n-b+1):
                    k = i + b
                    V[i-1][k-1] = []
                    for j in range(i, k):
                        for production in self.productions:
                            if len(production.rightSide) == 1:
                                continue
                            else:
                                if production.rightSide[0] in V[i-1][j-1] and production.rightSide[1] in V[j][k-1]:
                                    V[i-1][k-1].append(production.inputSymbol())
                                    N[i-1][k-1].append(([i-1, j-1], [j, k-1]))
            if returnTable:
                return self.startSymbol in V[i-1][n-1], V, N, n
            else:
                return self.startSymbol in V[i-1][n-1]

def genEquationGrammar():
    variables = ["S","E", "E1", "E2", "O", "R", "b1", "b2"]
    numbers = [str(x) for x in range(10)]
    operators = ["+", "-", "*", "/", "^"]
    parentheses = ["(", ")"]
    terminals = numbers + operators + parentheses
    startSymbol = "E"
    pairs = [["E", ["E", "E1"]], ["E1", ["O", "E"]], ["E", ["b1", "E2"]],
             ["E2", ["E", "b2"]], ["E", ["R", "R"]], ["R", ["R", "R"]],
             ["R", ["0"]], ["R", ["1"]], ["R", ["2"]], ["R", ["3"]], ["R", ["4"]],
             ["R", ["5"]], ["R", ["6"]], ["R", ["7"]], ["R", ["8"]], ["R", ["9"]],
             ["E", ["0"]], ["E", ["1"]], ["E", ["2"]], ["E", ["3"]], ["E", ["4"]],
             ["E", ["5"]], ["E", ["6"]], ["E", ["7"]], ["E", ["8"]], ["E", ["9"]],
             ["b1", ["("]], ["b2", [")"]],
             ["O", ["-"]],
             ["O", ["+"]],
             ["O", ["*"]],
             ["O", ["/"]],
             ["O", ["^"]]]
    productions = []
    for pair in pairs:
        productions.append(Production(pair[0], pair[1]))
    g = Grammar(variables, terminals, startSymbol, productions)
    return g

def printCYKPTable(cykPTable):
    print("CYK P Table: ")
    bar = ""
    for i in range(160):
        bar += "-"
    print(bar)
    for row in cykPTable:
        for column in row:
            string = str(column)
            maxStrLen = 32
            for i in range(maxStrLen - len(string)):
                string += " "
            print(string, end="")
        print()
    print("\n")

def printCYKTable(cykTable):
    print("CYK Table: ")
    bar = ""
    for i in range(160):
        bar += "-"
    print(bar)
    for row in cykTable:
        for column in row:
            maxStrLen = 32
            string = "["
            if len(column) > 0:
                string += column[0]
                if len(column) > 1:
                    string += ", " + column[1]
            string += "]"
            strLen = len(string)
            for i in range(maxStrLen - strLen):
                string += " "
            print(string, end="")
        print()
    print("\n")
