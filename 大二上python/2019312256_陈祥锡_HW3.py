# 陈祥锡 信管19-1 2019312256
# 2020/10/17
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return nums


def main():
    nums = [1, 2, 3, 4, 5]
    squareEach(nums)
    print(nums)
    print("************************************")


main()


####


def toNumbers(strList):
    newNumbers = []
    for i in strList:
        newNumbers.append(int(i))
    return newNumbers


def main():
    newNumber = []
    strList = ['1', '2', '3', '4']
    newNumber = toNumbers(strList)
    print(newNumber)
    print("************************************")


main()

####


from graphics import *


def drawFace(center, size, win):
    face = Circle(center, size)
    face.setFill("yellow")
    face.draw(win)
    leftEye = Circle(Point(center.getX()-size/2, center.getY()-size/2), size / 10)
    leftEye.setFill("black")
    leftEye.draw(win)
    rightEye = Circle(Point(center.getX()+size/2, center.getY()-size/2), size / 10)
    rightEye.setFill("black")
    rightEye.draw(win)
    mouth = Line(Point(center.getX()-size/2, center.getY()+size/2), Point(center.getX()+size/2, center.getY()+size/2))
    mouth.draw(win)


def main():
    win = GraphWin("2", 800, 800)
    drawFace(Point(200, 200), 100, win)
    drawFace(Point(100, 500), 50, win)
    drawFace(Point(500, 500), 200, win)
    message = Text(Point(400, 790), "Click anywhere to Quit")
    message.draw(win)
    win.getMouse()
    win.close()


main()
