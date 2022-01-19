#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 16,2020
#this program makes a turtle walk 200 times

import turtle
import random

walk=turtle.Turtle()
walk.speed(10)
    for i in range(200):
        walk.forward(5)
        w=random.randrange(0,361,30)
        walk.right(w)
        
