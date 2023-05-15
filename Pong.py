import turtle
import pygame

# Creating the Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
# Ball's sound
pygame.mixer.init()
bounce_sound = pygame.mixer.Sound("bounce.wav")

# Screen properties
wn = turtle.Screen()
wn.title("Pong by Gracia")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Left Paddle (Paddle A)
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("deeppink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.dy = 0

# Right Paddle (Paddle B)
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("#0FFF50")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.dy = 0

# Ball
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Game Rules
game_over = False
winner = None
points = {
    "player_A": 0,
    "player_B": 0
}
game_rules = {
    "max_points": 20,
    "ball_speed": 0.15
}

# Score Display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0 Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Function to move paddle_a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Function to move paddle_a down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Function to move paddle_b up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Function to move paddle_b down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Game loop
while not game_over:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for ball collision with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.05  # Increase in horizontal speed
        ball.dy *= 1.05  # Increase in vertical speed
        bounce_sound.play()

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= 1.05  # Increase the horizontal speed
        ball.dy *= 1.05  # Increase the vertical speed
        bounce_sound.play()

    # Check for ball going off screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player_A"] += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player_B"] += 1

    # Check for ball colliding with top or bottom of screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        bounce_sound.play()
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounce_sound.play()

    # Update score display
    score_display.clear()
    score_display.write("Player A: {}  Player B: {}".format(points["player_A"], points["player_B"]),
                        align="center", font=("Arial", 24, "normal"))

    # Check for game over conditions
    if points["player_A"] == game_rules["max_points"]:
        game_over = True
        winner = "Player A"
    elif points["player_B"] == game_rules["max_points"]:
        game_over = True
        winner = "Player B"

# Display game over message
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write("Game Over! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))

turtle.done()
