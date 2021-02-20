import turtle
import time
import random

# setup screen.

wn = turtle.Screen()
wn.title("pong game by achiya")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# setup paddle's.

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_wid=10, stretch_len=2)
paddle1.color("black")
paddle1.penup()
paddle1.goto(240,0)
paddle1.direction = "stop"

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=10, stretch_len=2)
paddle2.color("black")
paddle2.penup()
paddle2.goto(-240,0)
paddle2.direction = "stop"

# setup ball.

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.color("red")
ball.penup()
a = random.choice([-60,-40,-20,0,20,40,60])
b = random.choice([-60,-40,-20,0,20,40,60])
ball.goto(a,b)
ball.direction1 = random.choice(["up","down"])
ball.direction2 = random.choice(["right","left"])

# setup scoreing system.

score1 = 0
score2 = 0
score_manager = turtle.Turtle()
score_manager.speed(0)
score_manager.shape("circle")
score_manager.color("gold")
score_manager.penup()
score_manager.hideturtle()
score_manager.goto(0, 250)
score_manager.write(f"{score1} | {score2}", align="center", font=("Courier", 30, "normal"))



# functions.

def paddle1_up():
    paddle1.direction = "up"

def paddle1_down():
    paddle1.direction = "down"

def paddle2_up():
    paddle2.direction = "up"

def paddle2_down():
    paddle2.direction = "down"

# ball functions.

# direction1 means y axis.

def ball_up():
    ball.direction1 = "up"

def ball_down():
    ball.direction1 = "down"

# direction2 means x axis.

def ball_left():
    ball.direction2 = "left"

def ball_right():
    ball.direction2 = "right"

# movement function for paddle 1. 

def pad1_move():

    if  paddle1.direction == "up" and paddle1.ycor() != 200:
        y = paddle1.ycor()
        paddle1.sety(y + 20)
        paddle1.direction = "stop"

    if  paddle1.direction == "down" and paddle1.ycor() != -200:
        y = paddle1.ycor()
        paddle1.sety(y - 20)
        paddle1.direction = "stop"

# movement function for paddle 2.

def pad2_move():

    if  paddle2.direction == "up" and paddle2.ycor() != 200:
        y = paddle2.ycor()
        paddle2.sety(y + 20)
        paddle2.direction = "stop"

    if  paddle2.direction == "down" and paddle2.ycor() != -200:
        y = paddle2.ycor()
        paddle2.sety(y - 20)
        paddle2.direction = "stop"

# movement function for the ball.

def ball_move():
    # the ball on the way up.
    if ball.direction1 == "up" and ball.ycor() != 280:
        y = ball.ycor()
        ball.sety(y + 20)
        time.sleep(0.05)
    elif ball.ycor() == 280:
        ball.direction1 = "down"

    # the ball on the way down.
    if ball.direction1 == "down" and ball.ycor() != -280:
        y = ball.ycor()
        ball.sety(y - 20)
        time.sleep(0.05)
    elif ball.ycor() == -280:
        ball.direction1 = "up"

    # the ball on the way right, and hit's border and paddle.
    if ball.direction2 == "right" and ball.xcor() != 280:
        if ball.xcor() == paddle1.xcor() and (ball.ycor() == paddle1.ycor() or ball.ycor() == (paddle1.ycor() + 80) or ball.ycor() == (paddle1.ycor() - 80)or ball.ycor() == (paddle1.ycor() - 60) or ball.ycor() == (paddle1.ycor() - 40) or ball.ycor() == (paddle1.ycor() - 20) or ball.ycor() == (paddle1.ycor() + 20) or ball.ycor() == (paddle1.ycor() + 40) or ball.ycor() == (paddle1.ycor() + 60)):
            ball.direction2 = "left"
        else:
            x = ball.xcor()
            ball.setx(x + 20)
            time.sleep(0.05)
    elif ball.xcor() == 280:
        global score1
        score1 += 10
        a = random.choice([-60,-40,-20,0,20,40,60])
        b = random.choice([-60,-40,-20,0,20,40,60])
        ball.direction1 = random.choice(["up","down"])
        ball.direction2 = random.choice(["right","left"])
        ball.goto(a,b)

    # the ball on the way left, and hit's border and paddle.
    if ball.direction2 == "left" and ball.xcor() != -280:
        if ball.xcor() == paddle2.xcor() and (ball.ycor() == paddle2.ycor() or ball.ycor() == (paddle2.ycor() + 80) or ball.ycor() == (paddle2.ycor() - 80) or ball.ycor() == (paddle2.ycor() - 60) or ball.ycor() == (paddle2.ycor() - 40) or ball.ycor() == (paddle2.ycor() - 20) or ball.ycor() == (paddle2.ycor() + 20) or ball.ycor() == (paddle2.ycor() + 40) or ball.ycor() == (paddle2.ycor() + 60)):
            ball.direction2 = "right"
        else:
            x = ball.xcor()
            ball.setx(x - 20)
            time.sleep(0.05)
    elif ball.xcor() == -280:
        global score2
        score2 += 10
        a = random.choice([-60,-40,-20,0,20,40,60])
        b = random.choice([-60,-40,-20,0,20,40,60])
        ball.direction1 = random.choice(["up","down"])
        ball.direction2 = random.choice(["right","left"])
        ball.goto(a,b)

# listening for key press's.
wn.listen()

# binding key press's.
wn.onkeypress(paddle1_up, "Up")
wn.onkeypress(paddle1_down, "Down")
wn.onkeypress(paddle2_up, "w")
wn.onkeypress(paddle2_down, "s")

# main game loop.
while True:
    wn.update()
    pad1_move()
    pad2_move()
    ball_move()
    score_manager.clear()
    score_manager.write(f"{score1} | {score2}", align="center", font=("Courier", 30, "normal"))
    if score1 == 100 or score2 == 100:
        wn.bye()


wn.mainloop()