# Might only work in Anaconda / Jupyter Notebook

import turtle
import random 
import time

screen = turtle.Screen()
adam = turtle.Turtle()
adam.pu()
adam.goto (0,-300)
adam.pd()
adam.pensize(20)
adam.write ("RANDOM COLORED CIRCLE GENERATOR!")
adam.pensize(5)
adam.pu()



def circ_les (x,y,r,color):
    adam.goto(x,y)
    adam.pd()
    adam.fillcolor(color)
    adam.begin_fill()
    time.sleep(2)
    adam.circle (r)
    adam.end_fill()
    adam.pu()
    
    pass

def detailed (r):
    num = random.randint(1,10)
    list_colors = ["red","blue","yellow","green","lime","pink","#9370DB","#008B8B"]
    for i in range(num):
        ind = random.randint(0,(len(list_colors) - 1))
        color = list_colors[ind]
        random_x = random.randint(-300,300)
        random_y = random.randint(-300,300)
        circ_les (random_x, random_y, r, color)
     
        pass 
        
detailed (60)
