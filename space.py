# importing the turtle module
import turtle
# importing the random module
import random
# importing the winsound module
import winsound


# now lets create the window or screen for the game
wn = turtle.Screen()
wn.title('SPACE WARS')
wn.bgpic('background.gif')
wn.bgcolor('black')
wn.tracer(0)

# registering the shapes for using them in the game
turtle.register_shape('shooter.gif')
turtle.register_shape('bullet.gif')
turtle.register_shape('red_enemy.gif')
turtle.register_shape('green_enemy.gif')
turtle.register_shape('missile.gif')

# declaring basic vars to use it in the game all around
player_speed = 10
bullet_speed = 1.5
enemy_speed1 = 0.5
enemy_speed2 = 0.5
enemy_speed3 = 0.5
enemy_speed4 = 0.5
missile_speed = 0.5

running = True
bulletstate = 'ready'

score = 0
remain = 0

# create a border so that everything goes in the game
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(5)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# create the heading of the game ie writing space wars as the heading
head = turtle.Turtle()
head.color('white')
head.penup()
head.setposition(0, 330)
head.write('space invaders', align = 'center', font = ('consolas', 28, 'normal'))
head.hideturtle()

# creating a player to shoot the enemies and missiles
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape('shooter.gif')
player.setposition(0, -240)

# create a bullet to shoot the enemies and missiles to save the plaeyr
bullet = turtle.Turtle()
bullet.speed(0)
bullet.penup()
bullet.shape('bullet.gif')
bullet.hideturtle()

# creating the first enemy who targets the player
enemy1 = turtle.Turtle()
enemy1.shape('red_enemy.gif')
enemy1.speed(0)
enemy1.penup()
x = random.randint(-250, 250)
y = random.randint(100, 250)
enemy1.setposition(x, y)

# creating the second enemy who targets the player
enemy2 = turtle.Turtle()
enemy2.shape('green_enemy.gif')
enemy2.speed(0)
enemy2.penup()
x = random.randint(-250, 250)
y = random.randint(100, 250)
enemy2.setposition(x, y)

# creating the second enemy who targets the player
enemy3 = turtle.Turtle()
enemy3.shape('green_enemy.gif')
enemy3.speed(0)
enemy3.penup()
x = random.randint(-250, 250)
y = random.randint(100, 250)
enemy3.setposition(x, y)


# creating the second enemy who targets the player
enemy4 = turtle.Turtle()
enemy4.shape('red_enemy.gif')
enemy4.speed(0)
enemy4.penup()
x = random.randint(-250, 250)
y = random.randint(100, 250)
enemy4.setposition(x, y)

# creating the score-board that displays the score of the player
sc = turtle.Turtle()
sc.color('white')
sc.penup()
sc.setposition(-280, 260)
sc.hideturtle()
sc.write('score: 0', align = 'left', font = ('consolas'))


# here lets create basic functions like moving the player up or
# firing the bullet from the player, checking for collision etc

# making sure that the player doesnt go out of the border
def player_up():
    y = player.ycor()
    y += player_speed
    if y > 250:
        y = 250
    player.sety(y)

# making sure that the player doesnt go out of the border
def player_down():
    y = player.ycor()
    y -= player_speed
    if y < -250:
        y = -250
    player.sety(y)

# making sure that the player doesnt go out of the border
def player_left():
    y = player.xcor()
    y -= player_speed
    if y < -250:
        y = -250
    player.setx(y)

# making sure that the player doesnt go out of the border
def player_right():
    y = player.xcor()
    y += player_speed
    if y > 250:
        y = 250
    player.setx(y)

# creating a function to fire the bullet and hit the enemy
def fire_bullet():
    global bulletstate
    if bulletstate == 'ready':
        x = player.xcor()
        y = player.ycor() + 25
        bullet.setposition(x, y)
        bullet.showturtle()
        winsound.PlaySound('shot.wav', winsound.SND_ASYNC)
        bulletstate = 'fire'

# check collision between the red enemy and the bullet
def collision1(t1, t2):
    if enemy1.distance(bullet) < 20:
        return True
    else: return False

# check collision between the green enemy and the bullet
def collision2(t1, t2):
    if enemy2.distance(bullet) < 20:
        return True
    else: return False

#check collision between the green enemy and the bullet
def collision3(t1, t2):
    if enemy3.distance(bullet) < 20:
        return True
    else: return False

#check collision between the green enemy and the bullet
def collision4(t1, t2):
    if enemy4.distance(bullet) < 20:
        return True
    else: return False

# check collision between the red enemy and the player
def collide1(t1, t2):
    if enemy1.distance(player) < 20:
        return True
    else: return False

# check collision between the green enemy and the player
def collide2(t1, t2):
    if enemy2.distance(player) < 20:
        return True
    else: return False

# check collision between the third enemy and the player
def collide3(t1, t2):
    if enemy3.distance(player) < 20:
        return True
    else: return False

# check collision between the fourth enemy and the player
def collide4(t1, t2):
    if enemy4.distance(player) < 20:
        return True
    else: return False

