import math
def drawing(num):
    half = math.ceil(num/2)
    for i in range(1, num+1):
        space = abs(i-half)
        dot = num-2*space
        print(space*" "+dot*"*")
drawing(17)

