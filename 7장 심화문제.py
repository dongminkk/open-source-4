import turtle
import random

##2017038093 김동민
myTurtle, tX, tY, tColor, tSize, tShape, tSum = [None] * 7
pot = []
swidth, sheight = 500, 500

if __name__ == "__main__" :
    turtle.title('7장 심화문제')
    turtle.setup(width = swidth + 500, height = sheight + 500)
    turtle.screensize(swidth, sheight)

    for i in range(0, 5) :
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1, 100)/10 ## 1.0~9.9 소수점크기 램덤 생성
        tSum = tX + tY
        pot.append([myTurtle, tX, tY, tSize, r, g, b, tSum])

    std = sorted(pot, key=lambda turtles : turtles[1] ,reverse = True)
        
    for index, tList in enumerate(std[0:]) : 
        myTurtle = tList[0]
        myTurtle.color((r,g,b))
        myTurtle.pencolor((r,g,b))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        r = random.random()
        g = random.random()
        b = random.random()
          
        if index == 0 : ## 처음 거북이는 이전 거북이 없으니 위치 지정
            myTurtle.goto(tList[1], tList[2])
            continue
        
        myTurtle.goto(std[index-1][1], std[index-1][2])
        
        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2]) ## 선긋기
        
    turtle.done()

