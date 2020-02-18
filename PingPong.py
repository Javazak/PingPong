import turtle # Նկարելու համար մոդուլ
import os # Ձայնային ֆորմատի հետ աշխատելու համար

window = turtle.Screen()
window.title("PingPong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Հաշիվ(Score)
score_a = 0
score_b = 0

# Փուլի արագություն(Level Speed)

speed_ball = 4

# Ձող(Pol) A
pol_a = turtle.Turtle()
pol_a.speed(0)
pol_a.shape("square")
pol_a.color("white")
pol_a.shapesize(stretch_wid=5, stretch_len=1)
pol_a.penup()
pol_a.goto(-350, 0)

# Ձող(Pol) B
pol_b = turtle.Turtle()
pol_b.speed(0)
pol_b.shape("square")
pol_b.color("white")
pol_b.shapesize(stretch_wid=5, stretch_len=1)
pol_b.penup()
pol_b.goto(350, 0)

# Գնդակ(Ball)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = speed_ball
ball.dy = speed_ball

# Pen (Էկրանի վրա տեքստ ավելացնելու համար)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Խաղացող A: 0  Խաղացող B: 0", align="center", font=("Courier", 24, "normal"))

# Ֆունկցիաներ(Functions)
def paddle_a_up():
    y = pol_a.ycor()
    y += 20
    pol_a.sety(y)

def paddle_a_down():
    y = pol_a.ycor()
    y -= 20
    pol_a.sety(y)

def paddle_b_up():
    y = pol_b.ycor()
    y += 20
    pol_b.sety(y)

def paddle_b_down():
    y = pol_b.ycor()
    y -= 20
    pol_b.sety(y)

# Ստեղնաշարի սեղմում (Keyboard binding)
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Խաղի ամբողջ պրոցեսը (Main game loop)
while True:
    window.update()

    # Գնդակի տեղաշարժ(move the ball)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Էկրանի սահմանների հպումը գնդակի հետ(border cheking)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay PingPong.mp3&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay PingPong.mp3&")


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system("afplay pat.mp3")
        score_a += 1
        speed_ball += 1
        pen.clear()
        pen.write("Խաղացող A:  {} Խաղացող B:  {} ".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system("afplay pat.mp3")
        score_b += 1
        speed_ball += 1
        pen.clear()
        pen.write("Խաղացող A:  {} Խաղացող B:  {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Ձողի ու գնդակի հպումը (pol and ball collision)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pol_b.ycor() + 40 and ball.ycor() > pol_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay PingPong.mp3&")

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < pol_a.ycor() + 40 and ball.ycor() > pol_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay PingPong.mp3&")

    if score_a == 5:
        pen.clear()
        pen.write("Խաղացող A_ն հաղթեց", align="center", font=("Courier", 30, "bold"))
        os.system("afplay gameover.mp3")
        break
    if score_b == 5:
        pen.clear()
        pen.write("Խաղացող B_ն հաղթեց", align="center", font=("Courier", 30, "bold"))
        os.system("afplay gameover.mp3")
        pen.up()
        break

