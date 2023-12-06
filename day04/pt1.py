file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day04/input.txt", "r")
content = file.readline().strip('\n')
tot_points = 0
while content:
    card_points=0.5
    content = content[content.find(':')+2:]
    card = content.split('|')
    win_list = [x for x in card[0].split(' ') if x != '']
    mynum_list = [x for x in card[1].split(' ') if x != '']
    for num in mynum_list:
        if(num in win_list):
            card_points = card_points*2
    content = file.readline().strip('\n')
    if(card_points==0.5):
        continue
    tot_points += card_points

print(tot_points)
file.close()