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

def constructParseTree(cykTable, cykPTable, grammar, n):

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
    return rootNode

def getLeafNodes(rootNode):
    leaves = []

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
            
def printParseTree(rootNode):
    print(rootNode.nodeSymbol)
    if len(rootNode.children) > 0:
        printParseTree(rootNode.children[0])
        if len(rootNode.children) > 1:
            printParseTree(rootNode.children[1])
