pentNums = []
PSD = false


def pentagonNums(n):
    return n*(3*n-1)/2


d = 0

for x in range(1, 100):
    pentNums[x] = pentagonNums(x)
    if(x > 1):
        for y in range(1, x):
            if (pentNums[x] + pentNums[y]) in pentNums:
                if(pentNums[x] - pentNums[y]) in pentNums:
                    d = pentNums[x] - pentNums[y]
                    print(d)

print("End of program. d = " + d)
