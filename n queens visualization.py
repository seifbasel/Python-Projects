import turtle

# queens list
list1 = [[0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0]]

# we take nqueens positions and then we draw them into the chess board
queens_list = []
for i in range(0, 8):
    elem_index = list1[i].index(1)
    queens_list.append(elem_index)
print(queens_list)


# create screen object
sc = turtle.Screen()
# create turtle object
pen = turtle.Turtle()

# method to draw square


def draw_square():
    for i in range(4):
        pen.forward(50)
        pen.left(90)
    pen.forward(50)


# set screen
sc.setup(1000, 1000)

# set turtle speed
pen.speed(0)
pen.penup()
pen.goto(-200, 200)
pen.down()
x = -200
y = 200

# draw all of the board
for j in range(4):
    y = y-50
    pen.penup()
    pen.goto(x, y)
    pen.down()

    for i in range(4):
        pen.color("white", "black")
        pen.begin_fill()
        draw_square()
        pen.end_fill()
        pen.color("black", "white")
        pen.begin_fill()
        draw_square()
        pen.end_fill()
    y = y-50
    pen.penup()
    pen.goto(x, y)
    pen.down()

    for i in range(4):
        pen.color("black", "white")
        pen.begin_fill()
        draw_square()
        pen.end_fill()
        pen.color("white", "black")
        pen.begin_fill()
        draw_square()
        pen.end_fill()

# here is the method used to draw queens into their positions
distance_y = 165
for j in queens_list:
    distance_x = j*50
    pen.penup()
    pen.goto(-175+distance_x, distance_y)
    pen.pendown()
    pen.color("black")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(10, None, 50)
    pen.end_fill()
    distance_y = distance_y-50


turtle.done()
