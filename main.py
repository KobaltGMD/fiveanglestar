import tkinter
from math import sin, cos, pi
radius = 200
halfangle = pi / 10
sindoubleangle = sin(4 * halfangle)
p1coordx = 300
p1coordy = 150
p1 = (p1coordx, p1coordy)
p3coordy = p1coordy + 2 * radius * (cos(halfangle) ** 2)
p3coordx = p1coordx - 2 * radius * sin(halfangle) * cos(halfangle)
p3 = (p3coordx, p3coordy)
p2coordx = p1coordx - radius * cos(halfangle)
p2coordy = p3coordy - radius * \
    cos(halfangle) / sin(3 * halfangle) * sindoubleangle
p2 = (p2coordx, p2coordy)
p4coordx = p1coordx + 2 * radius * sin(halfangle * cos(halfangle))
p4coordy = p3coordy
p4 = (p4coordx, p4coordy)
p5coordx = p1coordx + radius * cos(halfangle)
p5coordy = p2coordy
p5 = (p5coordx, p5coordy)
master = tkinter.Tk()
canvas = tkinter.Canvas(master, height=radius*3, width=radius*3, bg='#ffffff')
canvas.create_line(p1, p3, p5, p2, p4, p1, fill='#ff0000')
canvas.pack()
master.mainloop()
