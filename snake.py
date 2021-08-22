# importing the turtle module
import turtle
# importing the time module
import time
# importing the random module
import random


# first create the turtle screen for the game
wn = turtle.Screen()
wn.title('Snake Game Python')
wn.setup(width = 650, height = 650)
wn.bgcolor('black')
wn.tracer(0)

# create a basic var
delay = 0.1

score = 0
high_score = 0

# create a border so that the game looks nice!
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.shape('square')
border.penup()
# the turtle goes to the bottom left position
border.goto(-260, -260)
border.hideturtle()
border.pendown()
border.pensize(5)
# draws the border that is four lines
for side in range(4):
    border.fd(520)
    border.lt(90)

# create the head of the snake for the game
head = turtle.Turtle()
head.speed(0)
head.color('white')
head.shape('square')
head.penup()
head.setposition(0, 0)
head.direction = 'stop'

# create the food for snake in the game
food = turtle.Turtle()
food.speed(0)
food.color('red')
food.shape('circle')
food.penup()
food.setposition(0, 100)

sc = turtle.Turtle()
sc.speed(0)
sc.color('white')
sc.shape('square')
sc.penup()
sc.goto(0, 275)
sc.hideturtle()
sc.write('Score: 0    High score: 0', align = 'center', font = ('consolas', 24, 'normal'))


# the function that makes the snake to move
def move():

    # if the direction is up the move up
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    # if the direction is down the move down
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    # if the direction is left the move left
    if head.direction == 'left':
        y = head.xcor()
        head.setx(y - 20)

    # if the direction is right the move right
    if head.direction == 'right':
        y = head.xcor()
        head.setx(y + 20)


# changes the head direction to up
def move_up():
    head.direction = 'up'

# changes the head direction to up
def move_down():
    head.direction = 'down'

# changes the head direction to up
def move_left():
    head.direction = 'left'

# changes the head direction to up
def move_right():
    head.direction = 'right'


# create the keyboard bindings
wn.listen()
# changes the key based on click
wn.onkey(move_up, 'Up')
wn.onkey(move_down, 'Down')
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')


# the things in the loop runs every time
while True:
    # keeps updating the screen
    wn.update()

    # calls the move function
    move()

    # create collision between the snake and the borders
    if (head.xcor() > 250 or head.xcor() < -250) or (head.ycor() > 250 or head.ycor() < -250):
        time.sleep(1)
        head.goto(0, 0)
        # change direction to stop
        head.direction = 'stop'

        sc.clear()
        score = 0
        # changes the scoreboard every time the snake gets collided with the border
        sc.write('Score: {}    High score: {}'.format(score, high_score), align = 'center', font = ('consolas', 24, 'normal'))
        delay = 0.1

        
    # making the snake to eat the food to increase score
    if head.distance(food) < 15:
        # randomly posisitioning the food
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        food.setposition(x, y)

        # increase the score every the snake eats the food in the game
        score += 10
        # if the score is greater than high then make it the high score
        if score > high_score:
            high_score = score
        sc.clear()
        # changes the scoreboard every time the snake eats the food in the game
        sc.write('Score: {}    High score: {}'.format(score, high_score), align = 'center', font = ('consolas', 24, 'normal'))
        delay += 0.001

    # stop for 0.1s after every move
    time.sleep(delay)
