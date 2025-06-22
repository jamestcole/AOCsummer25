import timeit
def positioncalc():
    list = open("2021Day2.txt")
    depth = 0
    horizontal = 0

    for m in list:
        if m[0] == "f":
            horizontal += int(m[8])
        if m[0] == "d":
            depth += int(m[5])
        if m[0] == "u":
            depth -= int(m[3])

    print(" horizontal position is :"+str(horizontal))
    print(" depth is :"+str(depth))

    print(depth*horizontal)

timer = timeit.Timer(lambda: positioncalc())
print("Elapsed time for positioncalc()",timer.timeit(1))
print("Position of sub:",positioncalc())
# horizontal position is :1906
# depth is :1017
# 1938402
# Elapsed time for positioncalc() 0.0016592920292168856