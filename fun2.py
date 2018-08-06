import turtle
turtle.goto(0,0)

UP = 0
DOWN=1
LEFT=2
RIGHT=3
direction = None

def up():
    global direction
    direction=UP
    print("You pressed the up key.")
    on_move()
    
def down():
    global direction
    direction=DOWN
    print("You pressed the down key.")
    on_move()
    
def left():
    global direction
    direction=LEFT
    print("You pressed the left key.")
    on_move()
    
def right():
    global direction
    direction=RIGHT
    print("You pressed the right key.")
    on_move()
    
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right") 
turtle.listen()

def on_move():
    x,y=turtle.pos()
    if direction == UP:
        turtle.goto(x, y+10)
    elif direction==DOWN:
        turtle.goto(x,y-10)
    elif direction==LEFT:
        turtle.goto(x-10,y)
    elif direction==RIGHT:
        turtle.goto(x+10,y)
    
    
   
