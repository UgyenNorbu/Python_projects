import curses
from curses import wrapper
import time
import queue

maze = [
    ['-', '-', '-', '-', '-', 'O', '-', '-', '-'], 
    ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'], 
    ['-', ' ', '-', '-', ' ', '-', '-', ' ', '-'], 
    ['-', ' ', '-', ' ', ' ', ' ', '-', ' ', '-'], 
    ['-', ' ', '-', ' ', '-', ' ', ' ', ' ', '-'], 
    ['-', ' ', ' ', ' ', '-', '-', ' ', ' ', '-'], 
    ['-', ' ', '-', ' ', '-', ' ', ' ', '-', '-'], 
    ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'], 
    ['-', '-', '-', '-', '-', '-', '-', 'X', '-'], 
]

def print_maze(maze, stdscr, path = []):
    yellow = curses.color_pair(1)
    blue = curses.color_pair(2)

    for outter_index, row in enumerate(maze):
        for inner_index, val in enumerate(row):
            stdscr.addstr(outter_index, inner_index*2, val, blue) # inner_index * 2 to make it print 2x wider

def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    
    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)