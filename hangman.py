def hangman(word):
    
    """
    wrong: プレイヤーが間違えた回数
    

    """

    count = 0
    wrong = 0
    stages = ["",
              "_____     ",
              "|    |    ",
              "|    |    ",
              "|    0    ",
              "|   /||   ",
              "|    |    ",
              "|   /||   ",
              "|         "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Wellcome to the Hangman!")
    while wrong < len(stages) - 1:
        count += 1
        print("----------count:{}----------".format(count))
        msg = "Please input a character:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print("[SUCCESS!]")
        else:
            wrong += 1
        print("[↓Word↓]")
        print(" ".join(board))
        print("\n[↓Hangman↓]")
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("[YOU WIN! {} count.]".format(count))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("[YOU LOSE! A: {}.]".format(word))


hangman("division")
