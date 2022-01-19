
#Name:Britney Huiracocha
#Email:britney.huiracocha44@myhunter.cuny.edu
#Date: September 6,2020
#This program implements pseudocode
     #Set the turtle shape to be a turtle
     #Set the color to purple
     # Repeat i 15 times:
        #Walk forward 50 steps
        #Turn left 24 degrees
        #Turn left 125 degrees
      # Repeat i 15 times:
        #Walk forward 50 steps
        #Turn left 24 degrees
        #Turn left 125 degrees
       #Repeat i 15 times:
        #Walk forward 50 steps
        #Turn left 24 degrees

import turtle
screen = turtle.Screen()

circle=turtle.Turtle()
circle.shape("turtle")
circle.color("purple")

for i in range(15):
        circle.forward(50)
        circle.left(24)
circle.left(125)

for i in range(15):
        circle.forward(50)
        circle.left(24)
circle.left(125)

for i in range(15):
        circle.forward(50)
        circle.left(24)

screen.exitonclick()
