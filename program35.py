
#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: October 27,2020
#this program takes a string as input and uses that string to control what the turtle draws on the screen

import turtle

tess=turtle.Turtle()
myWin=turtle.Screen()
commands=input('Please enter a command string: ')

for ch in commands:
               if ch=='F':
                  tess.forward(50)
               elif ch=='L':
                   tess.left(90)
               elif ch=='R':
                    tess.right(90)
               elif ch=='^':
                    tess.penup()
               elif ch=='v':
                    tess.pendown()
               elif ch=='r':
                    tess.color("red")
               elif ch=='g':
                    tess.color("green")
               elif ch=='b':
                    tess.color("blue")
               elif ch=='S':
                    tess.stamp()
               elif ch=='D':
                    tess.dot()
               elif ch=='B':
                    tess.backward(50)
               elif ch=='p':
                    tess.color("purple")
               else:
                    print("Error:do not know the command: ",ch)
print("See graphics window for your image")
myWin.exitonclick()
                
