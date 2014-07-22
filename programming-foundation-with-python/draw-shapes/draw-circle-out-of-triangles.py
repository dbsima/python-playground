import turtle

def draw_triangle(some_turtle):
    for i in range (1, 4):
        some_turtle.forward(100)
        some_turtle.right(120)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    # Create a turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.color('blue')
    brad.shape('turtle')
    brad.speed(2)
    
    #draw_triangle(brad)
    for i in range (1, 36):
        draw_triangle(brad)
        brad.right(10)
    
    window.exitonclick()
    
draw_art()