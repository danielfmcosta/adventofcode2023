file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day04/input.txt", "r")
content = file.readline().strip('\n')

while content:
    content = content[content.find(':')+2:]
    card = content.split('|')
    win_list = [x for x in card[0].split(' ') if x != '']
    mynum_list = [x for x in card[1].split(' ') if x != '']
    print(win_list)
    print(mynum_list)

    content = file.readline().strip('\n')


file.close()