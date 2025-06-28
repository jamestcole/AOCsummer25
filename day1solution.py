depths = (open("input.txt","r"))
depths = [int(line.strip()) for line in depths.readlines()]
dc=0
uc=0
l = depths[0]
for n in depths[1:]:
    if n>l:
        dc+=1
    if n<l:
        uc+=1
    l=n
print("Number of times depth increases:",dc)
print("Number of times depth is less than the previous:",uc)

#gives answer for part 1 of 1709 which is correct