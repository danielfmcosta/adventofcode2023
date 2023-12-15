file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day04/input.txt", "r")
content = file.readline().strip('\n')
def num_match(win_list, mynum_list):
    count = 0 
    for num in mynum_list:
        if(num in win_list):
            count +=1
    return count

def getter(content):
    num_card = int(content[5:content.find(':')])
    content = content[content.find(':')+2:]
    card = content.split('|')
    win_list = [x for x in card[0].split(' ') if x != '']
    mynum_list = [x for x in card[1].split(' ') if x != '']
    return num_card, win_list, mynum_list

tot_cards = 0
num_cards = [1 for _ in range(199)]
while content:
    num_card, win_list, mynum_list = getter(content)
    for i in range(num_card, num_card+num_match(win_list, mynum_list)):
        num_cards[i] += num_cards[num_card-1]
    content = file.readline().strip('\n')  

for i in range(len(num_cards)):
    tot_cards += num_cards[i]
print(tot_cards -1)
file.close()