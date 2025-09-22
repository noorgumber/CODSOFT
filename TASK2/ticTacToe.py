from aiPlayer import best_turn, is_win, is_draw

def printBoard(board):
    for row in [board[i:i+3] for i in range(0,9,3)]:
        print('| ' + ' | '.join(row) + ' |')

def gamePlay():
    board = [' '] * 9
    curr_player = 'X'

    print("Positions are numbered like this:")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 ")
    print("You are X, AI is O\n")

    while True:
        printBoard(board)

        if curr_player == 'X':
            try:
                turn = int(input("Enter your move (0-8): "))
                if turn < 0 or turn > 8 or board[turn] != ' ':
                    print("Invalid!! Try again.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number 0-8.")
                continue
        else:
            print("AI is making its move...")
            turn = best_turn(board)

        board[turn] = curr_player

        if is_win(board, curr_player):
            printBoard(board)
            print(f"{curr_player} wins!! ")
            break
        elif is_draw(board):
            printBoard(board)
            print("Oops.. It's a draw.")
            break

        curr_player = 'O' if curr_player == 'X' else 'X'

if __name__ == "__main__":
    gamePlay()
