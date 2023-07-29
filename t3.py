from turtle import *

pensize(2)
speed('fastest')
bgcolor('black')
pencolor('white')

for i in range(6):
    lt(60)
    fd(100)
    for i in range(6):
        lt(60)
        fd(50)
        for i in range(6):
            lt(60)
            fd(25)
            fillcolor('pink')
            begin_fill()
            for i in range(6):
                lt(60)
                fd(10)
            end_fill()
            

    
hideturtle()
mainloop()
