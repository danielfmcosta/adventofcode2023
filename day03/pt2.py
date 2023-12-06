
def check_num(matrix, i, j):
    start, end = j, j
    while start > 0 and matrix[i][0][start-1].isdigit():
        start -= 1
    while end < len(matrix[i][0])-1 and matrix[i][0][end+1].isdigit():
        end += 1
    return int(matrix[i][0][start:end+1])

def find_nums (matrix, i, j): # i and k are rows, j and h are columns
    nums = []
    num = ''
    for k in range(i-1, i+2):
        for h in range(j-1, j+2):
            if(matrix[k][0][h].isdigit()):
                num = check_num(matrix, k, h)
                if(num not in nums):
                    nums.append(num)
    return nums             

file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventcode23/day03/input.txt", "r")
content = file.readline().strip('\n')
matrix = []
while content:
    matrix.append([content])
    content = file.readline().strip('\n')

nums = []
aux = []
for i in range(1, len(matrix)):
    for j in range(1, len(matrix[i][0])):
        if (matrix[i][0][j] == '*'):
            aux = find_nums(matrix, i, j)
            if((aux not in nums) and len(aux)>1):
                nums.append(aux)
print(nums)
print(len(nums))
ans=0
for i in range(330):
    ans += nums[i][0]*nums[i][1]

print(ans)


#print('\n'.join([el[0] for el in matrix]))
file.close()