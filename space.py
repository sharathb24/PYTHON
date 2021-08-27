# importing the turtle module
import turtle
# importing the random module
import random
# importing the winsound module
import winsound

# creating the turtle screen or window
wn = turtle.Screen()
wn.title('Space Wars')
wn.bgpic('space.gif')
wn.bgcolor('black')
wn.tracer(0)

# creating variables
score = 0
running = True


# registering the photos used in the space invadres game
turtle.register_shape('shooter.gif')
turtle.register_shape('yellow_bullet.gif')
turtle.register_shape('red_enemy.gif')
turtle.register_shape('green_enemy.gif')
turtle.register_shape('missile.gif')

# creating the heading for the game ie space invadres
head = turtle.Turtle()
head.color('white')
head.penup()
head.setposition(0, 330)
head.write('space wars', align = 'center', font = ('consolas', 32 , 'normal'))
head.hideturtle()

# creating a missile that falls from the top
missile = turtle.Turtle()
missile.shape('missile.gif')
missile.speed(0)
missile.penup()
x = random.randint(-280, 280)
missile.setposition(x, 280)

# speed of the missile that falls from the top
missilespeed = 0.3

# creating the border where the game still goes on
border = turtle.Turtle()
border.color('white')
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(5)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# creating the scoreboard to display the score of the player
sc = turtle.Turtle()
sc.color('white')
sc.penup()
sc.setposition(-240, 260)
sc.write('score: 0', align = 'center', font = ('consolas'))
sc.hideturtle()

# creating the player to shoot the enemy and the missile
player = turtle.Turtle()
player.color('blue')
player.shape('shooter.gif')
player.penup()
player.setposition(0, -250)
player.setheading(90)

# setting the speed of the player to move in all directions
playerspeed = 10

# creating the first enemy to dodge from the player and kill
enemy = turtle.Turtle()
enemy.shape('red_enemy.gif')
enemy.penup()
x = random.randint(-270, 270)
y = random.randint(100, 270)
enemy.setposition(x, y)

# setting the speed of the enemy to move in all directions
enemyspeed = 0.4

# creating the second enemy to dodge from the player and kill
enemy2 = turtle.Turtle()
enemy2.shape('green_enemy.gif')
enemy2.penup()
x = random.randint(-270, 270)
y = random.randint(100, 270)
enemy2.setposition(x, y)

# setting the speed of the enemy to move in all directions
enemyspeed2 = 0.4

# creating the player's weapon ie bullet to shoot the enemy
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('yellow_bullet.gif')
bullet.penup()
bullet.setheading(90)
bullet.goto(-100, -100)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# creating vars for the speed of bullet and its state
bulletspeed = 1
bulletstate = 'ready'

# creating the basic functions that is to make the player move
# to make the bullet shoot from the player and other things s

# making the player to move upwards
def player_up():
    y = player.ycor()
    if y > 250:
        y = 250
    y += playerspeed
    player.sety(y)

# making the player to move downward 
def player_down():
    y = player.ycor()
    if y < -250:
        y = -250
    y -= playerspeed
    player.sety(y)

# making the player to move leftwardds 
def player_left():
    y = player.xcor()
    if y < -250:
        y = -250
    y -= playerspeed
    player.setx(y)

# making the player to move rightwards 
def player_right():
    y = player.xcor()
    if y > 250:
        y = 250
    y += playerspeed
    player.setx(y)

# function to fire the bullet from the player
def fire_bullet():

    # accesing the global variables ie outside the function
    global bulletstate, score, remain

    if bulletstate == 'ready':
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        # adding sound when the player shoots a bullet
        winsound.PlaySound('shot.wav', winsound.SND_ASYNC)
        bulletstate = 'fire'

# checking collision between bullet and enemy
def collision(t1, t2):
    if bullet.distance(enemy) < 15:
        return True
    else:
        return False

# checking collision between player and first enemy
def collide(t1, t2):
    if player.distance(enemy) < 25:
        return True
    else:
        return False

# checking collision between bullet and enemy
def collision2(t1, t2):
    if bullet.distance(enemy2) < 15:
        return True
    else:
        return False

# checking collision between player and second enemy
def collide2(t1, t2):
    if player.distance(enemy2) < 25:
        return True
    else:
        return False

# checking collision between player and missile
def collision3(t1, t2):
    if player.distance(missile) < 15:
        return True
    else:
        return False

# checking collision between bullet and missile
def collide3(t1, t2):
    if bullet.distance(missile) < 15:
        return True
    else:
        return False

# function to quit the game and move out of teh game
def quit():
    global running
    running = False
    print('\n\n\nGame ended')
    print('Score: ', score)
    print('\n\n')

# this listens to all the events in the game
wn.listen()
# executes the functions based on the keys pressed
wn.onkeypress(player_up, 'Up')
wn.onkeypress(player_down, 'Down')
wn.onkeypress(player_left, 'Left')
wn.onkeypress(player_right, 'Right')
wn.onkeypress(fire_bullet, 'space')
wn.onkeypress(quit, 'q')


# until running is true keep on looping
while running:
    
    # keeps updating the screen
    wn.update()

    # makes the bullet move up
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    # makes the enemy to move sideways
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # makes the enemy to move sideways
    x = enemy2.xcor()
    x += enemyspeed2
    enemy2.setx(x)

    # tell to fire the bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'

    # keep the enemy inside the border in the game
    if enemy.xcor() > 270 or enemy.xcor() < -270:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    
    # keep the enemy inside the border in the game
    if enemy2.xcor() > 270 or enemy2.xcor() < -270:
        y = enemy2.ycor()
        y -= 40
        enemyspeed2 *= -1
        enemy2.sety(y)

    # check colliskion between the bullet and the enemy
    if collision(bullet, enemy):
        enemy.hideturtle()
        bullet.hideturtle()
        x = random.randint(-270, 270)
        y = random.randint(-100, 270)
        enemy.setposition(x, y)
        enemy.showturtle()
        score += 10
        sc.clear()
        # clears the scores and then displays it again on the screen
        sc.write(' score: {}'.format(score), align = 'center', font = ('consolas'))

    # check colliskion between the bullet and the enemy2
    if collision2(bullet, enemy2):
        enemy2.hideturtle()
        bullet.hideturtle()
        x = random.randint(-270, 270)
        y = random.randint(-100, 270)
        enemy2.setposition(x, y)
        enemy2.showturtle()
        score += 10
        sc.clear()
        # clears the scores and then displays it again on the screen
        sc.write(' score: {}'.format(score), align = 'center', font = ('consolas'))

    # check colliskion between the player and the enemy
    if collide(player, enemy):
        print('Game over!')
        print('score :', score)
        break

    # check colliskion between the player and the enemy2
    if collide2(player, enemy2):
        print('\n\n\nGame over!')
        print('score :', score)
        print('\n\n')
        break

    # makes the missile fall from the top
    y = missile.ycor()
    y -= missilespeed
    missile.sety(y)

    # check colliskion between the player and the missile
    if collision3(player, missile):
        print('\n\n\nGame over!')
        print('score: ', score)
        print('\n\n')
        break

    # check colliskion between the bullet and the missile
    if collide3(missile, bullet):
        missile.hideturtle()
        missile.goto(0, 0)

# hope u like the space invadres game which is built in pythons
# and play it and enjoy it with your family and have a good day