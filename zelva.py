import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3)

def draw_house():
    t.penup()
    t.goto(-100, -100)  
    t.pendown()

    t.goto(-100, 0)      
    t.goto(0, 0)         
    t.goto(-100, -100)   
    t.goto(0, -100)      
    t.goto(0, 0)        


    t.goto(-50, 50)     
    t.goto(-100, 0)    
    t.goto(0, -100) 

    t.hideturtle()

draw_house()
screen.mainloop()
