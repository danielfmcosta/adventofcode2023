file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day01/input.txt", "r")
content = file.readline().strip('\n')
fnum, lnum, sum, temp = '0', '0', 0, 0
digits1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
while content:
    n=len(content)
    k, j= 0, n
    flag1, flag2 = True, True
    while j>k:
        for i in range(9):
            #print(f"content: {content}, flag1: {flag1}, flag2: {flag2}, i: {i}, j: {j}, k: {k}")
            if((content[k:].startswith(digits1[i]) or content[k:].startswith(digits2[i])) and flag1):
                fnum = str(i+1)
                flag1=False
            if((content[:j].endswith(digits1[i]) or content[:j].endswith(digits2[i])) and flag2):
                lnum = str(i+1)
                flag2=False
        if(flag1):
            k+=1
        elif(flag2):
            j-=1
        else:
            break
    
    temp = int(fnum + lnum)
    print(f"n: {n}, content: {content}, fnum: {fnum}, lnum: {lnum}, temp: {temp}")
    sum += temp
    content = file.readline().strip('\n')
    fnum, lnum = '0', '0'

print(sum)
file.close()