import curses

stdscr = curses.initscr()
curses.noecho()

quit = False
ball_movement = [0,-1, 100] # x movement, y movement, delay (milliseconds)

while quit == False:
    input_command = check_keys()
    if input_command:
        plot_paddle(input_command)
    check_paddle_collision() # is ball about to hit a paddle?
    collide = check wall_collision() # is ball about to hit a wall?
    if collide == True:
        quit = True
    else:
        move_ball()

def check_keys():
    
def plot_paddle():
    
def check_paddle_collision():

def check_wall_collision():

#pad = curses.newpad(100, 100)
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