file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day06/input.txt", "r")
time_list = file.readline()[5:].split()
distance_list = file.readline()[10:].split()

def isPossible(time_holding, distance_record, total_time):
    delta_time = total_time - time_holding
    if ((delta_time*time_holding)>distance_record):
        return 1
    return 0

def how_many_ways(time, distance_record): 
    num_ways = 0
    for i in range(1, time):
        num_ways += isPossible(i, distance_record, time)

    return num_ways

ans = 1
for i in range(len(time_list)):
    ans = ans * how_many_ways(int(time_list[i]), int(distance_list[i]))
    print(ans)

file.close()