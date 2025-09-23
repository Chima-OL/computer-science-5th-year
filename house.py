

# drawing a house
from turtle import *

def square(length):
    for counter in range(4):
        forward(length)
        right(90)

def triangle(length):
    for counter in range(3):
        forward(length)
        left(120)     



def house():
    s = int(input("square length"))
    door()
    
    
    
    triangle(int(input("triangle length")))
    square(int(input("square length")))
    penup()
    fd(60)
    right(90)
    fd(75)
    pendown()
    square(int(input("door length")))
        
house()