# the function thqat show the ending statement ie game over when the plyer loses the game
def game_over():
    end = turtle.Turtle()
    end.color('white')
    end.speed(0)
    end.penup()
    end.setposition(0, 0)
    end.write('GAME OVER!', align = 'center', font = ('consolas', 30))
    end.hideturtle()

# creating a function to quit the game and do something other
def quit():
    global running
    running = False

# listens to all the events that occur in the game
wn.listen()
# executes the function based on the key pressed
wn.onkeypress(player_up, 'Up')
wn.onkeypress(player_down, 'Down')
wn.onkeypress(player_left, 'Left')
wn.onkeypress(player_right, 'Right')
wn.onkeypress(fire_bullet, 'space')
wn.onkeypress(quit, 'q')

# keeps on looping until its running is false
while running:

    # keeps on updating the screen every time the program runs
    wn.update()

    y = bullet.ycor()
    y += bullet_speed
    bullet.sety(y)

    # telling the player that the shooter is ready to fire
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'

    # making the enemy move up and down in the game and the border
    x = enemy1.xcor()
    x += enemy_speed1
    y = enemy1.ycor()
    y -= 40
    # making sure that the enemy sets down when it hits the side borders
    if x > 270:
        enemy_speed1 *= -1
        enemy1.sety(y)
    if x < -270:
        enemy_speed1 *= -1
        enemy1.sety(y)
    enemy1.setx(x)

    # making the enemy move up and down in the game and the border
    x = enemy2.xcor()
    x += enemy_speed2
    y = enemy2.ycor()
    y -= 40
    # making sure that the enemy sets down when it hits the side borders
    if x > 270:
        enemy_speed2 *= -1
        enemy2.sety(y)
    if x < -270:
        enemy_speed2 *= -1
        enemy2.sety(y)
    enemy2.setx(x)

    # making the enemy move up and down in the game and the border
    x = enemy3.xcor()
    x += enemy_speed3
    y = enemy3.ycor()
    y -= 40
    # making sure that the enemy sets down when it hits the side borders
    if x > 270:
        enemy_speed3 *= -1
        enemy3.sety(y)
    if x < -270:
        enemy_speed3 *= -1
        enemy3.sety(y)
    enemy3.setx(x)

    # making the enemy move up and down in the game and the border
    x = enemy4.xcor()
    x += enemy_speed4
    y = enemy4.ycor()
    y -= 40
    # making sure that the enemy sets down when it hits the side borders
    if x > 270:
        enemy_speed4 *= -1
        enemy4.sety(y)
    if x < -270:
        enemy_speed4 *= -1
        enemy4.sety(y)
    enemy4.setx(x)

    # if the bullet and the red enemy collide each other then
    if collision1(bullet, enemy1):
        bulletstate = 'ready'
        x = random.randint(-250, 250)
        y = random.randint(100, 250)
        enemy1.setposition(x, y)
        score += 10
        sc.clear()
        sc.write('score: {}'.format(score), align = 'left', font = ('consolas'))

    # if the bullet and the green enemy collide each other then
    if collision2(bullet, enemy2):
        bulletstate = 'ready'  
        x = random.randint(-250, 250)
        y = random.randint(100, 250)
        enemy2.setposition(x, y)
        score += 10
        sc.clear()
        sc.write('score: {}'.format(score), align = 'left', font = ('consolas'))

    # if the bullet and the third enemy collide each other then
    if collision3(bullet, enemy3):
        bulletstate = 'ready'  
        x = random.randint(-250, 250)
        y = random.randint(100, 250)
        enemy3.setposition(x, y)
        score += 10
        sc.clear()
        sc.write('score: {}'.format(score), align = 'left', font = ('consolas'))
        
    # if the bullet and the third enemy collide each other then
    if collision4(bullet, enemy4):
        bulletstate = 'ready'  
        x = random.randint(-250, 250)
        y = random.randint(100, 250)
        enemy4.setposition(x, y)
        score += 10
        sc.clear()
        sc.write('score: {}'.format(score), align = 'left', font = ('consolas'))

    # giving the ending statement when the player loses the game
    if collide1(player,enemy1):
        player.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        enemy4.hideturtle()
        border.hideturtle()
        game_over()

    # giving the ending statement when the player loses the game
    if collide2(player,enemy2):
        player.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        enemy4.hideturtle()
        border.hideturtle()
        game_over()

    # giving the ending statement when the player loses the game
    if collide3(player,enemy3):
        player.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        enemy4.hideturtle()
        border.hideturtle()
        game_over()

    # giving the ending statement when the player loses the game
    if collide4(player,enemy4):
        player.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        enemy4.hideturtle()
        border.hideturtle()
        game_over()

    
# Rules of the game are mentioned belown:
# 1 . The player can shoot the enemy by pressing the space
# 2 . Every time the player shoots the bullet on the enemy
#     the score of the player increases by 10 points
# 3 . If the player comes in contact with the enemy and 
#     touches the enemy then the player loses the game here
# 4 . The player must escape from the enemy and shoot it

# This project is coded by Sharath Bhat. All rights reserved.
# @ Copyright issues are going to be very severe because I can
# take the project from you and can report tp github against u