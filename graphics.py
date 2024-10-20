import turtle as r 
import colorsys as sum 
r.tracer(2)Ca
r.bgcolor("black")
r.pensize(2)
n=100
h=0
for i in range(500):
    for i in range(4):
        c=sum.hsv_to_rgb(h,1,1)
        h+=1/n
        r.color(c)
        r.circle(49+i*5,90)
        r.forward(100)
    r.right(10)
r.done()