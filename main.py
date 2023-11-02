import curses
import time
import random


def generate_random_matrix(rows, cols):
    return [[random.choice("RGBY") for _ in range(cols)] for _ in range(rows)]


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    rows, cols = 3, 3
    matrix = generate_random_matrix(rows, cols)

    while True:
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                color_pair = (i + j) % 3 + 1
                stdscr.addstr(i, j * 2, cell, curses.color_pair(color_pair))

        stdscr.refresh()
        time.sleep(1)  # Delay for 1 second

        stdscr.clear()  # Clear the screen

        # Generate a new random matrix
        matrix = generate_random_matrix(rows, cols)


if __name__ == "__main__":
    curses.wrapper(main)
