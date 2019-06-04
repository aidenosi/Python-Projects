import math


def testPentNum(x):
    n = (math.sqrt(24*x + 1) + 1)/6
    return(n == int(n))


d = 0
x = 1
found = False
while(not found):
    k = x*(3*x - 1)/2
    x += 1
    for y in range(1, x):
        j = y*(3*y - 1)/2
        if(testPentNum(k + j) & testPentNum(k - j)):
            d = k - j
            found = True
            break

print("End of program. d =", d)
