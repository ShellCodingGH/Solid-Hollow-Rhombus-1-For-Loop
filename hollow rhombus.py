import math
def drawingWithHalf(num):
    doub = 2*num+1
    for i in range(1, doub+1):
        space = abs(i-num-1)
        innerSpace = max(doub-2*space-2, 0)
        end = "*\n" if i != 1 and i != doub else "\n"
        print(space*" ", end="*")
        print(innerSpace*" ", end=end)
drawingWithHalf(3)
