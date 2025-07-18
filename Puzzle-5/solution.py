ith open('input.txt') as f:
    lines=f.readlines()
    
def parse_line(line):
    card_part, number_part=line.split(": ")      #splits card part and numbers part
    winning_str,mine_str=number_part.split("|")  #splits winnings and our cards
    my_winnings=winning_str.strip()              #strips spaces 
    mine=mine_str.strip()                         # strips spaces
    my_winnings=set(map(int,my_winnings.split())) # returns unique numbers 
    mine=set(map(int,mine.split()))                # returns unique numbers
    return my_winnings,mine
    
def PartA():
    total_score=0
    for line in lines:
        winnings, mine = parse_line(line)
        matches=len(winnings & mine)
        if matches>0:
            total_score+=2**(matches-1)
    return total_score

def PartB():
    card_counts=[1] * len(lines)
    
    for i,line in enumerate(lines):
        winnings, mine = parse_line(line)
        matches=len(winnings & mine)               # gets the common numbers in winnings & mine and finds the length
        
        for j in range(i+1,min(i+1+matches,len(lines))):
            card_counts[j]+=card_counts[i]
            
    return sum(card_counts)
            

print(PartA())
print(PartB())
