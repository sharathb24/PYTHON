# importing the turtle module
import turtle
# importing the time module
import time
# importing the time module
import winsound

# lets setup the window screen for the game
wn = turtle.Screen()
wn.title('Soccer Game Python')
wn.setup(width = 1000, height = 600)
wn.bgcolor('#398c0a')
wn.tracer(0)

# creating basic vars
score_1 = 0
score_2 = 0

border = turtle.Turtle()
border.speed(0)
border.color('white')
border.shape('square')
border.penup()
border.setposition(-460, -260)
border.pendown()
border.pensize(10)
# exexute the loop four times to create border
for side in range(2):
    border.fd(920)
    border.lt(90)
    border.fd(525)
    border.lt(90)
border.hideturtle()

# create an heading for the game so that it looks nice
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.setposition(0, 320)
head.write('PRIEMIER LEAGUE', align = 'center', font = ('consolas', 24, 'normal'))
head.hideturtle()

# creating a scoreboard that displays the score of the two players in the game
sc = turtle.Turtle()
sc.speed(0)
sc.shape('square')
sc.color('white')
sc.penup()
sc.setposition(0, 200)
sc.hideturtle()
sc.write('Player one: 0         Player two: 0', align = 'center', font = ('consolas', 24, 'normal'))

# creating the center line of the ground
center = turtle.Turtle()
center.speed(0)
center.shape('square')
center.color('white')
center.penup()
center.setposition(0, 260)
center.pendown()
center.pensize(10)
center.goto(0, -260)
center.hideturtle()

# now lets create our goal post for the game
goal1 = turtle.Turtle()
goal1.speed(0)
goal1.shape('square')
goal1.color('white')
goal1.penup()
goal1.setposition(-460, 100)
goal1.pendown()
goal1.pensize(10)
# setting the pen thickness so that its nice
goal1.goto(-380, 100)
goal1.goto(-380, -100)
goal1.goto(-460, -100)
goal1.hideturtle()

# now lets create our goal post for the game
goal2 = turtle.Turtle()
goal2.speed(0)
goal2.shape('square')
goal2.color('white')
goal2.penup()
goal2.setposition(460, -100)
goal2.pendown()
# setting the pen thickness so that its nice
goal2.pensize(10)
goal2.goto(380, -100)
goal2.goto(380, 100)
goal2.goto(460, 100)
goal2.hideturtle()

# create the first paddle to smash the ball
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape('square')
pad1.color('white')
pad1.penup()
pad1.setposition(-270, 0)
# extending the length of the paddle
pad1.shapesize(stretch_len = 1, stretch_wid = 5)

# create the first paddle to smash the ball
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape('square')
pad2.color('white')
pad2.penup()
pad2.setposition(270, 0)
# extending the length of the paddle
pad2.shapesize(stretch_len = 1, stretch_wid = 5)

# creating the football which moves around the stadium
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.setposition(0, 0)
ball.penup()
ball.dx = 0.5
ball.dy = -0.5


# creating funcion for moving pad1 up to top
def pad1_up():
    y = pad1.ycor()
    y += 15
    if y > 220:
        y = 220
    pad1.sety(y)

# creating funcion for moving pad1 down below
def pad1_down():
    y = pad1.ycor()
    y -= 15
    if y < -210:
        y = -210
    pad1.sety(y)

# creating funcion for moving pad2 up to top
def pad2_up():
    y = pad2.ycor()
    y += 15
    if y > 220:
        y = 220
    pad2.sety(y)

# creating funcion for moving pad2 down below
def pad2_down():
    y = pad2.ycor()
    y -= 15
    if y < -210:
        y = -210
    pad2.sety(y)


# creating the keyboard binding with window
wn.listen()
# these executes the function based on the keys
wn.onkeypress(pad1_up, 'w')
wn.onkeypress(pad1_down, 's')
wn.onkeypress(pad2_up, 'Up')
wn.onkeypress(pad2_down, 'Down')


# loops until there is a break
while True:

    # keeps updating the screen
    wn.update()

    # make the ball move to a direction
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # creating borders so that the ball doesnt go out

    # creating the top border for the ball
    if ball.ycor() > 250:
        ball.dy *= -1

    # creating the right border for the ball
    if ball.xcor() > 450:
        ball.dx *= -1

    # creating the bottom border for the ball
    if ball.ycor() < -250:
        ball.dy *= -1

    # creating the left border for the ball
    if ball.xcor() < -450:
        ball.dx *= -1

    # making the collisions between the paddle and the ball so that game continues on and on doesnt stop
    if (ball.xcor() > 260 and ball.xcor() < 270) and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() -40):
        ball.setx(260)
        ball.dx *= -1
        # adding sound when the paddle hits the ball
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # making the collisions between the paddle and the ball so that game continues on and on doesnt stop
    if (ball.xcor() < -260 and ball.xcor() > -270) and (ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() -40):
        ball.setx(-260)
        ball.dx *= -1
        # adding sound when the paddle hits the ball
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # if the ball goes inside the goal post then its a goal! hurray and also congratulations
    if (ball.xcor() > 385 and ball.xcor() < 460) and (ball.ycor() > -85 and ball.ycor() < 100):
        time.sleep(1)
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        sc.clear()
        # this writes whenever a player scores a goal and displays the score on the screenboard
        sc.write('Player one: {}         Player two: {}'.format(score_1, score_2), align = 'center', font = ('consolas', 24, 'normal'))
        

    # if the ball goes inside the goal post then its a goal! hurray and also congratulations
    if (ball.xcor() < -385 and ball.xcor() > -460) and (ball.ycor() < 85 and ball.ycor() > -100):
        time.sleep(1)
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        sc.clear()
        # this writes whenever a player scores a goal and displays the score on the screenboard
        sc.write('Player one: {}         Player two: {}'.format(score_1, score_2), align = 'center', font = ('consolas', 24, 'normal'))
        
