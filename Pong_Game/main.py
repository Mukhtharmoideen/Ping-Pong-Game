# import Screen and Turtle from turtle module
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()
screen.listen()

# Keyboard bindings for left paddle
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')

# Keyboard bindings for right paddle
screen.onkeypress(right_paddle.go_up, 'Up')
screen.onkeypress(right_paddle.go_down, 'Down')
game_is_on = True
finalScore = 5
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when r_paddles misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    # Detect when l_paddles misses

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        # Check for winner
        if score.l_score == finalScore:
            winner_text = turtle.Turtle()
            winner_text.color("white")
            winner_text.penup()
            winner_text.hideturtle()
            winner_text.goto(0, 0)
            winner_text.write("Left opponent wins!", align="center", font=("Courier", 24, "normal"))
            game_is_on = False

        elif score.r_score == finalScore:
            winner_text = turtle.Turtle()
            winner_text.color("white")
            winner_text.penup()
            winner_text.hideturtle()
            winner_text.goto(0, 0)
            winner_text.write("Right opponent wins!", align="center", font=("Courier", 24, "normal"))
            game_is_on = False
screen.mainloop()
screen.exitonclick()
