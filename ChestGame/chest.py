board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

def print_board(board):
    print("  a b c d e f g h")
    for i in range(8):
        print(f"{8-i} ", end="")
        for j in range(8):
            print(board[i][j], end=" ")
        print(f"{8-i}")
    print("  a b c d e f g h")

def pos_to_coords(pos):
    col = ord(pos[0]) - ord("a")
    row = 8 - int(pos[1])
    return row, col

def coords_to_pos(row, col):
    return chr(ord("a") + col) + str(8 - row)

def is_valid_move(board, start, end, turn):
    start_row, start_col = pos_to_coords(start)
    end_row, end_col = pos_to_coords(end)
    piece = board[start_row][start_col]
    target = board[end_row][end_col]
    
    if piece == " ":
        return False
    if (turn == "white" and piece.islower()) or (turn == "black" and piece.isupper()):
        return False
    if target != " " and ((turn == "white" and target.isupper()) or (turn == "black" and target.islower())):
        return False
    
    if piece.lower() == "r":  # Rook
        if start_row != end_row and start_col != end_col:
            return False
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] != " ":
                    return False
        else:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] != " ":
                    return False
        return True
    
    if piece.lower() == "p":  # Pawn
        direction = -1 if piece.isupper() else 1  # White moves up (-1), Black moves down (+1)
        if start_col != end_col:
            return False  # No capturing for simplicity
        if start_row + direction == end_row and target == " ":
            return True
        if (start_row == 6 and piece.isupper() and end_row == 4 and target == " " and board[5][start_col] == " ") or \
           (start_row == 1 and piece.islower() and end_row == 3 and target == " " and board[2][start_col] == " "):
            return True
        return False
    
    return False

def make_move(board, start, end):
    start_row, start_col = pos_to_coords(start)
    end_row, end_col = pos_to_coords(end)
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = " "
    return board

def evaluate_board(board):
    score = 0
    piece_values = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9, "k": 100}
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece == " ":
                continue
            value = piece_values.get(piece.lower(), 0)
            if piece.isupper():
                score += value
            else:
                score -= value
    return score

def get_all_moves(board, turn):
    moves = []
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if (turn == "white" and piece.isupper()) or (turn == "black" and piece.islower()):
                for row in range(8):
                    for col in range(8):
                        start = coords_to_pos(i, j)
                        end = coords_to_pos(row, col)
                        if is_valid_move(board, start, end, turn):
                            moves.append((start, end))
    return moves

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate_board(board), None
    
    if maximizing:
        best_score = float("-inf")
        best_move = None
        for start, end in get_all_moves(board, "white"):
            new_board = [row[:] for row in board]
            make_move(new_board, start, end)
            score, _ = minimax(new_board, depth - 1, alpha, beta, False)
            if score > best_score:
                best_score = score
                best_move = (start, end)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = float("inf")
        best_move = None
        for start, end in get_all_moves(board, "black"):
            new_board = [row[:] for row in board]
            make_move(new_board, start, end)
            score, _ = minimax(new_board, depth - 1, alpha, beta, True)
            if score < best_score:
                best_score = score
                best_move = (start, end)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move

def play_game():
    turn = "white"
    while True:
        print_board(board)
        if turn == "white":
            move = input("Your move (e.g., e2 e4): ").strip()
            start, end = move.split()
            if not is_valid_move(board, start, end, turn):
                print("Invalid move! Try again.")
                continue
            make_move(board, start, end)
            turn = "black"
        else:
            print("AI is thinking...")
            _, best_move = minimax(board, 2, float("-inf"), float("inf"), False)
            if best_move:
                start, end = best_move
                print(f"AI moves: {start} {end}")
                make_move(board, start, end)
            else:
                print("AI has no valid moves. You win!")
                break
            turn = "white"

play_game()