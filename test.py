def printHangman(numStages):
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    for stage in stages[:numStages]:
        print(stage)

def hangman(word):
    wrong = 0
    
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    

hangman([""])

