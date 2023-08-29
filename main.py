import random


original_board = [
    [r"[1 ]", r"[2 ]", r"[3 ]", r"[4 ]"],
    [r"[5 ]", r"[6 ]", r"[7 ]", r"[8 ]"],
    [r"[9 ]", r"[10]", r"[11]", r"[12]"],
    [r"[13]", r"[14]", r"[15]", "[  ]"],
]


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def randomize_board(original_board):
    for i in original_board:
        random.shuffle(i)
    return original_board
    # _board = []
    # for i in original_board:
    #     for j in i:
    #         _board.append(j)

    # random.shuffle(_board)
    # return list(divide_chunks(_board, len(original_board[0])))


def find_2d_list(el, lst):
    for ind, x in enumerate(lst):
        if el in x:
            return (x.index(el), ind)


def check_win(board, original_board):
    if str(board) == str(original_board):
        return True
    return False


def display_board(board):
    print("\033c\033[3J")
    for i, _ in enumerate(original_board[0]):
        print(f"   {i + 1}", end=" ")
    print()
    for ind, row in enumerate(board):
        print(chr(ind + 97).upper(), end=" ")
        for i in row:
            print(i, end=" ")

        print("\n")


def valid_move(board, x, y):
    space_pos = find_2d_list("[  ]", board)

    move_total = abs(sum(space_pos) - (x + y))
    return move_total == 1


def input_move(board, original_board):
    while True:
        inp = input("Enter a move in the format A1: ")
        if len(inp) < 2:
            print("Invalid input: Must be atleast 2 characters long")
            continue

        if not inp[0].isalpha():
            print("First character must be a position letter")
            continue
        if not inp[1].isdigit():
            print("Second character must be a digit")
            continue
        y = ord(inp[0].lower()) - 97
        x = int(inp[1]) - 1
        if x < 0:
            print("Number must be larger than or equal to 1")
            continue
        if x > len(original_board[0]) - 1:
            print("Number out of range")
            continue

        if y > len(original_board) - 1:
            print("Letter out of range")
            continue

        if not valid_move(board, x, y):
            print("Invalid move space is not empty")
            continue

        return x, y


def game():
    board = randomize_board(original_board)
    while True:
        display_board(board)
        x, y = input_move(board, original_board)
        space_pos = find_2d_list("[  ]", board)

        _1 = board[y][x]
        board[space_pos[1]][space_pos[0]] = _1
        board[y][x] = "[  ]"
        if check_win(board, original_board):
            print("Good job, Puzzle solved!")


if __name__ == "__main__":
    game()
