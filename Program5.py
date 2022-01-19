#Name:Britney Huiracocha
#Email:britney.huiracocha44@myhunter.cuny.edu
#Date: September 6,2020
#This program uses turtle graphics to draw a flower

import turtle

screen = turtle.Screen()
screen.bgcolor("hotpink")

star = turtle.Turtle()
star.shape("turtle")
star.pencolor("red")
star.fillcolor("yellow")

for i in range(36):
    star.forward(200)
    star.right(170)
    star.stamp()


screen.exitonclick()
