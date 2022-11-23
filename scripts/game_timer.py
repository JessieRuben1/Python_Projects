import turtle 
import time


wn = turtle.Screen()
wn.title("Game Timer Demo")
wn.bgcolor("yellow")

bob = turtle.Turtle()
bob.speed(0)
bob.color("blue")
bob.shape("triangle")
bob.penup()

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
        
wn.listen()
wn.onkeypress(toggle_pause, "p")

time_limit = 15
start_time = time.time()

# This is the main game loop. It is an infinite loop that will run until the game is over. The `if not
# is_paused` part is a conditional statement that will only run the code inside the `if` block if the
# game is not paused.
while True:
    if not is_paused:
        bob.fd(1)
        bob.lt(1)
        
        # Timer
        elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            print("GAME OVER")
            exit()
    else:
        start_time = time.time() - elapsed_time
        wn.update()