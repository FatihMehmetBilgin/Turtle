import turtle,time, threading
from random import randint

screen1 = turtle.Screen()
screen1.bgcolor("black")
screen1.title("TurtleGame")

turtle1 = turtle.Turtle()
turtle1.color("green")

############# time  board ##############
countdown= turtle.Turtle()
countdown.color("white")
countdown.penup()
countdown.hideturtle()
style2= ("Courier", 20, " italic")
countdown.goto(-450,360)
countdown.write(" Time: 20", font=style2)

turtle1.shape("turtle")
turtle1.shapesize(3,3,5)

############# Score Board   ##########
point =turtle.Turtle()
point.color("white")
point.hideturtle()
style1= ("Courier",20,"italic")
point.penup()
point.goto(-450,330)
point.write(" Your Score: 0",font=style1)


score = 0
print(type(score))
def playgame(x,y):
    global score
    if 0< second <= 20:
        point.clear()
        score += 1
        point.write(" Your Score:" + str(score), font=style1)


turtle1.onclick(playgame)

second = 20

def game():
    global second
    while True:
        turtle1.speed(3)
        turtle1.penup()
        turtle1.hideturtle()
        turtle1.goto(randint(-400, 400), randint(-400, 400))
        turtle1.showturtle()
        time.sleep(0.5)
        if second==0 :
            break

def gametime():
    global second
    while True:
        if second <= 20:
            second -= 1
            countdown.clear()
            countdown.write(" Time: " + str(second), font=style2)
            time.sleep(1)
        if second == 0 :
            countdown.clear()
            countdown.write(" Time: GameOver ", font=style2)
            break

turtlestart = threading.Thread(target=game)
timestart = threading.Thread(target=gametime)

timestart.start()
turtlestart.start()

turtle.mainloop()

