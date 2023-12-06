file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day02/input.txt", "r")
content = file.readline().strip('\n')[5:]
ans=0
while content:
    max_blue_balls, max_green_balls, max_red_balls= 0,0,0
    id = int(content[:content.find(':')])
    content = content[content.find(':')+2:]
    content = content.replace(';', ',')
    sets = content.split(', ')
    for set in sets:
        print(set)
        num_balls = int(set[:2])
        if("blue" in set):
            if(num_balls>max_blue_balls):
                max_blue_balls = num_balls
        if("green" in set):
            if(num_balls>max_green_balls):
                max_green_balls = num_balls
        if("red" in set):
            if(num_balls>max_red_balls):
                max_red_balls = num_balls
    ans += max_blue_balls*max_green_balls*max_red_balls
    print(f"max_blue_balls: {max_blue_balls}, max_green_balls: {max_green_balls}, max_red_balls: {max_red_balls}")
    print(content)
    content = file.readline().strip('\n')[5:]
print(ans)
file.close()