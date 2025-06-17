import timeit
def depthtri():
    depths = (open("input.txt","r"))
    depths = [int(line.strip()) for line in depths.readlines()]
    l = len(depths)
    tri = 0
    last = (depths[0]+depths[1]+depths[2])
    tot = 0
    pos = 1
    for n in depths[1:l-2]:
        tri = (n+depths[pos+1]+depths[pos+2])
        pos += 1
        if tri > last:
            tot+=1
        last = tri
    return tot
timer = timeit.Timer(lambda: depthtri())
print("Elapsed time for depthtri()",timer.timeit(1))
print("Number of times depth increases:",depthtri())
#timeit gives results of around 0.0006 s which is ok
#gives answer for part 2 of 1761 which is correct