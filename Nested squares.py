import turtle

# 1 -important- to create main window or frame
main_window = turtle.Screen()

# 2 -important- to create turtle
little_turtle = turtle.Turtle()

# optional attributes =========================
main_window.bgcolor("lightgray")
little_turtle.pensize(2)
little_turtle.speed(10)
# 3 end==========================================

def draw_1_square(turtle, tole_zel):
    for i in range(4): # square has 4 sides
        turtle.forward(tole_zel)
        turtle.left(90)  # SQUARE has 90 degree

tedad = 10
tole_zel = 50
position_x = -10
position_y = -10

for i in range(tedad):
    draw_1_square(little_turtle, tole_zel)

    little_turtle.penup() # fa: galam ro az ro kagaz bardar
    little_turtle.goto(position_x, position_y) # go to x, y on screen
    little_turtle.pendown() # fa: galam ro bezar ro kagaz

    position_x -= 10
    position_y -= 10
    tole_zel += 20

# 3 -important- fa: bad az rasme shekl, window baste nashe
main_window.mainloop()


