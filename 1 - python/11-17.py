import turtle as t
import math
import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

from random import randrange
"""11) S využitím želví grafiky napište funkci draw_pictures, ktera bude mít na vstupu zadán počet vrchlů n-úhelníku 
a počet kopií tohoto n-úhelníku rovnoměrně rozprostřených po kružnici, a která tyto n-úhelníky vykreslí."""

def draw_polygon(sides, length=50):
    angle = 360 / sides  # Each internal angle of the polygon
    for _ in range(sides):
        t.pendown()
        t.forward(length)
        t.left(angle)
        t.penup()
def draw_pictures(sides, count, length=150):
    angle = 360 / count  # Each internal angle of the polygon
    t.speed(300)
    for _ in range(count):
        draw_polygon(sides)
        t.forward(length)
        t.right(angle)
        t.penup()
    t.done()

"""12) S využitím želví grafiky napište program, který vykreslí zadaný počet soustředných kružnic (max 30) se středy 
v bodě [0,0] = střed plátna a s různými poloměry. Barvy kružnic generujte náhodně."""
"""13) S využitím želví grafiky napište program, který vykreslí 36 kružnic o zadaném poloměru r (r je maximálně 150). 
Kružnice budou mít společnčný bod v bodě [0,0] = střed plátna. Barvy kružnic generujte náhodně."""
def draw_circles(n=36, base_r=20, step=15):
    t.colormode(255)
    t.speed(300)
    for i in range(n):
        t.penup()
        t.goto(0, -(base_r + i * step))
        t.setheading(0)
        t.pencolor((randrange(0,255) for i in range(3)))
        t.pendown()
        t.circle(base_r + i * step)
    t.done()

"""14) Z klávesnice zadejte délky stran a, b obdélníku (přirozená čísla). Napište program, který vykreslí obdélník tak,
aby vždy ležel delší stranou naležato a levý dolní roh obdélníku byl v bodě [100, 250]. Obdélník vybarvěte červenou barvou."""
def draw_rectangle(d, l):
    (d, l) = (l, d) if l < d else (d, l)
    t.penup()
    t.setpos(100,250)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(l)
        t.left(90)
        t.forward(d)
        t.left(90)
    t.end_fill()
    t.done()

"""15) Z klávesnice zadejte jeden z názvů zemí: Nizozemí, Německo, Maďarsko. Na monitor vykreslete barvu příslušné země."""
def color_countries(name):
    colors = {"Nizozemí": "orange","Německo": "black", "Maďarsko": "green" }
    t.bgcolor(colors[name])
    t.done()
"""16) Na monitor vykreslete šachovnici. 8*8 políček s velikostí strany 50."""
def draw_square():
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

def draw_checkerboard():
    t.speed(300)
    t.setheading(180)
    for x in range(8):
        for i in range(4):
            draw_square()
            t.forward(100)
        if x % 2 == 0:
            t.right(90)
            t.forward(100)
            t.right(90)
        else:
            t.left(180)
    t.left(90)
    t.forward(400)
    t.done()



"""17) Na monitor vykreslete plástev medu podle vzoru uvedeného na obrázku Vceli_plastev.jpg."""

def draw_honeycomb(a=30, width = 10, height=5):
    v = math.sqrt(3) * a
    for row in range(height):
        for col in range(width):
            x = col * (3 * a // 2)
            y = row * v
            if col % 2 == 1:
                y += v / 2

            points = [
                x + a, y,
                x + a / 2, y + v / 2,
                x - a / 2, y + v / 2,
                x - a, y,
                x - a / 2, y - v / 2,
                x + a / 2, y - v / 2,
            ]
            canvas.create_polygon(points, outline='black', fill='yellow')



# draw_pictures(6, 5)
# draw_circles()
# draw_rectangle(500,100)
# color_countries("Maďarsko")
# draw_checkerboard()
draw_honeycomb()
root.mainloop()