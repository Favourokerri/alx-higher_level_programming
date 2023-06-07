#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def create_board(n):
    """Create an `n`x`n` sized chessboard filled with empty spaces."""
    board = [[' '] * n for _ in range(n)]
    return board


def copy_board(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]


def extract_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row_idx in range(len(board)):
        for col_idx in range(len(board)):
            if board[row_idx][col_idx] == "Q":
                solution.append([row_idx, col_idx])
                break
    return solution


def mark_unavail_spots(board, row, col):
    """Mark spots on a chessboard as unavailable.

    All spots where non-attacking queens can no
    longer be placed are marked as 'x'.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    n = len(board)
    # Mark all spots horizontally and vertically as 'x'
    for i in range(n):
        board[row][i] = "x"
        board[i][col] = "x"
    # Mark all spots diagonally as 'x'
    for i in range(n):
        for j in range(n):
            if i - j == row - col or i + j == row + col:
                board[i][j] = "x"


def solve_nqueens(board, row, queens, solu):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solu (list): A list of lists of solutions.
    Returns:
        solu
    """
    n = len(board)

    if queens == n:
        solu.append(extract_solution(board))
        return solu

    for col in range(n):
        if board[row][col] == " ":
            t_board = copy_board(board)
            t_board[row][col] = "Q"
            mark_unavail_spots(t_board, row, col)
            if row + 1 < n:
                solu = solve_nqueens(t_board, row + 1, queens + 1, solu)
            else:
                solu = solve_nqueens(t_board, 0, queens + 1, solu)

    return solu


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    chessboard = create_board(n)
    solution_set = solve_nqueens(chessboard, 0, 0, [])
    for solution in solution_set:
        print(solution)
