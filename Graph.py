from turtle import *

#makeGraph is the function called to draw a graph based off of user data inputed
def makeGraph(data, labels):
    # Setting turtle and screen properties, creating turtle
    t = Turtle()
    s = t.getscreen()
    s.onclick(reset)
    s.setup(1000, 600, 0, 0)
    s.setworldcoordinates(-100, -50, 850, 550)
    t.hideturtle()
    t.speed(0)
    t.color("black")
    

    # Setting variables
    minMax = findMinMax(data)
    xdist = 800.0 / float(len(data) - 1)
    pixel = 500.0 / float(minMax[1])
    points = []
    
    # Drawing X axis
    t.up()
    t.pensize(6)
    t.goto(0, 0)
    
    t.down()
    t.forward(800)

    # Drawing Y axis
    t.up()
    t.goto(0, 0)
    t.setheading(90)
    t.down()
    t.forward(500)

    # Drawing markers on X axis
    t.up()
    t.goto(0, 0)
    t.setheading(0)
    for x in range(len(data) - 1):
        t.forward(xdist)
        verLine(t, x + 1)
        

    # Drawing markers on Y axis
    t.up()
    t.goto(0, 0)
    t.setheading(90)
    for x in range(10):
        label = float(minMax[1]) * (float(x + 1) / 10.0)
        label = round(label, 2)
        t.forward(50)
        horLine(t, label)

    # Labeling axis
    labelAxis(t, labels)

    # Determine data points
    for var in range(len(data)):
        x = xdist * var
        y = float(data[var]) * pixel
        points.append((x, y))

    # Mapping graph line
    t.up()
    t.goto(0, 0)
    t.pensize(1)
    t.color("blue")
    for x in range(len(points)):
        t.goto(points[x])
        t.down()
    t.up()



# findMinMax determines the highest and lowest numbers in a list and returns a list
# with those numbers
def findMinMax(lyst):
    high = lyst[0]
    low = lyst[0]
    for x in range(len(lyst)):
        if (high < lyst[x]):
            high = lyst[x]
        if (low > lyst[x]):
            low = lyst[x]
    nums = [low, high]
    return nums

# Draws short horizontal lines and labels them
def horLine(turt, num):
    start = turt.heading()
    size = turt.pen("pensize")
    turt.setheading(0)
    turt.pensize(3)
    turt.down()
    turt.forward(10)
    turt.up()
    turt.backward(60)
    turt.write(num)
    turt.forward(50)
    turt.setheading(start)
    turt.pensize(size)

# Draws short vertical lines and labels them
def verLine(turt, num):
    start = turt.heading()
    size = turt.pen("pensize")
    turt.setheading(90)
    turt.pensize(3)
    turt.down()
    turt.forward(10)
    turt.up()
    turt.backward(35)
    turt.write(num)
    turt.forward(25)
    turt.setheading(start)
    turt.pensize(size)

# Draws labels
def labelAxis(turt, labels):
    turt.up()
    turt.goto(-90, 260)
    turt.down()
    turt.write(labels[0])
    turt.up()
    turt.goto(400, -42)
    turt.down()
    turt.write(labels[1])
    turt.up()

# Resets the screen after clicking on it
def reset(x, y):
    resetscreen()
    hideturtle()

