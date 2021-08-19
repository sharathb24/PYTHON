# importing the turtle module
import turtle
# importing the time module
import time
# importing the winsound module
import winsound


# creating the screen for the game
wn = turtle.Screen()
wn.setup(width = 1000, height = 600)
wn.title('FIFA EURO WORLD CUP')
wn.bgcolor('#5a830d')
wn.tracer(0)


# creating vars for the score
score_a = 0
score_b = 0


# this creates the border for the field
border = turtle.Turtle()
border.color('white')
border.hideturtle()
border.shape('square')
border.penup()
border.goto(470, 280)
border.pensize(15)
border.pendown()
border.goto(470, -280) # right border
border.goto(-470, -280) # bottom border
border.goto(-470, 280) # left border
border.goto(470, 280) # top border


# this creates the right goal post
goal2 = turtle.Turtle()
goal2.penup()
goal2.color('white')
goal2.hideturtle()
goal2.goto(0, 0)
goal2.penup()

# the front side of goal post
goal2.goto(380, -100)
goal2.pensize(15)
goal2.pendown()
goal2.goto(380, 100)
# top side goal post in the game
goal2.goto(465, 100)
goal2.penup()
goal2.goto(380, -100)
goal2.pendown()
# bottom side goal post in the game
goal2.goto(465, -100)


# this creates the left goal post in the game
goal1 = turtle.Turtle()
goal1.penup()
goal1.color('white')
goal1.hideturtle()
goal1.goto(0, 0)
goal1.penup()

# goal side goal already done
goal1.goto(-380, 100)
goal1.pensize(15)
goal1.pendown()
goal1.goto(-380, -100)
goal1.goto(-465, -100)
goal1.penup()
# top side goal post in the game
goal1.goto(-380, 100)
goal1.pendown()
# bottom side goal post in the game
goal1.goto(-465, 100)


# this creates the center line for game start
center = turtle.Turtle()
center.color('white')
center.penup()
center.hideturtle()
center.goto(0, 275)
center.pendown()
center.pensize(5)
center.right(90)
center.goto(0, -270)


# this creates the center circle of the game
circ = turtle.Turtle()
circ.color('white')
circ.penup()
circ.goto(0, -37)
circ.pendown()
circ.pensize(10)
# this drwas the circle the main thing
circ.circle(40)


# this shows the score when nobody has scored yet
pen = turtle.Turtle()
pen.color('white')
pen.shape('square')
pen.hideturtle()
pen.penup()
pen.goto(0, 220)
pen.write('Player A: 0     Player B: 0', align = 'center', font = ('Courier', 24, 'normal'))


# this creates the first paddle of the game
pad1 = turtle.Turtle()
pad1.shape('square')
pad1.color('white')
pad1.shapesize(stretch_len = 1, stretch_wid = 5)
pad1.penup()
pad1.goto(-300, 0)


# this creates the second paddle of the game
pad2 = turtle.Turtle()
pad2.shape('square')
pad2.color('white')
pad2.shapesize(stretch_len = 1, stretch_wid = 5)
pad2.penup()
pad2.goto(300, 0)


# this creates the football ie is main here for sos
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.turtlesize(1.1)
ball.goto(0, 0)
ball.penup()
ball.dx = 0.6
ball.dy = -0.6



# these are the main functions that makes the paddle to move

# this makes the pad1 to move up
def pad1_up():

    y = pad1.ycor()
    y += 20
    pad1.sety(y)

# this makes the pad1 to move down
def pad1_down():

    y = pad1.ycor()
    y -= 20
    pad1.sety(y)

# this makes the pad2 to move up
def pad2_up():

    y = pad2.ycor()
    y += 20
    pad2.sety(y)

# this makes the pad to move down
def pad2_down():

    y = pad2.ycor()
    y -= 20
    pad2.sety(y)

# this listens to the events that occurs
wn.listen()
# these executes the function when the paricular key is pressed
wn.onkeypress(pad1_up, 'w')
wn.onkeypress(pad1_down, 's')
wn.onkeypress(pad2_up, 'Up')
wn.onkeypress(pad2_down, 'Down')


# while this true keep on looping until its false
while True:

    # keeps on updating the window every time
    wn.update()

        
    # this makes the ball to move back or front
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # this creates the right border
    if ball.ycor() > 265:
        ball.sety(265)
        ball.dy *= -1
    # this creates the right border
    if ball.ycor() < -265:
        ball.sety(-265)
        ball.dy *= -1

    # this creates the right border
    if ball.xcor() > 470:
        ball.setx(470)
        ball.dx *= -1

    # this creates the right border
    if ball.xcor() < -470:
        ball.setx(-470)
        ball.dx *= -1


    # this makes the paddle 1 to collide with ball when the user wants, its his choice lol !
    if (ball.xcor() > 290 and ball.xcor() < 300) and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() - 40):
        ball.dx *= -1
        winsound.PlaySound('bounce.wav' ,winsound.SND_ASYNC)

    # this makes the paddle 2 to collide with ball when the user wants, its his choice lol !
    if (ball.xcor() < -290 and ball.xcor() > -300) and (ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() - 40):
        ball.dx *= -1
        winsound.PlaySound('bounce.wav' ,winsound.SND_ASYNC)


    # when the ball goes into the goal post it must do the things that is mentioned below
    if (ball.xcor() > 400 and ball.xcor() < 470) and (ball.ycor() > -80 and ball.ycor() < 80):
        # do nothing for one second
        time.sleep(1)
        ball.goto(0, 0)
        ball.dx *= -1
        # increments the score by one
        score_a += 1
        pen.clear()
        # displays the score when a goal is scored by the team b
        pen.write('Player A: {}     Player B: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24, 'normal'))

    # when the ball goes into the goal post it must do the things that is mentioned below
    if (ball.xcor() < -400 and ball.xcor() > -470) and (ball.ycor() < 80 and ball.ycor() > -80):
        time.sleep(1)
        ball.goto(0, 0)
        ball.dx *= -1
        # increments the score by one
        score_b += 1
        pen.clear()
        # displays the score when a goal is scored by the team b
        pen.write('Player A: {}     Player B: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24, 'normal'))