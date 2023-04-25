#this project is  a pong game
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scorebord import Scoreboard




screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard() 
 
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")





while True:
    t=.1
    screen.update()
    sleep(t)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x() 
    
        
        
    
        
    #cheak if right side miss the ball   
    if ball.xcor()>380 :
        ball.reset() 
        scoreboard.l_point()

    #cheak if left side miss the ball
    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()


    t-=.1





screen.exitonclick()
