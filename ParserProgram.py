from Grammar import *
from ParseTree import *
from InstructionTree import *

class EquationParserProgram:
    def __init__(self):
        self.running = False
        self.command = ""
        self.result = ""
        self.grammar = genEquationGrammar()

    def acceptInput(self):
        self.command = input(">>> ")

    def process(self):
        #Accepts:
            #Equations
            #Print grammar
            #Quit
        if self.command == "quit":
            self.running = False
            self.result = "Goodbye"
        elif self.command == "print grammar" or self.command == "print":
            self.result = self.grammar.output()
        else:
            self.command = self.command.replace(" ", "")
            results = self.grammar.generates(self.command)
            if results[0]:
                cykTable = results[1]
                cykPTable = results[2]
                n = results[3]
                pTreeRoot = constructParseTree(cykTable, cykPTable, self.grammar, n-1)
                leaves = getLeafNodes(pTreeRoot)
                parseLeafNodes(leaves, self.command)
                iTree = parseToInstructionTree(pTreeRoot)
                self.result = evaluateInstructionTree(iTree)
            else:
                self.result = "Error: Command not recognised!"

    def output(self):
        print(str(self.result))
        print()

    def run(self):
        self.running = True
        while(self.running):
            #Accept input
            self.acceptInput()
            #Process input
            self.process()
            #Output
            self.output()
