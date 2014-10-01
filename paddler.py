from time import sleep
import curses
import os
import ConfigParser

def plot_border():
    for a in [0,79]:
        for b in range(0,22):
            stdscr.addstr(b,a,"*", curses.color_pair(1))
    for a in [0,22]:
        for b in range(0,80):
            stdscr.addstr(a,b,"*", curses.color_pair(1))
    #stdscr.addstr(22,78,"*", curses.color_pair(1))

def check_keys():
    charin = stdscr.getch()
    if charin == ord('\\'):
        return "\\"
    if charin == ord('/'):
        return "/"
    return None
    
def plot_paddle(input_key):
    stdscr.addstr(ball_location[1],ball_location[0],input_key)
    scorechange = (1/ball_movement[2])
    ball_movement[2] = ball_movement[2]-0.004
    return scorechange
    
def check_paddle_collision():
    in_key = stdscr.inch(ball_location[1],ball_location[0])
    
    if in_key == ord("/") and ball_movement[0] == 1 and ball_movement[1] == 0:
        ball_movement[0] = 0
        ball_movement[1] = -1
        move_ball()
    
    elif in_key == ord("/") and ball_movement[0] == -1 and ball_movement[1] == 0:
        ball_movement[0] = 0
        ball_movement[1] = 1
        move_ball()
    
    elif in_key == ord("/") and ball_movement[0] == 0 and ball_movement[1] == 1:
        ball_movement[0] = -1
        ball_movement[1] = 0
        move_ball()
    
    elif in_key == ord("/") and ball_movement[0] == 0 and ball_movement[1] == -1:
        ball_movement[0] = 1
        ball_movement[1] = 0
        move_ball()
    
    elif in_key == ord("\\") and ball_movement[0] == 1 and ball_movement[1] == 0:
        ball_movement[0] = 0
        ball_movement[1] = 1
        move_ball()
    
    elif in_key == ord("\\") and ball_movement[0] == -1 and ball_movement[1] == 0:
        ball_movement[0] = 0
        ball_movement[1] = -1
        move_ball()
    
    elif in_key == ord("\\") and ball_movement[0] == 0 and ball_movement[1] == 1:
        ball_movement[0] = 1
        ball_movement[1] = 0
        move_ball()
    
    elif in_key == ord("\\") and ball_movement[0] == 0 and ball_movement[1] == -1:
        ball_movement[0] = -1
        ball_movement[1] = 0
        move_ball()
        
    return

def check_wall_collision():
    if ball_location[0] <= 0 or ball_location[0] >= 79 or ball_location[1] >= 22 or ball_location[1] <= 0:
        return True
    else:
        return None

def move_ball():
    ball_location[0] = ball_location[0] + ball_movement[0]
    ball_location[1] = ball_location[1] + ball_movement[1]

def plot_ball():
    stdscr.addstr(ball_location[1],ball_location[0], "o") # plot ball

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
quit = False
ball_movement = [-1,0, 0.1] # x movement, y movement, delay (seconds)
ball_location = [40,12]
stdscr.nodelay(1)
collide = None
score = 0
curses.start_color()
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
plot_border()
stdscr.addstr(23,35,"SCORE: " + str(int(score)), curses.color_pair(2))

while not(collide):
    
    plot_ball()
    stdscr.refresh()
    sleep(ball_movement[2])
    
    stdscr.addstr(ball_location[1],ball_location[0], ' ') # erase ball
    move_ball()
    
    input_command = None
    collide = None
    input_command = check_keys()

    if input_command:
        scorediff = plot_paddle(input_command)
        score = score + scorediff
        stdscr.addstr(23,35,"SCORE: " + str(int(score)), curses.color_pair(2))
     
    check_paddle_collision() # is ball about to hit a paddle?
    collide = check_wall_collision() # is ball about to hit a wall?
    
curses.nocbreak()
stdscr.keypad(0)
curses.endwin()
os.system('clear')
print "You hit the side!"
print ""
print "Final score: " + str(int(score))