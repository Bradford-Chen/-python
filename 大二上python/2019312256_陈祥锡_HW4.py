# 陈祥锡 信管19-1 2019312256
# 2020/10/24
import math
from graphics import *


def isLeapYear(year):
    result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return result


def isTrueDate(month, day, year):
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    if (month in month31) and (day > 0) and (day <= 31):
        return True
    elif (month == 2) and (day > 0):
        if isLeapYear(year) and (day <= 29):
            return True
        elif (not isLeapYear(year)) and (day <= 28):
            return True
        else:
            return False
    elif (month in month30) and (day > 0) and (day <= 30):
        return True
    else:
        return False


def main():
    date = str(input("请输入一个日期(月/日/年)"))
    list1 = date.split("/")
    month = int(list1[0])
    day = int(list1[1])
    year = int(list1[2])
    if isTrueDate(month, day, year):
        dayNum = 31 * (month - 1) + day
        if month == 2:
            dayNum = dayNum - (4 * month + 23) // 10
        elif month > 2:
            dayNum = dayNum + 1
        print(date + "是一个正确的日期,是第%d天。" % dayNum)
        print("************************************")
    else:
        print(date + "是一个错误的日期。")
        print("************************************")


main()

####


def target():
    win = GraphWin("16", 500, 500)
    win.setBackground("gray")
    win.setCoords(-6, -6, 6, 6)
    center = Point(0, 0)

    c1 = Circle(center, 5)
    c1.setFill("white")
    c1.draw(win)
    c2 = Circle(center, 4)
    c2.setFill("black")
    c2.draw(win)
    c3 = Circle(center, 3)
    c3.setFill("blue")
    c3.draw(win)
    c4 = Circle(center, 2)
    c4.setFill("red")
    c4.draw(win)
    c5 = Circle(center, 1)
    c5.setFill("yellow")
    c5.draw(win)

    return win


def arrowScore(win):
    title = Text(Point(0, 5.5), "Click the arrow")
    title.setSize(24)
    title.draw(win)
    oneShot = Text(Point(4, -4.5), "One Shot:")
    oneShot.setSize(15)
    oneShot.draw(win)
    totalScore = Text(Point(4, -5.5), "Total: ")
    totalScore.setSize(15)
    totalScore.draw(win)
    return title, oneShot, totalScore


def getScore(point):
    x = point.getX()
    y = point.getY()
    r = math.sqrt(x * x + y * y)
    if r <= 1:
        score = 9
    elif r <= 2:
        score = 7
    elif r <= 3:
        score = 5
    elif r <= 4:
        score = 3
    elif r <= 5:
        score = 1
    else:
        score = 0
    return score


def main():
    win = target()
    title, oneShot, totalScore = arrowScore(win)
    total = 0
    for i in range(5):
        arrows = win.getMouse()
        dot = Circle(arrows, 0.1)
        dot.setFill("white")
        dot.draw(win)
        score = getScore(arrows)
        oneShot.setText("Arrow: %d" % score)
        total = total + score
        totalScore.setText("Total: %d" % total)

    title.setText("Click anywhere to quit.")
    t2 = Text(Point(0, -6), "*********************************************************")
    t2.draw(win)
    win.getMouse()
    win.close()


main()


####

def main():  # 输入数值异常
    try:
        a = eval(input("请输入一个数"))
        b = math.sqrt(a)
        print(b)
    except ValueError:
        print("输入的数小于零")


main()


def main():  # 文本IO异常
    try:
        openFile = open('notExistsFile.txt', 'r')
        fileContent = openFile.readlines()
    except IOError:
        print('File not Exists')


main()


def lessSqrt(a, b):  # 调用函数异常
    if math.sqrt(a) < math.sqrt(b):
        return True
    else:
        return False


def main():
    try:
        a = eval(input("输入a:"))
        b = eval(input("输入b:"))
        print(lessSqrt(a, b))
    except ValueError:
        print("输入的数小于零")


main()
