# 陈祥锡 信管19-1 2019312256
# 2020/9/23

from graphics import *

win = GraphWin("2", 400, 400)
center = Point(200, 200)
cir1 = Circle(center, 100)
cir1.setFill('white')
cir1.draw(win)
cir2 = Circle(center, 80)
cir2.setFill('black')
cir2.draw(win)
cir3 = Circle(center, 60)
cir3.setFill('blue')
cir3.draw(win)
cir4 = Circle(center, 40)
cir4.setFill('red')
cir4.draw(win)
cir5 = Circle(center, 20)
cir5.setFill('yellow')
cir5.draw(win)
t1 = Text(Point(200, 350), "Click anywhere to quit.")
t2 = Text(Point(200, 385), "*********************************************************")
t1.draw(win)
t2.draw(win)
win.getMouse()
win.close()

####

from graphics import *

win = GraphWin("9", 800, 800)
t = Text(Point(200, 350), "Click on two points.")
p1 = win.getMouse()
p2 = win.getMouse()
ret = Rectangle(p1, p2)
ret.draw(win)
length = abs(p1.getX() - p2.getX())
weight = abs(p1.getY() - p2.getY())
c = 2 * (length + weight)
s = length * weight
t1 = Text(Point(280, 600), "C of the rectangle is ")
t11 = Text(Point(600, 600), c)
t2 = Text(Point(280, 500), "S of the rectangle is ")
t22 = Text(Point(600, 500), s)
t3 = Text(Point(400, 700), "Click anywhere to quit.")
t4 = Text(Point(400, 750), "*********************************************************")
t1.draw(win)
t11.draw(win)
t2.draw(win)
t22.draw(win)
t3.draw(win)
t4.draw(win)
win.getMouse()
win.close()

####

from graphics import *

win = GraphWin("11", 800, 800)
p1 = win.getMouse()
p2 = win.getMouse()
body = Rectangle(p1, p2)
body.draw(win)

p3 = win.getMouse()
weightOfHouse = abs(p2.getX() - p1.getX())
p6 = Point(p3.getX() - weightOfHouse / 10, p1.getY())
p7 = Point(p3.getX() + weightOfHouse / 10, p3.getY())
door = Rectangle(p6, p7)
door.draw(win)

p4 = win.getMouse()
p8 = Point(p4.getX() - weightOfHouse / 20, p4.getY() - weightOfHouse / 20)
p9 = Point(p4.getX() + weightOfHouse / 20, p4.getY() + weightOfHouse / 20)
window = Rectangle(p8, p9)
window.draw(win)

p5 = win.getMouse()
p10 = Point(p1.getX(), p1.getY() - (abs(p2.getY() - p1.getY())))
roof = Polygon(p10, p2, p5)
roof.draw(win)

t1 = Text(Point(400, 700), "Click anywhere to quit.")
t2 = Text(Point(400, 750), "*********************************************************")
t1.draw(win)
t2.draw(win)
win.getMouse()
win.close()
