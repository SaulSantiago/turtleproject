import turtle
fred=turtle.Pen()
fred.shape("turtle")
fred.width(3)

def changeTurtleColor(color: str):
    fred.color(color)

def square():
    for i in range(4):
        fred.forward(100)
        fred.left(90)
        fred.forward(200)
        for i in range(4):
            fred.forward(100)
            fred.left(90)

changeTurtleColor("Red")
square()
changeTurtleColor("Green")
square()