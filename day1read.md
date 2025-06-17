# Day 1
This question asks to count the number of times the depth increases and decreases , firstly we can make a variable for these two results with an integer initially set to 0.
to count when it increases or decreases we can iterate through the list and compare the numbers with operators <> , then simply increase the count if the conditions are met. there is no complexity here as it either will or will not apply. start from position 1 since the first number will not have a previous value, the last value ist stored and then overwritten starting with the value held for position 0.
'''
l = depths[0]
for n in depths[1:]:
    if n>l:
        dc+=1
    if n<l:
        uc+=1
    l=n
```
The answers can then simple be printed in terminal.