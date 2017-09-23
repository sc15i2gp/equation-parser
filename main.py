from Grammar import *

def genTestGrammar():
    p0 = Production("S", "T")
    p1 = Production("T", "a")
    p2 = Production("T", "b")
    variables = ["S", "T"]
    terminals = ["a", "b"]
    startSymbol = "S"
    productions = [p0, p1, p2]
    grammar = Grammar(variables, terminals, startSymbol, productions)
    return grammar

def main():
    g = genTestGrammar()
    print(g.output())

main()
