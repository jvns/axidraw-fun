from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.addstr(0, 0, 'hi')

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
