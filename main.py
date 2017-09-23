from Production import *

def main():
    p = Production("a", "b")
    print("Production rule: " + p.output())
    if p.generate("a"):
        print("Yay")
    else:
        print("Nay")

main()
