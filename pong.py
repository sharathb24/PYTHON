# importing the turtle module
import turtle
# importing the turtle module
import time

# creating the screen of the pong
wn = turtle.Screen()
wn.setup(width = 800, height = 600)
wn.title('PONG GAME PYTHON')
wn.bgcolor('black')
wn.tracer(0)


# creating vars for scoreboard
score_a = 0
score_b = 0


# creating the first paddle of the game
pad1 = turtle.Turtle()
pad1.shape('square')
pad1.color('white')
pad1.shapesize(stretch_len = 1, stretch_wid = 5)
pad1.penup()
pad1.goto(-350, 0)


# creating the second paddle of the game
pad2 = turtle.Turtle()
pad2.shape('square')
pad2.color('white')
pad2.shapesize(stretch_len = 1, stretch_wid = 5)
pad2.penup()
pad2.goto(350, 0)



# creating the main ball of the game
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.goto(0, 0)
ball.penup()
ball.dx = 0.2
ball.dy = -0.2


# creating pen to write score
pen = turtle.Turtle()
pen.shape('square')
pen.color('white')
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write('Player A: 0   Player B: 0', align = 'center', font = ('Courier', 24))



# making the paddle to move

def pad1_up():
    y = pad1.ycor()
    y += 20
    pad1.sety(y)

def pad1_down():
    y = pad1.ycor()
    y -= 20
    pad1.sety(y)

def pad2_up():
    y = pad2.ycor()
    y += 20
    pad2.sety(y)

def pad2_down():
    y = pad2.ycor()
    y -= 20
    pad2.sety(y)


# the window listens to the functions
wn.listen()
wn.onkeypress(pad1_up, 'w')
wn.onkeypress(pad1_down, 's')
wn.onkeypress(pad2_up, 'Up')
wn.onkeypress(pad2_down, 'Down')


while True:
    wn.update()



    # making the ball to move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



    # creating border for the top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # creating border for bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # creating border for left
    if ball.xcor() > 390:
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        # showing the score of the players on the top of the screen
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24))
    
    # creating border for right
    if ball.xcor() < -390:
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        # showing the score of the players on the top of the screen
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24))



    # colliding the ball with paddles in the pong game
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() - 40):
        ball.dx *= -1
    # colliding the ball with paddles in the pong game  
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() - 40):
        ball.dx *= -1