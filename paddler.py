from time import sleep
import curses

def check_keys():
    pass
    
def plot_paddle():
    pass
    
def check_paddle_collision():
    pass

def check_wall_collision():
    pass

def move_ball():
    #stdscr.addstr(ball_location[1],ball_location[0], ' ') # erase ball
    ball_location[0] = ball_location[0] + ball_movement[0]
    ball_location[1] = ball_location[1] + ball_movement[1]
    stdscr.addstr(ball_location[1],ball_location[0], "o") # plot ball
    sleep(ball_movement[2])

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
quit = False
ball_movement = [0,-1, 1] # x movement, y movement, delay (seconds)
ball_location = [40,12]

while quit == False:
    
    input_command = None
    collide = None
    
    input_command = check_keys()
    if input_command:
        plot_paddle(input_command)
    check_paddle_collision() # is ball about to hit a paddle?
    collide = check_wall_collision() # is ball about to hit a wall?
    if collide:
        quit = True
    else:
        move_ball()
    stdscr.refresh()

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

#
#  These loops fill the pad with letters; this is
# explained in the next section
#for y in range(0, 100):
#    for x in range(0, 100):
#        try:
#            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
#        except curses.error:
#            pass

#  Displays a section of the pad in the middle of the screen
#pad.refresh(0,0, 5,5, 20,75)

raw_input()