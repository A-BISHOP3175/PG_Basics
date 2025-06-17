import random

def hangman():
    word_list = ["cat", "dog", "apple", "banana", "orange"]  # List of possible words
    word = random.choice(word_list)

    stages = [
        "",
        "________        ",
        "|               ",
        "|        |      ",
        "|        0      ",
        "|       /|\\     ",
        "|       / \\     ",
        "|               "
    ]

    rletters = list(word)
    board = ["__"] * len(word)
    wrong = 0
    win = False

    print("ハングマンへようこそ")
    print(f"単語は {len(word)} 文字です。")
    print(" ".join(board))

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg).lower()

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print("いいね！当たり！")
        else:
            wrong += 1
            print("ハズレ！残り間違い回数:", len(stages) - 1 - wrong)

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "__" not in board:
            print("あなたの勝ち！おめでとう！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("あなたの負け！正解は {} でした。".format(word))

hangman()

