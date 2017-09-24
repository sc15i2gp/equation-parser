from Grammar import *
from ParseTree import *

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

def printParseTree(rootNode):
    print(rootNode.nodeSymbol)
    if len(rootNode.children) > 0:
        printParseTree(rootNode.children[0])
        if len(rootNode.children) > 1:
            printParseTree(rootNode.children[1])


def constructParseTree(cykTable, cykPTable, grammar, n):
    #Process:
        #Input: current node coords in table, currentSymbol, parent node
        #Create current node: ParseTree(currentSymbol, parent node)
        #Get coords for child symbols
        #If coords not -1
            #For each combination of symbols:
                #If the current node generates the 2 symbols:
                    #Set left child node as 1st symbol
                    #Set right child node as 2nd symbol
    def constructNode(currentNodeCoords, currentSymbol, parentNode):
        currentNode = ParseTree(currentSymbol, parentNode)
        currentTableList = cykPTable[currentNodeCoords[0]][currentNodeCoords[1]]
        if currentTableList[0] != -1:
            firstCoords = currentTableList[0][0]
            secondCoords = currentTableList[0][1]
            firstTablePos = cykTable[firstCoords[0]][firstCoords[1]]
            secondTablePos = cykTable[secondCoords[0]][secondCoords[1]]
            for symbol1 in firstTablePos:
                br = False
                for symbol2 in secondTablePos:
                    if grammar.isProductionRule(currentSymbol, [symbol1, symbol2]):
                        currentNode.children.append(constructNode(firstCoords, symbol1, currentNode))
                        currentNode.children.append(constructNode(secondCoords, symbol2, currentNode))
                        br = True
                        break
                if br:
                    break
        return currentNode

    rootNode = constructNode([0, n], grammar.startSymbol, None)
    printCYKTable(cykTable)
    printCYKPTable(cykPTable)
    return rootNode

def getLeafNodes(rootNode):
    leaves = []
    #Process
        #Input: currentNode
        #If currentNode has no children
            #Add to leaves
        #Else
            #Call this process with child nodes
    def findLeaves(currentNode):
        if currentNode.hasChildren():
            findLeaves(currentNode.children[0])
            findLeaves(currentNode.children[1])
        else:
            leaves.append(currentNode)

    findLeaves(rootNode)
    return leaves

def parseLeafNodes(leaves, equationString):
    if len(leaves) == len(equationString):
        for i in range(len(leaves)):
            leaves[i].children.append(ParseTree(equationString[i], leaves[i]))

def acceptEquation():
    equation = input("Equation: ")
    return equation.replace(" ", "")

def main():
    g = genEquationGrammar()
    print(g.output())
    equation = acceptEquation()
    print()
    ret = g.generates(equation)
    gen = ret[0]
    cykTable = ret[1]
    cykPTable = ret[2]
    n = ret[3]
    print("Grammar generates " + equation + "? " + str(gen) + "\n")

    rootNode = constructParseTree(cykTable, cykPTable, g, n-1)
    leaves = getLeafNodes(rootNode)
    parseLeafNodes(leaves, equation)
    printParseTree(rootNode)
    print("\n")
    for leaf in leaves:
        print(leaf.nodeSymbol)

main()
