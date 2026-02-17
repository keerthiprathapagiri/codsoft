import math

# Initialize board
board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"


# Print board
def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print()


# Check winner
def check_winner(player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False


# Check draw
def is_draw():
    return " " not in board


# Get available moves
def get_empty_cells():
    return [i for i in range(9) if board[i] == " "]


# Minimax with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):

    if check_winner(AI):
        return 10 - depth

    if check_winner(HUMAN):
        return depth - 10

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for move in get_empty_cells():
            board[move] = AI
            score = minimax(depth + 1, False, alpha, beta)
            board[move] = " "

            best_score = max(best_score, score)
            alpha = max(alpha, score)

            if beta <= alpha:
                break

        return best_score

    else:
        best_score = math.inf

        for move in get_empty_cells():
            board[move] = HUMAN
            score = minimax(depth + 1, True, alpha, beta)
            board[move] = " "

            best_score = min(best_score, score)
            beta = min(beta, score)

            if beta <= alpha:
                break

        return best_score


# AI Move
def ai_move():
    best_score = -math.inf
    best_move = None

    for move in get_empty_cells():
        board[move] = AI
        score = minimax(0, False, -math.inf, math.inf)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = AI


# Human Move
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move in get_empty_cells():
                board[move] = HUMAN
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Please enter a number between 1 and 9.")


# Main Game Loop
def play_game():

    print("TIC TAC TOE - HUMAN vs AI")
    print("You are X | AI is O")
    print("Positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    print_board()

    while True:

        # Human turn
        human_move()
        print_board()

        if check_winner(HUMAN):
            print("🎉 You Win!")
            break

        if is_draw():
            print("🤝 It's a Draw!")
            break

        # AI turn
        print("AI is thinking...")
        ai_move()
        print_board()

        if check_winner(AI):
            print("🤖 AI Wins!")
            break

        if is_draw():
            print("🤝 It's a Draw!")
            break


# Start Game
if __name__ == "__main__":
    play_game()
