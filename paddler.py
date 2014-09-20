import curses

stdscr = curses.initscr()
curses.noecho()

pad = curses.newpad(100, 100)
#  These loops fill the pad with letters; this is
# explained in the next section
for y in range(0, 100):
    for x in range(0, 100):
        pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

#  Displays a section of the pad in the middle of the screen
pad.refresh(0,0, 5,5, 20,75)

pause()