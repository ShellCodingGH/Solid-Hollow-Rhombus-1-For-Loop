import math

def drawingWithHalf(num):
    doub = 2*num+1
    for i in range(1, doub+1):
        space = abs(i-num-1)
        dot = doub-2*space
        print(space*" "+dot*"*")
drawingWithHalf(4)
