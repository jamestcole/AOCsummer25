import timeit
def positioncalc():
    list = open("2021Day2.txt")
    aim = 0
    depth = 0
    horizontal = 0

    for m in list:
        if m[0] == "f":
            horizontal += int(m[8])
            depth += aim*int(m[8])
        if m[0] == "d":
            aim += int(m[5])
        if m[0] == "u":
            aim -= int(m[3])

    print(" horizontal position is :"+str(horizontal))
    print(" depth is :"+str(depth))

    print(depth*horizontal)

timer = timeit.Timer(lambda: positioncalc())
print("Elapsed time for positioncalc()",timer.timeit(1))

# horizontal position is :1906
# depth is :1021972
# 1947878632
# Elapsed time for positioncalc() 0.0016592920292168856