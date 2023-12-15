# made by https://www.youtube.com/watch?v=22IrAlrWqu4

import sys
import re
from collections import defaultdict, Counter

file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day07/input.txt", "r")
content = file.read()
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q' , 'K', 'A']
lines = content.split('\n')

def strength(hand):
    hand = hand.replace('T', chr(ord('9')+1))
    hand = hand.replace('J', chr(ord('2')-1))
    hand = hand.replace('Q', chr(ord('9')+3))
    hand = hand.replace('K', chr(ord('9')+4))
    hand = hand.replace('A', chr(ord('9')+5))

    C = Counter(hand)
    if(list(C.values())==[5]):
        return(10, hand)
    elif(sorted(C.values())==[1,4]):
        return(9, hand)
    elif(sorted(C.values())==[2,3]):
        return(8, hand)
    elif(sorted(C.values())==[1, 1, 3]):
        return(7, hand)
    elif(sorted(C.values())==[1,2,2]):
        return(6, hand)
    elif(sorted(C.values())==[1,1,1,2]):
        return(5, hand)
    elif(sorted(C.values())==[1,1,1,1,1]):
        return(4, hand)
    else:
        assert False, f'{C} {hand} {sorted(C.values())}'

H = []
for line in lines:
    hand, bid = line.split()
    H.append((hand, bid))
H = sorted(H, key=lambda hb:strength(hb[0]))

ans = 0
for i,(h,b) in enumerate(H):
    ans += (1+i)*int(b)

print(ans)

file.close()