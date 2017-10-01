from ParseTree import *

class InstructionTree:
    def __init__(self, node, children):
        self.node = node
        self.children = children

class Node:
    def __init__(self, symbol):
        self.nodeSymbol = symbol

class InstructionNode(Node):
    def __init__(self, operator):
        super(InstructionNode, self).__init__(operator)
        self.operator = operator

class NumberNode(Node):
    def __init__(self, number):
        super(NumberNode, self).__init__(str(number))
        self.number = number

def parseToInstructionTree(parseTree):
    rootNode = parseTree
    return processExpression(rootNode)

def processExpression(parentNode):
    lChild = parentNode.children[0]
    if len(parentNode.children) > 1:
        rChild = parentNode.children[1]
        if lChild.nodeSymbol == "E" and rChild.nodeSymbol == "E1":
            iNode = InstructionNode(parentNode.children[1].children[0].children[0].nodeSymbol)
            iTree = InstructionTree(iNode, [])
            iTree.children.append(processExpression(parentNode.children[0]))
            iTree.children.append(processExpression(parentNode.children[1].children[1]))
            return iTree
        elif lChild.nodeSymbol == "b1" and rChild.nodeSymbol == "E2":
            return processExpression(parentNode.children[1].children[0])
        elif lChild.nodeSymbol == "R" and lChild.nodeSymbol == "R":
            lSymbol = lChild.children[0].nodeSymbol
            rSymbol = rChild.children[0].nodeSymbol
            numberSymbol = lSymbol + rSymbol
            number = float(numberSymbol)
            nNode = NumberNode(number)
            iTree = InstructionTree(nNode, [])
            return iTree
    else:
        numberSymbol = lChild.nodeSymbol
        number = float(numberSymbol)
        nNode = NumberNode(number)
        iTree = InstructionTree(nNode, [])
        return iTree

def evaluateInstructionTree(instructionTree):
    currentNode = instructionTree.node
    if type(currentNode) is NumberNode:
        return currentNode.number
    else:
        lChild = instructionTree.children[0]
        rChild = instructionTree.children[1]
        lResult = evaluateInstructionTree(lChild)
        rResult = evaluateInstructionTree(rChild)
        if currentNode.operator is "+":
            return lResult + rResult
        elif currentNode.operator is "-":
            return lResult - rResult
        elif currentNode.operator is "*":
            return lResult * rResult
        elif currentNode.operator is "/":
            return lResult / rResult
        elif currentNode.operator is "^":
            return lResult ** rResult

def printInstructionTree(rootNode):
    print(rootNode.node.nodeSymbol)
    if len(rootNode.children) > 0:
        printInstructionTree(rootNode.children[0])
        printInstructionTree(rootNode.children[1])
