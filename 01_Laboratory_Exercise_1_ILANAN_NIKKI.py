
#01 Laboratory Exercise 1 - ARG
#ILANAN, NIKKI C.

#IM GONNA DRAW STITCH
from turtle import Turtle

t = Turtle()
side = 20 
t.width(2)
numSquares = 27
t.speed(200)

t.hideturtle()
t.setpos(-270,-270)
t.pos()

#SQUARE FUNCTION & ARRANGEMENT
def drawSquare (color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
         t.forward(side)
         t.right(90)
    t.end_fill()
    t.forward(side)
    
def nextRow():
   t.penup()
   t.backward(numSquares * side)
   t.left(90)
   t.forward(side)
   t.right(90)
   t.pendown ()
   
def drawRow(colors, numbers):
    for j in range(len(colors)):
        for k in range(numbers[j]):
            drawSquare(colors[j])
    nextRow()

#NUMBER OF PIXELS

#1
colors = ["white", "black", "white", "black", "white"]
numbers = [8, 3, 5, 3, 8]
drawRow(colors, numbers)
#2
colors = ["white", "black", "blue","black", "blue","black","white"]
numbers = [7, 1, 3, 5, 3, 1, 7]
drawRow(colors, numbers)
#3
colors = ["white", "black", "blue" , "black" , "lightblue" , "black" , "blue" , "black" , "white"]
numbers = [7, 3, 1, 1, 3, 1, 1, 3, 7]
drawRow(colors, numbers)
#4
colors = ["white", "black", "blue" , "black" , "lightblue" , "black" , "blue" , "black" , "white"]
numbers = [7, 3, 1, 1, 3, 1, 1, 3, 7]
drawRow(colors, numbers)
#5
colors = ["white", "black", "blue" , "black" , "lightblue" , "black" , "blue" , "black" , "white"]
numbers = [7, 1, 3, 2, 1, 2, 3, 1, 7]
drawRow(colors, numbers)
#6
colors = ["white", "black", "blue" , "black" , "lightblue" , "black" , "blue" , "black" , "white"]
numbers = [8,3,1,1,1,1,1,3,8]
drawRow(colors, numbers)
#7
colors = ["white", "black", "blue" , "black" , "lightblue" , "black" , "blue" , "black" , "white"]
numbers = [9,1,2,1,1,1,2,1,9]
drawRow(colors, numbers)
#8
colors = ["white", "black", "blue" , "lightblue", "blue" , "black" , "white"]
numbers = [6,5,1,3,1,5,6]
drawRow(colors, numbers)
#9
colors = ["white", "black", "blue" , "lightblue" , "blue", "black" , "white"]
numbers = [5,1,1,13,1,1,5]
drawRow(colors, numbers)
#10
colors = ["white", "black", "blue", "black" , "white"]
numbers = [4,1,17,1,4]
drawRow(colors, numbers)
#11
colors = ["white", "black", "blue", "lightblue" , "blue", "black"
          , "blue", "lightblue" ,"blue", "black", "white"]
numbers = [4,1,2,2,3,3,3,2,2,1,4]
drawRow(colors, numbers)
#12
colors = ["white", "black", "blue", "lightblue" , "black" , "lightblue"
          ,"blue", "black", "blue", "lightblue" , "black", "lightblue" ,"blue", "black" ,"white"]
numbers = [4,1,1,1,2,1,1,5,1,1,2,1,1,1,4]
drawRow(colors, numbers)

#13
colors = ["white", "black", "lightblue" , "black" , "white", "black",
          "lightblue","blue", "black","blue", "lightblue","black","white",
          "black","lightblue","black","white"]
numbers = [4,1,1,1,1,2,1,1,3,1,1,2,1,1,1,1,4]
drawRow(colors, numbers)

#14
colors = ["white", "black", "lightblue" , "black" , "white", "black",
          "lightblue","blue", "lightblue","black","white",
          "black","lightblue","black","white"]
numbers = [3,2,1,2,1,1,1,5,1,1,1,2,1,2,3]
drawRow(colors, numbers)

#15
colors = ["white", "black", "pink" , "black" ,
          "lightblue","black","white",
          "black","lightblue","blue","lightblue","black",
          "white","black","lightblue","black","pink","black","white"]
numbers = [2,1,1,1,1,2,1,1,1,5,1,1,1,2,1,1,1,1,2]
drawRow(colors, numbers)

#16
colors = ["white", "black", "pink" , "black" ,
          "lightblue","black","lightblue","blue","lightblue","black",
          "lightblue","black","pink","black","white"]
numbers = [2,1,1,1,1,3,1,7,1,3,1,1,1,1,2]
drawRow(colors, numbers)

#17
colors = ["white", "black", "pink" , "black" ,
          "lightblue","black","lightblue","blue","lightblue","black",
          "lightblue","black","pink","black","white"]
numbers = [1,1,3,1,1,1,1,9,1,1,1,1,3,1,1]
drawRow(colors, numbers)

#18
colors = ["black", "pink" , "blue","black" ,
          "lightblue","blue","lightblue","black",
          "blue","pink","black"]
numbers = [1,4,1,1,1,11,1,1,1,4,1]
drawRow(colors, numbers)

#19
colors = ["black", "pink" , "blue","black" ,
          "blue","black",
          "blue","pink","black"]
numbers = [1,4,1,2,11,2,1,4,1]
drawRow(colors, numbers)

#20
colors = ["black", "pink" , "blue","black" ,"white",
          "black",
          "blue","black","white","black","blue","pink","black"]
numbers = [1,4,1,1,1,2,7,2,1,1,1,4,1]
drawRow(colors, numbers)

#21
colors = ["black", "pink" , "blue","black" ,"white",
          "black",
          "white","black","blue","pink","black"]
numbers = [1,3,1,1,4,7,4,1,1,3,1]
drawRow(colors, numbers)

#22
colors = ["white","black", "pink" , "blue","black" ,"white",
          "black",
          "blue","pink","black","white"]
numbers = [1,1,2,1,1,15,1,1,2,1,1]
drawRow(colors, numbers)

#23
colors = ["black", "pink" , "blue","black" ,"white",
          "black",
          "blue","pink","black"]
numbers = [1,2,1,1,17,1,1,2,1]
drawRow(colors, numbers)

#24
colors = ["black", "pink" , "blue","black" ,"white",
          "black",
          "blue","pink","black"]
numbers = [1,2,1,1,17,1,1,2,1]
drawRow(colors, numbers)

#25
colors = ["white","black" , "blue","black" ,"white",
          "black",
          "blue","black","white"]
numbers = [1,1,1,1,19,1,1,1,1]
drawRow(colors, numbers)

#26
colors = ["white","black" ,"white",
          "black","white"]
numbers = [2,1,21,1,2]
drawRow(colors, numbers)

