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
